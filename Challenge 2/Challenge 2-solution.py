import numpy as np
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
master_data = pd.read_csv("senior-developer-challenge-master.csv")
sales_data = pd.read_csv("senior-developer-challenge-sales.csv")
sales_data['Date']=sales_data['Date'].astype('datetime64[ns]')
temp = master_data['PartId'][master_data['IsActive']==1]
output_data = pd.DataFrame()
for i in temp:
    active_data = sales_data[sales_data['PartId']== i]
    if(len(active_data)==0):
        continue
    active_data_1 = active_data.groupby(by = [pd.Grouper(key='Date',freq='W')]).sum()
    active_data_1['WeeklyMovingAvg'] = active_data_1['SalesAmount'].rolling(3,min_periods=1).mean()
    active_data_1.drop('SalesAmount',axis=1,inplace=True)
    model = ARIMA(active_data_1.WeeklyMovingAvg, order=(5,1,0))
    model_fitted = model.fit()
    forecast = model_fitted.predict(start = len(active_data_1), end = (len(active_data_1)) + 52, typ = 'levels').rename('Forecast')
    forecast = forecast.to_frame()
    forecast['PartId'] = i
    initial_stock = 1000
    forecast['StockonHand'] = initial_stock
    forecast['Output'] = 1
    for ind in forecast.index:
        forecast['StockonHand'][ind] = initial_stock - forecast['Forecast'][ind]
        initial_stock = forecast['StockonHand'][ind]
        if(forecast['StockonHand'][ind]<0):
            forecast['Output'][ind] = 0
        else:
            forecast['Output'][ind] = 1   
    output_data = output_data.append(forecast)
output_data.to_csv('Output.csv')  
output_data.reset_index(inplace=True) 
sns.lmplot(x="index", y="Forecast", data=output_data, fit_reg=False, hue="PartId",legend=True,palette='Set1', height=15)
plt.xlabel("Timeseries")
plt.ylabel("Weekly forecasting data")
plt.title('Data Forecasting')
plt.savefig("output.png",dpi=300, bbox_inches='tight')