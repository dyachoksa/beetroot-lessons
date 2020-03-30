def find_max_3(a, b, c):
    if a > b > c: 
        return a
    elif b > a > c:
        return b
    else:
        return c

def find_max_n(a_list):
    current_max = a_list[0]
    for item in a_list:
        if item > current_max:
            current_max = item
    
    return current_max

def find_max(a_list):
    if len(a_list) == 3:
        res = find_max_3(a_list[0], a_list[1], a_list[2])
    else:
        res = find_max_n(a_list)
    
    return res

def main():
    list1 = []
    max_value = find_max(list1)
    print(list1, "max:", max_value)

    list2 = [5, 10, 15, 1, 14, 11]
    max_value = find_max(list2)
    print(list2, "max:", max_value)

if __name__ == "__main__":
    main()









