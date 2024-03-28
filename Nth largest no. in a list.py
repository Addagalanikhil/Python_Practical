def find_nth_largest_number(lst, n):
    
    sorted_list = sorted(lst, reverse=True)
    
    
    return sorted_list[n - 1]


lst = list(map(int, input("Enter the list of numbers separated by space: ").split()))
n = int(input("Enter the value of N: "))


nth_largest = find_nth_largest_number(lst, n)

print(f"{n}th Largest number:", nth_largest)
