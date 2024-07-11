import numpy as np

def min_production_time(station_times, transfer_times, dependencies):
    n = len(station_times[0])
    f1 = [0] * n
    f2 = [0] * n
    f3 = [0] * n

    f1[0] = station_times[0][0]
    f2[0] = station_times[1][0]
    f3[0] = station_times[2][0]

    for i in range(1, n):
        f1[i] = min(f1[i - 1] + station_times[0][i], f2[i - 1] + transfer_times[1][0] + station_times[0][i], f3[i - 1] + transfer_times[2][0] + station_times[0][i])
        f2[i] = min(f2[i - 1] + station_times[1][i], f1[i - 1] + transfer_times[0][1] + station_times[1][i], f3[i - 1] + transfer_times[2][1] + station_times[1][i])
        f3[i] = min(f3[i - 1] + station_times[2][i], f1[i - 1] + transfer_times[0][2] + station_times[2][i], f2[i - 1] + transfer_times[1][2] + station_times[2][i])

    return min(f1[n - 1], f2[n - 1], f3[n - 1])

station_times = [
    [5, 9, 3],
    [6, 8, 4],
    [7, 6, 5]
]

transfer_times = [
    [0, 2, 3],
    [2, 0, 4],
    [3, 4, 0]
]

dependencies = [(0, 1), (1, 2)]

min_time = min_production_time(station_times, transfer_times, dependencies)
print("Minimum Production Time:", min_time)
