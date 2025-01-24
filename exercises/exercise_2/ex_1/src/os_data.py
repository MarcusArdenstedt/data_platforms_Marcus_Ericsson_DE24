from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

data_path = Path(__file__).parent

df = pd.read_csv(data_path/"athlete_events.csv").head()

print(df)

fig, ax = plt.subplots(figsize=(15,7))
plt.bar(df["Name"], height= df["Age"], color = "darkblue")
plt.xticks(rotation= 45, fontsize= 10)
plt.tight_layout()
fig.savefig(data_path/"Ages")