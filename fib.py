def generate_fibonnaci_repl(n):
    curr_el=0
    prev1_el=1
    prev2_el=1
    fib_list=[1,1]
    if n<=0:
        fib_list=None
    elif n==1:
        fib_list=[1]
    elif n!=2:
        for _ in range(3,n+1):
            curr_el=prev1_el+prev2_el
            prev2_el=prev1_el
            prev1_el=curr_el
            fib_list.append(curr_el)
    return fib_list

def generate_fibonnaci_recurs(n):
    print("n", n)
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:
        fib_list = generate_fibonnaci_recurs(n-1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

if __name__ == '__main__':
    sequence_qnt = int(input("How many Fibonnaci numbers do you want? "))
    print('Replacement ', sorted(generate_fibonnaci_recurs(sequence_qnt)))
