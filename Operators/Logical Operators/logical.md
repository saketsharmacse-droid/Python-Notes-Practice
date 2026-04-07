# Python Logical Operators

Python logical operators are used to combine or modify conditions and return a Boolean result (`True` or `False`). They are commonly used in conditional statements to control the flow of a program based on multiple logical conditions.

---

## Example: Logical Operators (and, or, not)

```python
a, b, c = True, False, True

# AND: Both conditions must be True
if a and c:
    print("Both a and c are True (AND condition).")

# OR: At least one condition must be True
if b or c:
    print("Either b or c is True (OR condition).")

# NOT: Reverses the condition
if not b:
    print("b is False (NOT condition).")
```

**Output:**
```
Both a and c are True (AND condition).
Either b or c is True (OR condition).
b is False (NOT condition).
```

---

## Explanation

- `a and c` returns True because both values are True.  
- `b or c` returns True because at least one value is True.  
- `not b` reverses False to True, so the condition executes.  

---

## Logical Operators Table

| Operator | Description | Syntax | Example |
|----------|------------|--------|---------|
| and | Returns True if both operands are true | x and y | x > 7 and x > 10 |
| or | Returns True if either operand is true | x or y | x < 7 or x > 15 |
| not | Returns True if operand is false | not x | not(x > 7 and x > 10) |

---

## Truth Table for Logical Operators

A truth table shows how logical operators behave for all possible combinations of Boolean values.

### AND Operator

| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### OR Operator

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### NOT Operator

| A | not A |
|---|--------|
| True | False |
| False | True |

---

## AND Operator

The Boolean AND operator returns True if both operands are True.

### Example 1

```python
a = 10
b = 10
c = -10

if a > 0 and b > 0:
    print("The numbers are greater than 0")

if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")
```

**Output:**
```
The numbers are greater than 0
Atleast one number is not greater than 0
```

---

### Example 2

```python
a = 10
b = 12
c = 0

if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")
```

**Output:**
```
Atleast one number has boolean value as False
```

**Note:** If the first expression is False, remaining expressions are not evaluated (short-circuiting).

---

## OR Operator

The Boolean OR operator returns True if at least one operand is True.

### Example 1

```python
a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
```

**Output:**
```
Either of the number is greater than 0
No number is greater than 0
```

---

### Example 2

```python
a = 10
b = 12
c = 0

if a or b or c:
    print("Atleast one number has boolean value as True")
else:
    print("All the numbers have boolean value as False")
```

**Output:**
```
Atleast one number has boolean value as True
```

**Note:** If the first expression is True, remaining expressions are not evaluated.

---

## NOT Operator

The Boolean NOT operator works with a single boolean value and reverses it.

### Example

```python
a = 10

if not a:
    print("Boolean value of a is True")

if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")
```

**Output:**
```
10 is divisible by either 3 or 5
```

---

## Order of Precedence of Logical Operators

When multiple logical operators are used in a single expression, Python evaluates them using short-circuit evaluation.

### Example

```python
def check(x):
    print("Method called for value:", x)
    return x > 0

a = check
b = check
c = check

if a(-1) or b(5) or c(10):
    print("At least one of the numbers is positive")
```

**Output:**
```
Method called for value: -1
Method called for value: 5
At least one of the numbers is positive
```

---

## Explanation

- `a(-1)` returns False → next condition evaluated  
- `b(5)` returns True → evaluation stops  
- `c(10)` is not executed due to short-circuiting  

---
