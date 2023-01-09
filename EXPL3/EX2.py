# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

some_list = input().split()
new_list = []
for start in range(0, (len(some_list) - 1) // 2 + 1):
    new_list.append(int(some_list[start]) * int(some_list[len(some_list) - start - 1]))
print(new_list)

# def pair_multy(nums: list[int]) -> list[int]:
#     pairs = []
#     iterations = (len(nums)+1)//2
#     print(iterations)
#     for i in range(iterations):
#         pairs.append(nums[i]*nums[-1-i])
#     return(pairs)
        
# nums = [2, 3, 4, 5, 6]
# print(pair_multy(nums))