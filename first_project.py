""" Input arguments """


def input_args():
    """ input and return args """
    a_var = input("Введите аргумент \"a\" ")
    b_var = input("Введите аргумент \"b\" ")
    n_var = input("Введите аргумент \"n\" ")
    return [a_var, b_var, n_var]


def correct_checker(args_inp):
    """ Are the args numbers """
    args_ipn_int = []
    for i in args_inp:
        try:
            args_ipn_int.append(int(i))
        except arg_is_not_int:
            arg_is_not_int = Exception
            return False
  # Are the args in the interval
    if  args_ipn_int[0] >= 2 and \
        args_ipn_int[1] >= 1 and  args_ipn_int[2] >= 0:
        return True
    return False

# Get checked args
def get_args():
    """ wait for correct args """
    while True:
        args_inp = input_args()
        if correct_checker(args_inp):
            print("Все введено правильно!")
            return [int(i) for i in args_inp]
        print("Повторите попытку ввода.")
        continue

# Divisibility check
def divider(count, div):
    """ check of divisibility """
    return count / div == 0

def output(args):
    """ printing output """
    a_var = args[0]
    b_var = args[1]
    n_var = args[2]
    count = a_var**2**n_var + b_var**2**n_var
    print("Число Ферма под номером", n_var, "это ",count)
    print("Делимость на 2:", divider(count,2))
    print("Делимость на 3:", divider(count,3))
    print("Делимость на 5:", divider(count,5))



def main():
    """get args and print it"""
    print("Здравствуйте!")
    output(get_args())

if __name__ == "__main__":
    main()
