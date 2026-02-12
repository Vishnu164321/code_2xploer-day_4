list=[10,"python","",20,"loop",40]
num_list=[]
str_list=[]
num_count=0
str_count=0
for i in list:
    if type(i)==int:
        num_list.append(i)
        num_count+=1
    elif type(i)==str and i!="":
        str_list.append(i)
        str_count+=1
print("Number list",num_list)
print("Total numbers:",num_count)
print("String list",str_list)
print("Total Strings:",str_count)

name="Vishnu"
if len(name)%2==0:
    del num_list[0]
    del str_list[0]
else:
    del num_list[-1]
    del str_list[-1]

print("Updated number list",num_list)
print("Updated string list",str_list)