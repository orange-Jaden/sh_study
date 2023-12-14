import sys

def my_gen():
    n = 0
    while n < 100:
        yield n
        n += 1

# generator
a = my_gen()
print(sys.getsizeof(a))
print(list(a))

a = my_gen()
print(a.__next__())  # 0
print(a.__next__())  # 1
print(a.__next__())  # 2
