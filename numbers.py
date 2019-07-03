#numeric data types
    #1. int
    #2. float
    #3. complex

a = 12.434
b = -32.43

print(type(a))
print(type(b))

# float(int) converts to float
u = 100
u_to_float = float(u)
print(u_to_float)

# Casting - uses constructor functions
# int() - conv from string (whole no. - "12345"), float
# str() - conv from variety
# float() - conv from string , int
'''
f = 144
g = 144.9
h = "144"
i = "144.9"

print("f =" + str(type(f)))
print("g =" + str(type(g)))
print("h =" + str(type(h)))
print("i =" + str(type(i)))
'''

"rounds down"

x = int(1)
print(type(x))

y = int(2.8)
print(type(y))

z = int("30")
print(type(z))

#Assignment: Cast x, y, z to string & float
print(float(x))
print(str(x))
print(float(y))
print(str(y))
print(float(z))
print(str(z))