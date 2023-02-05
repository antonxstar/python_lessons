# for k in range(8):
#    print(k, (k)//2, (k)//2 - (k-1)%2)

k = int(input())
dt = 45 * k + 5*(k//2) + 15*((k//2) - (k-1)%2)
h = dt // 60
m = dt % 60
print(h + 9,m)