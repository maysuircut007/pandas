import pandas as pd
import numpy as np

ndata = np.array([10, 20, 30, "maysa kumnerdde", "iphone", True])
print(ndata)
print(ndata.dtype)
ps = pd.Series(ndata)
print(ps)