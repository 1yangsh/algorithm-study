# Queue가 꽉 찼는지 확인하는 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if(rear == SIZE - 1):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if(front == rear):
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if(isQueueFull()):
        print("Queue is full")
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("Queue is Empty")
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data




SIZE = 5
queue = ['화사', '솔라', '문별', '휘인', 'None']
front = -1
rear = 3

# 큐에 데이터 삽입
print(queue)
enQueue('선미')
print(queue)
enQueue('재남')

# 큐에 데이터 추출
for _ in range(3):
    retData = deQueue()
    print('deQueue-->', retData)
    print(queue)

