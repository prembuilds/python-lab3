stack=[]
queue=[]
while True:
    print("enter 1:push 2:pop 3:enqueue 4:dequeue 5:display stack and queue 6:exit")
    choice=input("enter 1-6:")
    if choice=='1':
        n=int(input("enter number to push into stack:"))
        stack.append(n)
        print("pushed to stack")
    elif choice=='2':
        if(len(stack)==0):
            print("stack is empty")
            continue
        print(f'deleted element is:{stack.pop()}')
    elif choice=='3':
        n=int(input('enter a number to enqueue in queue:'))
        queue.append(n)
        print("enqueued to queue")
    elif choice=='4':
        if(len(queue)==0):
           print("queue is empty")
           continue
        print(f'deleted element is: {queue.pop(1)}')
    elif choice=='5':
         if(len(stack)==0):
            print("stack is empty")
            continue
         print(f"elements in stack:{stack}")
         if(len(queue)==0):
           print("queue is empty")
           continue
         print(f"elements in queue:{queue}")
    elif choice=='6':
        print("exiting the program")
        break
    else:
        print("invalid choice")
