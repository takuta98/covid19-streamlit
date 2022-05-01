from covid19 import *
import matplotlib.pyplot as plt

class DrawGraphMatplotlib():
    
    PREFECTURE = {
        '全国': ['ALL', 'Japan'],
        '東京': ['Tokyo', 'Tokyo'],
        '神奈川': ['Kanagawa', 'Kanagawa']
    }
    
    def draw_bar_graph(self, prefecture):
        c19d = Covid19Data()
        data_df = c19d.get_new_cases_covid19(self.PREFECTURE[prefecture][0])
        date_df = c19d.get_date()
        
        fig = plt.figure(
            figsize=(10, 5),
            dpi=150,
            facecolor='orange',
            edgecolor='black',
            linewidth=5,
            tight_layout=True)

        ax = fig.add_subplot(
            111, 
            facecolor='black',
            xlabel='Date',
            ylabel='PCR positive daily in ' + self.PREFECTURE[prefecture][1])

        ax.bar(
            date_df, 
            data_df,
            color='white')
        
        return fig
