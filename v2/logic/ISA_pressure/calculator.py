from logic.constants import CONSTANTS

def compute_pressure_from_altitude_tropo(alt, units):
    """
    Computes ISA pressure in the troposphere (0-11 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        units (str): "si" or "english"

    Returns:
        float: Pressure (Pa or lbf/ft² depending on units)
        """
    P0 = CONSTANTS[units]["P0"]
    T0 = CONSTANTS[units]["T0"]
    L = CONSTANTS[units]["L_tropo"]
    g = CONSTANTS[units]["g"]
    R = CONSTANTS[units]["R"]

    P = P0*(1-((L*alt)/T0))**(g/(R*L))

    return P