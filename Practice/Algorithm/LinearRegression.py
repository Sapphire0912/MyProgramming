# Linear Regression 
# Supervised Learning (Regression)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class LR(object):
    # xydata, list consist of tuples
    def datasets(self, xydata):
        self.coordinate = xydata
        plt.show()
    
    def _sse(self, distance):
        pass

    def predict(self, xdata):
        pass


# Assume: the linear function of prediction is Y = 2x + 1
samples = [(0, 1), (2, 5), (5, 11), (6, 13), (8, 17)]
text_data = 3
# predict O/P is 7

Linear = LR()
Linear.datasets(samples)
# result = Linear.predict(text_data)
# print("Predict: ", result)