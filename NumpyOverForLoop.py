import time
import numpy as np

#using for loop

numbers = np.random.randint(1, 100, size = 10000010)

start = time.time()
ltf = 0
sn = 0

for n in numbers:
  if n < 50:
    sn += n
    ltf += 1
    
end = time.time()
print("Execution time: ", end - start)

#using numpy

numbers = np.random.randint(1, 100, size = 10000010)

start = time.time()

mean = (numbers[numbers<50]).mean()
    
end = time.time()
print(f'Numpy time taken: ", {end - start}, seconds')
