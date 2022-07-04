import ccxt
import pandas as pd
from datetime import datetime
import pandas_ta as pta #visit https://github.com/twopirllc/pandas-ta
from ta.momentum import rsi as ta_rsi #visit https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html


exchange = ccxt.bybit({
    'options': {
        'adjustForTimeDifference': True,
    },

})
symbol = 'BTC/USDT:USDT'  # my symbol

print(f"Fetching new bars for {datetime.now().isoformat()}")
bars = exchange.fetch_ohlcv(symbol, timeframe='1m', limit=500)  # fetch ohlcv
df = pd.DataFrame(bars[:-1], columns=['timestamp',
                  'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

df['pandas_ta_lib_rsi'] = pta.rsi(df.close, 14)  # pandas ta library example

df['ta_lib_rsi'] = ta_rsi(df.close, 14)  # ta library example 


print(df)
