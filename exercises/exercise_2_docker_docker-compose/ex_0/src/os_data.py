import subprocess
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

subprocess.run(["pip", "freeze"])


data_file = Path(__file__).parent/"athlete_events.csv"

df = pd.read_csv(data_file).head()

print(df)

fig, ax = plt.subplots(1)
ax.bar(x= df["Name"], height= df["Age"])
fig.savefig(Path(__file__).parent/"ages.png")
fig.tight_layout()
