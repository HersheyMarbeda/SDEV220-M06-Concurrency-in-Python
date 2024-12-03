import multiprocessing
import time
import random
from datetime import datetime

def worker():
   wait_time = random.uniform(0, 1)
   time.sleep(wait_time)
   print(f'\nCurrent time: {datetime.now()}\n')

if __name__ == '__main__':
   processes = []
   for _ in range(3):
      p = multiprocessing.Process(target=worker)
      processes.append(p)
      p.start()

   for p in processes:
      p.join()
      
      
# Output:
''' 
Depedending on the random wait time, the output will vary.
However, the output will be similar to the following:

Current time: 2024-12-02 22:14:57.386662

Current time: 2024-12-02 22:14:57.853646

Current time: 2024-12-02 22:14:58.130305

'''