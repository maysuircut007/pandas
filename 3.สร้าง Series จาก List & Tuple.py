import pandas as pd
data_ls = [10, 20, 30, "maysa kumnerddee", "iphone", True]
ps = pd.Series(data_ls)
print(ps)
data_ls = (10, 20, 30, "maysa kumnerddee", "iphone", "python", True)
ps_tp = pd.Series(data_ls)
print(ps_tp)
