from sys import getsizeof
my_comp = [x*5 for x in range(1000)]
my_gen = (x*5 for x in range(1000))
print(getsizeof(my_comp))
print(getsizeof(my_gen))
