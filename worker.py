def add_numbers(a, b):
    return a + b

# We define the numbers here so the test script can "see" them
NUM_1 = 13
NUM_2 = 2

if __name__ == "__main__":
    # We use the variables here instead of hardcoding the numbers
    result = add_numbers(NUM_1, NUM_2)
    print(f"The sum of {NUM_1} and {NUM_2} is: {result}")
