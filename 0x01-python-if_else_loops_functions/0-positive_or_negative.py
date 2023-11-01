#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print(f"number {number} is negative")
elif number == 0:
    print(f"number {number} is zero")
else:
    print(f"number {number} is positive")
