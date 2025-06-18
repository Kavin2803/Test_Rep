# def simpleGeneratorFun():
# 	yield 1
# 	yield 2
# 	yield 3

# # x is a generator object
# x = simpleGeneratorFun()

# # Iterating over the generator object using next

# # In Python 3, __next__()
# print(next(x))
# print(next(x))
# print(next(x))

# from collections import ChainMap
# dict1={'a':1,'b':2}
# dict2={'b':3,'c':4}
# cm=ChainMap(dict1,dict2)
# print(cm['a'])
# print(cm['b'])
# print(cm['c'])

from collections import Counter
x=Counter("kavinjudesnowin")
print(x)
# for i in x.elements():
#     print(i, end=" ")