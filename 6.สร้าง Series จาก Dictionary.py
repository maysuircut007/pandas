import pandas as pd

colors = {"green":"เขียว", "red":"แดง", "yellow":"เหลือง"}
colors_ps = pd.Series(colors)
print(colors_ps, "\n")

age = {"Jonh":30, "somchai":40, "sompong":20}
age_ps = pd.Series(age)
print(age_ps)