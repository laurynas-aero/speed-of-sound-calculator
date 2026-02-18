from calculator import compute_speed_of_sound

def get_float_or_unknown(prompt):
    while True:
        value = input(prompt)
        if value == "_":
            return None
        try:
            return float(value)
        except ValueError:
            print("Error: Invalid input")
            

def main():

    #   User Input Checking
    while True:
        print("\nIf value unknown, write '_'")
        units = input("Is it in English or SI units?")
        if units.lower() in ['english','si']:
            break
        print("Error: Invalid input")
    alt_1 = get_float_or_unknown("What is the standard altitude?")
    temperature = get_float_or_unknown('What is the temperature?')
    speed_of_sound = get_float_or_unknown('What is the speed of sound?')

    known_values = [alt_1, temperature, speed_of_sound]
    count_known = sum(v is not None for v in known_values)
    if count_known > 1:
        print("Specify only one value")
        return main()
    elif count_known == 0:
        print("Specify at least one value")
        return main()

    speed_of_sound, temperature, alt_m, speed, temp, distance = compute_speed_of_sound(
        units, alt_1, temperature, speed_of_sound
    )

    #   Printing Results
    print(f"The speed of sound is: {speed_of_sound} {speed}")
    print(f"The temperature is: {temperature} {temp}")
    print(f"The standard altitude is: {alt_1} {distance}")

    while True:
        again = input("Would you like to run again? (y/n)")
        if again.lower() in ['y','n']:
            break
        print("Error: Invalid input")
    if again == 'y':
        return
    else:
        exit

if __name__ == "__main__":
    while True:
        main()