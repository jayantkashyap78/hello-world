def reverse(n):
    S=0
    while(n>0):
        x=n%10
        S=(S*10)+x
        n=n//10
    return S
n=int(input())
print(reverse(n))
