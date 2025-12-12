import time

start = time.time()
a = 5
b = 6
print(f"Values Before Swapping :", "a = {a}, b = {b}") 
temp = a
a = b
b = temp       
print(f"Values After Swapping :", "a = {a}, b = {b}")
print("Time Taken :", round(time.time() - start   ,5))   