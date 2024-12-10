import pandas as pd
# import pvlib 
import pvlib
from pvlib import iotools
from pvlib.pvsystem import PVSystem 
from pvlib.location import Location
from pvlib.modelchain import ModelChain
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS

import pvlive
import plot
# Nacitanie teplotneho modelu
temperature_model_param = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']

# Nacitanie modelu a striedaca
sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod')
cec_modules = pvlib.pvsystem.retrieve_sam('CECMod')
cec_inverters = pvlib.pvsystem.retrieve_sam('cecinverter')

sandia_module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
cec_inverter = cec_inverters['Huawei_Technologies_Co___Ltd___SUN2000_10KTL_USL0__240V_']
cec_module = cec_modules['Canadian_Solar_Inc__CS1U_430MS']


latitude, longitude = 48.15, 17.11  # Bratislava

location = Location(latitude, longitude, tz='Europe/Bratislava')

sklon = 20              # surface_tilt : uhol natocenia float, default 0 
azimut = 0              # surface_azimuth : uhol natocenia float, default 180
racking = 'open_rack'   # racking_model : str, optional
vyska = 10              # module_height : vyska nad zemou, optional

mount = pvlib.pvsystem.FixedMount(
    surface_tilt= sklon,
    surface_azimuth=azimut,
    racking_model=racking,
    module_height=vyska, 
)

pole = pvlib.pvsystem.Array(
    mount=mount,
    module_parameters=cec_module,
    modules_per_string= 10 ,       # Pocet modulov v stringu
    strings=1,                    # Pocet stringov                    
    temperature_model_parameters=temperature_model_param
    )

pvsystem = PVSystem(
    arrays=pole,
    inverter_parameters=cec_inverter
    )

def run_model(weather):
    mc = ModelChain(system=pvsystem,location=location,aoi_model="no_loss")
    mc.run_model_from_effective_irradiance(weather)
    return mc.results