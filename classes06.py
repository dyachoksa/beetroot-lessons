class MyStr:
    def __init__(self, my_str=''):
        self.my_str = my_str

    def __repr__(self):
        return f'MysStr my_str={self.my_str}'

    def __str__(self):
        return self.my_str

    def print_String(self):
        print(self.my_str.upper())

    def get_String(self, my_str):
        self.my_str = my_str
        self.print_String()
        

if __name__ == '__main__':
    s1 = MyStr('kherson')
    s1.print_String()
    print(s1)
    print(repr(s1))

    s2 = MyStr()
    s2.print_String()
    user_str = input('Enter yor string: ')
    s2.get_String(user_str)
    print(s2)
    print(repr(s2))
