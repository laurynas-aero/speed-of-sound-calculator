from ..speedofsound_calculator.main import main
from ..speedofsound_calculator.plots import plot_speed_vs_temperature_si, plot_speed_vs_altitude_english, plot_speed_vs_altitude_si, plot_speed_vs_temperature_english

def main_menu():
    while True:
        print("\n=== Speed of Sound / ISA Calculator ===") 
        print("1. Compute speed of sound / temperature / altitude") 
        print("2. Plot speed of sound vs temperature") 
        print("3. Plot speed of sound vs altitude") 
        print("4. Exit")

        choice = input("Choose an option:")

        if choice == "1":
            main()
        elif choice == "2": 
            while True:
                print("\n=== Speed of Sound vs Temperature Graph ===") 
                print("1. SI units") 
                print("2. English units") 
                print("3. Return")

                choice = input("Choose an option:")

                if choice == "1":
                    u_min_T = float(input("Minimum temperature:"))
                    u_max_T = float(input("Maximum temperature:"))
                    if u_min_T < u_max_T:
                        plot_speed_vs_temperature_si(u_min_T, u_max_T)
                    else:
                        print("Error: Your minimum value must be less than the maximum")
                elif choice =="2":
                    u_min_T = float(input("Minimum temperature:"))
                    u_max_T = float(input("Maximum temperature:"))
                    if u_min_T < u_max_T:
                        plot_speed_vs_temperature_english(u_min_T, u_max_T)
                    else:
                        print("Error: Your minimum value must be less than the maximum")
                    
                elif choice == "3":
                    break
                else:
                    print("Invalid choice")

        elif choice == "3": 
            while True:
                print("\n=== Speed of Sound vs Altitude Graph ===") 
                print("1. SI units") 
                print("2. English units") 
                print("3. Return")

                choice = input("Choose an option:")

                if choice == "1":
                    u_min_h = float(input("Minimum altitude:"))
                    u_max_h = float(input("Maximum altitude:"))
                    if u_min_h < u_max_h:
                        plot_speed_vs_altitude_si(u_min_h, u_max_h)
                    else:
                        print("Error: Your minimum value must be less than the maximum")

                elif choice =="2":
                    u_min_h = float(input("Minimum altitude:"))
                    u_max_h = float(input("Maximum altitude:"))
                    if u_min_h < u_max_h:
                        plot_speed_vs_altitude_english(u_min_h, u_max_h)
                    else:
                        print("Error: Your minimum value must be less than the maximum")

                elif choice == "3":
                    break
                else:
                    print("Invalid choice") 

        elif choice == "4": 
            break 
        else: 
            print("Invalid choice")

if __name__ == "__main__": 
    main_menu()