# def func(x):
#     return x
# print(func(6))
# class kavin:
#     x=7
#     y=9
# pi=kavin()
# print(pi.x)
# print(pi.y)

# class add:
#     def __init__(self,x,y):
#         self.result=x+y
# class sub:
#     def __init__(self,x,y):
#         self.result=x-y
# n1=int(input("Enter the first number: "))
# n2=int(input("Enter the second number: "))
# h1=add(n1,n2)
# h2=sub(n1,n2)
# print(f"The addition of two number is {h1.result}")
# # print(f"The difference between two number is {h2.result}")

# class kavin:
#     def __init__(self):
#         pass
#     def add(self,x,y):
#         self.result=x+y
#         return self.result
#     def sub(self,x,y):
#         self.result=x-y
#         return self.result
# n1=int(input("Enter the first number: "))
# n2=int(input("Enter the second number: "))
# h1=kavin()
# print(f"The addition of two number is {h1.add(n1,n2)}")
# print(f"The difference between two number is {h1.sub(n1,n2)}")

# class CustomError(Exception):
#     pass
# def age_check(n):
#     try:
#         if(n<18):
#             raise CustomError
#         else:
#             print("He/She is Eligible to Vote")
#     except CustomError:
#         print("He/She is not eligible to vote")
# n1=int(input("Enter the age:"))        
# age_check(n1)

class animal:
    def __init__(self,name):
        self.name=name
        
class reptile(animal):
    def rep(self):
        print(f"{self.name} is a reptile")
class lizard(reptile):
    pass
class snake(reptile):
    pass
class Mammal(animal):
    def ani(self):
        print(f"{self.name} is a mammal")
class dog(Mammal):
    pass
class cat(Mammal):
    pass
class cow(Mammal):
    pass
name=input("Enter the animal name: ")
if name=="dog":
    a1=dog.ani(name)
elif name=="cat":
    a1=cat.ani(name)
elif name=="cow":
    a1=cow.ani(name)
elif name=="snake":
    a1=snake.rep(name)
elif name=="lizard":
    a1=lizard.rep(name)
else:
    print("The name provided is not a animal type")