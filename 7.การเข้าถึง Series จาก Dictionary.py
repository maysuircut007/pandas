import pandas as pd
num = [10, 20, 30, 40]
num_ps = pd.Series(num)
print(num_ps,"\n")
print("การเข้าถึงข้อมูล", num_ps[2], "\n")

colors = {"red":"แดง", "green":"เขียว", "yellow":"เหลือง"}
cl_ps = pd.Series(colors)
print(cl_ps, "\n")
print("การเข้าถึงข้อมูล",cl_ps["red"])