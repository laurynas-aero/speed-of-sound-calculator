from logic.constants import CONSTANTS

def compute_temperature_from_altitude(alt, units):
    """
    Computes ISA temperature in the troposphere and tropopause (0-20 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        units (str): "si" or "english"

    Returns:
        float: Temperature (K or R depending on units)
        """
    
    const = _constants(units)
    h11 = const["h11"]
    h20 = const["h20"]
    h32 = const["h32"]
    h47 = const["h47"]
    h51 = const["h51"]
    h71 = const["h71"]

    if alt < h11:
        T = _compute_temperature_from_altitude_troposphere(alt, const)
    elif h11 <= alt < h20:
        T = _compute_temperature_from_altitude_tropopause(alt, const)
    elif h20 <= alt < h32:
        T = _compute_temperature_from_altitude_stratosphere(alt, const)

    return T

def _constants(units):
    """
    Finds constants and formats in dictionary.

    Parameters:
        units (str): "si" or "english"

    Returns:
        Dictionary of constants
        """
    return{
        "T0":CONSTANTS[units]["T0"],
        "T11":CONSTANTS[units]["T11"],
        "T20":CONSTANTS[units]["T20"],
        "h11":CONSTANTS[units]["h11"],
        "h20":CONSTANTS[units]["h20"],
        "h32":CONSTANTS[units]["h32"],
        "h47":CONSTANTS[units]["h47"],
        "h51":CONSTANTS[units]["h51"],
        "h71":CONSTANTS[units]["h71"],
        "L_tropo":CONSTANTS[units]["L_tropo"],
        "L_strato":CONSTANTS[units]["L_strato"]
    }

def _compute_temperature_from_altitude_troposphere(alt, const):
    """
    Computes temperature from alititude in the troposphere (0-11 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Temperature (K or R depending on units)
        """
    T0 = const["T0"]
    L= const["L_tropo"]
    T = T0 + L*alt

    return T

def _compute_temperature_from_altitude_tropopause(alt, const):
    """
    Computes temperature from alititude in the tropopause (11-20 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Temperature (K or R depending on units)
        """
    T11 = const["T11"]
    T = T11

    return T

def _compute_temperature_from_altitude_stratosphere(alt, const):
    """
    Computes temperature from alititude in the stratosphere (20-32 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Temperature (K or R depending on units)
        """
    T20 = const["T20"]
    L = const["L_strato"]
    h20 = const["h20"]
    T = T20 + L*(alt - h20)

    return T