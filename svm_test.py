import numpy as NP
from svm import*

Data = NP.random.randint(-5,5,1000).reshape(500,2)

#rx = [(x**2 + y**2)<9 and 1 or 0 for (x,y) in Data]

#px = svm_problem(rx,Data)

#pm = svm_parameter(kernel_type=RBF)

#v = svm_model(px,pm)

#v.predict([3,1])

print Data
