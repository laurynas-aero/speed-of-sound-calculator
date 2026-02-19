
CONSTANTS = {
    "si": {
        "gamma": 1.4,
        "R": 287.05,            # J/(kg*K)
        "g": 9.80665,           # m/s^2
        "T0": 288.15,           # K
        "P0": 101325.0,         # Pa
        "L_tropo": -0.0065,     # K/m
        "units": {
            "altitude": "m",
            "temperature": "K",
            "pressure": "Pa",
            "density": "kg/m^3",
            "speed": "m/s"
        }
    },

    "english": {
        "gamma": 1.4,
        "R": 1716.59,           # ft*lbf/(slug*R)
        "g": 32.174,            # ft/s^2
        "T0": 518.67,           # Rankine
        "P0": 2116.22,          # lbf/ft^2
        "L_tropo": -0.00356616, # R/ft
        "units": {
            "altitude": "ft",
            "temperature": "R",
            "pressure": "lbf/ft^2",
            "density": "slug/ft^3",
            "speed": "ft/s"
        }
    }
}