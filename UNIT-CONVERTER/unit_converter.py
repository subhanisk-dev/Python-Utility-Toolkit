# every value is stored with respect to one base unit
length = {"m": 1, "km": 1000, "cm": 0.01, "mm": 0.001, "inch": 0.0254,
          "feet": 0.3048, "mile": 1609.34}
weight = {"kg": 1, "g": 0.001, "mg": 0.000001, "pound": 0.453592, "ounce": 0.0283495}
time_u = {"second": 1, "minute": 60, "hour": 3600, "day": 86400}
 
tables = {"1": ("Length", length), "2": ("Weight", weight), "3": ("Time", time_u)}
 
print("1. Length   2. Weight   3. Time")
choice = input("Select the category : ")
 
if choice in tables:
    name, table = tables[choice]
    print(name, "units available :", ", ".join(table))
    value = float(input("Enter the value  : "))
    frm = input("Convert from     : ").lower()
    to = input("Convert to       : ").lower()
 
    if frm in table and to in table:
        result = value * table[frm] / table[to]
        print(value, frm, "=", round(result, 6), to)
    else:
        print("Unknown unit entered.")
else:
    print("Invalid category.")
