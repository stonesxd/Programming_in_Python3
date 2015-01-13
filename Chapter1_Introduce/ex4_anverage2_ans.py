total = 0
cnt = 0

numlist = []

while True:
    line = input("enter a number or Enter to finish:")
    if line:
        try:
            num = int(line)
            total += num
            cnt += 1
            numlist.append(num)
        except ValueError as err:
            print(err)
            continue
    else:
        break
#冒泡排序
for i in range(cnt-1,-1,-1):
    for j in range(i):
        if numlist[j] > numlist[j+1]:
            numlist[j], numlist[j+1] = numlist[j+1], numlist[j]
#        print(i,j)
#        print(numlist)
#取中位数
if cnt%2:   # odd
    median = numlist[cnt//2]
else:
    median = (numlist[(cnt-1)//2] + numlist[(cnt-1)//2 + 1]) / 2
    
print("number: ",numlist)
print("count: ", cnt, "lowest: ",min(numlist), "highest: ",max(numlist),
      "mean: ", total / cnt, "midian:",median)
