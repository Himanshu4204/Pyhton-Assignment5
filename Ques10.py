# Q10. Write a python script to use IS operator to display if both variables are the same object or not?
x1=5
y1=5
x2='Himanshu'
y2='Himanshu'
x3=[1,2,3]
y3=[1,2,3]

print(x1 is y1)   #True
print(x2 is y2)   #True
print(x3 is y3)   #False  x3 and y3 are lists. They are equal but not identical.