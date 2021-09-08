import time


t1 = time.time()
x = "Act fast." 
x1 = "Fail fast." 
x2 = "Learn fast." 
x3 = "Make more interesting mistakes." 
x4 = "Life is an experiment."


print("but not way too fast")
print(bool(x1))
print(bool(x2))
print(bool(x3))
print(bool(x4))

t2 = time.time()
t = t2 - t1
print("Elapsed time is : ", t, " seconds")
