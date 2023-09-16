import matplotlib.pyplot as plt
import matplotlib as mpl
import random
import timeit
import numpy as np
import json


def our_bs(arr, target, istart, istop):
    if istart >= istop:
        return False
    midpoint = (istart + istop) // 2
    x = arr[midpoint]
    

    if x == target:
        return midpoint
    if x < target:
        return bin_search(arr, target, midpoint + 1, istop)
    if x > target:
        return bin_search(arr, target, istart, midpoint)

def bin_search_repeat():
    times = []
    for i in range(1, 1000):
        arr = sorted([j for j in range(i)])
        times.append(timeit.timeit(lambda x = random.choice(arr): bin_search(arr, x, 0, len(arr) - 1), number=10000) / 10000)
    return times

if __name__ == "__main__":
    # data_set = []
    # for i in range(20):
    #     data_set.append(bin_search_repeat())
    #     print(i)
    # plottable_set = [np.mean(k) for k in zip(*data_set)]
    # data = json.dump(plottable_set, open('data.jason', 'w+'))
    log = [np.log(n) / 5000000 for n in range(1, 1000)]
    plottable_set = json.load(open('data.json', 'r'))
    xs = [i for i in range(len(plottable_set))]
    plt.plot(xs, plottable_set)
    plt.plot([i for i in range(len(log))], log)
    plt.savefig('plot.png')
