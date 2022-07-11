from cProfile import label
import ccxt
from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_column', None)


exchange = ccxt.bybit({
    'options': {
        'adjustForTimeDifference': True,
    },

})


def fetch(symbol: str, timeframe: str, limit: int):
    print(f"Fetching {symbol} new bars for {datetime.now().isoformat()}")

    bars = exchange.fetch_ohlcv(
        symbol, timeframe='1d', limit=199)  # fetch ohlcv
    df = pd.DataFrame(bars[:-1], columns=['timestamp',
                      'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df


BTC = fetch('BTC/USDT:USDT', '1h', 200)
ETH = fetch('ETH/USDT:USDT', '1h', 200)
SOL = fetch('SOL/USDT:USDT', '1h', 200)


print(BTC.close, ETH.close, SOL.close)


plt.subplot(3, 1, 1)
plt.plot(BTC.close, label='BTC closes price')
plt.xlabel('time')
plt.ylabel('price')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(ETH.close, label='ETH closes price')
plt.xlabel('time')
plt.ylabel('price')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(SOL.close, label='SOL closes price')
plt.xlabel('time')
plt.ylabel('price')
plt.legend()

plt.show()
