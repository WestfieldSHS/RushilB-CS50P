expression = input("Expression: ")

x, y, z = expression.split(" ")

x = float
z = float

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
print(result)