import aerosandbox

RATIO_OF_SPECIFIC_HEATS = 1.4
SPECIFIC_HEAT_SI = 287
SPECIFIC_HEAT_ENGLISH = 1716

def compute_speed_of_sound(units, alt_1, temperature, speed_of_sound):
    alt_m = None
    # Determine constant
    if units.lower() == 'english':
        constant = RATIO_OF_SPECIFIC_HEATS * SPECIFIC_HEAT_ENGLISH
        speed_unit = 'ft/s'
        distance_unit = 'ft'
        temp_unit = 'R'
        if alt_1 is not None:
            alt_m = alt_1 * 0.3048
    else:
        constant = RATIO_OF_SPECIFIC_HEATS * SPECIFIC_HEAT_SI
        speed_unit = 'm/s'
        distance_unit = 'm'
        temp_unit = 'K'
        alt_m = alt_1

    # Case 1: altitude known
    if alt_1 is not None:
        atm = aerosandbox.Atmosphere(altitude=alt_m)
        T_K = atm.temperature()
        T_R = T_K * 1.8

        if units.lower() == 'english':
            speed_of_sound = (constant * T_R) ** 0.5
            temperature = T_R
        else:
            speed_of_sound = (constant * T_K) ** 0.5
            temperature = T_K

    # Case 2: temperature known
    elif temperature is not None:
        speed_of_sound = (constant * temperature) ** 0.5

    # Case 3: speed known
    elif speed_of_sound is not None:
        temperature = (speed_of_sound ** 2) / constant

    return speed_of_sound, temperature, alt_m, speed_unit, temp_unit, distance_unit
