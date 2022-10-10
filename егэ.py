n=int(input("введите натуральное число = "))
nd=bin(n)[2:]
print(nd)
symm=nd.count('1')
print(symm)

if symm%2 == 0:
    symmtr = str(nd)
    itogtr = "1"+"0"+symmtr[2:]
    print(f'{itogtr}0')
else:
    symmel = str(nd)
    itogel = "1"+"1"+symmel[2:]
    a=(f'{itogel}1')
    print(a)
    b=int(a,2)
    print(b)
    
