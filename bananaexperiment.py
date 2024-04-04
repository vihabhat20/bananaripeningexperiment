import numpy as np
import math
import scipy.stats as stats

# number of days times number of bananas over ripened on that day,
# sum it up and divide by total number of bananas to get weighted average number of days

def findweightedaverage(days, bananas):
    result = np.multiply(days,bananas)
    return (np.sum(result))/np.sum(bananas)
    
# finds average and standard deviation using numpy library
# standard deviation is the square root of variance

def findweightedavgandstddev(days, bananas):
    average = np.average(days, weights=bananas)
    variance = np.average((days-average)**2, weights=bananas)
    return (average, math.sqrt(variance))
    
# performs Mann-Whitney U test using the scipy statistics package

def mannwhitney(firstset, secondset):
    #perform the Mann-Whitney U test
    statistic, p_value = stats.mannwhitneyu(firstset, secondset, alternative = 'greater')
    return (statistic, p_value)

#experiement1 - exposed to air

days1 = [6,7]
bananas1 = [1,14]
average, deviation = findweightedavgandstddev(days1, bananas1)
print("Bananas over ripening in air: average, std deviation", average, deviation)

#experiment 2 - submerged in water

days2 = [3,4,6,7,8,10]
bananas2 = [1,1,4,4,2,1]
result2 = findweightedaverage(days2,bananas2)
average, deviation = findweightedavgandstddev(days2, bananas2)
print("Bananas rotting time in water: average, std deviation", average, deviation)

#experiment 3 - submerged in water for 2 days and then exposed to air

days3 = [10,11]
bananas3 = [3,12]
average, deviation = findweightedavgandstddev(days3, bananas3)
print("Bananas in water and air: average, std deviation", average, deviation)

#mann-whitney with greater check
#the sets contain days it took for the bananas to over ripen

firstset = [10,10,10,11,11,11,11,11,11,11,11,11,11,11,11]
secondset = [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7]

statistic,pval = mannwhitney(firstset, secondset)
print("p-value is", pval)

