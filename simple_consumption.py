"""
Minimalistic example for using the pylpg package
"""
from pylpg import lpg_execution, lpgdata
import utils
import plotly.graph_objects as go

# Simulate the predefined household CHR01 (couple, both employed) for the year 2022
data = lpg_execution.execute_lpg_single_household(
    2021,
    lpgdata.Households.CHR01_Couple_both_at_Work,
    lpgdata.HouseTypes.HT20_Single_Family_House_no_heating_cooling,
)

# Extract the generated electricity load profile
electricity_profile = data["Electricity_HH1"]
# print(electricity_profile)

# Resample to 15 minute resolution
profile = electricity_profile.resample("15min").sum()

# Show a carpet plot
# utils.carpet_plot(profile)

data["Electricity_HH1"].to_csv("simple_consumption.csv")