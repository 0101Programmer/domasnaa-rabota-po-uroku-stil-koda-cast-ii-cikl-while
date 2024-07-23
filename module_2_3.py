my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num_0 = 0

while num_0 < len(my_list):
    if my_list[num_0] > 0:
        print(my_list[num_0])
    if my_list[num_0] < 0:
        break
    num_0 += 1
