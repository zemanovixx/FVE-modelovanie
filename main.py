import solar_power
import plot
import pvlive
import pandas as pd

# Import dát z PVlive
# df_weather, metadata = pvlive.get_pvlive(
#     station=1,
#     start=pd.Timestamp(2021,8,1),    
#     end=pd.Timestamp(2021,8,31))
# df_weather.to_csv('pvlive_august.csv')

df_weather = pd.read_csv('pvlive_august.csv') # Nacitanie do df - ak uz mam data z pvlive aby som nemusel posielat poziadavky na api pvlive

# Vyber hodnot z df iba pre rozsah z filtra
start_date = '2021-08-21' # Hodnoty pre Filter pre vyber datumov z DF   
end_date = '2021-08-22'
df_weather = df_weather.loc[(df_weather['datetime'] >= start_date) & (df_weather['datetime'] <= end_date)]
df_weather['effective_irradiance'] = df_weather['Gg_pyr']

df_resoluts = solar_power.run_model(df_weather) # Spustenie vypoctu modelu

ac = df_resoluts.ac
df_ac = ac.to_frame(name='ac')
df_ac['datetime'] = df_weather['datetime']

df_dc = df_resoluts.dc
df_dc['datetime'] = df_weather['datetime']



start_date_cons = '2021-08-21' # Hodnoty pre Filter pre vyber datumov z DF   
end_date_cons = '2021-08-22'
df_consumption = pd.read_csv('power_consumption.csv')
df_consumption = df_consumption.loc[(df_consumption['datetime'] >= start_date_cons) & (df_consumption['datetime'] <= end_date_cons)]
df_consumption['Consumption_W'] = df_consumption['Electricity_HH1']*100_000

# df_ac['Wh'] = df_ac['ac']*(1/60)
# total_energy = df_ac['Wh'].sum()/1000

# print(f"Suma Vykonu : {total_energy:.2f} kWh")

# PLOT
plot.power_ac(df_ac,df_consumption)
plot.power_dc(df_dc,df_consumption)
