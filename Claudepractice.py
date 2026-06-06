#1.Write a program that prints the sum of all odd numbers from 1 to 50 (inclusive).
total = 0
for i in range(1, 51):
    # your code here
   if i%2 ==0:
    total = total + i
   else:
    print(total)

#2.Caesar Cipher Encoder
def caesar(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result

print(caesar("Hello, World!", 3))
print(caesar("xyz", 2))

#3.revers the string 
def reverse_string(s):
    return s[::-1]

print(reverse_string('Python'))

#4.remove duplicate numbers 
numbers = [4,2,7,9,4,1,7,5]
a = sorted(numbers)
print(a)

#5. Word frequency Counter 
sentence = "many always lies"
words = sentence.split()
freq = {}
for word in words:
    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
print(freq)

#6. FizzBuzz
for i in range(1,31):
    if i%3 ==0 and i%5==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0:
        print('Fizz')
    else:
        print(i)

#7.Factorial with recursion 
def factorial(n):
   if n ==1:
      return 1
   else :
      return n * factorial(n-1)
   

print(factorial(5)) 

#8.print the list from 1 to 100 which is divided by 3
square = []

for num in range(1,101):
    result = num**2
    if result % 3 ==0:
        square.append(result)
    else:
        pass

print(square)


#9. adding two list with removing duplicates 
list_a = [1,2,3,4,5,6]
list_b = [4,5,6,7,8,9]
new_list = list_a + list_b
unique = set(new_list)
print(list(unique))

#10.Sort them by score in descending order
students = [
    ("Ram", 88),         
    ("Bhim", 72),
    ("Safal",21),
    ("Diana",80)
]

result = sorted(students, key = lambda student: student[1])

print(result)

#simple phonebook with three people in it
def add_contact(book,name,number):
    book[name] = number

def lookup(book,name):
    if name in book:
        return book[name]
    else:
        return "Not Found"

# phonebook dictionary
phone_book = {}

# adding contacts
add_contact(phone_book, "Safal", 123)
add_contact(phone_book, "Bhim", 2222)
add_contact(phone_book, "Sita", 3232)

# printing phonebook
print(phone_book)

# lookup examples
print(lookup(phone_book, "Safal"))
print(lookup(phone_book, "Bhim"))



 




