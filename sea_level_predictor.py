import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    years_extended = pd.Series(
        range(df['Year'].min(), 2051)
    )

    plt.plot(
        years_extended,
        intercept + slope * years_extended
    )

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )

    years_extended2 = pd.Series(
        range(2000, 2051)
    )

    plt.plot(
        years_extended2,
        intercept2 + slope2 * years_extended2
    )

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()