import MetaTrader5 as mt5
from datetime import datetime,time
import pandas as pd 
import time
import pandas_ta as ta 
#order placing and closing without sl
def send_order( buy, sell,symbol, lot, id_position=None,comment=" No specific comment", magic=1):
    
   
    
    
    """ OPEN A TRADE """
    if buy and id_position==None:
        request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": mt5.symbol_info_tick(symbol).ask,
        "tp":0.0,
        "sl":0.0,
        "deviation": 10,
        "magic": magic,
        "comment": comment,
        "type_filling": mt5.ORDER_TIME_GTC,
        "type_time": mt5.ORDER_TIME_GTC,
        }
        
        result = mt5.order_send(request)
        return result
        
    if sell and id_position==None:
        request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL,
        "price": mt5.symbol_info_tick(symbol).bid,
            
        "deviation": 10,
        "magic": magic,
        "comment": comment,
        "type_filling": mt5.ORDER_TIME_GTC,
        "type_time": mt5.ORDER_TIME_GTC,
        }
        
        result = mt5.order_send(request)
        return result
    """ CLOSE A TRADE """
    if buy and id_position!=None:
        request = {
        "position": id_position,
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL,
        "price": mt5.symbol_info_tick(symbol).bid,
        "deviation": 10,
        "magic": magic,
        "comment": comment,
        "type_filling": mt5.ORDER_TIME_GTC,
        "type_time": mt5.ORDER_TIME_GTC,
        }
        
        result = mt5.order_send(request)
        return result
        
    if sell and id_position!=None:
        request = {
        "position": id_position,
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": mt5.symbol_info_tick(symbol).ask,    
        "deviation": 10,
        "magic": magic,
        "comment": comment,
        "type_filling": mt5.ORDER_TIME_GTC,
        "type_time": mt5.ORDER_TIME_GTC,
        }
        result = mt5.order_send(request)
        return result
#trade with specific time     
def time_check():
    start_time = time(20,0,0,0)
    end_time = time(23,59,0,0)
    current_datetime = datetime.now()
    current_weekday = current_datetime.weekday()
    current_time = current_datetime.time()

    if 0 <= current_weekday <= 4 and start_time <= current_time <= end_time:
        return 1
    else:
        return 0
#placing buy order with sl and tp
def send_SLTP_order_buy(symbol,volume,deviation=10,magic=1):
    #this is for only one position at a time run 
    
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume ,
        "type": mt5.ORDER_TYPE_BUY,
        "price":mt5.symbol_info_tick(symbol).ask,
        "tp":mt5.symbol_info_tick(symbol).ask+8,
        "sl":mt5.symbol_info_tick(symbol).ask-4,
        "deviation":deviation,
        "magic": magic,
        "comment": " No specific comment",
        "type_filling": mt5.ORDER_TIME_GTC,
        "type_time": mt5.ORDER_TIME_GTC
        }
        
    result = mt5.order_send(request)
    return result   
#placing sell order with tp and sl
def send_SLTP_order_sell(symbol,volume,deviation=10,magic=1):
  
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume ,
        "type": mt5.ORDER_TYPE_SELL,
        "price":mt5.symbol_info_tick(symbol).bid,
        "tp":mt5.symbol_info_tick(symbol).bid-8,
        "sl":mt5.symbol_info_tick(symbol).bid+4,
        "deviation":deviation,
        "magic": magic,
        "comment": " No specific comment",
        "type_filling": mt5.ORDER_TIME_GTC,
        "type_time": mt5.ORDER_TIME_GTC
        }
        
    result = mt5.order_send(request)
    return result
#to check the number of open position 
def opean_position():
    num_positions = mt5.positions_total()
    if num_positions==0:
        return 0
    if num_positions>=1:
        return 1


#to calculate risk per day
def risk_per_trade(riskt):
    # Get account info
    account_info = mt5.account_info()

    # Calculate risk per trade as 1% of account balance
    risk_per_trade = account_info.balance * riskt/100
    #to calculate the risk per day 
   
    return int(risk_per_trade)
    #calculating SL
def sl(symbol,riskt,slp):
    # Get account info
    account_info = mt5.account_info()

    # Calculate risk per trade as 1% of account balance
    risk_per_trade = account_info.balance * riskt/100

    # Get bid price of the instrument
    bid_price = mt5.symbol_info(symbol).bid

    # Calculate stop loss (SL) as 0.02% of bid price of symbol
    sl = bid_price * slp/100
    return sl

def calculate_lot_size(symbol,riskt,slp):
    account_info = mt5.account_info()

    # Calculate risk per trade as 1% of account balance
    risk_per_trade = account_info.balance *riskt/100

    # Get bid price of the instrument
    bid_price = mt5.symbol_info(symbol).bid

    # Calculate stop loss (SL) as 0.15% of bid price
    sl = bid_price * slp/ 100

    # Calculate lot size based on risk per trade and stop loss
    lot_sizes = (int(risk_per_trade)) /sl
    symbol_info = mt5.symbol_info(symbol)._asdict()
    con_size=symbol_info['trade_contract_size']
    lot_size1=(lot_sizes/con_size)
    lot_size=round(lot_size1,2)
    return lot_size


def check_initialize():
    if mt5.initialize():
        print ("mt5 is initialize")
    else:
        print("not mt5 initialize")
    return 1    
def autoclose(risk_per_trade=risk_per_trade):
    risk_per_trade=-risk_per_trade
    while 1:
        profit=mt5.account_info().profit
        time.sleep(15)
        if profit>=(risk_per_trade):
            ("send order for closing")
def contract_size(symbol):
    symbol_info = mt5.symbol_info(symbol)._asdict()
    con_size=symbol_info['trade_contract_size']
    return con_size

def position_id():
    positions = mt5.positions_get()
    ticket=positions[0].ticket
    return ticket