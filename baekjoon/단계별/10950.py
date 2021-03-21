n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in data:
    print(sum(i))
    
