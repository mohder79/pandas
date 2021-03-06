from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt

data = 'F:\python\Bitstamp_BTCUSD_d.csv'  # data file address
Columns = ['date', 'open', 'high', 'low', 'close',
           'Volume USD']  # column you want to pandas read

df = pd.read_csv(data, sep=',', usecols=Columns, header=1)
# sep= separator (open your data file with notpad to see separator)
# usecols = your column
# header = Row number(s) to use as the column names, and the start of the data

df = df[::-1].reset_index(drop=True)
# reverse data . in csv file data start 2022 t0 2014 , so last data is 2014 .

print(df.close)
# /////////////// plot close data
plt.plot(df.close, label='BTC/USD close')
plt.xlabel('time or day')
plt.ylabel('price')
plt.legend()
plt.show()
 
