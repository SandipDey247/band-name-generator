import random  # Importing the random module to randomly pick band names

# Welcome message
print("Welcome to the Band Name Generator.")

# Asking the user for input and removing any extra spaces
city = input("Which city did you grow up in?\n").strip()
pet = input("What is the name of a pet?\n").strip()

# Creating a list of different band name formats using f-strings
band_names = [
    f"{city} {pet}",
    f"The {pet} of {city}",
    f"{city}-{pet} Squad",
    f"{pet} from {city}"
]

# Loop to allow the user to generate multiple names
while True:
    # Randomly select a band name from the list and print it
    print(f"Your band name could be: {random.choice(band_names)}.")

    # Ask the user if they want to try again
    play_again = input("Generate another name? (yes/no): ").lower()

    # If the user says anything other than "yes", break the loop
    if play_again != "yes":
        break

# Exit message
print("Thanks for using the Band Name Generator. Goodbye!")
