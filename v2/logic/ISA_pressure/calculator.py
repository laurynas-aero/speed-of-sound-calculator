from logic.constants import CONSTANTS

def compute_pressure_from_altitude(alt, units):
    """
    Computes ISA pressure.

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        units (str): "si" or "english"

    Returns:
        float: Pressure (Pa or lbf/ft² depending on units)
        """

    P = _compute_pressure_from_altitude_troposphere(alt, units)

    return P

def _consts(units):
    """
    Finds constants.

    Parameters:
        units (str): "si" or "english"

    Returns:
        Constants
        """
    P0 = CONSTANTS[units]["P0"]
    T0 = CONSTANTS[units]["T0"]
    L = CONSTANTS[units]["L_tropo"]
    g = CONSTANTS[units]["g"]
    R = CONSTANTS[units]["R"]

    return P0, T0, L, g, R

def _compute_pressure_from_altitude_troposphere(alt, units):
    """
    Computes pressure from alititude in the troposphere (0-11 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Pressure (Pa or lbf/ft² depending on units)
        """
    P0, T0, L, g, R = _consts(units)
    P = P0*(1-((L*alt)/T0))**(g/(R*L))
    
    return P