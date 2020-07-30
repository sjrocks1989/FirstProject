

str1=input(print("Enter your first name"))
str2=input(print("Enter your last name"))
for i in range (len(str1),0,-1):
    print(str1[i-1],end="")
print(end=" ")
for j in range (len(str2),0,-1):
    print(str2[j-1],end="")

