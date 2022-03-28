# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    arr = []
    number = 0
    participants = int(input("press how many people are you\n"))
    for i in range(participants):
        print(f'press the id of participant{i+1}:')
        for j in range(9):
            num = int(input(f'digit{j+1}:'))
            arr.append(num)
    while number < 19 or number > 30:
        unity = random.choice(arr)
        dozen = random.choice(arr)
        number = dozen*10 + unity
print(f'your question is: {number}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
