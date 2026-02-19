from logic.speed_of_sound.calculator import (
    compute_speed_of_sound_from_temperature, 
    compute_speed_of_sound_from_altitude
    )

def compute_mach_number_from_temperature(temp, speed, units):
    speed_of_sound = compute_speed_of_sound_from_temperature(temp, units)
    _check_inputs(speed_of_sound, speed)

    mach_number = speed/speed_of_sound

    return mach_number

def compute_mach_number_from_altitude(alt, speed, units):
    speed_of_sound = compute_speed_of_sound_from_altitude(alt, units)
    _check_inputs(speed_of_sound, speed)

    mach_number = speed/speed_of_sound

    return mach_number

def compute_mach_number_from_speed_of_sound(speed_of_sound, speed):
    _check_inputs(speed_of_sound, speed)
    
    mach_number = speed/speed_of_sound

    return mach_number

def compute_speed_from_mach_number(mach_number, speed_of_sound):
    speed = mach_number*speed_of_sound

    return speed

def compute_speed_from_temperature(mach_number, temp, units):
    speed_of_sound = compute_speed_of_sound_from_temperature(temp, units)
    speed = mach_number*speed_of_sound

    return speed

def compute_speed_from_altitude(mach_number, alt, units):
    speed_of_sound = compute_speed_of_sound_from_altitude(alt, units)
    speed = mach_number*speed_of_sound

    return speed

def compute_speed_of_sound_from_mach_number(speed, mach_number):
    speed_of_sound = speed/mach_number

    return speed_of_sound

def _check_inputs(speed_of_sound, speed):
    if speed_of_sound <= 0:
        raise ValueError("Speed of sound must be positive.")
    if speed < 0:
        raise ValueError("Speed cannot be negative.")
    return