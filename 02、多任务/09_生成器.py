def creat_num(all_nums):
    print("-------1------")
    a, b = 1, 1
    current_num = 0
    while current_num < all_nums:
        print("------2------")
        yield a
        a, b = b, a+b
        print("------3----")
        current_num += 1

obj = creat_num(10)

print( next(obj) )
print( next(obj) )
print( next(obj) )
print( next(obj) )
print( next(obj) )

