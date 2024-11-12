import random
import time

"""
Sorts a list of numbers in ascending order using the insertion sort algorithm.
"""
def insertion_sort(small_data):
   for i in range(1, len(small_data)):  # for loop to start from index 1 and compare and go up till length of data based on indexes, start from index 1 because we assume index0/element 1 is sorted
        temp = small_data[i]  # the value we are currently trying to sort
        j = i - 1  # identifies j must be one index less than i, in this case index 0 (sorted element)
        while j >= 0 and temp < small_data[j]: 
            small_data[j + 1] = small_data[j]  # if temp value is less than j, j moves forward by one index
            j -= 1  # to check the value on the left of j
        small_data[j + 1] = temp  # temp variable becomes part of the sorted data
        return small_data

# Function to generate an array of random numbers and sort it
"""
Generates a list of random numbers and sorts it using insertion sort.
"""
def generate_sorted_data(size):
    # Generate random numbers between 1 and 100
    data = [random.randint(1, 100) for _ in range(size)]
    sorted_data = insertion_sort(data)  # Sort using insertion sort
    return sorted_data

# phase 1: generate and sort small data
small_data = [34, 7, 23, 32, 5, 62, 29, 12, 40, 8]
insertion_sort(small_data)
print("sorted data is:", insertion_sort(small_data))

# function to perform binary search
"""
Searches for a target value in a sorted list using binary search.
Returns the index of the target if found, or None if not found.
"""
def binary_search(sorted_array, target):
    left, right = 0, len(sorted_array) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

# phase 2: binary search on small data
sorted_array = [5, 7, 8, 12, 23, 29, 32, 34, 40, 62]
print("Index of target (29):", binary_search(sorted_array, 29))
print("Index of target (100):", binary_search(sorted_array, 100))

# Function to perform merge sort
"""
Sorts a list of numbers in ascending order using the merge sort algorithm.
"""
def merge_sort(array):
    if len(array) > 1:
        middle_ind = len(array) // 2  # Find the middle point
        left_half = array[:middle_ind]  # Split the array into left and right halves
        right_half = array[middle_ind:]
        merge_sort(left_half)  # Sort the left half
        merge_sort(right_half)  # Sort the right half
        left_position = 0
        right_position = 0
        sorted_position = 0
        # Merge the halves together
        while left_position < len(left_half) and right_position < len(right_half):
            if left_half[left_position] < right_half[right_position]:
                array[sorted_position] = left_half[left_position]
                left_position += 1
            else:
                array[sorted_position] = right_half[right_position]
                right_position += 1
            sorted_position += 1
        # Add remaining elements of left half
        while left_position < len(left_half):
            array[sorted_position] = left_half[left_position]
            left_position += 1
            sorted_position += 1
        # Add remaining elements of right half
        while right_position < len(right_half):
            array[sorted_position] = right_half[right_position]
            right_position += 1
            sorted_position += 1

# phase 3: Generate and Sort Large Data with Merge Sort
large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]
merge_sort(large_data)
# print(large_data)
print("First 10 elements of sorted large data:", large_data[:10])

# Simple linear search function
"""
Searches for a target value in a list using linear search.
Returns the index of the target if found, or None if not found.
"""
def linear_search(array, target):
    for ind in range(len(array)):
        if array[ind] == target:
            return ind
    return None

# Function to compare search times
"""
Compares the time taken to search for a target value using linear and binary search,
printing the time taken by each search method.
"""
def compare_search_times(array, target):
    # Timing linear search
    start_time = time.perf_counter()
    linear_search(array, target)
    end_time = time.perf_counter()
    linear_time = end_time - start_time
    # Timing binary search
    start_time = time.perf_counter()
    binary_search(array, target)
    end_time = time.perf_counter()
    binary_time = end_time - start_time
    # Displaying the times
    print("Linear Search Time:", linear_time)
    print("Binary Search Time:", binary_time)
