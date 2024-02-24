print("Hello Iris")
print("Welcome to Python 1.0")

name = "Andres Felipe Cabezas Quicano" ## How can I retrieve the uppercase letters in the string?

# Whenever you create a variable give it a meaning
# listOfUppercase = []
# for l in name:
#     # if ord("A") <= ord(l) <= ord("Z"):
        
#     #     listOfUppercase.append(l)
    
#     # if l.upper(): # i == "j"
#     #     listOfUppercase.append(l)
    
#     if True: # upper == True -> upper()
#         print("Hello")
#     else:
#         print("Bye")d

wordlist = name.split()
print(wordlist[3])

myDictirionary = {
    'a': ["Apple","Appereance","Alarm"],
    'b': ["Bananas","Bee","Boiler"],
    'c': ["Color","Case","Cert"],
    'd': ["Dice","Door","Dormant"]
}

print(myDictirionary['a'])

numbers = [i+1 for i in range(30)] ## List comprehension

myList= [] 
for i in range(30):
    myList.append(i+1)

number = 43
def numbercheck(x):
    if x%2 == 0:
        print("even")
    else:
        print("odd")

numbercheck(number)

print(numbers)
print(myList)        




# for i in name:
#     if 97 >= ord(i) >= 120: # Good can i uderstand this code by itself
        