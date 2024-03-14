import matplotlib.pyplot as plt
import numpy as np

X = np.array([[1,2,3,4,5,6,7,8,9,10]]).T
y = np.array([[2,4,3,6,9,12,13,15,18,20]]).T

def caculate_b1_b0(X,y):
    # Tinh trung binh
    Xbar = np.mean(X)
    ybar = np.mean(y)
    X2bar = np.mean(X**2)
    Xybar = np.mean(X*y)

    #Tinh B0, B1
    B1 = (Xbar *ybar - Xybar)/ (Xbar**2- (X2bar))
    B0 = ybar - B1*Xbar
    return B1,B0

B1, B0 =  caculate_b1_b0(X,y)
print("B1 = ", B1)
print("B0 = ", B0)

#---------------------------------------------------
print("-"*30)
print('Visualize')
# Visualize data
def showGraph(x, y, title="", xlabel="", ylabel=""):
    plt.figure(figsize=(14, 8))
    plt.plot(x, y, 'r-o', label="value sample")
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)
    # mean y
    ybar = np.mean(y)

    plt.axhline(ybar, linestyle='--', linewidth=4, label="mean")
    plt.axis([x_min*0.95, x_max*1.05, y_min*0.95, y_max*1.05])
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.text(x_min, ybar*1.01, "mean", fontsize=16)
    plt.legend(fontsize=15)
    plt.title(title, fontsize=20)
    plt.show()

showGraph(X, y,
          title='Giá trị Y theo X',
          xlabel='Giá trị X',
          ylabel='Giá trị Y')







