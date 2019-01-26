import pandas as pd
import Quandl

df = Quandl.get('WIKI/GOOGLE')

print(df.head())
