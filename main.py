import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = data.dropna(subset=['Primary Fur Color'])["Primary Fur Color"]

color_freq = {}
for color in fur_colors:
    if color not in color_freq:
        color_freq[color] = 0
    color_freq[color] += 1

color_list = color_freq.keys()
count_list = []
for color in color_list:
    count_list.append(color_freq[color])

freq_df = pandas.DataFrame({
    "Fur Color": color_list,
    "Count": count_list
})

freq_df.to_csv('color_count.csv', index=False)
