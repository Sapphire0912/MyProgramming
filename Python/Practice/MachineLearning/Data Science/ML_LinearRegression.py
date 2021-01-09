import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()


# 高斯基函數(自定義)
class GaussianFeatures(object):
    from sklearn.base import BaseEstimator, TransformerMixin
    def __init__(self, N, width_factor = 2.0):
        self.N = N
        self.width_factor = width_factor
    
    @staticmethod
    def _gauss_basis(x, y, width, axis = None):
        arg = (x - y) / width
        return np.exp(-0.5 * np.sum(arg ** 2, axis))
    
    def fit(self, X, y = None):
        self.centers_ = np.linspace(X.min(), X.max(), self.N)
        self.width_ = self.width_factor * (self.centers_[1] - self.centers_[0])
        return self
    
    def transform(self, X):
        return self._gauss_basis(X[:, :, np.newaxis], self.centers_, self.width_, axis = 1)

    def use(self):
        from sklearn.pipeline import make_pipeline
        from sklearn.linear_model import LinearRegression
        rng = np.random.RandomState(1)
        x = 10 * rng.rand(50)
        y = np.sin(x) + 0.1 * rng.randn(50)
        xfit = np.linspace(0, 10, 1000)

        gauss_model = make_pipeline(GaussianFeatures(self.N), LinearRegression())
        gauss_model.fit(x[:, np.newaxis], y)
        yfit = gauss_model.predict(xfit[:, np.newaxis])
        plt.scatter(x, y, color = 'Blue')
        plt.plot(xfit, yfit, color = 'Red')
        plt.xlim(0, 10)
        plt.show()

class Linear_Regression(object):
    def introduce(self):
        '''NaiveBayes 對於分類工作是一個好的起點, 那麼Linear Regression則是回歸工作的好起點\n\
           線性回歸(簡稱LR)可以擬合的非常快速, 易於解讀.\n'''
    
    def SimpleLR(self):
        '''這是最熟悉的線性回歸, 也就是擬合一條直線開始; 一條直線擬合形式為y = ax + b的模型, a為斜率, b為截距.\n'''
        # 這裡的用法 y = 2x - 5的直線上
        rng = np.random.RandomState(1)
        x = 10 * rng.rand(50)
        y = 2 * x - 5 + rng.randn(50)
        plt.scatter(x, y)
        # plt.show()

        # 使用 ScikitLearn 的 LR estimator 來擬合資料, 建立一最佳擬合的線條
        from sklearn.linear_model import LinearRegression as LR
        model = LR(fit_intercept = True)
        model.fit(x[:, np.newaxis], y) 

        xfit = np.linspace(0, 10, 1000)
        yfit = model.predict(xfit[:, np.newaxis])
        # plt.plot(xfit, yfit, color = 'Red')
        print("Modle slope: ", model.coef_[0])
        print("Modle intercept: ", model.intercept_)
        # Result: Modle slope:  2.0272088103606944
                # Modle intercept:  -4.9985770855532
        # 預測結果和一開始輸入的資料十分接近
        # plt.show()

    def BasicFunctionRegression(self):
        '''基函數回歸, 把兩個變數之間的關係從線性回歸調適成非線性;\n\
           在特徵工程中使用到了PolynomialRegression管線, 這個概念可以被使用到以下的多維度線性模型.\n\
           注: fn(x) = x^n; y = a0 + a1x + a2x^2... 依然是一個線性模型\n\
               線性關係提到的一個事實, 就是這些係數彼此之間不會有乘或除的關係\n\
               我們可以有效地做到, 取得1維的x值, 並且把它投影到較高的維度, 讓線性擬合可以擬合在x,y之間更複雜的關係.'''
        
        # 多項式基函數
        # 多項式投影很有用, 被內建在Scikit-Learn中, 使用 PolynomialFeatures轉換器
        from sklearn.preprocessing import PolynomialFeatures
        x = np.array([2, 3, 4])
        poly = PolynomialFeatures(3, include_bias = False)
        result = poly.fit_transform(x[:, None]) # x[:, None] = x[:, np.newaxis]
        # print(result)

        # 使用管線來建立一個7階多項式的模型
        from sklearn.pipeline import make_pipeline
        from sklearn.linear_model import LinearRegression
        poly_model = make_pipeline(PolynomialFeatures(7), LinearRegression())

        # 在位置中進行轉換之後, 可以使用線性模型去擬合更複雜的x, y關係. 例如以下是一個帶有雜訊的正弦函數波形
        rng = np.random.RandomState(1)
        x = 10 * rng.rand(50)
        y = np.sin(x) + rng.randn(50) * 0.1

        poly_model.fit(x[:, np.newaxis], y)
        xfit = np.linspace(0, 10, 1000)
        yfit = poly_model.predict(xfit[:, np.newaxis])
        plt.scatter(x, y, color = 'Blue')
        plt.plot(xfit, yfit, color = 'Red')
        plt.show()

    def Regularization(self):
        '''正規化: 把基函數引入到線性回歸中會讓模型更加彈性, 但也有可能會造成Overfit.\n\
           如果使用太多的高斯基函數會導致結果看起來沒有這麼好.(高斯基函數參考底下連結資料).'''
        
        from sklearn.pipeline import make_pipeline
        from sklearn.linear_model import LinearRegression
        rng = np.random.RandomState(1)
        x = 10 * rng.rand(50)
        y = np.sin(x) + 0.1 * rng.randn(50)
        xfit = np.linspace(0, 10, 1000)

        # 過多的高斯基函數產生了Overfitting
        # model = make_pipeline(GaussianFeatures(30), LinearRegression())
        # model.fit(x[:, np.newaxis], y)
        # yfit = model.predict(xfit[:, np.newaxis])
        # plt.scatter(x, y, color = 'Blue')
        # plt.plot(xfit, yfit, color = 'Red')
        # plt.xlim(0, 10)
        # plt.ylim(-1.5, 1.5)
        # plt.show()
        # 這些資料被投影到 30-Dimensional的基礎, 此模型過於彈性, 使得極度被受限在資料點之間的位置
        # 若把高斯基的係數和相對應的位置畫出來, 就可以找到原因了

        def basis_plot(model, title = "None"):
            fig, ax = plt.subplots(2, sharex = True)
            model.fit(x[:, np.newaxis], y)
            yfit = model.predict(xfit[:, np.newaxis])
            ax[0].scatter(x, y)
            ax[0].plot(xfit, yfit)
            ax[0].set(xlabel = 'x', ylabel = 'y', ylim = (-1.5, 1.5))
            if title:
                ax[0].set_title(title)
            ax[1].plot(model.steps[0][1].centers_, model.steps[1][1].coef_)
            ax[1].set(xlabel = 'basis location', ylabel = 'coefficient', xlim = (0, 10))
            plt.show()

        # 下方的圖顯示每一個位置基函數的振幅, 這是一個典型的"當基礎函數重疊時"的過度擬合行為: 
        # 鄰接的基函數之係數暴增而取消了彼此的輸出. 則藉由處罰模型參數中那些過大的值來限制在模型中
        # 明顯的突波就會比較好一些, 而此種方式就稱為正規化(Regularization)
        # 而正規化有以下幾種形式: 

        # 1. Ridge regression(L2 regularization)
        # P = α * sigma(n = 1 to N){thete(n)^2}
        from sklearn.linear_model import Ridge
        # model = make_pipeline(GaussianFeatures(30), Ridge(alpha = 0.1))
        # basis_plot(model, title = 'Ridge Regression')
        # alpha 參數是一個可調整的變數, 用來控制模型的複雜度 limit α -> 0 會回到標準的線性回歸結果
        # limit α -> ∞ 則所有模型回應將都會被抑制下來.
        # Ridge 回歸其中一個特別的好處, 它可以被有效率的計算, 幾乎不會比原來的LR模型增加更多成本

        # 2. Lasso regularization(L1)
        # P = α * sigma(n = 1 to N){abs(thete(n))}
        from sklearn.linear_model import Lasso
        model = make_pipeline(GaussianFeatures(30), Lasso(alpha = 0.001))
        basis_plot(model, title = 'Lasso Regression')
        # Lasso Regression處罰中, 大部分的係數都正好為0, 此時函數的行為就會被可用的基函數的小型子集合所塑模
        # 使用 alpha 參數來微調處罰的強度, 而且應該藉由交叉驗證加以決定

# 高斯基函數
# Reference: https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html 
# gaussianbf = GaussianFeatures(20)
# gaussianbf.use()

LinearR = Linear_Regression()
# help(LinearR.introduce)
# LinearR.SimpleLR()

# help(LinearR.BasicFunctionRegression)
# LinearR.BasicFunctionRegression() # 裡面是多項式基函數

# help(LinearR.Regularization)
LinearR.Regularization()

