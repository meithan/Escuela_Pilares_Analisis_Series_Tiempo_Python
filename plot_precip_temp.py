import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("temp_precip.csv")
print(df)

mostrar_etiquetas = True

if mostrar_etiquetas:
  colors = ["red" if c == "MEX" else "C0" for c in df["Code"]]
  plt.scatter(df["Temp"], df["Precip"], color=colors)
else:
  plt.scatter(df["Temp"], df["Precip"])

plt.xlabel("Temperatura (°C)")
plt.ylabel("Precipitación (mm)")
plt.title("Precipitación vs temperatura de países del mundo")
plt.grid(ls=":")

if mostrar_etiquetas:
  for code, row in df.iterrows():
    plt.text(row["Temp"], row["Precip"], row["Code"], fontsize=8, ha='center', va='bottom')

plt.tight_layout()
plt.show()
