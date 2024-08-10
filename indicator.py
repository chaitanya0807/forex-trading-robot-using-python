import MetaTrader5 as mt5
from datetime import datetime,time
import pandas as pd 
import pandas_ta as ta
import time
def get_rates(symbol="EURUSD", timeframe=mt5.TIMEFRAME_M5,number_of_data=25):
    # Compute now date
    from_date = datetime.now()

    # Extract n Ticks before now
    rates = mt5.copy_rates_from(symbol, timeframe, from_date, number_of_data)


    # Transform Tuple into a DataFrame
    df_rates = pd.DataFrame(rates)

    # Convert number format of the date into date format
    df_rates["time"] = pd.to_datetime(df_rates["time"], unit="s")
    
    df_rates = df_rates.set_index("time")
    
    return df_rates
def LTP(live_data):
    while 1:
        ltp=live_data.iloc[-1]
        ltp=ltp.iloc[3]
        return(ltp)

#calling fun like below 
#while 1:
    #live_data=fun.get_rates(symbol=symbol, timeframe=timeframe,number_of_data=10)
    #print(LTP(live_data))
def Close(live_data):
    while 1:
        ltp=live_data.iloc[-2]
        ltp=ltp.iloc[3]
        return(ltp)
def EMA(live_data,length):
    # Calculate the 200-period EMA using pandas_ta
    live_data['ema'] = ta.ema(live_data['close'], length=length)
    
    return (live_data[['ema']]) 



def macd(live_data):

    macd=live_data.ta.macd(fast=10, slow=24, signal=7,append=True)
    return(macd)