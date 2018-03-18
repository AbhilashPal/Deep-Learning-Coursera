# a.shape = (3,4)
# b.shape = (4,1)
a = np.random.randn(3, 4) 
b = np.random.randn(4, 1) 
c = np.random.randn(3, 4) 
d = np.random.randn(3, 4) 
for i in range(3):
  for j in range(4):
    c[i][j] = a[i][j] + b[j]
d = a + b.T
if d.all()==c.all():
	print("Yes")
