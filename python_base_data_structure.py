def data_structure():

    list_var = [12,"banana", 5.3, 9,1,2,3] #list_var    Ordered, changeable, duplicates
    T = (12, "banana", 5.3, 12) #Tuple  Ordered, unchangeable, duplicates
    S = {12, "banana", 5.3} #Set    Unordered, addable/removable, no duplicate
    D = {"Val": 12, "name": "Ban"} #Dict    Unordered, changeable, no duplicate


    list_var[0] = 15

    del list_var[1] #delete "banana"

    # T[2] = Return Error 5 TypeError: 'tuple' object does not support item assignment


    #T.pop() Return ErrorAttributeError: 'tuple' object has no attribute 'pop'
    #T.add(25)  Return AttributeError: 'tuple' object has no attribute 'add'

    S.pop()     #Remove last Set Element
    S.add(23)   #Add Element in last position

    S.update({"updating"}) #update Set
    S.remove(5.3)  # Remove 5.3

    #print(S[0])    Return Error TypeError: 'set' object is not subscriptable


    list_var.pop() #Remove last item element

    # list_var.add(25)   #Return Error list_var object has no attribute add


    #print(D[0])    #Return KeyError: 0
    D["Val"] = 15
    print(D["name"]) #print "Ban" into terminal
    D["New"] = "New Key add "

    D2 = D

   # D = D+D2   Return TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

    L2 = list_var #any changes in L2, L1 will be also affected, that's because it's pointed to the same memory address 
    del L2[-1] # Deleta 5.3 de L2 e list_var

    L3 = list_var.copy()   #Create a actually a copy of the variable
   
    del L3[0]  #Now i can delete without affect list_var 

    #L3 = list_var[0:1]    It's already a copy


    list_var.append(55)    #Add 55 in the end of the list_var

    return {"This_data_structure": "Dict","list_var(list_var)": list_var, "list_var(L2)":L2, "list_var(L3)": L3, "Tuple": T, "Set": S, "Dict": D}



print(data_structure())