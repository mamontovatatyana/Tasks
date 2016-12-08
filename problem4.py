from  math import sqrt
import random

def distance(x,y):
    return sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

# manifold of dots in the form of X = [sum_i[x_i,y_i]}
X = list()
n = 3 #number of random dots
for i in range(n):
    X.append([random.random(),random.random()])


Y = list() #massive of distance
for i in range(n):#i - dot
    sum = 0
    for j in range(n):#distance to j - dot
        sum += distance(X[i],X[j])
    Y.append(sum)
dot = X[Y.index(min(Y))]
print(dot)