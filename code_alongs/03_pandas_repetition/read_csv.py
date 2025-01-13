import pandas as pd
from pathlib import Path

data_path = (Path(__file__).parent / "data")

df = pd.read_csv(data_path / "calories.csv")

print(Path(__file__))