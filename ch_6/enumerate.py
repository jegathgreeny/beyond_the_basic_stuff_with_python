tv_series = ["wandavision", "falcon and winter solider", "loki"]

for i in range(len(tv_series)):
    print(i, tv_series[i])

print()

# Use emumerate instead of range(len()).
for i, series in enumerate(tv_series):
    print(i, series)
