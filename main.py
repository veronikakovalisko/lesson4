"""
Task 1

The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets
the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""
import random

if __name__ == '__main__':
    a = input("хочеш зіграти?")
    while a in "yYтТ":
        x = random.randint(1, 10)
        y = input("введи своє число")
        if x == y:
            print("ти вгадав")
        a = input("хочеш зіграти?")
"""
Task 2
The birthday greeting program.
Write a program that takes your name as input, 
and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years”   
"""
if __name__ == '__main__':
    name = input("введіть своє ім'я:")
    age = int(input("введіть свій вік:"))
    print(f"Hello {name}, on your next birthday you’ll be {age + 1} years")
"""
Task 3
Words combination
Create a program that reads an input string and 
then creates and prints 5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’,
 so it should print 5 random strings(words) that combine characters 
 ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
Tips: Use random module to get random char from string)
"""
if __name__ == '__main__':
    word = input("enter your word")
    x = 0
    n = 1
    while True:
        while x < len(word):
            print(random.choice(word), sep="", end="")
            x = x + 1
        print("\n")
        n = n + 1
        if n == 6:
            break
"""
Task 4
The math quiz program
Write a program that asks the answer for a mathematical expression, 
checks whether the user is right or wrong, and then responds with a message accordingly.
"""
if __name__ == '__main__':
    answer = int(input("\n 5*16="))
    while True:
        if answer == 5*16:
            print(" молодець")
            break
        else:
            print(" не правильно спробуй ще раз")
            answer = int(input("5*16="))


