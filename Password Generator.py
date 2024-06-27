import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", ",", ".", "<", ">", "/", "?", "|", "`", "~"]

amount = int(input('Choose the amount of passwords: '))
length = int(input('Choose password length: '))

file1 = open('C:\\Users\\beybu\\Saved Games\\PycharmProjects\\pythonProject\\textfile.txt','w')

def generate_password(x):
    password = ''
    for i in range(x):
        category = random.randint(1, 3)

        if category == 1:
            character = letters[random.randint(0,len(letters))-1]
            if len(password) > 0:
                while password[-1] in letters and abs(letters.index(character) - letters.index(password[-1])) < 2:
                    character = letters[random.randint(0, len(letters))-1]
            password += character

        elif category == 2:
            character = numbers[random.randint(0,len(numbers))-1]
            if len(password) > 0:
                while password[-1] in numbers and abs(numbers.index(character) - numbers.index(password[-1])) < 2:
                    character = numbers[random.randint(0, len(numbers))-1]
            password += character

        else:
            character = symbols[random.randint(0,len(symbols))-1]
            if len(password) > 0:
                while password[-1] in symbols and abs(symbols.index(character) - symbols.index(password[-1])) < 2:
                    character = symbols[random.randint(0, len(symbols))-1]
            password += character
    return password

for i in range(amount):
    file1.write(generate_password(length))
    file1.write('\n')
file1.close()