# Python Arithmetic Operators

Python operators are fundamental for performing mathematical calculations. Arithmetic operators are symbols used to perform mathematical operations on numerical values. Arithmetic operators include addition (+), subtraction (-), multiplication (*), division (/), and modulus (%).

## Arithmetic Operators

| Operator | Description | Syntax |
|----------|------------|--------|
| + | Addition: adds two operands | x + y |
| - | Subtraction: subtracts two operands | x - y |
| * | Multiplication: multiplies two operands | x * y |
| / | Division (float): divides the first operand by the second | x / y |
| // | Division (floor): divides the first operand by the second | x // y |
| % | Modulus: returns the remainder when the first operand is divided by the second | x % y |
| ** | Power: Returns first raised to power second | x ** y |

---

## Addition Operator

In Python, `+` is the addition operator. It is used to add 2 values.

```python
val1 = 2
val2 = 3

res = val1 + val2
print(res)
```

**Output:**
```
5
```

---

## Subtraction Operator

In Python, `-` is the subtraction operator. It is used to subtract the second value from the first value.

```python
val1 = 2
val2 = 3

res = val1 - val2
print(res)
```

**Output:**
```
-1
```

---

## Multiplication Operator

Python `*` operator is the multiplication operator. It is used to find the product of 2 values.

```python
val1 = 2
val2 = 3

res = val1 * val2
print(res)
```

**Output:**
```
6
```

---

## Division Operator

In Python programming language, division operators allow us to divide two numbers and return a quotient.

There are two types of division operators:

- Float division
- Floor division

### Float Division

The quotient returned by this operator is always a float number.

```python
print(5/5)
print(10/2)
print(-10/2)
print(20.0/2)
```

**Output:**
```
1.0
5.0
-5.0
10.0
```

---

### Floor Division

The quotient returned by this operator is dependent on the arguments. It is also known as floor division because values are rounded down.

```python
print(10//3)
print(-5//2)
print(5.0//2)
print(-5.0//2)
```

**Output:**
```
3
-3
2.0
-3.0
```

---

## Modulus Operator

The `%` operator is used to find the remainder when one number is divided by another.

```python
val1 = 3
val2 = 2

res = val1 % val2
print(res)
```

**Output:**
```
1
```

---

## Exponentiation Operator

The `**` operator is used to raise a number to the power of another.

```python
val1 = 2
val2 = 3

res = val1 ** val2
print(res)
```

**Output:**
```
8
```

---

## Precedence of Arithmetic Operators

| Operator | Description | Associativity |
|----------|------------|--------------|
| ** | Exponentiation Operator | Right to Left |
| %, *, /, // | Modulus, Multiplication, Division, Floor Division | Left to Right |
| +, - | Addition and Subtraction operators | Left to Right |