import risk_managment as fun
import MetaTrader5 as mt5
import time
import pandas_ta as ta 
import indicator as ifun
symbol="XAUUSD"#dymbol name 
riskt=1 # risk per trade  of total ac balances
slp=0.20 #stop loss per trade
timeframe=mt5.TIMEFRAME_M15 # timeframe like 1 min ,5min,15min etc
fun.check_initialize()#login to the MT5 terminal 
while 1:
    #risk managment parameter calculation
    risk_per_trade=fun.risk_per_trade(riskt=riskt)
    sl=fun.sl(symbol=symbol,riskt=riskt,slp=slp)
    lot_size=fun.calculate_lot_size(symbol=symbol,riskt=riskt,slp=slp)
    #creating dataframe in form of OHLC
    live_data=ifun.get_rates(symbol=symbol, timeframe=timeframe,number_of_data=500)
    #calculate the macd previous candel
    macd=ifun.macd(live_data)
    macd=macd.iloc[-2]
    macd_line=macd.iloc[0]
    signal_line=macd.iloc[-1]
    #calculating the LTP
    ltp=ifun.LTP(live_data)
    #ema calculation
    ema=ifun.EMA(live_data,length=21)
    ema=ema.iloc[-1]
    ema=ema.iloc[-1]
    #close calculating privious candel
    close=ifun.Close(live_data)
    diff=ema-ltp
#condition for buying order  
    if (macd_line>signal_line and ema<close and macd_line<=-0.50 and diff>=-1 and fun.opean_position()==0) :
        lot_size=fun.calculate_lot_size(symbol=symbol,riskt=riskt,slp=slp)
        buy_order=fun.send_SLTP_order_buy(symbol=symbol,volume=lot_size)
        while fun.opean_position()==1:
            #calculate the live data 
            live_data=fun.get_rates(symbol=symbol, timeframe=timeframe,number_of_data=500)
            #calculate the macd previous candel
            macd=ifun.macd(live_data)
            macd=macd.iloc[-2]
            macd_line=macd.iloc[0]
            signal_line=macd.iloc[-1]
            #calculate current pnl
            profit=mt5.account_info().profit
            #condition for exit the buy order
            if ((macd_line<signal_line or macd_line>=2.5) and fun.opean_position()==1) or (profit>=(risk_per_trade*3.5)) :
                fun.send_order(True,False,symbol=symbol,lot=lot_size,id_position=buy_order.order)
        time.sleep(900)
    if ( macd_line<signal_line and ema>close and macd_line>=0.50 and diff<=1 and fun.opean_position()==0) :
        #condition for sell order
        lot_size=fun.calculate_lot_size(symbol=symbol,riskt=riskt,slp=slp)
        sell_order=fun.send_SLTP_order_sell(symbol=symbol,volume=lot_size)
        while fun.opean_position()==1:
            #calculate the live data 
            live_data=fun.get_rates(symbol=symbol, timeframe=timeframe,number_of_data=300)
            #calculate the macd previous candel
            macd=ifun.macd(live_data)
            macd=macd.iloc[-2]
            macd_line=macd.iloc[0]
            signal_line=macd.iloc[-1]
            #calculate current pnl
            profit=mt5.account_info().profit
            #condition for exit current sell order
            if ((macd_line>signal_line or macd_line<=-2.5)and  fun.opean_position()==1) or (profit>=(risk_per_trade*3.5)) :
                fun.send_order(False,True,symbol=symbol,lot=lot_size,id_position=sell_order.order)
        time.sleep(900)