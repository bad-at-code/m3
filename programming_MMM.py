from collections import Counter
import dataset_loader as d
from math import *
import matplotlib.pyplot as plot


"""List."""
"""remember use py then file name"""

# d.gender
# d.age
# d.income
# d.education

n_num = [1, 1, 2, 2, 2, 3, 4, 5, 5, 5]
n = len(n_num)


def mean(list):
    get_sum = sum(list)
    mean = get_sum / n

    print(list)
    print("Mean / Average is: " + str(mean))


def median(list):
    list.sort()

    if n % 2 == 0:
        median1 = list[n//2]
        median2 = list[n//2 - 1]
        median = (median1 + median2)/2
    elif n % 2 > 0:
        median = list[n//2]
    print("Median is: " + str(median))


def mode(list):
    data = Counter(list)
    data.most_common()
    data.most_common(1)
    print("Mode:")
    print(data.most_common)


def myVariance(list):
    variance = 0
    get_sum = sum(list)
    mean = get_sum / n

    for x in list:
        variance += (mean - x) ** 2
    print("Variance")
    print(variance / len(list))


print("Gender")
mean(d.gender)
median(d.gender)
myVariance(d.gender)
mode(d.gender)

print("")
print("-------------------------")
print("")

print("Age")
mean(d.age)
median(d.age)
myVariance(d.age)
mode(d.age)

print("")
print("-------------------------")
print("")

print("Income")
mean(d.income)
median(d.income)
myVariance(d.income)
mode(d.income)

print("")
print("-------------------------")
print("")

print("Education")
mean(d.education)
median(d.education)
myVariance(d.education)
mode(d.education)

plot.scatter(d.income, d.age)
plot.show()
