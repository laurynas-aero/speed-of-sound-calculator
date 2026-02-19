from logic.ISA_temperature.calculator import temperature_from_altitude
from logic.constants import CONSTANTS

def compute_speed_of_sound_from_temperature(temp, units):
    SPECIFIC_HEAT = CONSTANTS[units]["R"]
    GAMMA = CONSTANTS[units]["gamma"]

    speed_of_sound = (GAMMA*SPECIFIC_HEAT*temp) ** 0.5

    return speed_of_sound

def compute_speed_of_sound_from_altitude(alt_m, units):
    temp = temperature_from_altitude(alt_m, units)
    SPECIFIC_HEAT = CONSTANTS[units]["R"]
    GAMMA = CONSTANTS[units]["gamma"]

    speed_of_sound = ((GAMMA*SPECIFIC_HEAT) * temp) ** 0.5

    return speed_of_sound

def compute_temperature_from_speed_of_sound(speed_of_sound, units):
    SPECIFIC_HEAT = CONSTANTS[units]["R"]
    GAMMA = CONSTANTS[units]["gamma"]

    temp = (speed_of_sound ** 2) / (GAMMA*SPECIFIC_HEAT)

    return temp