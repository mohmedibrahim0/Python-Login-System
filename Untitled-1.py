
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse= True)
count = 1
for num in my_nums:
    if  num % 5 == 0:
     print(f"{count} => {num}")
     count +=1
print("All number painted")
