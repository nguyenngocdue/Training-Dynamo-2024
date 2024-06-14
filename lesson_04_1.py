# for x in range(10):
#     for y in range(3):
#         # print(f"x = {x} , y = {y}")
#         if x == 2:
#             # print(f"x = {x} , y = {y}")
#             break


# for i in range(100):
#     if i == 2: continue
#     print(i)

# positiveNums = [1,2,3,4,5,10,-5,10,2,30,5,-10]
# negNums = [1,2,3,4,5,10,-5,10,2,30,5,-10]


# # f("nguyen van hung {stt}")



# apbet = ['a', 'b', 'c', 'd', 'e', 'f']


# for index , value in enumerate(apbet):
#     print(f"index = {index}, value = {value}")

# square = lambda x,y: (2*x + 1) ** 2   + y

# number = square(5, 1)

# print(number)

objects = ['a', 'b', 'c',500,600,501,'500', 'd', 'e', 'f']

lstStr=  []
for obj in objects:
    if isinstance(obj,int):
        lstStr.append(obj)

print(lstStr)


objects = ['text_a-3000', 'text_a-4000', 'text_a-4000', 'text_a-8000']
