import time
import random
 
def print_callback(wt):
  print(f"I've waited for {wt}s")
 
def higher_order_fn(callback):
  wt = random.randint(0, 3)
  time.sleep(wt)
  callback(wt)
 
higher_order_fn(print_callback)