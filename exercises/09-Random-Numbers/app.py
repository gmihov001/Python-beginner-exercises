import random
import math

def get_randomInt():
  # CHANGE ONLY THIS LINE BELOW
	random_number = math.ceil(random.random()*10)
	return random_number



print(get_randomInt())