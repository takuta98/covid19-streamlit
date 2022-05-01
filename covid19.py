import pandas as pd

class Covid19Data():
    
    DATA_URL = 'https://covid19.mhlw.go.jp/public/opendata/'
    DATA_FILE_NAME = 'newly_confirmed_cases_daily.csv'
    
    def get_all_data(self):
        data_df = pd.read_csv(
            f'{self.DATA_URL}{self.DATA_FILE_NAME}', 
            parse_dates=[0]
        )
        return data_df
    
    def get_new_cases_covid19(self, prefecture:str):
        all_data_df = self.get_all_data()
        data_df = all_data_df[prefecture]
        return data_df
    
    def get_date(self):
        all_data_df = self.get_all_data()
        date_df = all_data_df['Date']
        return date_df


if __name__ == '__main__':
    c19d = Covid19Data()
    data_kanagawa_df = c19d.get_new_cases_covid19('Kanagawa')
    print(data_kanagawa_df)
    date_df = c19d.get_date()
    print(date_df)
