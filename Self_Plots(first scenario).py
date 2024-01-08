import matplotlib.pyplot as plt

# Data from the first table
parameters_1 = [
    'fps average (60fps)', 'fps average (30fps)', 'fps average (15fps)',
    'lag average (60fps)', 'lag average (30fps)', 'lag average (15fps)',
    'RP average (60fps)', 'RP average (30fps)', 'RP average (15fps)',
    'rejection'
]
# Updated values for the first table
values_1 = [
    [53.2830, 53.1977, 52.9297, 52.1986, 44.7093],
    [26.8982, 26.8641, 26.7302, 26.8560, 26.1177],
    [13.0248, 13.0419, 13.0238, 12.9944, 12.6473],
    [0.6341, 0.8553, 1.54184, 2.8733, 26.5183],
    [0.9630, 1.3581, 2.2549, 5.0732, 22.7661],
    [15.1375, 15.7210, 16.6139, 18.3968, 31.8673],
    [12.6408, 13.3837, 14.8080, 17.7825, 43.5174],
    [20.4301, 22.6252, 25.6745, 33.6252, 55.7159],
    [80.7939, 81.7734, 82.7457, 84.9622, 98.8540],
    [79055, 80397, 87652, 92095, 227995]
]

# Updated values for the second table
values_2 = [
    [54.2546, 53.5593, 53.2178, 49.5326, 41.1215],
    [27.7040, 27.4171, 27.3818, 25.8816, 22.4081],
    [13.15461, 13.0022, 13.0266, 12.2601, 10.8436],
    [0.13160, 1.2886, 1.5714, 15.3533, 65.0879],
    [0.0020, 0.6175, 0.4497, 13.7967, 64.8395],
    [0.0036, 0.8988, 0.6988, 22.0412, 87.3482],
    [13.0959, 15.2170, 16.6196, 31.5539, 82.0879],
    [19.0620, 22.2223, 25.7391, 44.1106, 97.8395],
    [39.6431, 46.0267, 55.1367, 86.5725, 154.3482],
    [51010, 56668, 58520, 120142, 283298]
]

# Updated values for the third table
values_3 = [
    [55.2624, 54.4425, 53.8704, 47.3331, 33.2870],
    [27.7872, 27.4220, 27.24911, 24.4883, 16.4777],
    [13.0376, 12.8922, 12.8653, 11.4861, 9.4582],
    [0.00627, 0.9942, 1.1206, 22.7215, 114.3990],
    [0, 0.6043, 0.3375, 19.6780, 122.5465],
    [0, 0.9443, 0.3463, 30.0301, 140.5185],
    [11.35903, 13.5594, 15.3098, 39.3643, 131.3990],
    [16.6746, 20.0911, 23.3134, 49.3105, 155.5465],
    [32.3140, 39.5027, 48.1979, 94.3413, 182.5214],
    [84473, 94593, 105342, 231652, 841428]
]


# Plotting each parameter for all three tables
for param, vals_1, vals_2, vals_3 in zip(parameters_1, values_1, values_2, values_3):
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 6), vals_1, marker='o', label='Four layer')
    plt.plot(range(1, 6), vals_2, marker='s', label='Three layer')
    plt.plot(range(1, 6), vals_3, marker='^', label='Two layer')
    plt.xlabel('Cases')
    plt.ylabel('Parameter Value')
    plt.title(f'{param} across Cases')
    plt.xticks(range(1, 6), ['Case 1', 'Case 2', 'Case 3', 'Case 4', 'Case 5'])
    plt.legend()
    plt.grid(True)
    plt.show()
