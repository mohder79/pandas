import ccxt
import pandas as pd
from datetime import datetime
import pandas_ta as pta  # visit https://github.com/twopirllc/pandas-ta
# visit https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html
from ta.momentum import rsi as ta_rsi


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

df['rsi'] = pta.rsi(df.close, 14)  # current rsi

df['pre_rsi'] = df['rsi'].shift(1) # set current as pervious [use .shift()]


print(df)

