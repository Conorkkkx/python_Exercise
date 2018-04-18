while True:
    num = int(input("请输入您想得到斐波拉契数列第几位上的数字:"))
    def fib(num):
        if num == 1 :
            return 0
        else:
            i = num - 1
            a = 0
            b = 1
            while i>=1:
                b = a+b
                a = b-a
                i -= 1
            return b
    a = fib(num)
    print(a)
