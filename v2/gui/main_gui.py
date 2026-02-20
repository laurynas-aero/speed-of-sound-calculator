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
    MODES = {
    "Mach from Altitude + Speed": {
        "fields": [("Altitude:", "alt"), ("Speed:", "speed")],
        "button": "Compute Mach",
        "command": "compute_mach",
        "output_key": "mach",
        "output_label": "Mach:"
    },
    "Mach from Temperature + Speed": {
        "fields": [("Temperature:", "temp"), ("Speed:", "speed")],
        "button": "Compute Mach",
        "command": "compute_mach",
        "output_key": "mach",
        "output_label": "Mach:"
    },
    "Mach from Speed of Sound + Speed": {
        "fields": [("Speed of Sound:", "sos"), ("Speed:", "speed")],
        "button": "Compute Mach",
        "command": "compute_mach",
        "output_key": "mach",
        "output_label": "Mach:"
    },
    "Speed from Mach + Speed of Sound": {
        "fields": [("Mach:", "mach"), ("Speed of Sound:", "sos")],
        "button": "Compute Speed",
        "command": "compute_speed",
        "output_key": "speed",
        "output_label": "Speed:"
    },
    "Speed from Mach + Temperature": {
        "fields": [("Mach:", "mach"), ("Temperature:", "temp")],
        "button": "Compute Speed",
        "command": "compute_speed",
        "output_key": "speed",
        "output_label": "Speed:"
    },
    "Speed from Mach + Altitude": {
        "fields": [("Mach:", "mach"), ("Altitude:", "alt")],
        "button": "Compute Speed",
        "command": "compute_speed",
        "output_key": "speed",
        "output_label": "Speed:"
    },
    "Speed of Sound from Mach + Speed": {
        "fields": [("Mach:", "mach"), ("Speed:", "speed")],
        "button": "Compute Speed of Sound",
        "command": "compute_sos",
        "output_key": "sos",
        "output_label": "Speed of Sound:"
    }
}
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
        
        self.update_fields()

    def update_fields(self, *args):
        method = self.method_var.get()
        config = self.MODES[method]
        unit_system = self.unit_var.get()
        
        self.build_inputs(
            config["fields"],
            config["button"],
            getattr(self, config["command"]),
            unit_system,
            config["output_key"],
            config["output_label"]
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