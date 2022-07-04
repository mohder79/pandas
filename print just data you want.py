import ccxt
import pandas as pd
from datetime import datetime


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

mydata = df[['open', 'close']]  #data you want

print(mydata)
