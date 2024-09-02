import time


# def net_price(list_price, discount=0, tax=0):
#     return list_price * (1 - (discount / 100)) * (1 + (tax / 100))
#
#
# print(net_price(500))
# print(net_price(500, 5, 5))

def count(start=0, end=10):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")


count()
