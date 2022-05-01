import pandas as pd

DATA_URL = 'https://covid19.mhlw.go.jp/public/opendata/'
DATA_FILE_NAME = 'newly_confirmed_cases_daily.csv'

data_df = pd.read_csv(
    f'{DATA_URL}{DATA_FILE_NAME}', 
    parse_dates=[0]
)

print(data_df)