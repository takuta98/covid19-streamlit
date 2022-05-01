import matplotlib.pyplot as plt

class DrawGraphMatplotlib():
    
    def draw_bar_graph(self, data_df, prefecture, pref_display):       
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
            ylabel='PCR positive daily in ' + pref_display)

        ax.bar(
            data_df['Date'], 
            data_df[prefecture],
            color='white')
        
        return fig
