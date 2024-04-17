#Task 1: Write a function that lets the user add items to a list until the user replies "stop", 
#and then returns the shopping list
print('''
        My Shopping List        
''')
def my_shopping_list():
    shopping_list = []
    while True:
        item = input('Enter an item to add to the list, or type "stop" to complete it: ')
        if item == 'stop': #list ends once user inputs stop
            break
        shopping_list.append(item)
    return shopping_list
#For some reason the input isn't showing up in the terminal.

#Task 2: Include feature to remove items from the list

def remove_item(shopping_list):
    print('Would you like to remove any items? yes or no?')
    choice = input()
    if choice == 'yes':
        print('Enter item you want to remove')
        item = input()
        if item in shopping_list:
            shopping_list.remove(item)
            print('You have removed this item')
        else:
            print('This item is not in the shopping list')
    elif choice == 'no':
        print('Congratulations, your shopping list is complete!')
    else:
        print('Invalid entry. Please enter yes or no')
    

#Task 3: Add a feature that prints out the entire list in a formatted way.

def print_list(shopping_list):
    print('Here is Your Shopping List:')
    for item in shopping_list:
        print(f'{shopping_list.index(item) + 1}. {item}')