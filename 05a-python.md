# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> In Python, lists and tuples are ordered (indexed) data structures used with `[]` and `()`, respectively. The main difference is that lists are mutable while tuples are not. Because of this fact, each tuple is a structured data point with each element of the tuple having a specific type/purpose. On the other hand, lists are collections of the same data types. Additionally, since tuples are immutable, they may be used as dictionary keys.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Syntactically, lists and sets use `[]` and `{}`, respectively. Lists are ordered, mutable, and indexed while sets are none of the above. Sets do not allow for multiple entires of the same value while lists do. An example of a list would be `[1,1,2,3,4,4,5,6]` and the set of the same list would be `{1,2,3,4,5,6}`. Comparing performance, sets are faster than lists when it comes to finding elements. This is because sets use hash tables, which gives each object a specific position determined by its hash. So when finding elements, only the specific position in memory is tested for membership where as a list goes through every entry.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The `lambda` operator is a quick way to create an anonymous function with the following syntax:  
```Python
`lambda` arguments: expression
```
>> Lambda functions can be used wherever function objects are required but are usually used in higher-order functions. The operator comes with `map()`, `filter()`, and `reduce()` built-in. An example using `sorted()`:  
```Python
d = [(25,3), (30,2), (22,1), (20,6), (33,0), (20, 9)]
sorted(d, key=lambda d: d[1])
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are easy, natural ways to create lists in Python. They take in expressions and iterate over a given range or list. An example of a list comprehension versus the `map()` and `filter()` functions:  
```Python
list_comp = [x**2 for x in range(11) if x%2 == 0]
list_map = list(map(lambda x: x**2, range(11)))
list_filter = list(filter(lambda x: x%2 == 0, list_map))
```
>> When using `lambda`, `map()` and `filter()` are outperformed by list comprehensions because the `lambda` expression calls a function for each element while the list comprehension builds a list from a single loop. Additionally, list comprehensions appear to be more pythonic and intuitive.

>> As for set and dictionary comprehensions, here are some examples:  
```Python
import string
{k: v for (k, v) in zip(string.ascii_lowercase, range(26))} #alphabet index dictionary
{x**2 for x in range(-10,11)} #square set
```


---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 81.4 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)
