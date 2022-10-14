a = int(input())

x = a % 1000
x1 = a - (x * 1000)

c = x1 % 100
c1 = x1 - (c * 100)

v = c1 % 10
v1 = c1 - (v * 10)

print (int(c + v +x))
print(3)