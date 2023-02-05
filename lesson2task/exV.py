n = int(input())
k = int(input())
x = (n - (k - n*(k//n)))%n
# -k%n
print(x)