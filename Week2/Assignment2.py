# 01786280557

# Write a program to sort by ascending order from the following list. (Create a function to solve it)

def ascending_sort(list):
    n = len(list)
    
    for i in range(n-1): 
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                
    print(list)


list = [1, 5, 2, 9, 3, 22, 13]
ascending_sort(list)
