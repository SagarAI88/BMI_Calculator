import input
import bmi_cal

w = input.weight

h = input.height

print("Weight in kg is",w)

print("Height in meters is",h)

Body_mass_index = bmi(w,h)

print("Body mass index of the person:",Body_mass_index)
