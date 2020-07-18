# 輸入一個正整數, 改用質因數乘積表達此數
def prime_factor(i):
    s = ""
    while True:
        for k in range(2, i + 1):
            if i % k == 0:
                i = i // k
                s += (str(k) + "x")
                break

        if i == 1:
            break
    return s[:-1]

try:
    i = int(input("Enter a positive integer: "))
    if(i <= 0):
        raise TypeError
except ValueError:
    print("The number is not an integer.")
except TypeError:
    print("The integer is not positive.")
else:
    answer = prime_factor(i)
    print("The answer is %s." % answer)

