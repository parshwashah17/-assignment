#break statement
print("break statement:")
for i in range(1,11):
    if i==5:
        break
    print(i)
else:
    print("Loop exited")
#pass statement 
print("\npass statement:")
for i in range(1,11):
    if i==5:
        pass
    else:
        print(i)
#continue statement
print("\ncontinue statement:")
for i in range(1,11):
    if i==5:
        continue
    else:
        print(i)
#for with else statement
print("\nfor with else statement:")
for i in range(1,11):
    if i%2==0:
        print("even number:",i)
    else:
        print("odd number:",i)
#while with else statement
print("\nwhile with else:")
i=1
while i<=10:
    print(i)
    i+=3
else:
    print("loop exited")
