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

print("number: ",numlist)
print("count: ", cnt, "lowest: ",min(numlist), "highest: ",max(numlist),
      "mean: ", total / cnt)
