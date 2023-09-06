def do_twice(f, value):
    f(value)
    f(value)


def print_spam(value):
    print('spam value is:', value)


def print_twice(bruce):
    print(bruce)
    print(bruce)


#do_twice(print_spam, 10)


do_twice(print_twice, 'spam')



