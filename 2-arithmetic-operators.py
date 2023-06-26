#initial solution that I come up with
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
    
#     print(a + b)
#     print(a - b)
#     print(a * b)

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/


    # a little improvement with f-string
#     print(f'{a + b}\n{a - b}\n{a * b}')

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/


# then I decided to encapsule the code in a function

# def print_operation(x, y):
#     print(f'{x + y}\n{x - y}\n{x * y}')

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())

#     print_operation(a, b)


# Finally, I made a lambda function

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print_operation = lambda x, y: print(f'{x + y}\n{x - y}\n{x * y}')
    print_operation(a, b)
    

    