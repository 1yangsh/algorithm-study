# Queue가 꽉 찼는지 확인하는 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if(rear == SIZE - 1):
        return True
    else:
        return False

# Queue가 비었는지 확인하는 함수
def isQueueEmpty():
    global SIZE, queue, front, rear
    if(front == rear):
        return True
    else:
        return False


SIZE = 5
queue = ['화사', '솔라', '문별', '휘인', '선미']
front = -1
rear = 4
print("Is Queue full? : ", isQueueFull())

queue = [None for _ in range(5)]
front = 2
rear = 2
print("Is Queue Empty? : ", isQueueEmpty())