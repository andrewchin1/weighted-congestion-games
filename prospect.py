import numpy as np
from scipy.stats import norm, gumbel_r
import matplotlib.pyplot as plt
N = 4
num = 1000

x = np.linspace(-N, N, num)
n = norm.pdf(x)
g = gumbel_r.pdf(x)

def w(x, gamma=.5):
    return x**gamma/(x**gamma + (1-x)**gamma)**(1/gamma)

def fake_int(x):
    return np.sum(x) *2*N/num

wn = w(n, .9)
gn = w(g, .9)

# print fake_int(n)
# print fake_int(wn)
# w_std = np.sqrt(np.dot(wn,x**2)*2*N/num)
# print 'std', w_std
# approx = norm.pdf(x, 0, w_std)

########################   

plt.plot(x, n)
plt.hold(True)
# plt.plot(x, wn/fake_int(wn))
# plt.plot(x, approx)
plt.show()
