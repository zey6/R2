## Learning Outcomes

By the end of this activity, a student should be able to:
1. Step through a python function manually
2. Explain verbally to his/her partner the result of executing the function given argument(s)
3. Modify the function to satisfy a stated requirement

## Introduction

This recitation requires that you form pairs and manually step through the Python function provided below.  Once you have explained the function to the satisfaction of your partner, you will execute the function and observe whether the result as you expected.  If the result is not as expected, you are required to go back and analyze why you did not get the observed result.  Once this task is completed, you will be asked to modify the function to satisfy a requirement.

## Python's Functions: First-Class Objects

Python's functions are first-class objects. You can assign them to variables, store them in data structures, pass them as arguments to other functions, and even return them as values from other functions.  For example,

```python
def bar(x):
    return x+5

def foo(func, x):
    return func(x)

>>>foo(bar,20)
25
```

the function <span style="font-family:'courier-new',courier; font-weight:bold;">foo</span> that takes a function as a parameter, applies the function on the parameter <span style="font-family:'courier-new',courier">x</span>, and returns the result.

Another example using a function that takes two arguments,

```python
def bar2(x,y):
    return x+y

def foo2(func, x,y):
    return func(x,y)

>>>foo2(bar2, 5,10)
15
```

The function <span style="font-family:'courier-new',courier; font-weight:bold;">foo2</span> takes a two parameter function as the first argument and applies the function to the parameters <span style="font-family:'courier-new',courier">x</span> and <span style="font-family:'courier-new',courier">y</span> and returns the result.

## Lambda Functions

Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda".   The syntax for a lambda function is

```python
lambda param1[, param2, param3, ...] : <expression>
``` 

Since lambda functions are first-class objects, we can assign them to variables and call them like functions.

```python
>>> bar = lambda x: x+5
>>> bar(15)
20
```

This makes lambda functions powerful to use.  Consider the example from the previous section.

```python
def bar(x):
    return x+5

def foo(func, x):
    return func(x)

>>>foo(bar,20)
25
```

Instead of defining bar as a function that will be used only for the purpose of using it once in foo, you can use a lambda function to effectively get the same result.

```python
def foo(func, x):
    return func(x)

>>>foo(lambda x: x+5 ,20)
25
```

The same can be true for the function foo2 in the previous section.

```python
def foo2(func, x,y):
    return func(x,y)

>>> foo2(lambda x,y: x+y, 5,10)
15
```

## Activity 1:  Manual Walkthrough a Function (20 min)

Consider the following Python function:

```python
def crypto(filename, cypher):
    with open(filename,'r') as fh, open(filename+'.enc','w') as fhenc:
        for line in fh:
            eLine = ''
            for ch in line:
                eLine += cypher(ch)
            fhenc.write(eLine)

>>>crypto('myDoc.txt', lambda x: chr((ord(x)+5)%256))
```

1. perform a manual walkthrough assuming myDoc.txt contains the word 'hello'.
2. Reason what the result will be and then run the function in Python.
3. If the result is not as expected, then analyze why.
4. Once the analysis is completed, proceed to the next section.

### Discussion (10 min)

1. What does this function do?
2. What are the difficulties in analyzing this function?
3. What new concept did you learn from analyzing this function?

## Activity 2: Modify a Function (On your own)

Bijzonder Spion, a super-spy extraordinaire, does not like the 
original file remaining after encryption.  He knows that other 
super spies have tools to retrieve deleted files.  He prefers 
encrypting a file and then writing over the original file.  Your 
job as a super-spy programmer is to modify the function 
<code>crypto</code> in the file <strong>crypto.py</strong> as given in  
<strong>Activity 1</strong> so that the original file is encrypted.  Your 
modification should not modify the line-by-line encryption in 
function crypto.  <span style="color:red">Your modification should read in the entire file, 
encrypt it, and then rewrite over the file</span>.


<p style="background-color:#f9cfcf;">
<span style="text-decoration:underline ;font-weight:bold;">NOTE</span>: Normally it would be useful to encrypt/decrypt the file in-place as you read it; however, there seems to be an intrinsic issue with the tell method of file objects.  As such, the approach of opening the file in r+ mode will not work.
</p>

**Once you have completed the function, submit it below for grading**.