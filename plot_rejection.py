# import numpy as np
import matplotlib.pyplot as plt 


# creating the dataset
data = {'Three level':305844, 'Four level':188784}
# data = {'Three level':296395, 'Three level (powerfull)': 307708, 'Four level':188784}
# data = {'Three level':305844,'Four layer(Least_loaded)':229820,  'Four level(Random)': 228670, 'Four level(D_SARSA)':188784}
# data = {'Least_Loaded':307224,  'Random': 307156, 'Three level':305844,'Four layer(Least_loaded)':229820,  'Four level(Random)': 228670, 'Four level(D_SARSA)':188784}
courses = list(data.keys())
values = list(data.values())
# color = ['black', 'gray', 'olive', 'tomato', 'lightblue', 'lightgreen', 'cyan']

color = ['tomato', 'lightblue', 'lightgreen', 'cyan']

fig = plt.figure(figsize = (10, 5))


# creating the bar plot
plt.bar(courses, values, color =color,
		width = 0.3)

plt.xlabel("System model")
plt.ylabel("No. of rejected jobs")
plt.title("Rejection Rate")
plt.show()
