import  talib
import numpy


c = numpy.random.randn(100)
print(c)
k, d = talib.STOCHRSI(c)
print("k",k,"d",d)

rsi = talib.RSI(c)
print("rsi",rsi)
k, d = talib.STOCHF(rsi, rsi, rsi)
print("k",k,"d",d)


close = numpy.random.random(100)
output = talib.SMA(close)
print("-"*50)
from talib import MA_Type

upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)
print(upper, middle, lower)
output = talib.MOM(close, timeperiod=5)
print("output",output)