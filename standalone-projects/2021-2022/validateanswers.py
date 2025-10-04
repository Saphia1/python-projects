def validateanswers(answer,letters):
    used=[]
    valid=False
    for i in range (0,len(answer)):
        for j in range (0,len(letters)):
            if answer[i]==letters[j]:
                    if answer[i] in used:
                        valid=False
                        break
                    else:
                        valid=True
                        used.append(answer[i])
                    break
    if valid==True:
        return(len(answer))
    else:
        return(0)

print(validateanswers("bat",["b","a","t","e"])) 
print(validateanswers("batt",["b","a","t","e"])) 
print(validateanswers("bath",["b","a","t","e"]))        
