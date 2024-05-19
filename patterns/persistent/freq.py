# method 1
def find_frequency(arr):
    frequency = {}

    for element in arr:
        # If the element is already in the dictionary, increment its count
        if element in frequency:
            frequency[element] += 1
        # If the element is not in the dictionary, add it with a count of 1
        else:
            frequency[element] = 1

    return frequency

# Example usage:
my_array = [1, 2, 3, 4, 1, 2, 1, 5, 4, 3, 2, 1]
result = find_frequency(my_array)

for key, value in result.items():
    print(f"{key}: {value} times")
    
print()
    
    
    
 #2nd method   
def find_frequency_with_count(arr):
    frequency = {}

    for element in arr:
        # Use the count method to find the frequency of the current element
        count = arr.count(element)
        frequency[element] = count

    return frequency

# Example usage:
my_array = [1, 2, 3, 4, 1, 2, 1, 5, 4, 3, 2, 1]
result = find_frequency_with_count(my_array)

for key, value in result.items():
    print(f"{key}: {value} times")

    

