import numpy as np
import matplotlib.pyplot as plt

from .calculator import compute_speed_of_sound

def plot_speed_vs_temperature_si(min_T, max_T):
    T = np.linspace(min_T, max_T, 200)
    
    a = [] 
    for t in T: 
        speed, temp, alt, speed_unit, temp_unit, dist_unit = compute_speed_of_sound(
            "si", None, t, None
            ) 
        a.append(speed)
    
    plt.figure(figsize=(8, 5))
    plt.plot(T, a, color="blue", linewidth=2, label="Speed of sound")

    plt.xlabel("Temperature (K)")
    plt.ylabel("Speed of Sound (m/s)")
    plt.title("Speed of Sound vs Temperature")

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    
    plt.show()

def plot_speed_vs_altitude_si(min_h, max_h):
    h = np.linspace(min_h, max_h, 300)

    a=[]
    for altitude in h: 
        speed, temp, alt_m, speed_unit, temp_unit, dist_unit = compute_speed_of_sound(
            "si", altitude, None, None) 
        a.append(speed)

    plt.figure(figsize=(8, 5))
    plt.plot(h, a, color="red", linewidth=2, label="Speed of sound (ISA)")

    plt.xlabel("Altitude (m)")
    plt.ylabel("Speed of Sound (m/s)")
    plt.title("Speed of Sound vs Altitude (ISA Model)")

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    
    plt.show()

def plot_speed_vs_temperature_english(min_T, max_T):
    T = np.linspace(min_T, max_T, 200)
    
    a = [] 
    for t in T: 
        speed, temp, alt, speed_unit, temp_unit, dist_unit = compute_speed_of_sound(
            "english", None, t, None
            ) 
        a.append(speed)
    
    plt.figure(figsize=(8, 5))
    plt.plot(T, a, color="blue", linewidth=2, label="Speed of sound")
    plt.xlabel("Temperature (R)")
    plt.ylabel("Speed of Sound (ft/s)")
    plt.title("Speed of Sound vs Temperature")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()

def plot_speed_vs_altitude_english(min_h, max_h):
    h = np.linspace(min_h, max_h, 300)

    a=[]
    for altitude in h: 
        speed, temp, alt_m, speed_unit, temp_unit, dist_unit = compute_speed_of_sound(
            "english", altitude, None, None) 
        a.append(speed)

    plt.figure(figsize=(8, 5))
    plt.plot(h, a, color="red", linewidth=2, label="Speed of sound (ISA)")

    plt.xlabel("Altitude (ft)")
    plt.ylabel("Speed of Sound (ft/s)")
    plt.title("Speed of Sound vs Altitude (ISA Model)")

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    
    plt.show()

if __name__ == "__main__": 
    plot_speed_vs_altitude_si()