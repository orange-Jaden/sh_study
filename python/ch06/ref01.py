# import sys

# def my_gen():
#     n = 0
#     while n < 100:
#         yield n
#         n += 1

# # generator
# a = my_gen()
# print(sys.getsizeof(a))
# print(list(a))

# a = my_gen()
# print(a.__next__())  # 0
# print(a.__next__())  # 1
# print(a.__next__())  # 2

n = "10 20 30"
ns = n.split() # ns = ['10', '20', '30']
print(ns)

print(list(map(int, ns)))

i = 0
while i < 10:
    print("상혁이 졸리다")
    i = i+1