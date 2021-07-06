def add(x, y):
    return x + y
# Call the function
print(add(2, 3))  # Output: 5

add = lambda x, y : x + y

l = [1,2,3,4,5]
def raise_to_power_two(x):
    return x ** 2
a = list(map(raise_to_power_two, l))  # Output [2, 4, 6, 8]
print(a)


## Single line
print(list(filter(lambda x:x%2,[1,2,3,4,5])))


dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print(*map(lambda x : x['name'], dict_a))
