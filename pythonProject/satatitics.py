import statistics
# harmonic mean calculation harmonic_mean(data,weights)
print(statistics.harmonic_mean([10, 30, 20]))
print(statistics.harmonic_mean([10, 20, 30], (5, 10, 15)))

# mean calculation
print(statistics.mean((10, 20, 30, 40, 50)))

# median calculation
print(statistics.median((10,35,12,4,6,7)))

# mode calculation
print(statistics.mode((10,20,30,20,10,10)))

# calculate standard deviation
print(statistics.stdev((10,20,30,40)))



