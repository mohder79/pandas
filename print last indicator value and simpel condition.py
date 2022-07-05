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

df['pandas_ta_lib_rsi'] = pta.rsi(df.close, 14)  # pandas ta library exmpel

df['ta_lib_rsi'] = ta_rsi(df.close, 14)  # ta library exmpel

print(df)


rsi_pandas_ta = df.iloc[-1]['pandas_ta_lib_rsi'] #last indicator value
print(f'last pandas ta rsi: {rsi_pandas_ta}') #

rsi_ta = df.iloc[-1]['ta_lib_rsi']    #last indicator value
print(f'last ta rsi: {rsi_ta}')

if rsi_pandas_ta > rsi_ta:
    print('pandas ta rsi is bigger')
elif rsi_pandas_ta == rsi_ta:
    print('are equal')
else:
    print('ta rsi is bigger')
