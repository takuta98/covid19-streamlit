import locale
locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

class LatestInfo():
    def get_latest_info(self, data_df, prefecture, pref_name):
        latest_date = data_df.loc[:, 'Date'].iloc[-1].strftime('%Y年%m月%d日（%a）')
        latest_new_case_covid19 = data_df.loc[:, prefecture].iloc[-1]
        info = f'{latest_date} の {pref_name} の新規陽性者数は {latest_new_case_covid19} 人です。'
        return info
