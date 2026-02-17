# Speed of Sound Calculator

A physics-based calculator for determining the speed of sound using temperature or ISA (International Standard Atmosphere) conditions.

## 📘 Overview
This project calculates the speed of sound in air based on user-provided temperature or standard atmospheric height. It is designed as a simple engineering tool to support early-stage aerospace calculations and to build familiarity with numerical modelling.

## 🧪 Physics Background
The speed of sound in air can be estimated using the equation:



$$
a = \sqrt{\gamma R T}
$$



Where:
- a = speed of sound  
- γ = ratio of specific heats (≈ 1.4 for air)  
- R = specific gas constant for air
- T = temperature

Under ISA conditions, temperature varies with altitude, allowing the calculator to estimate speed of sound at different flight levels.

## 🧮 Unit Support
This calculator supports both **SI** and **Imperial/English** units.

### SI Units
- Temperature: Kelvin (K)
- Output: Speed of sound in m/s

### Imperial Units
- Temperature: Rankine (°R)
- Output: Speed of sound in ft/s

The calculator automatically converts between units using:
  - R = 287, J/kg·K for SI  
  - R = 1716, ft·lbf/slug·°R for Imperial

## 🛠️ Features
- Calculate speed of sound from a given temperature  
- (Planned) Calculate speed of sound from altitude using ISA  
- (Planned) Plot speed of sound vs altitude  
- (Planned) Add command-line or GUI interface

## 📂 Project Structure
```
speed-of-sound-calculator/
│── speed_of_sound.py        # Main calculator script (SI + Imperial units)
│── README.md                # Project documentation
```
