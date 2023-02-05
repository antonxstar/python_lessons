t = int(input())
#t = 129700 # sec
t = t%(24*60*60)
h = t//(60*60)
#print(h)
t %= (60*60)
m = t//60
#print(f'{m:0{2}}')
s = t%60
#print(f'{s:0{2}}')
#print(f'{h}:{m:0{2}}:{s:0{2}}')
print(f'{h}:{m:02}:{s:02}')
