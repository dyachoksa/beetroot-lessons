from app.data import Circle, Square


def main():
    c = Circle(10)
    s = Square(5)

    print(c.get_name())
    print("Length:", c.length())

    print(s.get_name())
    s.make_double_size()
    print("Length:", s.length())
    s.make_zero()
    print("Length:", s.length())


if __name__ == '__main__':
    main()
