#01786280557

#Write a program to make another list of duplicate elements from the following list

count_dict = {}

num_list = [1, 5, 6, 5, 1, 2, 3]
dup_list = []

for i in num_list:
    if i not in count_dict:
        count_dict[i] = 1
    else:
        count_dict[i] += 1

for key, value in count_dict.items():
    if value > 1:
        dup_list.append(key)

print(dup_list)
