import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGLE")

print(df.head())
