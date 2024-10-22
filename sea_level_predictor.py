import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    extended_years = np.arange(df['Year'].min(), 2051)

    first_linear_regression = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    first_extended_sea_level = first_linear_regression.slope * extended_years + first_linear_regression.intercept
    
    plt.plot(extended_years, first_extended_sea_level)

    # Create second line of best fit
    second_extended_years = np.arange(2000, 2051)
    second_linear_regression = linregress(df['Year'][df['Year'] >= 2000], df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])
    second_extended_sea_level = second_linear_regression.slope * second_extended_years + second_linear_regression.intercept

    plt.plot(second_extended_years, second_extended_sea_level)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()