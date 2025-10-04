def validateanswers(answer,letters):
    used=[""]
    valid=False
    for i in range (0,len(answer)):
        for j in range (0,len(letters)):
            if answer[i]=letters[j]:
                for x in range (0, len(used)):
                    if answer[i]=used[i]:
                        valid=False
                    else:
                        valid=True
                used.append(answer[i])
    if valid=True:
        return(len(answer))
    else:
        return(0)

                
