
array = list(map(int, input("Enter the array elements separated by commas: ").split(',')))
m = int(input("Enter the value of M: "))
n = int(input("Enter the value of N: "))


array.sort()

mth_max = array[-m]
nth_min = array[n-1]


sum_result = mth_max + nth_min
diff_result = mth_max - nth_min


print(f"{m}th Maximum Number = {mth_max} {n}th Minimum Number = {nth_min} Sum = {sum_result} Difference = {diff_result}")
