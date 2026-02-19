SPECIFIC_HEAT_SI = 287
SPECIFIC_HEAT_ENGLISH = 1716

def compute_Mach_number(units, speed_of_sound, speed):
    if units.lower() == 'english':
        constant = SPECIFIC_HEAT_ENGLISH
        speed_unit = 'ft/s'
    else:
        constant = SPECIFIC_HEAT_SI
        speed_unit = 'm/s'

    # Case 1: Speed known
    if speed is not None:
        mach_number = speed/speed_of_sound

    elif mach_number is not None:
        speed = mach_number*speed_of_sound

    return mach_number, speed, speed_of_sound, speed_unit