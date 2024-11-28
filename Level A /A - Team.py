n=int(input())
resultat=0
for loop in range(n):
    a, b, c=map(int,input().split())
    if a+b+c>=2:
        resultat+=1
print(resultat)
