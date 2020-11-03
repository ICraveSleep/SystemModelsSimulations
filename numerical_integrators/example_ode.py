import numpy as np
import matplotlib.pyplot as plt

time_span = 30

dt = 0.065  # dt = 0.066
t = np.arange(0, time_span+dt, dt)
x = 0.1986*np.exp(-0.8679*t) + 0.0014*np.exp(-29.1421*t) + 1/45*np.sin(5*t)

dt1 = 0.01
t1 = np.arange(0, time_span+dt1, dt1)
x1 = 0.1986*np.exp(-0.8679*t1) + 0.0014*np.exp(-29.1421*t1) + 1/45*np.sin(5*t1)

dt2 = 0.05
t2 = np.arange(0, time_span+dt2, dt2)
x2 = 0.1986*np.exp(-0.8679*t2) + 0.0014*np.exp(-29.1421*t2) + 1/45*np.sin(5*t2)


# Forward euler
# xdd = (10*cos(5t) - 90xd - 75x)/3

a = np.zeros(len(t))
ad = np.zeros(len(t))
add = np.zeros(len(t))
for i in range(len(t)):
    if i == 0:
        a[i] = 0.2
        ad[i] = -0.1
        add[i] = (10*np.cos(5*t[i]) - 90*ad[i] - 75*a[i])/3
    else:
        add[i] = (10 * np.cos(5 * t[i-1]) - 90 * ad[i-1] - 75 * a[i-1]) / 3
        ad[i] = ad[i-1] + add[i]*dt
        a[i] = a[i-1] + ad[i]*dt

# Trapezoid method


plt.plot(t, x)
# plt.plot(t1, x1)
plt.plot(t, a)
# plt.plot(t2, x2)

plt.show()
