n = int(input())
data = list(map(int, input().split()))
    

    
def era_prime(n):
    a = [0 for _ in range(n + 1)]
    result = []
    
    for i in range(2, n):
        if a[i] == 0: result.append(i)
        else: continue
        for j in range(i**2, n, i):
            a[j] = 1
    
    return result


p_num = era_prime(max(data) + 1)
result = []
for d in data:
    if d in p_num:
        result.append(d)
        
print(max(data))
print(p_num)
print(result)
print(len(result))