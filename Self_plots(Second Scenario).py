import matplotlib.pyplot as plt

# Data from the first table
parameters_1 = [
    'fps average (60fps)', 'fps average (30fps)', 'fps average (15fps)',
    'lag average (60fps)', 'lag average (30fps)', 'lag average (15fps)',
    'RP average (60fps)', 'RP average (30fps)', 'RP average (15fps)',
    'rejection'
]

values_1 = [
    [27.4429, 29.7675, 31.8112, 45.3664, 48.0981],
    [14.2379, 15.4817, 17.1963, 26.6567, 26.8339],
    [6.7303, 7.3392, 7.9773, 12.6240, 12.9609],
    [331.0728, 216.7101, 150.1582, 27.5536, 13.0227],
    [369.7866, 240.1201, 152.1068, 17.1070, 12.0643],
    [502.2125, 331.7062, 217.4409, 30.1919, 21.8311],
    [348.0728, 233.7101, 167.1582, 44.5536, 30.0226],
    [402.7866, 273.1201, 185.1068, 50.1070, 44.9938],
    [569.2124, 398.7060, 284.4409, 97.1919, 88.8204],
    [773272, 662954, 627750, 142004, 147266]
]

# Data from the second table
values_2 = [
    [29.7010, 30.40169, 31.4739, 32.8377, 40.5858],
    [15.3838, 15.8007, 16.4224, 17.2526, 22.9539],
    [7.2705, 7.5390, 7.8664, 8.3800, 11.0923],
    [369.2055, 292.0170, 208.2923, 139.4443, 63.2244],
    [434.0079, 336.2960, 237.7625, 152.8914, 51.0048],
    [601.8229, 470.5858, 329.3839, 211.5556, 70.3843],
    [386.2055, 309.0170, 225.2923, 156.4443, 80.2244],
    [467.0079, 369.2960, 270.7625, 185.8914, 84.0048],
    [668.8229, 537.5858, 396.3839, 278.5556, 137.3843],
    [640082, 650340, 613082, 601506, 271535]
]

# Plotting each parameter for both tables
for param, vals_1, vals_2 in zip(parameters_1, values_1, values_2):
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 6), vals_1, marker='p', label='Four layer')
    plt.plot(range(1, 6), vals_2, marker='s', label='Three layer')
    plt.xlabel('Cases')
    plt.ylabel('Parameter Value')
    plt.title(f'{param} across Cases')
    plt.xticks(range(1, 6), ['Case 1', 'Case 2', 'Case 3', 'Case 4', 'Case 5'])
    plt.legend()
    plt.grid(True)
    plt.show()
