from matplotlib import pyplot
import numpy as np
import ccxt
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go


# { load exchange
exchange = ccxt.binance({
    'options': {
        'adjustForTimeDifference': True,
    },

})
# }


# { load data as function
def fetch(symbol: str, timeframe: str, limit: int):
    print(f"Fetching {symbol} new bars for {datetime.now().isoformat()}")

    bars = exchange.fetch_ohlcv(
        symbol, timeframe=timeframe, limit=limit)  # fetch ohlcv
    df = pd.DataFrame(bars[:-1], columns=['timestamp',
                      'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    #df = df.set_index(pd.DatetimeIndex(df.timestamp))
    return df
# }


symbol = 'BTC/USDT'
timeframe = '3m'  # 1m 3m 5m 15m 1h 4h 8h 1d
leverage = 10
limit = 1000
# }


BTC = fetch(symbol, timeframe, limit)


BTC.to_csv('Desktop/BTCUSDT_3M.csv')
BTC.to_csv('Desktop/BTCUSDT_3M_no_index.csv', index=False)
