# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    print(x)


def func2():
    print(x)


def func3():
    x = 23
    print(x)


x = 3
func1()
func2()
func3()
