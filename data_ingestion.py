import pandas as pd
import os

folder = "data/raw"

files = os.listdir(folder)

for file in files:

    if file.endswith(".csv"):

        print("\n" + "="*50)
        print("FILE:", file)

        path = os.path.join(folder,file)

        df = pd.read_csv(path)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())
        print(df.isnull().sum())
        print(df.duplicated().sum())