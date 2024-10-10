# Arithmetic Operations
a = 10
b = 5
print("Addition:", a + b)          # 15
print("Subtraction:", a - b)       # 5
print("Multiplication:", a * b)    # 50
print("Division:", a / b)          # 2.0
print("Floor Division:", a // b)   # 2
print("Modulus:", a % b)           # 0
print("Exponentiation:", a ** b)   # 100000

# Comparison Operations
print("Equal to:", a == b)         # False
print("Not equal to:", a != b)     # True
print("Greater than:", a > b)      # True
print("Less than:", a < b)         # False
print("Greater than or equal to:", a >= b)  # True
print("Less than or equal to:", a <= b)    # False

# Logical Operations
x = True
y = False
print("Logical AND:", x and y)      # False
print("Logical OR:", x or y)        # True
print("Logical NOT:", not x)        # False

# Bitwise Operations
c = 2  # (bin: 10)
d = 3  # (bin: 11)
print("Bitwise AND:", c & d)        # 2 (bin: 10)
print("Bitwise OR:", c | d)         # 3 (bin: 11)
print("Bitwise XOR:", c ^ d)        # 1 (bin: 01)
print("Bitwise NOT:", ~c)           # -3 (2's complement of 2)
print("Left Shift:", c << 1)        # 4 (bin: 100)
print("Right Shift:", c >> 1)       # 1 (bin: 1)

# Assignment Operations
e = 10
e += 2
print("Add and assign:", e)         # 12
e -= 2
print("Subtract and assign:", e)    # 10
e *= 2
print("Multiply and assign:", e)    # 20
e /= 2
print("Divide and assign:", e)      # 10.0
e //= 2
print("Floor divide and assign:", e)  # 5.0
e %= 3
print("Modulus and assign:", e)     # 2.0
e **= 2
print("Exponentiate and assign:", e) # 4.0

# Membership Operations
lst = [1, 2, 3]
print("In:", 2 in lst)              # True
print("Not in:", 4 not in lst)      # True

# Identity Operations
f = [1, 2, 3]
g = f
h = [1, 2, 3]
print("Is:", f is g)                # True
print("Is not:", f is not h)        # True
