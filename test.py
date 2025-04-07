try:
    # Declare and initialize variables
    first_name = "Sparsh"
    last_name = "Singh"
    age = int(input("Enter your age: "))  # Accepting user input

    # Concatenate strings and print
    full_name = first_name + " " + last_name
    print("Hello, my name is " + full_name + "!")

    # Using variables in a sentence
    print("I am", age, "years old.")

    # Performing a simple calculation
    birth_year = 2024 - age
    print("I was born in the year:", birth_year)

except ValueError:
    print("Invalid input! Please enter a valid number for age.")
except Exception as e:
    print("An unexpected error occurred:", e)