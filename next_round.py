n=input()
n=list(n.split(" "))
arr= input()
arr=list(arr.split(" "))
score = int(arr[int(n[1])-1])
result = 0

for i in range(int(n[0])):
    if (int(arr[i]) >= score) and (int(arr[i])!=0):
        result+=1
print(result)