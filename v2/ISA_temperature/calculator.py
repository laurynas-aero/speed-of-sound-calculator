from constants import CONSTANTS

def temperature_from_altitude(alt, units):
    T0 = CONSTANTS[units]["T0"]
    L = CONSTANTS[units]["L_tropo"]
    T = T0 + L*alt
    return T

if __name__ == "__main__":
    print(temperature_from_altitude(1000, "si"))
