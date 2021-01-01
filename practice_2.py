
import os


def add_to_dict(a, b, c=None):
    if type(a) != dict:
        tp = type(a)
        print("You need to send a dictionary. You sent: {0} ".format(tp))
    elif c == None:
        print("You need to send a word and a definition")
    elif b in a:
        print("{0} is already on the dictionary. Won't add.".format(b))
    else:
        a[b] = c
        print("{0} has been added".format(b))


def get_from_dict(a, b=None):
    if type(a) != dict:
        tp = type(a)
        print("You need to send a dictionary. You sent: {0} ".format(tp))
    elif b == None:
        print("you need to send a word to search for.")
    elif b not in a:
        print("{0} is not found in this dict".format(b))
    else:
        c = a.get(b)
        print("{0} : {1}".format(b, c))


def update_word(a, b, c=None):
    if type(a) != dict:
        tp = type(a)
        print("You need to send a dictionary. You sent: {0} ".format(tp))
    elif c == None:
        print("You need to send a word and definition to update.")
    elif b not in a:
        print("{0} is not on the dict. Can't update non-existing word.".format(b))
    else:
        a[b] = c
        print("{0} has been updated to: {1}".format(b, c))


def delete_from_dict(a, b=None):
    if type(a) != dict:
        tp = type(a)
        print("You need to send a dictionary. You sent: {0}".format(tp))
    elif b == None:
        print("You need to specify a word to delete.")
    elif b not in a:
        print("{0} is not in this dict. Won't delete.".format(b))
    else:
        a.pop(b)
        print("{0} has been deleted".format(b))


# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\


os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\
