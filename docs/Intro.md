# Python basics

Speedrun Python basics

---

# Basic operations (Arithmetic)

```python {1|3|5|7|9|11|13|all}
1 + 2 # Addition

1 - 2 # subtraction

2 * 3 # multiplication

9 / 2 # division

9 // 2 # floor division

2 ** 3 # exponent

5 % 2 # modulus
```

# Basic operations (Comparison)

```python {1|3|5|7|9|11|all}
2 == 3 #Is it equal?

1 != 2 #Is it NOT equal?

7 < 11 #Is it lesser?

5 > 9 #Is it greater?

67 >= 88 #Is it greater than or equal?

24 <= 666 #Is it lesser than or equal?
```

---

# Basic operations (Logical)

```python {1|3|5|all}
(1 < 2) or (3 < 5) #If either of the 2 operations returns true, the final result will also be true

(4 == 3) and (10 != 10) #Both operations need to return true in order for the final result to be true

not (5*3 == 15) #Reversal
```

---

# Variables

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

---

# Data types

Integer

```python
int
-1, 2, 0, 1000
```

Float

```python
float
0.1, 2.76, -9.45
```

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

None

```python
None
```

\-\-

### Check type

```python
a = 10
type(a)
```

---

# Operations with variables

```python
a,b = 10,20 # assign multiple variables
```

try these operations with `a` and `b`

```python {1|3|5|7|9|11|13|all}
print(a + b)

print(a - b)

print(a * b)

print(a / b)

print(a < b)

print(a > b)

print(a == b)
```

```python
del a,b #delete variables
```

---

# Strings

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

---

# Type Conversion

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

---

# Lists

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

---

# Tuples

Immutable collection of items

```python
# Immutable collection of items
t = (1, 2, 'a', 0.4, False)
```

```python
t[2] # accessing by index
```

```python
t[2:4] # accessing a slice
```

we cannot add, remove or modify items from a tuple

---

# Conditional Statements

```python
a, b, c = 10, 20, 30


if (a > b) and (a > c):
    print("a is the largest")
elif (b > a) and (b > c):
    print("b is the largest")
else:
    print("c is the largest")
```

---

# Problem (FizzBuzz)

A practice problem to learn how to use conditional statements.

> Fizzbuzz is a problem where you have to print the numbers from 1 to 100. 
> - But for multiples of 3 print "Fizz" instead of the number 
> - and for the multiples of 5 print "Buzz". 
> - For numbers which are multiples of both 3 and 5 print "FizzBuzz".

```python
1 # example output
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
```

---

# Sample Solution

```python {all|1|2-3|4-5|6-7|8-9|all}
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

>
> ### Challenge for you
> 
> Write the same program but using fewer conditional statements.
> 

---

# Solution 2

```python {1-2|3-4|5-6|7-8|9|all}
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if output == "":
        output = str(i)
    print(output)
```

---

# Solution 3

```python {all|1|2|2-3|2-4|5-6|7-8|9-10|all}
for i in range(1, 101):
    if i % 3:
        if i % 5:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % 5:
        print("Buzz")
    else:
        print(i)
```
