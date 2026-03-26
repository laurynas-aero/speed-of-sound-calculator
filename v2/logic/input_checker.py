from .constants import CONSTANTS

def check_inputs(var, num, units):

    try:
        num = to_float(num)

        if var == "alt":
            alt = num

            h86 = CONSTANTS[units]["h86"]

            if 0 > alt or alt > h86:
                return("Invalid input: Altitude must be between 0-86000 m or 0-282150 ft")
            else:
                return

        elif var == "speed" or "sos":
            speed = num

            if 0 > speed:
                return("Invalid input: Speed must be positive")
            else:
                return

        elif var == "mach":
            mach = num

            if 0 > mach:
                return("Invalid input: Mach number must be positive")
            else:
                return

        elif var == "temp":
            temp = num

            if 0 > temp:
                return("Invalid input: Temperature must be positive")
            else:
                return
    except:
        return("Invalid input: Input could not be converted to float.")
    
    

def to_float(num) -> float:
    str(num)
    # Normalize unicode minus signs to ASCII "-"
    num = num.replace("−", "-").replace("–", "-")

    # Remove normal and non-breaking spaces
    num = num.replace(" ", "").replace("\u00A0", "")

    # Convert comma decimal separator to dot
    num = num.replace(",", ".")

    return float(num)

