import numpy as np

arr = [
   [1,'a',['cat'],2],[[[3]],'dog'],4,5
]

ndarr = np.array(arr) 
print ndarr

fndarr = np.ndarray.flatten(ndarr) 
print fndarr
