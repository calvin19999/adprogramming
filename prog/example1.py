inches_str = input ("how many inches of rain have fallen: ")
inches_int = int(inches_str)
inches_float = float(inches_str)
volume = (inches_int/12)*43560
volume_f = (inches_float/12)*43560
gallons = volume * 7.48051945
gallons_f = volume_f * 7.48051945
print(inches_int,"in. rain on 1 acre is", gallons, "gallons")
print(inches_float,"in. rain on 1 acre is", gallons_f, "gallons")
