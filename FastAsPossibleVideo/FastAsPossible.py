# https://www.youtube.com/watch?v=VchuKL44s6E

x = {'someKey': 4}

for key, value in x.items():
    print(key, value)
    
for key, in x:
    print(key, x[key])

for eachValue in x.items():
    print(key, value)
    print(key, x[key])
