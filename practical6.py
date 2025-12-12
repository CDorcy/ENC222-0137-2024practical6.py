import random

def main():
    # Seed the random number generator (Python handles seeding automatically, unlike C++)

    SIZE = 20
    MIN_VAL = 1
    MAX_VAL = 100
    
    original_array = []
    odd_values = []
    even_values = []

    print("--- Original Array of 20 Random Integers (1-100) ---")
    for _ in range(SIZE):
        random_number = random.randint(MIN_VAL, MAX_VAL)
        original_array.append(random_number)

        if random_number % 2 == 0:
            even_values.append(random_number)
        else:
            odd_values.append(random_number)
        
        print(random_number, end=" ")

    print("\n")
    print(f"--- Odd Values Array ({len(odd_values)} elements) ---")
    for value in odd_values:
        print(value, end=" ")

    print("\n")
    print(f"--- Even Values Array ({len(even_values)} elements) ---")
    for value in even_values:
        print(value, end=" ")
    print()

if __name__ == "__main__":
    main()
