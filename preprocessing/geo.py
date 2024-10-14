import pandas as pd
import utils

DATA_PATH = '../ma-data/data/MAv1_CSVS'

# Array of desired states
states = [
    'AK'
]

for state in states:
    df = pd.read_csv(f'{DATA_PATH}/{state}.csv')
    print(list(df.columns))
    # print(len(list(df['Unnamed: 0'])))

    for item in df['Footprint2D']:
        pointlist = [utils.Location.parse(p) for p in item.split('_')]
        for p in pointlist:
            p.print()
        break
    # print(*df['Area2D'])
