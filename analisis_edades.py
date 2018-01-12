import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('201705-citibike-tripdata.csv')
#print(df)
#print(df.isnull().sum()) 
#df.dropna(axis=0, how='all')
df.rename(columns = {'start station id':'start_station_id'}, inplace = True)
#print(df.start_station_id.nunique())

df = df[np.isfinite(df['birth year'])]
#print(df.isnull().sum()) 
df["age"]=2017-df["birth year"]
df[['Date','Time']] = df.starttime.str.split(expand=True)
grupo_fechas=df[["Date","bikeid"]].groupby("Date").count()
grupo_fechas.reset_index(inplace=True)

grupo_fechas['day_of_week'] =pd.to_datetime(grupo_fechas['Date']).dt.weekday_name
grupo_fechas.drop
#print(grupo_fechas)
#df.groupby(['start_station_id','age']).sum()
#plt.figure(); grupo_fechas.plot();
grupo_fechas.rename(columns = {'bikeid':'trip_counts'}, inplace = True)
plt.figure();
df.set_index('Date')
grupo_fechas.plot(title='Cantidad de recorridos en Mayo')
plt.show()