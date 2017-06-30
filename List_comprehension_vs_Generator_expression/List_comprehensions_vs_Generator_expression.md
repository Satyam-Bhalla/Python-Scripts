
## Simple List


```python
my_list = []
for x in range(10):
    my_list.append(x*2)
print(my_list)
```

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    

## List Comprehension



```python
comp_list = [x*2 for x in range(10)]
print(comp_list)
```

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    

## List Comprehension with modifier


```python
comp_list_modif = [x ** 2 for x in range(7) if x%2 == 0]
print(comp_list_modif)
```

    [0, 4, 16, 36]
    

## List of Lists with List comprehension


```python
nums = [1,2,3,4,5,6]
letters = ['A','B','C','D','E','F']
nums_letters = [[n,l] for n in nums for l in letters]
print(nums_letters)
```

    [[1, 'A'], [1, 'B'], [1, 'C'], [1, 'D'], [1, 'E'], [1, 'F'], [2, 'A'], [2, 'B'], [2, 'C'], [2, 'D'], [2, 'E'], [2, 'F'], [3, 'A'], [3, 'B'], [3, 'C'], [3, 'D'], [3, 'E'], [3, 'F'], [4, 'A'], [4, 'B'], [4, 'C'], [4, 'D'], [4, 'E'], [4, 'F'], [5, 'A'], [5, 'B'], [5, 'C'], [5, 'D'], [5, 'E'], [5, 'F'], [6, 'A'], [6, 'B'], [6, 'C'], [6, 'D'], [6, 'E'], [6, 'F']]
    


```python
iter_string = "some text"
string_list = [x for x in iter_string if x != " "]
print(string_list)
```

    ['s', 'o', 'm', 'e', 't', 'e', 'x', 't']
    

## Create dicts and set comprehensions


```python
dict_comp = {x:chr(65+x) for x in range(1,11)}
print(dict_comp)
```

    {1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K'}
    


```python
set_comp = {x**3 for x in range(10) if x%2 == 0}
print(set_comp)
```

    {0, 8, 64, 512, 216}
    

## Difference Between Iterable and Iterator

 It will be easier to understand the concept of generators if you get the idea of iterables and iterators.
Iterable is a “sequence” of data, you can iterate over using a loop. The easiest visible example of iterable can be a list of integers - [1, 2, 3, 4, 5, 6, 7]. It’s possible to iterate over other types of data like strings, dicts, tuples, sets, etc.
Basically, any object that has iter() method can be used as an iterable. You can check it using hasattr() function in the interpreter.

```python
hasattr(str, '__iter__')
```




    True




```python
hasattr(bool,'__iter__')
```




    False




```python
simple_list = [1,2,3]
my_iterator = iter(simple_list)
print(next(my_iterator))
print(next(my_iterator))
```

    1
    2
    

## Generator Expressions
In Python, generators provide a convenient way to implement the iterator protocol. Generator is an iterable created using a function with a yield statement.
The main feature of generator is evaluating the elements on demand. When you call a normal function with a return statement the function is terminated whenever it encounters a return statement.
In a function with a yield statement the state of the function is “saved” from the last call and can be picked up the next time you call a generator function.

```python
gen_exp = (x ** 2 for x in range(10) if x%2 == 0)
for x in gen_exp:
    print(x)
```

    0
    4
    16
    36
    64
    

## Type of data differs for list comprehensions and generator expressions


```python
list_comp = [x**2 for x in range(10) if x%2 == 0]
print(list_comp)
gen_exp = (x**2 for x in range(10) if x%2 == 0)
print(gen_exp)
```

    [0, 4, 16, 36, 64]
    <generator object <genexpr> at 0x012869F0>
    

 ## Generator takes less memory


```python
from sys import getsizeof
my_comp = [x*5 for x in range(1000)]
my_gen = (x*5 for x in range(1000))
print(getsizeof(my_comp))
print(getsizeof(my_gen))
```

    4516
    48
    
