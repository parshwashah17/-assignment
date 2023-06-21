ex=[]
print("Enter 5 elements in the list!!")
for i in range(0,5):
    inp=int(input())
    ex.append(inp)
print(ex)
total=sum(ex)
print("Sum of all elements=",total)
minimum=min(ex)
print("Smallest element in the list is:",minimum)
maximum=max(ex)
print("Largest number in the list is:",maximum)
ex.sort()
print("list in ascending order is:",ex)
ex.reverse()
print("List in descending order is:",ex)
tp=tuple(ex)
print(tp)
del ex
print(ex)    #This will display empty list!!
