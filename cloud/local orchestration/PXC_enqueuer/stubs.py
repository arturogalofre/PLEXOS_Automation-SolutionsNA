# stubs.py

import clr
import sys

# Path to PLEXOS API assemblies
plexos_api_path = 'C:/Program Files/Energy Exemplar/PLEXOS 11.0 API'

# Add reference to assemblies if they are not already loaded
if plexos_api_path not in sys.path:
    sys.path.append(plexos_api_path)
    clr.AddReference('PLEXOS_NET.Core')
    clr.AddReference('EnergyExemplar.PLEXOS.Utility')
    clr.AddReference('EEUTILITY')

# Import the PLEXOS modules and Enums for IDE awareness
from PLEXOS_NET.Core import DatabaseCore
from EnergyExemplar.PLEXOS.Utility.Enums import *
from EEUTILITY.Enums import *
