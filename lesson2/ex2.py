# t = int(input()) # t = s+m*60+h*60*60+d*24*60*60
# d = t//(24*60*60)
# t %= 24*60*60 # остаток секунд
# h = t//(60*60)
# t %= 60*60
# m = t//60
# s = t%60
# print(d,h,m,s)
# print(300000//(24*60*60))
# print(300000/(3600))
# print(300000//(3600))
# print(300000//60)
# d=h=m=s=1
# t = s+m*60+h*60*60+d*24*60*60
# print(t)
# d = t//(24*60*60)
# print(d)
# d_rest = (t%(24*60*60))/(24*60*60)
# print(d_rest)
#
# h = t//(60*60)
# print(h)
# h_rest = (t%(60*60))/(60*60)
# print(h_rest)
#
# m = t//(60)
# print(m)
# m_rest = (t%(60))/(60))
# print(m_rest)

# d=h=m=s=1
# t = s+m*60+h*60*60+d*24*60*60 # Приравняем переменную t = все время в секундах
# print(t)
# d = t//(24*60*60)
# print(f'Число дней: {d}')
#
# #t = t%(24*60*60) # Приравняем переменную t = остатку секунд после выделения дней
# t %= (24*60*60)
# print(f'Число оставшихся секунд wo days: {t}')
#
# import math
# print(math.ceil(2.85))
# print(2000//700)
#
# S=2000
# p=700
# if S%p==0:
#     t = S//p
# if S%p!=0:
#     t = S//p+1
#
# print(t)
#
# t=(S+p-1)//p
# print(t)
t = 100000
# print(f'd: ', t//(24*60*60))
# print(f'h: ', (t%(24*60*60))//(60*60))
# print(f'm: ', (t%(24*60*60)) % (60*60) // 60)
# print(f's: ', (t%(24*60*60)) % (60*60) % 60)
d = t // (24*60*60)
t %= (24*60*60)
h = t // (60*60)
t %= (60*60)
m = t//60
t %= 60
s = t
print(d,h,m,s)

