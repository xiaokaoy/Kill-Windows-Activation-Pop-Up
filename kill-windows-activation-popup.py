import os 
from time import sleep

import subprocess
cmd = 'WMIC PROCESS get Caption'
success_counter = 0
failure_counter = 0

import datetime

while True:
    sleep(2)
    
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    
    for line in proc.stdout:
      if b"slui.exe" in line:
        
        print("\n", datetime.datetime.now())
        
        result = os.system("taskkill /im slui.exe")
        
        if (result == 0):
          success_counter = success_counter+1
          print("Killed slui.exe successfully", success_counter, "times")
          #sleep(60)
        else:
            failure_counter = failure_counter + 1
            print("Failed to kill slui.exe", failure_counter, "times")
                
        break