import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("temp_precip.csv")
df1 = df.sort_values(by="Precip", ascending=False).head(10)
df1.plot(x="Code", y="Precip", kind="bar")
plt.title("Top 10 países más lluviosos")
plt.tight_layout()
plt.show()
