import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.pylab import rcParams




txt = "721011081081113211911111410810010"
n=len(txt)
x=[]
for i in range(n,3):
        x = txt.split(" ")


print(x)

for item in input.split():
    decodedMessage += chr(int(item))
output = "ASCII to plaintext =  " + decodedMessage + "\n"

with open("output.txt", "w") as f1:
    for line in output:
        f1.write(line)