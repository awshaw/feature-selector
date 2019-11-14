import numpy as np
import pandas as pd
from sklearn.utils import shuffle

def batcher(data):
    '''
    Input: 
    * data - pd.DataFrame
    * n_batch - integer

    Output:
    * batch_indices - np.array
    '''
    
    index = shuffle(data.index)

    split_size = int(data.shape[0]/n_batch)
    batch_indices = []
    last_idx = 0
    
    for i in range(1, n_batch+1):
        if i == n_batch:
            batch_indices.append( index[last_idx:data.shape[0]])
        else:
            batch_indices.append(index[last_idx:i*split_size])
            last_idx = i*array_size

    return batch_indices

            
