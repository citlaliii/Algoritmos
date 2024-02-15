import tkinter as tk
from tkinter import filedialog
import pandas as pd

def generar_combinaciones(cadena, alteracion, ventana, salto):
    """
    Generates combinations of the string with the alteration in a sliding window.

    Args:
        cadena: The original string (ensure it's a string).
        alteracion: The alteration to replace.
        ventana: The window size.
        salto: The number of characters to jump between windows.

    Yields:
        The modified strings.
    """

    if not isinstance(cadena, str):
        raise TypeError("Input cadena must be a string.")

    for i in range(0, len(cadena), salto):
        if i + ventana <= len(cadena):
            nueva_cadena = cadena[:i] + alteracion + cadena[i + ventana:]
            yield nueva_cadena

# Create a Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Ask the user to select a file
file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

if not file_path:
    print("No file selected. Exiting.")
    exit()

# Load the CSV data
df = pd.read_csv(file_path)

# Store the original list
lista_original = df["string_a_modificar"].to_list()

# Iterate through each row
for i in range(df.shape[0]):
    # Get information from the current row
    posicion = df.loc[i, "posicion"]
    referencia = df.loc[i, "referencia"]
    alteracion = df.loc[i, "alteracion"]

    # Get the string to modify (handle NaN)
    string_original = df.loc[i, "string_a_modificar"]
    if pd.isna(string_original):
        string_original = ""  # If the value is NaN, assign an empty string

    # Print the original list
    if string_original:
        print("Lista original:", lista_original[i])
    else:
        print("Lista original: No disponible")

    # Generate and print new combinations
    nuevas_cadenas = generar_combinaciones(string_original, alteracion, 3, 2)
    print(f"Posición: {posicion}")
    print(f"Referencia: {referencia}")
    print(f"Alteración: {alteracion}")
    print("--------------------")
    for nueva_cadena in nuevas_cadenas:
        print(nueva_cadena)
    print("--------------------")
