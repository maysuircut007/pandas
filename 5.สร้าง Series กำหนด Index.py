import pandas as pd

items = ["มะม่วง", "กล้วย", "องุ่น"]
idx = [10, 20, 30]

ps = pd.Series(items, index = idx)
print(ps)