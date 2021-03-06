import pandas as pd

class Covid19Data():
    
    DATA_URL = 'https://covid19.mhlw.go.jp/public/opendata/'
    DATA_FILE_NAME = 'newly_confirmed_cases_daily.csv'
    
    def __init__(self):
        self.all_data_df = pd.read_csv(
            f'{self.DATA_URL}{self.DATA_FILE_NAME}', 
            parse_dates=[0])
        
    def reload_all_data(self):
        self.all_data_df = pd.read_csv(
            f'{self.DATA_URL}{self.DATA_FILE_NAME}', 
            parse_dates=[0])
    
    def get_new_cases_covid19(self, prefecture:str):
        data_df = self.all_data_df[['Date', prefecture]]
        return data_df
    
    def get_latest_info(self, prefecture:str):
        return self.all_data_df.tail(1)[['Date', prefecture]]


if __name__ == '__main__':
    c19d = Covid19Data()
    data_kanagawa_df = c19d.get_new_cases_covid19('Kanagawa')
    print(data_kanagawa_df.tail(1))
    latest_all_info = c19d.get_latest_info('ALL')
    print(latest_all_info)
