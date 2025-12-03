# Film Sim
film = {
    "Film Simulation": {
        1: "Provia",
        2: "Velvia",
        3: "Astia",
        4: "Classic Chrome",
        5: "Pro Neg Hi",
        6: "Pro Neg Std",
        7: "Classic Neg",
        8: "Nostalgic Neg",
        9: "Eterna",
        10: "Eterna Bleach Bypass",
        11: "Reala Ace",
        12: "Monochrome",
        13: "Monochrome + Y Filter",
        14: "Monochrome + R Filter",
        15: "Monochrome + G Filter",
        16: "Acros",
        17: "Acros + Y Filter",
        18: "Acros + R Filter",
        19: "Acros + G Filter",

    }
}
print("\n---------------------------------")
print("Film Simulation: \n")
for index, fs in film["Film Simulation"].items():
    print(f"{index}. {fs}")

while True:
    numero = input("\n>> Choose your Film Simulation: ").strip()
    if not numero.isdigit():
        print("Error: Type a number, not a character.")
        continue

    numero = int(numero)
    if numero in film["Film Simulation"]:
        fs_elegido = film["Film Simulation"][numero]
        print(f"\nYou selected: {fs_elegido}")
        break
    else:
        print("Error! Type a valid number.")

# Grain
grain = {
    "Grain Level": {
        1: "Off",
        2: "Weak - Small",
        3: "Weak - Large",
        4: "Strong - Small",
        5: "Strong - Large"
    }
}
print("\n---------------------------------")
print("Grain Level: \n")
for index, gl in grain["Grain Level"].items():
    print(f"{index}. {gl}")

while True:
    numero = input("\n>> Choose you Grain level: ").strip()
    if not numero.isdigit():
        print("Error! Type a number, not a character.")
        continue

    numero = int(numero)
    if numero in grain["Grain Level"]:
        gl_elegido = grain["Grain Level"][numero]
        print(f"\nYou selected: {gl_elegido}")
        break
    else:
        print("Error! Type a valid number")

# Color Chrome FX
chrome = {
    "Color Chrome": {
        1: "Off",
        2: "Weak",
        3: "Strong"
    }
}
print("\n---------------------------------")
print("Color Chrome FX: \n")
for index, cc in chrome["Color Chrome"].items():
    print(f"{index}. {cc}")

while True:
    numero = input("\n>> Choose Your Color Chrome Level: ").strip()
    if not numero.isdigit():
        print("Error! Type a number, not a character")
        continue

    numero = int(numero)
    if numero in chrome["Color Chrome"]:
        cc_elegido = chrome["Color Chrome"][numero]
        print(f"You selected: {cc_elegido}")
        break
    else:
        print("Error! Type a valid number")

# Color Chrome Blue FX
blue = {
    "Blue Chrome": {
        1: "Off",
        2: "Weak",
        3: "Strong"
    }
}
print("\n---------------------------------")
print("Color Chrome Blue FX: \n")
for index, cb in blue["Blue Chrome"].items():
    print(f"{index}. {cb}")

while True:
    numero = input("\n>> Choose Your Color Chrome Blue Level: ").strip()
    if not numero.isdigit():
        print("Error! Type a number, not a character")
        continue

    numero = int(numero)
    if numero in blue["Blue Chrome"]:
        cb_elegido = blue["Blue Chrome"][numero]
        print(f"You selected: {cb_elegido}")
        break
    else:
        print("Error! Type a valid number")

# White Balance
white = {
    "White Balance": {
        1: "White Priority",
        2: "Auto",
        3: "Ambience Priority",
        4: "Kelvin",
        5: "Daylight",
        6: "Tungsten"
    }
}
print("\n---------------------------------")
print("White Balance: \n")
for index, wb in white["White Balance"].items():
    print(f"{index}. {wb}")

while True:
    numero = input("\n>> Choose Your White Balance: ").strip()
    if not numero.isdigit():
        print("Error! Type a number, not a character")
        continue

    numero = int(numero)
    if numero in white["White Balance"]:
        wb_elegido = white["White Balance"][numero]
        print(f"You selected: {wb_elegido}")

        if wb_elegido == "Kelvin":
            while True:
                kelvin_txt = input(
                    "\nEnter Kelvin value (e.g., 5200): ").strip()
                if not kelvin_txt.isdigit():
                    print("Error! Enter a numeric value (e.g., 5200).")
                    continue
                kelvin = int(kelvin_txt)
                break

            while True:
                try:
                    red_offset = int(input("Red offset (+/-4): ").strip())
                    blue_offset = int(input("Blue offset (+/-4): ").strip())
                    break
                except ValueError:
                    print("Error! Offsets must be numbers between -4 and +4.")
                    continue

            wb_elegido = f"{kelvin}K, {red_offset:+} Red, {blue_offset:+} Blue"

        print(f"\nYou selected: {wb_elegido}")
        break
    else:
        print("Error! Type a valid number.")


# Dynamic Range
dynamic = {
    "Dynamic Range": {
        1: "DR 100",
        2: "DR 200",
        3: "DR 400"
    }
}

print("\n---------------------------------")
print("Dynamic Range: \n")
for index, dr in dynamic["Dynamic Range"].items():
    print(f"{index}. {dr}")

while True:
    numero = input("\n>> Choose your Dynamic Range: ").strip()
    if not numero.isdigit():
        print("Error: Debes ingresar un número, no texto.")
        continue

    numero = int(numero)
    if numero in dynamic["Dynamic Range"]:
        dr_elegido = dynamic["Dynamic Range"][numero]
        print(f"\nYou selected: {dr_elegido}")
        break
    else:
        print("Número inválido. Intenta nuevamente.")

# Highlight
high = {
    "Highlight": {
        1: "-4",
        2: "-3.5",
        3: "-3",
        4: "-2.5",
        5: "-2",
        6: "-1.5",
        7: "-1",
        8: "-0.5",
        9: "0",
        10: "+0.5",
        11: "+1",
        12: "+1.5",
        13: "+2",
        14: "+2.5",
        15: "+3",
        16: "+3.5",
        17: "+4"
    }
}

print("\n---------------------------------")
print("Highlight: \n")
for index, hl in high["Highlight"].items():
    print(f"{index}. {hl}")

while True:
    numero = input("\n>> Choose your Highlight: ").strip()
    if not numero.isdigit():
        print("Error: Type a number, not a character.")
        continue

    numero = int(numero)
    if numero in high["Highlight"]:
        hl_elegido = high["Highlight"][numero]
        print(f"\nYou selected: {hl_elegido}")
        break
    else:
        print("Error! Invalid number. Try again.")

# Shadow
shadow = {
    "Shadow": {
        1: "-4",
        2: "-3.5",
        3: "-3",
        4: "-2.5",
        5: "-2",
        6: "-1.5",
        7: "-1",
        8: "-0.5",
        9: "0",
        10: "+0.5",
        11: "+1",
        12: "+1.5",
        13: "+2",
        14: "+2.5",
        15: "+3",
        16: "+3.5",
        17: "+4"
    }
}

print("\n---------------------------------")
print("Shadow: \n")
for index, sd in shadow["Shadow"].items():
    print(f"{index}. {sd}")

while True:
    numero = input("\n>> Choose your Shadow: ").strip()
    if not numero.isdigit():
        print("Error: Type a number, not a character.")
        continue

    numero = int(numero)
    if numero in shadow["Shadow"]:
        sd_elegido = shadow["Shadow"][numero]
        print(f"\nYou selected: {sd_elegido}")
        break
    else:
        print("Error! Invalid number. Try again.")

# Sharpness
sharp = {
    "Sharpness": {
        1: "+4",
        2: "+3",
        3: "+2",
        4: "+1",
        5: "0",
        6: "-1",
        7: "-2",
        8: "-3",
        9: "-4"
    }
}

print("\n---------------------------------")
print("Sharpness: \n")
for index, sh in sharp["Sharpness"].items():
    print(f"{index}. {sh}")

while True:
    numero = input("\n>> Choose your Sharpness level: ").strip()
    if not numero.isdigit:
        print("Error! Type a number, not a character.")
        continue

    numero = int(numero)
    if numero in sharp["Sharpness"]:
        sh_elegido = sharp["Sharpness"][numero]
        print(f"You selected: {sh_elegido}")
        break
    else:
        print("Error! invalid number. Try again")

# High ISO NR
iso_nr = {
    "High ISO NR": {
        1: "+4",
        2: "+3",
        3: "+2",
        4: "+1",
        5: "0",
        6: "-1",
        7: "-2",
        8: "-3",
        9: "-4"
    }
}

print("\n---------------------------------")
print("High ISO NR: \n")
for index, nr in iso_nr["High ISO NR"].items():
    print(f"{index}. {nr}")

while True:
    numero = input("\n>> Choose your High ISO NR Level: ").strip()
    if not numero.isdigit:
        print("Error! Type a number, not a character.")
        continue

    numero = int(numero)
    if numero in iso_nr["High ISO NR"]:
        iso_nr_elegido = iso_nr["High ISO NR"][numero]
        print(f"You selected: {iso_nr_elegido}")
        break
    else:
        print("Error! Invalid number. Try again.")

# Clarity
clarity = {
    "Clarity": {
        1: "+4",
        2: "+3",
        3: "+2",
        4: "+1",
        5: "0",
        6: "-1",
        7: "-2",
        8: "-3",
        9: "-4"
    }
}

print("\n---------------------------------")
print("Clarity: \n")
for index, cl in clarity["Clarity"].items():
    print(f"{index}. {cl}")

while True:
    numero = input("\n>> Choose your Clarity level: ").strip()
    if not numero.isdigit():
        print("Error! Type a number, not a character.")
        continue

    numero = int(numero)
    if numero in clarity["Clarity"]:
        cl_elegido = clarity["Clarity"][numero]
        print(f"You selected: {cl_elegido}")
        break
    else:
        print("Invalid number. Try again.")

# ISO
iso = {
    "ISO": {
        1: "Manual",
        2: "Auto"
    }
}
print("\n---------------------------------")
print("ISO Type: \n")
for index, i in iso["ISO"].items():
    print(f"{index}. {i}")

while True:
    numero = input("\n>> Choose your type of ISO: ").strip()
    if not numero.isdigit():
        print("Error! Type a number, not a character")
        continue

    numero = int(numero)
    if numero in iso["ISO"]:
        iso_elegido = iso["ISO"][numero]
        print(f"\nYou selected: {iso_elegido}")
        break
    else:
        print("Error! type a valid number")


# Resumen
print("\n--------------------------------------")
print("\nRESUMEN: ")
print(f"Film Simulation: {fs_elegido}")
print(f"Grain Level: {gl_elegido}")
print(f"Color Chrome: {cc_elegido}")
print(f"Color Chrome Blue: {cb_elegido}")
print(f"White Balance: {wb_elegido}")
print(f"Dynamic Range: {dr_elegido}")
print(f"Highlight: {hl_elegido}")
print(f"Shadow: {sd_elegido}")
print(f"Sharpness: {sh_elegido}")
print(f"Iso Noise Reduction: {iso_nr_elegido}")
print(f"Clarity: {cl_elegido}")
print(f"ISO: {iso_elegido}")
