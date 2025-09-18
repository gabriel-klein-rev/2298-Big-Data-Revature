'''
Animal_Journal.py

A CLI application that allows for journaling of cats and dogs. Includes exception handling, 
file i/o, user input.

Required modules: Animal.py
Required files: Animal_log.txt
'''
import Animal

def main():
    while True:
        user_choice = input("Select:\n\t1) to read all animals in journal\n\t2) Enter new animal\n\t3) Quit\n>>>")
        if user_choice == "1":
            readJournal()
        elif user_choice == "3":
            break
        else:
            enterAnimal()

def enterAnimal():
    '''
    Function to prompt user for information about an animal to be submitted to journal.
    Valid animals will be stored in Animal_log.txt.
    '''
    try:
        type_Animal = input("Enter the type of animal you want to create (cat/dog): ")
        name = input("Enter animal name: ")
        age = int(input("Enter animal age: "))

        # For specifically getting an int for age
        # age = getAnimalAge()

        color = input("Enter animal color: ")

        if type_Animal.lower() == "cat":
            new_animal = Animal.Cat(name, age, color)
        elif type_Animal.lower() == "dog":
            new_animal = Animal.Dog(name, age, color)
        else:
            new_animal = None
            print("You must either enter a cat or a dog!")
            return

        with open("Animal_log.txt", "a") as f:
            f.write(f"{new_animal}\n")

        print(new_animal)
    except ValueError:
        print("WARNING: Enter a number for age!")
    except FileNotFoundError:
        print("WARNING: File not found")

# For specifically getting an int for age
# def getAnimalAge():
#     '''
#     Function to get only the age of the animal. Checks to make sure 
#     user input is in fact an integer.
#     '''
#     while True:
#         try:
#             age = int(input("Enter animal age: "))
#         except ValueError:
#             print("WARNING: Enter a number!")
#         else:
#             return age

def readJournal():
    '''
    Reads data from Animal_log.txt and prints to console. CURRENTLY HAS NO EXCEPTION HANDLING.
    '''
    with open("Animal_log.txt", "r") as f:
        for line in f:
            print(line.strip())

# main block
if __name__ == "__main__":
    main()