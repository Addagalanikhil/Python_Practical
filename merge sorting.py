def merge_sorted_lists(list1, list2):
    merged_list = sorted(list1 + list2)
    return merged_list

list1 = list(map(int(input("Enter sorted list 1: ").split())))
list2 = list(map(int(input("Enter sorted list 2: ").split())))

merged_list = merge_sorted_lists(list1, list2)
print(merged_list)

second_largest = sorted(merged_list)[-2]

# Test Case 2: Find the 4th smallest number
fourth_smallest = sorted(merged_list)[3]

# Test Case 3: Print the numbers in reverse order
reverse_order = merged_list[::-1]

# Test Case 4: Sum and Average of merged list
sum_merged = sum(merged_list)
average_merged = sum_merged / len(merged_list)

print("Merged List:", merged_list)
print("2nd Largest Number:", second_largest)
print("4th Smallest Number:", fourth_smallest)
print("Numbers in Reverse Order:", reverse_order)
print("Sum of Merged List:", sum_merged)
print("Average of Merged List:", average_merged)
