list_=['1', '2', '3', '40', '43', '5', '75', '9', '9', '9', '9', '9']
for i in range (0,(len(list_))):
                for j in range (len(list_)-1):
                    if (list_[j]>list_[j + 1]):
                        list_[j],list_[j+1]=list_[j+1],list_[j]
print (list_)
                        
            
