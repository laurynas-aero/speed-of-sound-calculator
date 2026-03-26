# Aero Calculator Suite

A series of modular aerospace and atmospheric engineering calculators.

---

## 📘 Overview

The **Aero Calculator Suite** is a growing set of physics-based tools designed for:

- Aerospace engineering students
- Pilots and aviation enthusiasts
- Physics learners
- Anyone needing quick, reliable engineering calculations

Each calculator is self-contained, readable, and built around real aerodynamic and atmospheric equations.

---

## 🧰 Included Calculators

### 1. Speed of Sound Calculator

- Compute speed of sound from temperature
- Compute temperature from speed of sound
- Compute speed of sound from altitude

### 2. Mach Number Calculator

- Compute Mach number from temperature and speed
- Compute Mach number from altitude and speed
- Compute Mach number from speed of sound and speed
- Compute speed from Mach number and speed of sound
- Compute speed from Mach number and temperature
- Compute speed from Mach number and altitude
- Compute speed of sound from Mach number and speed

### 3. ISA Temperature Calculator

- Compute temperature from altitude up to stratosphere (full coverage planned...)

### 4. ISA Pressure Calculator

- Compute pressure from altitude up to troposphere (full coverage planned...)

---

## 🧮 Unit Support

Supports both **SI** and **English** units.

### SI Units
- Temperature: K  
- Speed: m/s
- Distance: m

### English Units
- Temperature: °R  
- Speed: ft/s
- Distance: ft 

---

### Planned Enhancements
- Graphing
- Full ISA altitude model
- Lift and Drag calculators  
- Packaging as a pip‑installable module  

---

## 📂 Project Structure
```
Aero-Calculator-Suite/
│
├── README.md
│
├── v1/
│   ├── .gitignore
│   ├── run.py
│   ├── ui.py
│   │
│   ├── assets/
│   │   └── SpeedofSound_Calculator-FlowDiagram.png
│   │
│   └── speedofsound_calculator/
│       ├── calculator.py
│       ├── main.py
│       └── plots.py
│
└── v2/
    ├── .gitignore
    ├── main.py
    │
    ├── .vscode/
    │
    ├── gui/
    │   ├── base_page.py
    │   └── main_gui.py
    │
    └── logic/
        ├── constants.py
        ├── input_checker.py
        ├── units.py
        ├── __init__.py
        │
        ├── ISA_pressure/
        │   ├── calculator.py
        │   └── __init__.py
        │
        ├── ISA_temperature/
        │   ├── calculator.py
        │   └── __init__.py
        │
        ├── Mach_number/
        │   ├── calculator.py
        │   └── __init__.py
        │
        └── Speed_of_sound/
            ├── calculator.py
            └── __init__.py
```

## 🚀 Getting Started
Run the calculator:
```
python speedofsound_calculator/v2/main.py
```

## 📄 License
<<<<<<< HEAD
MIT License - free to use, modify, and learn from.
