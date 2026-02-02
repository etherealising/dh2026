from scipy.stats import ttest_ind
print(ttest_ind([3, 5, 4], [12, 16, 14]))
print(ttest_ind([3, 5, 4, 6, 5, 4], [12, 16, 14, 16, 15, 14]))
print(ttest_ind([13, 15, 14], [12, 16, 14]))
print(ttest_ind([13, 15, 14, 18], [12, 16, 14, 11]))
print(ttest_ind([13, 15, 14, 18, 16, 20], [12, 16, 14, 11, 12, 18]))

# topi terminali "pip install scipy", et allalaadida vajalik library