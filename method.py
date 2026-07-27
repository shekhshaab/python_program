s = {10 , 20 , 30}
print("Original Set :",s)                           

s.add(40)
print("After add :",s)                              

s.update([50 , 60])
print("After Update :",s)                           

s2 = s.copy()
print("Copies Set :",s2)                            

s.pop()
print("Popped Element :",s)                        

s.discard(60)
print("Discarded Element :",s)                      

s.remove(20)
print("Removed Element :",s)                        

s.clear()
print("Cleared Set :",s)                            




a = {1 ,2 ,3}
b = {3 ,4 ,5}

print("Value of Set A :",a)                                       
print("Value of Set B :",b)                                         
print("Union of Both Set :",a.union(b))                             
print("Intersection of Both Set :",a.intersection(b))                
print("Difference of Set A :",a.difference(b))