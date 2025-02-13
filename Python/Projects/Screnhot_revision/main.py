import pyscreenshot
import os
import time


# create a directory 
# use r for avoid escape characters
folder = r"C:\Users\ecasa\Documents\Capture_Review"

if not os.path.exists(folder):
    os.makedirs(folder)
    print("Directory created")

duration = 2 * 60 # Transform hours to minutes
interval = 5

try:
    for i in range(duration // interval):
        name_screnshot = f"screenshot_{i}.png"
        route = os.path.join(folder,name_screnshot)
        
        image=pyscreenshot.grab()
        image.save(route)
        time.sleep(interval)
        
except ModuleNotFoundError: 
    print("Module not found")
finally:
    print('This is always executed')
    