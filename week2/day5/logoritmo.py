import random

# Generate a list of 20000 random numbers
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

def find_pairs_with_sum(numbers, target):
    count = 0  # Initialize a counter for the number of pairs found
    
    # Create a set to store the unique numbers in the list
    num_set = set(numbers)
    
    # Iterate through the list of numbers
    for num in numbers:
        # Calculate the difference needed to reach the target
        diff = target - num
        
        # Check if the difference exists in the set and is not equal to the current number
        if diff in num_set and diff != num:
            count += 1
    
    # Since each pair is counted twice (once for each number), divide by 2 to get the actual count
    return count // 2

# Call the function to find the number of pairs that sum to the target_number
pair_count = find_pairs_with_sum(list_of_numbers, target_number)
print(f"Number of pairs that sum to {target_number}: {pair_count}")
