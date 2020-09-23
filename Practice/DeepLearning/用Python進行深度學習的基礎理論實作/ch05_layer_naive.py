# 執行乘法層
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
    
    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        return out
    
    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x
        return dx, dy
    
apple = 100
apple_num = 2
tax = 1.1

# layer
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# forward
# apple_price = mul_apple_layer.forward(apple, apple_num)
# price = mul_tax_layer.forward(apple_price, tax)

# backward
# dprice = 1
# dapple_price, dtax = mul_tax_layer.backward(dprice)
# dapple, dapple_num = mul_apple_layer.backward(dapple_price)
# print(dapple_price, dtax)
# print(dapple, dapple_num)

# 執行加法層
class Addlayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y
        return out
    
    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy

orange = 150
orange_num = 3
tax = 1.1

# layer
mul_orange_layer = MulLayer()
total = Addlayer()

# forward
apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange, orange_num)
total_price = total.forward(apple_price, orange_price)
last_price = mul_tax_layer.forward(total_price, tax)
# print(round(last_price))

# backward
dprice = 1
dtotal_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dorange_price = total.backward(dtotal_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)
# print(dtotal_price, dtax, dapple_price, dorange_price)
# print(dapple_num, dapple, dorange_num, dorange)


# 執行活化函數層
# ReLU(Rectified Linear Unit)
class ReLU:
    def __init__(self):
        self.mask = None
    
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx

import numpy as np
x = np.array([[1.0, -0.5], [-2.0, 3.0]])
relu = ReLU()
y = relu.forward(x)
dy = relu.backward(y)
# print(relu.mask)
# print(dy)

# Sigmoid 層
