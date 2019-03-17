
plt.figure(figsize=(15, 4))

######### FORECASTING
plt.subplot(131)
x1 = np.linspace(0, 10, 1000)
x2 = np.linspace(10, 12, 200)

ax = plt.plot(x1, np.sin(2*x1), '-',
              x2, np.sin(2*x2), '--', linewidth=2)

plt.title("Forecasting")
# plt.xlabel("Time $\longrightarrow$")

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='off')

######### ANOMALY DETECTION
plt.subplot(132)
x1 = np.linspace(0, 12, 1200)
x2 = np.linspace(0, np.pi, 50)


y1 = np.sin(2*x1)
y2 = np.sin(x2)

y = y1.copy()
y[790:840] += y2

ax = plt.plot(x1, y, '-', linewidth=2)

plt.title("Anomaly Detection")
# plt.xlabel("Time $\longrightarrow$")

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='off')

######### Pattern Recognition
plt.subplot(133)
x = np.linspace(0, 2* np.pi, 100)
x2 = np.linspace(0, 4* np.pi, 200)

y1 = np.sin(x)
y2 = 0.3 *np.sin(2*x2)*np.cos(0.08*x2)
y3 = 0.5*np.sin(3* x)

ax = plt.plot(np.hstack([0.9*y1, y2, y3,0.7*y1, 0.8*y1, y3, 0.9 * y1, 0.8*y1, 0.95*y1, 0.5*y1, 0.6*y1]),
              linewidth=2)

plt.title("Pattern Recognition")
# plt.xlabel("Time $\longrightarrow$")

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='off')




######### TRAIN / TEST
plt.figure(figsize=(10, 4))
x1 = np.linspace(0, 10, 1000)
x2 = np.linspace(10, 14, 400)

ax = plt.plot(x1, np.sin(2*x1), '-',
              x2, np.sin(2*x2), '-', linewidth=3)


for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='off')
