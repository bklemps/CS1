def chorus ():
    print ("you are my sunshine you make me happy when times are gray")
def sing_song():
    print("how much I love you please do not take my sunshine away")
    print("you never know dear how much I love you please im begging do not take my sunshine away Lenbron james you are so glorous your longejivty needs to be studied you are so imacualte your skills make me happy when I see you dribbling that ball I get so excited oh lebonbon i really love you you are my sunshine")
    chorus()


sing_song()

def is_integer(param):
    """
    This function checks if a given parameter is an integer."""
    return isinstance(param, int)






def print_sum(num1, num2):
    """
    This function takes two numbers as input and prints their sum.
    
    Parameters:
        num1 (int or): The first number.
        num2 (int or): The second number.
    """
    sum_result = num1 + num2
    print("The sum of", num1, "and", num2, "is:", sum_result)




def print_list_vertically(my_list):
    """
    This function takes a list as input and prints each element vertically.
    
    
        my_list (list): The list of elements to print vertically.
    """
    for item in my_list:
        print(item)



def is_element_in_list(my_list, element):
    """
    This function checks if a given element is present in a list.
    
    
        my_list (list): The list to search for the element.
        element: The element to search for in the list.
        
    
     True if the element is present in the list, False otherwise.
    """
    return element in my_list


import random

def is_integer(param):
    """
    This function checks if a given parameter is an integer.
    
    
    """
    return isinstance(param, int)

def print_random_between_two_numbers():
    """
    This function prompts the user for two numbers and prints a random number between them.
    """
    while True:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        # Check if both inputs are integers
        if is_integer(num1) and is_integer(num2):
            num1 = int(num1)
            num2 = int(num2)
            break
        else:
            print("Please enter valid integers.")

    # Ensure num2 is greater than num1
    if num2 < num1:
        num1, num2 = num2, num1

    random_number = random.randint(num1, num2)
    print("Random number between", num1, "and", num2, "is:", random_number)




def replace_characters(input_string, char_to_replace, replacement_char):
    """
    This function replaces every instance of a character in a string with another character.
    
    Parameters:
        input_string (str): The input string.
        char_to_replace (str): The character to be replaced.
        replacement_char (str): The character to replace with.
        
    Returns:
        str: The modified string with replacements.
    """
    modified_string = ""
    for char in input_string:
        if char == char_to_replace:
            modified_string += replacement_char
        else:
            modified_string += char
    return modified_string






