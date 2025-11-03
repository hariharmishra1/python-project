#!/usr/bin/python3
import os
tw_size=os.get_terminal_size().columns
str=input("Enter the string")
print(str.center(tw_size))
print(str.rjust(tw_size))
print(str.ljust(tw_size))


