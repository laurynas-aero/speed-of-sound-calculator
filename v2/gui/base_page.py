import tkinter as tk
from tkinter import ttk
from logic.units import UNITS, FIELD_TO_QUANTITY

class BaseCalculatorPage(ttk.Frame):
    def build_inputs(self, fields, button_text, command, unit_system, output_key, output_label):
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        self.entries = {}

        for row, (label, key) in enumerate(fields):
            quantity = FIELD_TO_QUANTITY[key]
            unit_suffix = UNITS[unit_system][quantity] if quantity else ""
            full_label = f"{label} {unit_suffix}" if unit_suffix else label
            ttk.Label(self.input_frame, text=full_label).grid(
                row=row, column=0, sticky="e", padx=5, pady=5
            )
            entry = ttk.Entry(self.input_frame)
            entry.grid(row=row, column=1, padx=5, pady=5)
            self.entries[key] = entry

        quantity = FIELD_TO_QUANTITY[output_key]
        unit_suffix = UNITS[unit_system][quantity] if quantity else ""
        
        full_result_label = f"{output_label} - {unit_suffix}" if unit_suffix else output_label

        self.result_label = ttk.Label(self.input_frame, text=full_result_label)
        self.result_label.grid(row=len(fields), column=0, columnspan=2, pady=10)

        ttk.Button(
            self.input_frame,
            text=button_text,
            command=command
        ).grid(row=len(fields)+1, column=0, columnspan=2, pady=10)