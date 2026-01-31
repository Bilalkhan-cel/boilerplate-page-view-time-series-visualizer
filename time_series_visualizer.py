import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv("https://raw.githubusercontent.com/Bilalkhan-cel/boilerplate-page-view-time-series-visualizer/refs/heads/main/fcc-forum-pageviews.csv",index_col='date',parse_dates=True)

# Clean data
df=df[(df['value'] < df['value'].quantile(0.975)) & (df['value'] > df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot

    plt.figure(figsize=(15,5))
    x=df.index
    y=df['value']
    fig=plt.plot(x,y)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel('Date')
    plt.ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    rdf=df.groupby(['year','month'])['value'].mean().reset_index()
    labels=['January','February','March','April','May','June','July','August','September','October','November','December']
    rdf
    rdf_pivot = rdf.pivot(index='year', columns='month', values='value')
    fig=rdf_pivot.plot.bar(
        figsize=(12,6),
        stacked=False,    # grouped bars
        width=0.8
    )

    plt.ylabel('Average Page Views')
    plt.xlabel('Years')
    plt.title('Average Page Views per Month')
    plt.legend(title='Months') 
    plt.xticks(rotation=0)  
    plt.tight_layout()
    plt.show()








    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    plt.figure(figsize=(15,5))
    plt.subplot(1,2,1)
    fig=sns.boxplot(x='month',y='value',data=df_box) 
    plt.subplot(1,2,2)
    sns.boxplot(x='year',y='value',data=df_box) 



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
