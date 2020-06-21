import pandas
import webbrowser
import os

# Read the dataset into a data table using Pandas
data_table = pandas.read_csv("ml_house_data_set.csv")

print(data_table.head(1))

data_table_pivot = pandas.pivot_table(data_table, index='city', aggfunc='mean', columns='year_built', values='num_bedrooms')

print(data_table_pivot.head(1))

# html = data_table[0:100].to_html()
# with open("data.html", "w") as f:
#     f.write(html)
#
# full_filename = os.path.abspath("data.html")
# webbrowser.open("file://{}".format(full_filename))