import tkinter as tk
from tkinter import ttk
from gui.base_page import BaseCalculatorPage
from logic.units import UNITS

# Import your physics engine
from logic.Mach_number.calculator import (
    compute_mach_number_from_altitude,
    compute_mach_number_from_speed_of_sound,
    compute_mach_number_from_temperature,
    compute_speed_from_altitude,
    compute_speed_from_mach_number,
    compute_speed_from_temperature,
    compute_speed_of_sound_from_mach_number
)
from logic.speed_of_sound.calculator import (
    compute_speed_of_sound_from_temperature,
)

class MachCalculatorPage(BaseCalculatorPage):
    def __init__(self, parent):
        super().__init__(parent)
        

        ttk.Label(self, text="Mach Calculator", font=("Segoe UI", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(10,20))
        self.method_var = tk.StringVar(value="Altitude + Speed")

        self.unit_var = tk.StringVar(value="si")
        self.unit_var.trace_add("write", lambda *args: self.update_fields())

        ttk.Checkbutton(
            self,
            text="Use English Units",
            variable=self.unit_var,
            onvalue="english",
            offvalue="si"
        ).grid(row=0, column=2, padx=10)

        ttk.Label(self, text="Compute:").grid(row=1, column=0, sticky="e", padx=5, pady=5)

        method_dropdown = ttk.OptionMenu(
            self,
            self.method_var,
            "Mach from Altitude + Speed",
            "Mach from Temperature + Speed",
            "Mach from Speed of Sound + Speed",
            "Speed from Mach + Speed of Sound",
            "Speed from Mach + Temperature",
            "Speed from Mach + Altitude",
            "Speed of Sound from Mach + Speed",
            command=self.update_fields
        )
        method_dropdown.grid(row=1, column=1, padx=5, pady=5)

        self.input_frame = ttk.Frame(self)
        self.input_frame.grid(row=2, column=0, columnspan=2, pady=10)

        unit_system = self.unit_var.get()

        self.build_inputs(
                [("Altitude:","alt"),("Speed:", "speed")],
                "Compute Mach",
                self.compute_mach,
                unit_system,
                "mach",
                "Mach:"
            )

    def update_fields(self, *args):
        method = self.method_var.get()
        unit = self.unit_var
        unit_system = self.unit_var.get()
        
        if method == "Mach from Altitude + Speed":
            self.build_inputs(
                [("Altitude:","alt"),("Speed:", "speed")],
                "Compute Mach",
                self.compute_mach,
                unit_system,
                "mach",
                "Mach:"
            )
        elif method == "Mach from Temperature + Speed":
            self.build_inputs(
                [("Temperature:","temp"),("Speed:", "speed")],
                "Compute Mach",
                self.compute_mach,
                unit_system,
                "mach",
                "Mach:"
            )
        elif method == "Mach from Speed of Sound + Speed":
            self.build_inputs(
                [("Speed of Sound:","sos"),("Speed:", "speed")],
                "Compute Mach",
                self.compute_mach,
                unit_system,
                "mach",
                "Mach:"
            )
        elif method == "Speed from Mach + Speed of Sound":
            self.build_inputs(
                [("Mach:","mach"),("Speed of Sound:", "sos")],
                "Compute Speed",
                self.compute_speed,
                unit_system,
                "speed",
                "Speed:"
            )
        elif method == "Speed from Mach + Temperature":
            self.build_inputs(
                [("Mach:","mach"),("Temperature:", "temp")],
                "Compute Speed",
                self.compute_speed,
                unit_system,
                "speed",
                "Speed:"
            )
        elif method == "Speed from Mach + Altitude":
            self.build_inputs(
                [("Mach:","mach"),("Altitude:", "alt")],
                "Compute Speed",
                self.compute_speed,
                unit_system,
                "speed",
                "Speed:"
            )
        elif method == "Speed of Sound from Mach + Speed":
            self.build_inputs(
                [("Mach:","mach"),("Speed:", "speed")],
                "Compute Speed of Sound",
                self.compute_sos,
                unit_system,
                "sos",
                "Speed of Sound:"
            )

    def compute_mach(self):
        method = self.method_var.get()
        units = self.unit_var.get()

        try:
            if method == "Mach from Altitude + Speed":
                alt = float(self.entries["alt"].get())
                speed = float(self.entries["speed"].get())

                mach = compute_mach_number_from_altitude(alt, speed, units)

            elif method == "Mach from Temperature + Speed":
                temp = float(self.entries["temp"].get())
                speed = float(self.entries["speed"].get())

                mach = compute_mach_number_from_temperature(temp, speed, units)

            elif method == "Mach from Speed of Sound + Speed":
                sos = float(self.entries["sos"].get())
                speed = float(self.entries["speed"].get())

                mach = compute_mach_number_from_speed_of_sound(sos, speed)

            self.result_label.config(text=f"Mach: {mach:.3f}")
        
        except ValueError:
            self.result_label.config(text="Invalid input")

    def compute_speed(self):
        method = self.method_var.get()
        units = self.unit_var.get()

        try:
            if method == "Speed from Mach + Speed of Sound":
                mach = float(self.entries["mach"].get())
                sos = float(self.entries["sos"].get())

                speed = compute_speed_from_mach_number(mach, sos)

            elif method == "Speed from Mach + Temperature":
                mach = float(self.entries["mach"].get())
                temp = float(self.entries["temp"].get())

                speed = compute_speed_from_temperature(mach, temp, units)

            elif method == "Speed from Mach + Altitude":
                mach = float(self.entries["mach"].get())
                alt = float(self.entries["alt"].get())

                speed = compute_speed_from_altitude(mach, alt, units)

            unit_suffix = UNITS[units]["speed"]
            self.result_label.config(text=f"Speed: {speed:.3f} {unit_suffix}")
        
        except ValueError:
            self.result_label.config(text="Invalid input")

    def compute_sos(self):
        method = self.method_var.get()
        units = self.unit_var.get()

        try:
            if method == "Speed of Sound from Mach + Speed":
                mach = float(self.entries["mach"].get())
                speed = float(self.entries["speed"].get())

                sos = compute_speed_of_sound_from_mach_number(speed, mach)

            unit_suffix = UNITS[units]["speed"]
            self.result_label.config(text=f"Speed of Sound: {sos:.3f} {unit_suffix}")
        
        except ValueError:
            self.result_label.config(text="Invalid input")

class SpeedOfSoundPage(ttk.Frame): 
    def __init__(self, parent): 
        super().__init__(parent) 
        ttk.Label(self, text="Speed of Sound Calculator", font=("Segoe UI", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(10, 20)) 
        ttk.Label(self, text="Temperature:").grid(row=1, column=0, sticky="e", padx=5, pady=5) 
        
        self.temp_entry = ttk.Entry(self) 
        self.temp_entry.grid(row=1, column=1, padx=5, pady=5) 
        
        self.result_label = ttk.Label(self, text="Speed of Sound: —") 
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10) 
        
        ttk.Button(
            self, 
            text="Compute Speed of Sound", 
            command=self.compute_sos
            ).grid(row=3, column=0, columnspan=2, pady=10)

    def compute_sos(self):
        try:
            temp = float(self.temp_entry.get())

            sos = compute_speed_of_sound_from_temperature(temp, "si")

            self.result_label.config(text=f"Speed of Sound: {sos:.3f}")
        
        except ValueError:
            self.result_label.config(text="Invalid input")

class App(tk.Tk):
    def __init__ (self):
        super().__init__()

        self.title("Aero Calculator Suite")
        self.geometry("500x400")

        self.page_var = tk.StringVar(value="Mach Calculator")

        top_bar = ttk.Frame(self)
        top_bar.pack(side="top", fill="x", padx=10, pady=10)

        ttk.Label(top_bar, text="Select calculator:").pack(side="left")

        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)

        self.pages = { 
            "Mach Calculator": MachCalculatorPage(self.container), 
            "Speed of Sound": SpeedOfSoundPage(self.container), 
            }

        for page in self.pages.values():
            page.place(relx=0, rely=0, relwidth=1, relheight=1)

        dropdown = ttk.OptionMenu(
            top_bar,
            self.page_var,
            "Mach Calculator",
            *self.pages.keys(),
            command=self.show_page,
        )
        dropdown.pack(side="left", padx=10)

        self.show_page("Mach Calculator")

    def show_page(self, name):
        page = self.pages[name]
        page.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()