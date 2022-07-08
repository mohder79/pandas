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

df['rsi'] = pta.rsi(df.close, 14)  # rsi

df['rsi15'] = pta.rsi(df.close, 15)  # rsi 15

df.loc[df['rsi'] <= df['rsi15'], 'new dataframe'] = 'True'
df.loc[df['rsi'] > df['rsi15'], 'new dataframe'] = 'False'

print(df)
