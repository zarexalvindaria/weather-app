# Weather Application

import tkinter as tk
from tkinter import BOTH

# Define window
root = tk.Tk()
root.title("Weather App")
root.iconbitmap("weather.ico")
root.geometry("400x400")
root.resizable(0,0)

# Define fonts and colors
sky_color = "#76c3ef"
grass_color = "#aad207"
output_color = "#dcf0fb"
input_color = "#ecf2ae"
large_font = ("Simsun", 14)
small_font = ("Simsun", 10)

# Define functions


# GUI layout
# Create frames
sky_frame = tk.Frame(root, bg=sky_color, height=250)
grass_frame = tk.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)


# Run root windows
root.mainloop()
