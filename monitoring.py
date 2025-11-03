#!/usr/bin/python3
#Monitoring the resources of system
import os
import psutil

def monitor_resources():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    print(f"CPU_Usage is : {cpu_usage}% and Memory_usage is: {memory_usage}%")

monitor_resources()

