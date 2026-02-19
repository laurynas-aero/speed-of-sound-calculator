import aerosandbox

def speed_of_sound_from_temperature(temp, SPECIFIC_HEAT):
    speed_of_sound = (1.4*SPECIFIC_HEAT*temp) ** 0.5
    return speed_of_sound

def compute_speed_of_sound_from_altitude(alt_m, SPECIFIC_HEAT):
    atm = aerosandbox.Atmosphere(altitude=alt_m)
    temp = atm.temperature()
    speed_of_sound = ((1.4*SPECIFIC_HEAT) * temp) ** 0.5
    return speed_of_sound

def compute_temperature_from_speed_of_sound(speed_of_sound, SPECIFIC_HEAT):
    temp = (speed_of_sound ** 2) / (1.4*SPECIFIC_HEAT)
    return temp