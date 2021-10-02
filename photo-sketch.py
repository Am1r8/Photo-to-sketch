print("""\n\n
   _____ __        __       __  
  / ___// /_____  / /______/ /_ 
  \__ \/ //_/ _ \/ __/ ___/ __ \
 ___/ / ,< /  __/ /_/ /__/ / / /
/____/_/|_|\___/\__/\___/_/ /_/ 
                                
\n\n""")

print("Opening Modules ...")
from sketchify import sketch
from time import sleep
import random
import os


img_n = input("\n\nEnter the Name of the Image with Extension\n")

file_p = os.path.dirname(os.path.abspath(__file__))

img_s_n = "output" + str(random.randint(0,500))

img = sketch.normalsketch(img_n, file_p, img_s_n)
print("\n\nDone\n\n")

sleep(20)