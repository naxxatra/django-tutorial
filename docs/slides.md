---
download: true
themeConfig:
  primary: "#0D9488"
background: https://thepracticaldev.s3.amazonaws.com/i/nmjc40v2drr2prt3wsbs.jpg
highlighter: shiki
---

# Django

<div id="cont">
The web framework for perfectionists with deadlines.
</div>

<style>
div#cont{
  @apply px-3 py-5 filter backdrop-blur-2xl rounded-md bg-gray-100/10;
}
</style>

---

# Outline

<v-clicks>

1. Python intro 
2. django Basics + models
3. Views, Forms, Templates
4. HTML, CSS, UI.
5. _Bonus #1 Deploying to internet_
6. _Bonus #2 API & react app_

</v-clicks>

---

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

---

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

# Dictionaries

Dictionaries are key value pairs

```python
apple = {
    "name": "Apple", 
    "price": 100, 
    "color": "red"
}
orange = {"name": "orange", "price": 50, "color": "orange"}
```

# Dictionaries

Updating dictionaries

```python
apple["price"] = 120 # updating a value
```

```python
apple["flavour"] = "sweet" # adding a new key-value pair
```

```python
apple.update({"calory":125,"type":"natural"}) # updating a dictionary with another dictionary
```


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
>
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

> ### Challenge for you
>
> Write the same program but using fewer conditional statements.

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

---
layout: cover
---

# Session 2

Django basics

---

# Django

Django is a batteries-included web framework for Python.

- can create robust web applications
- easy to get started and learn
- uses an ORM (Object Relational Mapping)
- uses a Model-View-Template (MVT) pattern
- can be used to create a RESTful API (Representational State Transfer) (REST)
  - `(GET, POST, PUT, DELETE)`


---

# Django ORM

Django ORM is an application layer that allows you to interact with a database without writing any raw SQL.

<img src="https://engineertodeveloper.com/wp-content/uploads/2021/01/django_orm_diagram_1.png" class="h-5/6 bg-white/50 rounded-xl">


---

# MVT (model-view-template)

<img src="https://i0.wp.com/blog.knoldus.com/wp-content/uploads/2019/03/mvt.png?resize=571%2C261&ssl=1" class="h-5/6 bg-white/50 rounded-xl">

---

# MVT in code

models.py

```python {all|1|2|3|4|6-7|all}
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

# Views

views.py

```python {all|6-10|11-17|all}
class PostView(View):
    """
    Views for post
    """

    def get(self, request):
        """url to get all posts"""
        posts = Post.objects.all()
        return render(request, 'blog/index.html', {'posts': posts})

    def post(self, request):
        """URL to create a post"""
        title = request.POST.get('title')
        body = request.POST.get('body')
        post = Post(title=title, body=body)
        post.save()
        return redirect('/')
```

---

# Template

blog/index.html

```html {all|1-2|3-7|8-21|10-14|16-20|all}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Blog</h1>
    <ul>
        {% for post in posts %}
            <li>{{ post.title }}</li>
        {% endfor %}
    </ul>
    <h2> create a post </h2>
    <form action="/blog/create" method="post">
        <input type="text" name="title" placeholder="Title">
        <textarea name="body" cols="30" rows="10" placeholder="Your post"></textarea>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```