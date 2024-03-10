import numpy as np
import math
import scipy.stats as stats

def findweightedaverage(days, bananas):
    result = np.multiply(days,bananas)
    return (np.sum(result))/np.sum(bananas)

def findweightedavgandstd(days, bananas):
    average = np.average(days, weights=bananas)
    variance = np.average((days-average)**2, weights=bananas)
    return (average, math.sqrt(variance))

def mannwhitney(firstset, secondset):
    #perform the Mann-Whitney U test
    statistic, p_value = stats.mannwhitneyu(firstset, secondset, alternative = 'greater')
    return (statistic, p_value)

#experiement1
days1 = [6,7]
bananas1 = [1,14]
average, deviation = findweightedavgandstd(days1, bananas1)
print("Bananas over ripening in air: average, std deviation", average, deviation)

#experiment 2

days2 = [3,4,6,7,8,10]
bananas2 = [1,1,4,4,2,1]
result2 = findweightedaverage(days2,bananas2)
average, deviation = findweightedavgandstd(days2, bananas2)
print("Bananas rottingg time in water: average, std deviation", average, deviation)

#experiment 3
days3 = [10,11]
bananas3 = [3,12]
average, deviation = findweightedavgandstd(days3, bananas3)
print("Bananas in water and air: average, std deviation", average, deviation)

#mann-whitney with greater check
firstset = [10,10,10,11,11,11,11,11,11,11,11,11,11,11,11]
secondset = [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7]

statistic,pval = mannwhitney(firstset, secondset)
print("p-value is", pval)

