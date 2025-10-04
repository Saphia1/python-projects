def updateDisplay(words):
    row=0
    column=0
    while len(words)!= 0:
        word=words.remove()
        word=word+" "
        if column=20:
            row=row+1
        elif len(word)>(20-column):
            row=row+1
        else:
            for j in range 0,len(word):
                display(column,row)=word[i]
                column=column+1
            
