from calculator import compute_speed_of_sound

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

    speed_of_sound, temperature, alt_m, speed, temp, distance = compute_speed_of_sound(
        units, alt_m, temperature, speed_of_sound
    )

    #   Printing Results
    print(f"The speed of sound is: {speed_of_sound} {speed}")
    print(f"The temperature is: {temperature} {temp}")
    print(f"The standard altitude is: {alt_m} {distance}")

if __name__ == "__main__":
    main()