n = int(input()) 
s = input()  
 
k_a = 0  
k_d = 0  
 
 
for i in range(n):
    if s[i] == 'A':
        k_a += 1
    else:
        k_d += 1
 
 
if k_a > k_d:
    print("Anton")
elif k_a < k_d:
    print("Danik")
else:
    print("Friendship")
 
