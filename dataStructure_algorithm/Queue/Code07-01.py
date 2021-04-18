# Data Structure : QUEUE
# Queue 생성
queue = [None for _ in range(5)]
front = rear = -1

# EnQueue
# 데이터 입력 시 rear 값을 1 증가시킨 후, rear 자리에 데이터 삽입
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print("==== 큐 상태 ====")
print('[출구] <--', end='')
for i in range(len(queue)):
    print(queue[i], end=' ')
print('<--[입구]', end='')

