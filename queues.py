def enqueue(q,ele):
    q.append(ele)
    print(ele,"inserted into queue")
def dequeue(q):
    if len(q)==0:
        print("queue is empty")
        return
    print(q[0],"is getting deleted")
    q.pop(0)

queue=[]
enqueue(queue,10)
enqueue(queue,20)
enqueue(queue,30)
enqueue(queue,40)
enqueue(queue,50)

dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
