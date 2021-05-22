#Calculate sum of all numbers included in the list.
num_list = [0,1,2,3,4,5]
def list_sum(num_list):
    sum = 0
    for num in num_list:
        sum += num
    print("The sum is "+str(sum))
list_sum(num_list)



#Show a random number from a list.
import secrets
x = [0,1,2,3,4,5]
print(secrets.choice(x))



#Calculate the number of amount letters in a txt file.
with open("Mayus.txt") as f:
    count = 0
    text= f.read()
    for character in text:
        if character.isupper():
            count += 1
    print(count)
    
   
   
#Save an image with a python library if the url is known.
import requests
url_imagen = "https://cdn.pixabay.com/photo/2020/04/23/16/45/eagle-5083248_960_720.jpg"
name_imagen = "Halcon.jpg"
imagen = requests.get(url_imagen).content
with open(name_imagen, 'wb') as handler:
    handler.write(imagen)
 


#Replace a specific word with another
import re
text = "Hola Mundo"
re.sub("Hola","Hi",text)



#Replace a word and return the replacement amount
re.subn("Hola","Hi",text)



"""
Generate a random number between 1 and 120.
Say if it is in the range between 10 and 50, or if it is greater than 50 up to 100,
or if it is greater than 100, or if it is less than 10.
"""
import random
number = random.randint(1, 120)

if number in range(10, 50):
    print("This number is the range: "+str(number))    
else: 
    print("This number is not the range: "+str(number))
    if number in range(50, 100):
        print("This number is greater than 50")
    elif number > 100:
        print("This number is greater than 100 ")
    else:
        print("This number is less than 10 ")



"""
List the even numbers from 10 to 20
"""
list_pairs = []
for i in range(10, 20, 2):
    list_pairs.append(i)
list_pairs



"""
Geometric progression
Calculate how many grains of wheat we would have to use if for each square on a chessboard
Let's put one grain in the first box, two in the second, four in the third, and so on, doubling up to the last.
"""
chess_vertical= 8
i = 0
grains = 1
wheats = 0
while i < chess_vertical:
    grains *=2
    wheats += grains
    i += 1
print(wheats)