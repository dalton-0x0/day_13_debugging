from random import randint


# debugging


# Describe Problem
def my_function():
    # range does not include the 'stop' number
    for i in range(1, 21):
        if i == 20:
            print("You found the bug!")


my_function()

# Reproduce the Bug
# errors out after many tries 'IndexError: list index out of range''
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# check randint params to match list indexes
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Play The Computer
year = int(input("What's your year of birth? "))
# what happens if you enter 1994 or 2010? remember to include those years
if 1980 < year <= 1994:
    print("You are a millenial.")
elif 1994 < year <= 2010:
    print("You are a Gen Z.")
else:
    print("You are neither a millenial nor a Gen Z.")


# Fix the Errors
def can_i_drive():
    age = int(input("How old are you? "))
    if age > 18:
        print(f"You can drive at age {age}.")
    else:
        print(f"You can't drive at age {age}.")


can_i_drive()

# Print is Your Friend
pages = int(input("Number of pages: "))
words_per_page = int(input("Number of words per page: "))
total_words = pages * words_per_page
print(total_words)


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        # careful of indentation errors
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
