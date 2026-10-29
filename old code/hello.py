# print("Hello World!")

# Variable

# number_one = 500
# number_two = 100 


# print(number_one + number_two)
# print(number_one - number_two)
# print(number_one * number_two)
# print(number_one / number_two)
# print(number_one % number_two)


# principal = 1000
# rate = 5
# time = 1 

# simple_interest = principal * rate * time / 100 

# print(simple_interest)


# print(5 + 5 - 5 * 5 / 5)

# string

# first_name = "Peter"
# last_name = "Parker"

# print(first_name + " " +last_name)

# your_name = input("Please Enter Your Name : ")

# print("Welcome : " , your_name)
# print(f"Welcome {your_name}")


# Boolean

# is_admin = True 

# print(is_admin)

# print(5 == 5)

# number = 6


# if(number == 5) :
#     print("Number is equal to 5")
# else :
#     print("Number is not equl to 5")


# marks = 40 

# if(marks >= 33) :
#     print("PASS")
# else:
#     print("FAIL")


# marks  = int(input("Enter Your Marks : "))


# print(type(marks))

# if(marks >= 33) :
#     print("Pass") 
# else :
#     print("Fail")


# status = input("PLEASE ENTER LIGHT COLOR : ")

# if(status == "RED"):
#     print("STOP")
# elif(status == "YELLOW") :
#     print("READY")
# elif(status == "GREEN") :
#     print("GO")
# else :
#     print("SOmething Went Wrong")


# List

numbers = [1,2,3,4,5]

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])


# for number in numbers :
#     print(number)

# for number in range(1,11) :
#     print(number * 13)


# for number in range(1, 101) :
#     if(number % 2 == 0) :
#         print(number)


# def print_name(name) :
#     print(f"Hello {name}")


# print_name("Peter")
# print_name("Thor")

# def find_distance(speed , time) :
#     print(speed / time)


# find_distance(150 , 2)

# def ikkis_din(paisa) : 
#     return paisa * 2


# result = ikkis_din(1000)
# print(result)

# def print_table(num) :
#     for number in range(1 , 11) :
#         print(num * number)


# print_table(10)


# def print_numbers(num) :
#     for number in range(1 , num + 1) :
#         if(number % 2 == 0) :
#             print(number)


# print_numbers(1000)


numbers = [1,2,3,4,5,6,7,8,9,10]


# for number in numbers : 
#     if(number % 2 == 0):
#         print(number)


# total = 0 

# for number in numbers :
#     total = total + number 

# print(total)


# def print_total(numbers) :
#     total = 0
#     for number in numbers :
#         total = total + number 
#     return total


# result = print_total([5,4,3,2,1])
# print(result)


# variable
# int/number
# string
# boolean
# if condition
# for
# range()
# function
# return


# def add_values(a,b) :
#     return a+b

# result = add_values(100,100)
# print(result)


# Match Case


# day = "WEDNESDAY"

# match day : 
#     case "MONDAY" :
#         print("Its Monday")
#     case "FRIDAY" :
#         print("Its FRIDAY")
#     case "SUNDAY" :
#         print("Its FRIDAY")
#     case _ :
#         print("ITS ANOTHER DAY!")


# word = input("Enter word :")


# match word :
#     case "a" :
#         print("Vowel")
#     case "e" :
#         print("Vowel")
#     case "i" :
#         print("Vowel")
#     case "o" :
#         print("Vowel")
#     case "u" :
#         print("Vowel")
#     case _ :
#         print("Consonent")


numbers =[1,2,3,4,5]

# print(numbers[0])
# print(numbers[-1])
# print(len(numbers))

numbers.append(6)

# numbers.pop(0)

# print(numbers)

# print(300 in numbers)

# Dictionary

# user = {
#     "name" : "Peter Parker",
#     "age" : 26,
#     "isAvenger" : False
# }

# user["email"] = "peter@gmail.com"

# user["name"] = "Tony"

# del user["age"]

# print(list(user.keys()))
# print(list(user.values()))

count = 0 

while count <= 3 :
    print(count)
    count = count + 1