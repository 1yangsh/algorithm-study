scoville = [1,2,3,9,10,12]
K = 7

scoville.sort()
print(scoville)
cnt = 0
while(min(scoville) < K ):
    scoville[0] = scoville[0] + scoville[1] * 2
    scoville.remove(scoville[1])
    cnt += 1
    scoville.sort()

print(cnt)
