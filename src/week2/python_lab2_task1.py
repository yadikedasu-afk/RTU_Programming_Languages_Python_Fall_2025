"""
Lab 3.1 Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# Student Name: Edasu Yadık
# Student ID: 231AEB028

# TODO: Create the datasets - up to you to fill in the data
temperatures = [11, 15, 14, 13, 16, 15, 12]
city_population = dict([
    ("Riga", 605802),
    ("Vilnius", 592389),
    ("Tallinn", 445000),
    ("Helsinki", 655281),
    ("Stockholm", 975551)
])

# TODO: Compute aggregates
average_temperature = round(sum(temperatures) / len(temperatures), 2)
largest_city, largest_population = max(city_population.items(), key=lambda item: item[1])
total_population = sum(city_population.values())

# TODO: Print results
print("Average temperature:", average_temperature)
print("Largest city:", f"{largest_city} - {largest_population}")
print("Total population:", total_population)
