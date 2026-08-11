# Dictionary Comprehension Assignment
# Objective: Practice dictionary comprehension for filtering and transforming data.

# Step 1: Create the original dictionary with names as keys and ages as values
people = {
    "Alice": 17,
    "Bob": 22,
    "Charlie": 19,
    "Diana": 15,
    "Ethan": 30
}

# Step 2: Use dictionary comprehension to filter individuals who are 18 or older
adults = {name: age for name, age in people.items() if age >= 18}

# Step 3: Use dictionary comprehension to convert ages to strings with " years old"
age_strings = {name: f"{age} years old" for name, age in people.items()}

# Step 4: Print out all dictionaries to demonstrate results
print("Original dictionary:")
print(people)

print("\nAdults (18+):")
print(adults)

print("\nAges as strings:")
print(age_strings)

