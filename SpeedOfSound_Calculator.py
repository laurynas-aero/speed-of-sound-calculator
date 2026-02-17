import aerosandbox

def main():
    #   Constant Variable Assignment
    ratio_of_specific_heats = 1.4
    specific_heat_constant_SI = 287
    specific_heat_constant_english = 1716

    #   User Input Checking
    print("\nIf value unknown, write '_'")
    units = input("Is it in English or SI units?")
    if units.lower() not in ['english','si']:
        print('That is not a valid input. Please try again')

    alt_m = input("What is the standard altitude?")
    if alt_m == "_":
        pass
    else: 
        try:
            float(alt_m) 
        except ValueError: 
            print("That is not a valid input. Please try again.")

    temperature = input('What is the temperature?')
    if temperature == "_":
        pass
    else: 
        try:
            float(temperature) 
        except ValueError: 
            print("That is not a valid input. Please try again.")

    speed_of_sound = input('What is the speed of sound?')
    if speed_of_sound == "_":
        pass
    else: 
        try:
            float(speed_of_sound) 
        except ValueError: 
            print("That is not a valid input. Please try again.")

    #   List of Inputs
    inputs = [alt_m, temperature, speed_of_sound]


    #   Finding Known
    for inp in inputs:
        if inp != '_':
            known = float(inp)

    #   Constant in Units and Altitude
    if units.lower() == 'english':
        constant = ratio_of_specific_heats*specific_heat_constant_english
        speed = 'ft/s'
        distance = 'ft'
        temp = 'R'
        if known == float(inputs[0]):
            known = float(known)
            alt_m = known*0.3048

    elif units.lower() == 'si':
        constant = ratio_of_specific_heats*specific_heat_constant_SI
        speed = 'm/s'
        distance = 'm'
        temp = 'K'
        
        if known == float(inputs[0]):
            known = float(known)
            alt_m = known


    if known == float(inputs[0]):
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
    elif known == float(inputs[1]):
        known = float(known)
        speed_of_sound = (constant*known)**0.5
    elif known == float(inputs[2]):
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