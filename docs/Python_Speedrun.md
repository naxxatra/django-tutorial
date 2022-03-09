# __Python Speedrun__
#### A speedrunning mission presented to you by _Naxxatra Sciences_

## Basic Operations

### Arithmetic Operations


```python
1 + 2 # Addition
```


```python
1 - 2 # subtraction
```


```python
2 * 3 # multiplication
```


```python
9 / 2 # division
```


```python
9 // 2 # floor division
```


```python
2 ** 3 # exponent
```


```python
5 % 2 # modulus
```

### Comparison Operations


```python
2 == 3 #Is it equal?
```


```python
1 != 2 #Is it NOT equal?
```


```python
7 < 11 #Is it lesser?
```


```python
5 > 9 #Is it greater?
```


```python
67 >= 88 #Is it greater than or equal?
```


```python
24 <= 666 #Is it lesser than or equal?
```

### Logical Operations


```python
(1 < 2) or (3 < 5) #If either of the 2 operations returns true, the final result will also be true
```


```python
(4 == 3) and (10 != 10) #Both operations need to return true in order for the final result to be true
```


```python
not (5*3 == 15) #Reversal
```

## Variables


```python
a = 10

print(a)
```


```python
name = "minion"

print(name)
```


```python
b = 42
B = "X-rays"

print(b,B)
```


```python
D = 22
D = "Ant"

print(D)
```

### Data types

Integer
```python
int
-1, 2, 0, 1000
```
---

Float 
```python
float
0.1, 2.76, -9.45
```
---
Strings

```python
str
'python', 'NAXXATRA', "hello", "wonder"

"""disco""",

"""
this is a multi-line string
"""

```
---
Boolean
```python
bool
True, False 
```
---
None
```python
None
```


```python
type(a)
```


```python
b = 20
print(b)
```


```python
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a < b)
print(a > b)
print(a == b)
```


```python
del a,b
```

## Strings


```python
# Strings are collection of characters
str1 = 'laka '
str2 = 'laka '
print(str1)
print(str2)
```


```python
print(str1 + str2)
print(str1 * 5)
```


```python
str1.upper(), str2.lower()
```


```python
s1 = '1'
s2 = '2'
print(s1 + s2)
```


```python
#Indexing (Collections in python are 0-indexed, i.e, the first element's index is 0)
print(str1[2])
```


```python
#Slicing - str1[start : stop : step] 
print(str1[1:5])
```


```python
del str1, str2, s1, s2
```

## Type Conversion


```python
a = 10
b = str(a)
c = float(a)
```


```python
type(a)
```


```python
type(b)
```


```python
type(c)
```


```python
d = int(b)
```


```python
type(d)
```


```python
a = input("Enter the first number: ")
type(a)
```


```python
a = int(input("Enter the first number: "))
type(a)
```


```python
del a,b,c,d
```

## Lists

Mutable collection of heterogenous items


```python
# Mutable collection of heterogenous items
l = [1, 2, 'a', 0.4, False]
```


```python
l[2] # accessing by index
```


```python
l[2:4] # accessing a slice
```


```python
l.append(42) # adding to end of a list
l
```


```python
l.append([9,0]) # adding to a list
l
```


```python
del l # delete
```

## Conditional Statements


```python
a = 10
b = 11
c = 20
```


```python
if (a > b) and (a > c):
    print("a is the largest")
elif (b > a) and (b > c):
    print("b is the largest")
else:
    print("c is the largest")
```


```python
del a, b, c
```

## Looping Statements

### For loops


```python
for i in range(5):
    print(i)
```


```python
for i in [2, 3, 'naxxatra', 'rasp']:
    print(i)
```

### While loops


```python
i = 0
while i <= 10:
    print("Python")
    i = i + 1
```

## Functions


```python
def add(a, b):
    c = a + b
    return c

n1 = 4
n2 = 6
n3 = add(n1, n2)
print(n3)
```

### Default Arguments


```python
def greet(name = "Alfred"):
    print("Hello " + name)
```


```python
greet("Bruce")
```


```python
greet()
```

### Keyword Arguments


```python
def greet(msg, name):
    print(msg + " " + name)
```


```python
greet("Good morning", "Peter")
```


```python
greet(name="Peter", msg="Good night")
```

### Arbitrary Arguments


```python
def greet(*names):
    for name in names:
        print("Hello " + name)
```


```python
greet("Tony", "Alfred", "Bruce")
```

## Importing Packages


```python
import random
```


```python
l = [1, 2, 3, 4, 5]
random.choice(l)
```


```python
random.randint(4, 30)
```


```python
random.random()
```


```python
import math
```


```python
x = 3
print(math.sin(x))
```


```python
y = 36
print(math.sqrt(y))
```
