import pandas as pd
import sys
from pathlib import Path
import matplotlib.pylab as plt

print("\n\n")
print(f"{sys.version =}")

data = {
    "name": ["Erik", "Anna", "Johan", "Lisa", "Oskar"],
    "age": [25, 34, 40, 25, 50],
    "city": ["Stockholm", "Göteborg", "Malmö", "Uppsala", "Lund"],
    "salary_sek": [45000, 32000, 20000, 25000, 30000]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(1)
ax.bar(x= df["name"], height= df["age"])
fig.savefig(Path(__file__).parent / "ages.png")
fig.tight_layout()

print(df.columns)

