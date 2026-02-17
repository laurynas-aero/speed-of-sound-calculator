import aerosandbox

#  Constant Variable Assignment
RATIO_OF_SPECIFIC_HEATS = 1.4
SPECIFIC_HEAT_SI = 287
SPECIFIC_HEAT_ENGLISH = 1716

def get_float_or_unknown(prompt):
    value = input(prompt)
    if value == "_":
        return None
    try:
        return float(value)
    except ValueError:
        print("That is not a valid input")
        return None

def main():

    #   User Input Checking
    print("\nIf value unknown, write '_'")
    units = input("Is it in English or SI units?")
    if units.lower() not in ['english','si']:
        print('That is not a valid input. Please try again')

    alt_m = get_float_or_unknown("What is the standard altitude?")
    temperature = get_float_or_unknown('What is the temperature?')
    speed_of_sound = get_float_or_unknown('What is the speed of sound?')

    #   List of Inputs
    inputs = [alt_m, temperature, speed_of_sound]


    #   Finding Known
    for inp in inputs:
        if inp is not None:
            known = float(inp)

    #   Constant in Units and Altitude
    if units.lower() == 'english':
        constant = RATIO_OF_SPECIFIC_HEATS*SPECIFIC_HEAT_ENGLISH
        speed = 'ft/s'
        distance = 'ft'
        temp = 'R'
        if alt_m is not None:
            known = float(known)
            alt_m = known*0.3048

    elif units.lower() == 'si':
        constant = RATIO_OF_SPECIFIC_HEATS*SPECIFIC_HEAT_SI
        speed = 'm/s'
        distance = 'm'
        temp = 'K'
        
        if alt_m is not None:
            known = float(known)
            alt_m = known


    if alt_m is not None:
        known = float(known)
        atm = aerosandbox.Atmosphere(altitude=alt_m) 
        T_K = atm.temperature()
        T_R = T_K*1.8
        if units.lower() == 'english':
            speed_of_sound = (constant*T_R)**0.5
            temperature = T_R
        elif units == 'si':
            speed_of_sound = (constant*T_K)**0.5
            temperature = T_K
    #   Speed of Sound Calculation
    elif temperature is not None:
        known = float(known)
        speed_of_sound = (constant*known)**0.5
    elif speed_of_sound is not None:
        known = float(known)
        temperature = ((speed_of_sound)**2)/constant
    else:
        "ERROR. Please try again."

    #   Printing Results
    print(f"The speed of sound is: {speed_of_sound} {speed}")
    print(f"The temperature is: {temperature} {temp}")
    print(f"The standard altitude is: {alt_m} {distance}")

if __name__ == "__main__":
    main()