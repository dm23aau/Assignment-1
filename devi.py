# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Line plot
def line_plot(filtered_data_countries, countries_to_plot):
    
    # Set size of the plot
    plt.figure(figsize=(10, 6))
    
    # Loop through selected countries and plot their data
    for country in countries_to_plot:
        country_data = filtered_data_countries[filtered_data_countries['Country Name'] == country]
        plt.plot(country_data.columns[1:], country_data.values.flatten()[1:], label=country)
    
    plt.xlabel('Year')
    plt.ylabel('Mortality Rate (per 1,000 live births)')
    plt.title('Mortality Rate under-5 years')
    plt.legend()
    plt.grid(True)
    plt.show()


# Bar Plot
def bar_plot(filtered_data_countries):
    # Set the size of the plot
    plt.figure(figsize=(10, 6))
    
    # Calculate the average under-5 mortality rates across the selected years
    average_mortality_rates = filtered_data_countries.set_index('Country Name').mean(axis=1)
    
    # Plotting the bar chart
    average_mortality_rates.plot(kind='bar', color='skyblue')
    plt.xlabel('Country')
    plt.ylabel('Average Under-5 Mortality Rate (2000-2021)')
    plt.title('Average Under-5 Mortality Rate (2000-2021) across countries')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()


# Box Plot
def box_plot(filtered_data_countries):
    # Set the size of the plot.
    plt.figure(figsize=(10, 6))
    
    # Choose specific years for comparison
    years_to_compare = ['2000', '2020']  
    
    # Prepare the data for the box plot
    data_to_plot = [filtered_data_countries[year] for year in years_to_compare]
    
    # Create the box plot
    plt.boxplot(data_to_plot, labels=years_to_compare)
    plt.ylabel('Under-5 Mortality Rate')
    plt.title('Under-5 Mortality Rate Comparison (2000 vs. 2020) across countries')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()


# Read the CSV file, skipping the first 4 rows 
data = pd.read_csv("mortality.csv", skiprows=4)
print(data.head())

# Select relevant columns (Country Name and years 2000 to 2021)
selected_columns = ['Country Name'] + [str(year) for year in range(2000, 2022)]
filtered_data = data[selected_columns]

# Select data for specific countries (Afghanistan, Tanzania, Thailand, South Sudan, Kenya, India, United States, and Zambia)
countries_to_plot = ['Afghanistan', 'Tanzania', 'Thailand', 'South Sudan', 'Kenya', 'India', 'United States', 'Zambia']
filtered_data_countries = filtered_data[filtered_data['Country Name'].isin(countries_to_plot)]

# Call the plot functions
line_plot(filtered_data_countries, countries_to_plot)
bar_plot(filtered_data_countries)
box_plot(filtered_data_countries)

