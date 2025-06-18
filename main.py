'''
n=int(input("Enter a number: "))
print(f"The factors of {n} are :")
for i in range(1,n+1):
    if n%i==0:
        print(i)

to_do_list=[]
while True:
    task= input("Enter a task: ")
    if task.lower()== 'done':
        break
    to_do_list.append(task)
print(to_do_list)

str1 = [3,4,6,7,5] # Example from the image, assuming fixed or correctly input
str2 = []
n = len(str1)
flag = True # 'flag' here seems unused before the loop. It might be meant for something else or is a leftover.

if n == 0:
    print("no element")
elif n == 1:
    print(str1[0]) # If there's only one element, it's a peak by definition
    str2.append(str1[0]) # Add it to str2 as well
else:
    for i in range(n): # Iterate using indices (0, 1, 2, ...)
        current_element_is_peak = True # Use a more descriptive flag name

        # Check left neighbor (if it exists)
        # An element is NOT smaller than its left neighbor
        if i > 0 and str1[i] < str1[i-1]:
            current_element_is_peak = False
        
        # Check right neighbor (if it exists)
        # An element is NOT smaller than its right neighbor
        if i < n - 1 and str1[i] < str1[i+1]:
            current_element_is_peak = False
            
        if current_element_is_peak: # If it passed both checks (or single for corners)
            str2.append(str1[i]) # Add the element itself (not its index) to str2

print(str2) # This will print the list of peak elements

p_num=[]
n_num=[]
li=[4,7,9,-9,-34,8,-6,-4,8,5,6,7]
for i in li:
    if i >=0:
        p_num.append(i)
    else:
        n_num.append(i)
tot=p_num+n_num
print(tot)

n=input()
li=[]
for i in n:
    if i==',':
        continue
    else:
        li.append(i)
print(li)        
'''
# def find_multiple_of_20(n):
'''
    Finds the first multiple of 20 that is greater than or equal to n.
    Uses a 'break' statement to exit the loop once the multiple is found.

    Args:
        n: The integer value from which to start searching for a multiple of 20.

    Returns:
        The first multiple of 20 that is >= n, or a message if n is negative.
    
    n=int(input())
    if n<0:
        print("Enter a positive number")
    else:
        i=n
        while True:
            if i%20==0:
                print(i)
                break
       i+=1
'''
# import score
# name = input("Enter your name: ")
# while True:
#     try:
#         n_sub=int(input("Enter subjects: "))
#         break
#     except ValueError:
#         print(" Different datatype is used!!!. Enter Again ")
# sub=[]
# mark=[]
# for i in range(1,n_sub+1):
#     subject=input(f"Enter subj {i}:")
#     while True:
#         try:
#             marks=int(input(f"mark for {subject}:"))
#             break
#         except ValueError:
#             print("integer is not provided in the marks!!!. Please Enter again")
#     sub.append(subject)
#     mark.append(marks)
# print(f"Hello, {name}!")
# print("Marks subject based: ")
# for i in range(n_sub):
#     print(f"{sub[i]} {mark[i]}")
    
# import score
# score.avg(mark,n_sub)

# import score
# name = input("Enter your name: ")
# while True:
#     n_sub=int(input("Enter subjects: "))
#     try:
#         if type(n_sub)=='int':
#             break
#     except ValueError:
#         print(" Different datatype is used!!!. Enter Again ")
# sub=[]
# mark=[]
# for i in range(1,n_sub+1):
#     subject=input(f"Enter subj {i}:")
#     while True:
#         try:
#             marks=int(input(f"mark for {subject}:"))
#             break
#         except ValueError:
#             print("integer is not provided in the marks!!!. Please Enter again")
#     sub.append(subject)
#     mark.append(marks)
# print(f"Hello, {name}!")
# print("Marks subject based: ")
# for i in range(n_sub):
#     print(f"{sub[i]} {mark[i]}")
    
# import score
# score.avg(mark,n_sub)

tx=input("Enter a word to create txt: ")
# tx_1=tx.replace(" ","\n")
f_name=input("Enter file name to write: ")
file=open(f"{f_name}","w")
file.write(tx)
try:
    with open(f"{f_name}","a") as f1:
        f1.write(" Good luck")
except IOError:
    print("File not Found")
else:
    print("Sucessfully Runned")
    