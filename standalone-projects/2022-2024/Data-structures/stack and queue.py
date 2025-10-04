queue=[]
action=input("Add or remove data?")
queueing=True
while queueing==True:
    if action=="add":
        finished=False
        while finished != True:
            data=input("What would you like to add?")
            queue.append(data)
            print(queue)
            done=input("Add more data?")
            if done== "no":
                finished=True
        print(queue)
    elif action == "remove":
        finished=False
        while finished != True:
            data=int(input("how much data to remove?"))
            for i in range(0,data):
                queue.remove(queue[1])
            print(queue)
            done=input("Remove more data?")
            if done== "no":
                finished=True
        print(stack)
    queueing=input("Are you finished queueing?")
    if queueing=="no":
        queueing=True
    action=input("Add or remove data?")



stack=["A","B","C","D","E"]
action=input("Add or remove data?")
stacking=True
while stacking==True:
    if action=="add":
        finished=False
        while finished != True:
            data=input("What would you like to add?")
            print(stack)
            stack.append(data)
            print(stack)
            done=input("Add more data?")
            if done== "no":
                finished=True
        print(stack)
    elif action == "remove":
        finished=False
        while finished != True:
            data=int(input("how much data to remove?"))
            for i in range(0,data):
                stack.remove(stack[-1])
            print(stack)
            done=input("Remove more data?")
            if done== "no":
                finished=True
        print(stack)
    stacking=input("Are you finished stacking?")
    if stacking=="no":
        stacking=True
    action=input("Add or remove data?")
