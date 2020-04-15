def func_name(num):
    print(num, end=" ")
    if num >= 100:
        return

    func_name(num + 1)


func_name(1)
