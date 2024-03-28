from statistics import mean, median, mode

array = list(map(int, input("Enter the elements: ").split()))

mean_value = mean(array)

median_value = median(array)

mode_value = mode(array)

print(f"Mean = {mean_value}")
print(f"Median = {median_value}")
print(f"Mode = {mode_value}")
