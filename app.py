print("Hello World")

# TODO: Comment
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#TODO: String
name = "thoriq"
age = "21"

print(name + " " + age)
print("my name: " + name +"\nmy age: " + age )
print(name * 10)

#TODO: Input
nama = input("Whate is your name: ")
fcolor = input("What is your favorite color: ")
print("Hello " + nama + " likes " + fcolor )

birth_year = int(input('Birth year: '));
birth_month = int(input('Birth month: '));

print(type(birth_year))
age_year = int(2022 - birth_year)
age_month = int(12 - birth_month)
print(age_year, age_month)

#TODO: Position
name = "M Thoriq A S"
name2 = name[-4:-1];

msg= f'{name} [{name2}] yes!!!'
print(msg)
print(name[0:3]) #! M
print(name[4:-9]) #! Thoriq

#TODO: Function
name = "Learning Python"
age = "16"
print(len(name))
print(name.upper())
print(name.lower())
print(age.isnumeric()) #! True
print(name.isupper()) #! false
print(name.upper().isupper()) #! True

print(name.find("P"))
print(name.replace('Python','Java'))
print('python' in name) #! false
print('Python' in name) #! True
print(name.title())

# TODO: Numeric

number = 10
number += 5;
number2 = number - 3;
print(number, number2) #! 15 12

number = 2 ** 3;
number2 = 8 // 2;
number3 = 10 % 5;
print(number, number2, number3) #! 8 4 0

# TODO: Numeric Function
number = 2.9999
print(round(number)) #! 3
print(abs(-number))

import math
print(math.ceil(number)) #! 3
print(math.floor(number)) #! 2

#TODO: Condition

#? Weather
hot = False;
cold = False;
if hot:
    print("It's a hot day")
elif cold:
    print("It's a cold day")
else:
    print("Warm Day")

weather = input("Suhu Hari Ini? ")
if weather > "20" :
    print("It's a hot day")
elif weather <= "20":
    if(weather >= "15"):
        print("It's a lovely day")
    else:
         print("It's a cold day")

#? House
priceHouse = 1000;
goodCreadit = True;
if goodCreadit:
    payment = 1000 * 10//100;
else:
    payment = 1000 * 20//100;
print(f"Rp. {payment}")

#? Animal
likeCat = True;
likeDog = False;

if likeCat and likeDog:
    print("Love Animal")
elif likeCat or likeDog:
    print("Love One Animal")
    if likeCat:
        print("Love Cat")
    elif likeDog and not likeCat:
        print("Love Dog")
else:
    print("Not Love Animal")

passwordInput = input("Input Your Password: ")

#? Password
if len(passwordInput) <= 5:
    print(f" Password Weak \n Password: {passwordInput}")
elif len(passwordInput) >5 and len(passwordInput)<=10:
    print(f"Okay \n Password: {passwordInput}")
else:
    print(f"Password Strong \n Password: {passwordInput}")

#? Taste Food 

Food = input("What Food : ")
Taste = input("Manis Atau Pedas ? ")
foodTaste= Taste.lower();
if foodTaste == "manis":
    print(f"Pesanan: {Food} \n Rasa {Taste}")
elif foodTaste =="pedas":
    print(f"Pesanan: {Food} \n Rasa {Taste}")
elif foodTaste != "manis" and foodTaste != "pedas" :
    print("Wrong Input at Taste")
else : 
    print("Something Wrong")

#TODO: While Loop

i = 1;
while i <= 5:
    print(i)
    i += 1;
print("Done")

#? Copy
inputI = input("Number of Copy: ")
inputName = input("Your Name: ")

i=1;
while i <= int(inputI):
    print(f"{i}. {inputName}")
    i += 1;
print("Copy Finish");

#? Guess Game

secretNumber = 7 and 2;
guessCount = 0;
lose = 4;

while guessCount < lose:
    inputGuess = int(input("Your Guess: "))

    guessCount +=1
    if(guessCount == 3):
        print("This is Your last change: ")
    if inputGuess == secretNumber:
        print(f"Your Answer Corret, The Secret Number is {secretNumber}")
        break;
else: 
    print(f"You Lose!! \n Your Last Guess is {inputGuess}")


#? Phone Start And Lock

inputStart =False
inputLock = False

print("""start - to unlock the phone
lock - to lock the phone
exit - to shutdown phone""")

while True:
    userInput = input("> ")
    if(userInput.lower() == "start"):
        if inputStart:
            print("Phone Already Started!")
        else:
            print("Phone Starting")
    elif(userInput.lower() == "lock"):
        if not inputStart:
            print("Phone Already Lock")
        else:
            inputStart = False
            print("Phone Lock")
    elif(userInput.lower()== "help" or userInput.lower()== "how"):
        print("start - to unlock the phone")
        print("lock - to lock the phone")
        print("exit - to shutdown phone")
    elif(userInput.lower() == "exit"):
        print("Exit Success")
        break;
    else: 
        print("Input Unknown")

#TODO: For Loop

for i in [1,2,3]:
    print(i)

for i in range(10):
    print(i)

for i in range(1,10):
    print(i)

for i in range(1,10,2):
    print(i)

#? Total Price Input
many = int(input("How many input: "))
i=1
result=0
while i <= many:
    inputMany = int(input(f"Price {i}: "))
    result += inputMany
    i +=1

print(f"Total: {result}")

for x in range(1,4):
    for y in  range(1,3):
        print(f"{x},{y}")

for x in range(5):
    for y in range(1,5):
        print("1")
    print("*")

numbers = [5,2,5,2,5]
for x in numbers:
    output = ""
    for count in range(x):
        output += "x"
    print(output)

#? Max Number Array

numbers = [2,4,6,10,8]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)

#TODO: 2D List Matrix

matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][2] = 100;
print(matrix[0][1])
print(matrix[0][2])
print(matrix)

#? Print All Value Matrix
for row in matrix:
    for x in row:
        print(x)

numbers = [2,6,10,3]
numbers.append(20) #! insert last
numbers.insert(1,100) #! insert at position index
numbers.remove(2) #! remove one value
numbers.pop() #! romove last value
numbers.clear() #! remove all value
numbers.sort() #! sort from ascending
numbers.reverse() #! sort from descending but need sort first
numbers2 = numbers.copy() #! copy all value
print(numbers)
print("This is a copy: ", numbers2)
print(100 in numbers) #! False Because 100 not in numbers array

#? Remove duplicate value
numbers = [2,6,2,10,3]
duplicate = []
for i in numbers:
    if i not in duplicate: #! if value numbers not in duplicate array +
        duplicate.append(i)
        duplicate.sort()

print(duplicate)

# TODO: Tuples & Unpacking

numbers = (1,True,"Cat",1000,1) #! This is Tuples
numbers1 = tuple(numbers)
print(numbers1)

numbers = (2,4,6)
x,y,z = numbers
print(y)


# TODO: Dictionaries

#Value Must be Uniq
identity = {
    "name" : "Thoriq",
    "age" : 18,
    "is_collage" :True
}
print(identity["name"])
print(identity.get("is_marry")) #! None
print(identity.get("Adress","Earth"))

identity["Number"] = "08xxx"
identity["age"] = 19
print(identity["Number"])
print(identity["age"]) 

#? Convert Phone Number to Letter

phone = input("Your Phone Number: ")

phone_number ={
    "0" : "zero", 
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five", 
    "6" : "six", 
    "7" : "seven", 
    "8" : "eight", 
    "9" : "nine", 
}
result =""
for number in phone:
    result += phone_number.get(number, "'unkonwn number'") + " "

print(result)

#? Emoji Convert
messege = input("Input Here: ")
words = messege.split(" ")

emojis = {
    ":)" : "😃",
    ":(" : "🙁"
}
result=""
for emo in words:
    result += emojis.get(emo,emo) + " "

print(result)

# TODO: Function & Exception

def phone():
    try:
        number = int(input("Input Your PhoneNumber: "));
        print('Your Phone Number: ',number)
    except (ValueError, TypeError):
        print("PhoneNumber must be a int")
        phone()

phone()

def welcome(firstname, lastname):
    print('Welome ',firstname,lastname)

name = input("Enter your first name: ")
name2 = input("Enter your last name: ")
welcome(name, name2)
welcome("A", "S")

def square(side):
    return side * side;

try:
    inputSide = int(input("Enter your side: "))
    print(square(inputSide))
except ValueError:
    print("Side mush be a number")
    square(inputSide)

#? Convert Emoji With Function
def converEmoji(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😃",
        ":(" : "🙁"
    }
    result=""
    for emo in words:
        result += emojis.get(emo,emo) + " "
    return result;

message = input("input Here: ")
print(converEmoji(message))

# TODO: Classes

class Point:
    def move(self):
        print("move")
    
    def attack(self):
        print("attack")
    
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x, point1.y)
point1.attack()

point2 = Point()
point2.move()

# TODO: Constructor

class Game:
    def __init__(self,x,y):
        self.x = x
        self.y = y

score = Game(100,200)
print(score.x)  

class Person: 
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
    def talk(self):
        print(f"Hello, {self.name} {self.lastname}")

input2 = input("Input your Name: ")
input3 = input("Input your Last Name: ")
name2 = Person(input2,input3)
name2.talk()

# TODO: Inheritance
class Game:
    def name(self):
        print("This is game")

class FPS(Game):
    def shot(self):
        print("This is shot key")
    pass

class Moba(Game):
    pass

Fps1 = Game()
Fps1.name()
Fps2 = FPS()
Fps2.shot()

# TODO: Modules

import learnModuls
from  learnModuls import dollar_to_rupiah

try:
    moneyRp=int(input("Your Rupiah Money:"))
    print(learnModuls.rupiah_to_dollar(moneyRp),"Dollar")
    moneyDollar=int(input("Your Dollar Money:"))
    print("Rp.",dollar_to_rupiah(moneyDollar))

except:
    print("Money mush be a number!")

#? Max Number

from learnModuls import find_max
result=[]
many = int(input("How many number: "))

for i in range(many):
    inputNumber =int(input("> "))
    result.append(inputNumber)

print(find_max(result))

# TODO: Packages

import learnPackages.shop
learnPackages.shop.fruit("appel")

from learnPackages import shop
shop.fruit("manggo")

from learnPackages.shop import fruit
fruit("orange")

# TODO: Random Values

import random

for i in range(3):
    print(random.randint(1,5))

memebers = ['M','thoriq','AS']
leader = random.choice(memebers)
print(leader)

import random
class Dice:
    def roll(self):
        tuple1 = random.randint(1,5)
        tuple2 = random.randint(1,5)
        return tuple1, tuple2

dice = Dice()
print(dice.roll())

# TODO: Directory

from pathlib import Path

path = Path("shop")
print(path.exists())

new = Path("newFile")
print(new.mkdir())

globPath= Path()
for file in globPath.glob("*.py"):
    print(file)