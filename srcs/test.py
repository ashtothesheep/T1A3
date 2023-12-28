import pandas as pd

df = pd.DataFrame(columns=['Name', 'Designer', 'Yarn Weight', 'Meterage', 'Gauge', 'Needle Sizes', 'Category'])
try:
    df_existing = pd.read_csv("docs/Patterns.csv")
    df = pd.append([df_existing, pd.DataFrame(new_pattern)], ignore_index=True)