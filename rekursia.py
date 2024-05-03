# def func(x):
#     print(x)
#     func(x+1)
# func(1)

# def func(x):
#     if x < 7:
#         print(x)
#         func(x+1)
#         print(x)
# func(1)

# def summa(x):

#     if x == 1:
#         return 1
#     else:
#         return x + summa(x-1)
# print(summa(10))


# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(10))

# def main(number):
#     print(number)
#     if number == 0:
#         return number
#     else:
#         main(number+1)

# main(-20)


# def main(number):
#     print(number)
#     if number == 0:
#         return number
#     else:
#         main(number-1)

# main(20)

# l = lambda num: True if num > 5 else False
# print(l(3))

# def compare(n):
#     if n>5:
#         return True
#     else:
#         return False
# print(compare(12))

# l = lambda b, a: b * a
# print(l(15, 100))

# list = [12,3,4,5,45]
# def get_filters(a, filter=None):
#     if filter is None:
#         return a
#     else:
#         result =[]
#         for i in a:
#             if filter(i):
#                 result.append(i)
#     return result
# print(get_filters(list, lambda x: x>5)) 
        
# g = (lambda x, y: f'Количество пикселей из картинке {x*y}')(10, 15)
# d = (lambda weight, height: f'Вам необходимо набрать {(height-110) -weight}кг')(50, 167)
# print(g)
# print(d)




















































































