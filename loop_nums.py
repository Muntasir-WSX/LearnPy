list_nums = []


for value in range(1,10):
    list_nums.append(value)
    # value=value*2
    print(list_nums)
# max number from the list
max_num = max(list_nums)
min_num= min(list_nums)
sum_num = sum(list_nums)
even_nums = list(range(0,100,2))
print("Max number from the list:", max_num)
#minimum number from the list
print("Minimum number from the list:", min_num)
print("Sum of all numbers in the list:", sum_num)
print("Even numbers from 0 to 100:", even_nums)