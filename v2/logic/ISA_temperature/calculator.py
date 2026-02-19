from logic.constants import CONSTANTS

def temperature_from_altitude(alt, units):
    T0 = CONSTANTS[units]["T0"]
    L = CONSTANTS[units]["L_tropo"]
    T = T0 + L*alt
    return T
