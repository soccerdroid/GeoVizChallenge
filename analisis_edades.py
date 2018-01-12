import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('201705-citibike-tripdata.csv')
#print(df)
#print(df.isnull().sum()) 
#df.dropna(axis=0, how='all')
df.rename(columns = {'start station id':'start_station_id'}, inplace = True)
df.rename(columns = {'birth year':'birth_year'}, inplace = True)

#print(df.start_station_id.nunique())

df = df[np.isfinite(df['birth_year'])]
df = df[df.birth_year >1927]

#print(df.isnull().sum()) 
df["age"]=2017-df["birth_year"]
df["tripduration"]=df["tripduration"]/60
df[['Date','Time']] = df.starttime.str.split(expand=True)
# grupo_fechas=df[["Date","bikeid"]].groupby("Date").count()
grupo_edades=df[["age","tripduration"]].groupby("age").mean()
grupo_edades.rename(columns = {'tripduration':'tripduration_mean'}, inplace = True)
grupo_edades.reset_index(inplace=True)
print(grupo_edades)

# # print(grupo_edades)
# grupo_fechas.reset_index(inplace=True)

# grupo_fechas['day_of_week'] =pd.to_datetime(grupo_fechas['Date']).dt.weekday_name
# grupo_fechas.drop
# #print(grupo_fechas)
# #df.groupby(['start_station_id','age']).sum()
# #plt.figure(); grupo_fechas.plot();
# grupo_fechas.rename(columns = {'bikeid':'trip_counts'}, inplace = True)

plt.figure();
plt.scatter(grupo_edades["age"], grupo_edades["tripduration_mean"],alpha=.1)

# grupo_fechas=grupo_fechas.set_index('Date')
# print(grupo_fechas)
# grupo_fechas.plot(title='Cantidad de recorridos en Mayo')
# #plt.xticks(np.arange(1, 31, 1))
# #plt.set_xtickslabels(df["day_of_week"].values)
plt.show()