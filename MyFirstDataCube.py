
# coding: utf-8

# # My First Data Cube
# 
# A small notebook showing how to initialise connection and access the Data Cube a display a small section of data

# In[1]:

#get_ipython().magic(u'pylab')
#%pylab inline
#import mpld3; mpld3.enable_notebook() 


# In[2]:

from datetime import datetime, date, timedelta
from gdf import GDF
from pprint import pprint
import matplotlib.pyplot as plt


# In[3]:

def plotImages(arrays):
    img = arrays
    num_t = img.shape[0]
    num_rowcol = math.ceil(math.sqrt(num_t))
    fig = plt.figure()
    fig.clf()
    plot_count = 1
    for i in range(img.shape[0]):
       data = img[i]
       ax = fig.add_subplot(num_rowcol,num_rowcol,plot_count)
       plt.setp(ax, xticks=[], yticks=[])
       #cax = ax.imshow(data, interpolation='nearest', aspect = 'equal')
       cax = ax.pcolormesh(data) #, interpolation='nearest', aspect = 'equal')
       #fig.colorbar(cax)
       plot_count += 1
    fig.tight_layout()
    plt.show()


# In[4]:

g = GDF()
#g.debug = True


# In[5]:

data_request_descriptor = {'storage_type': 'LS7ETM',
                               'variables': ('B30', 'B40'),
                               'dimensions': {'X': {'range': (140.0, 140.125)},
                                              'Y': {'range': (-35.0, -35.0+0.125)},
                                              #'T': {'range': (0, 6325376000),
                                              #      'array_range': (0, 4)
                                                    #'crs': 'SSE', # Seconds since epoch
                                                    #'grouping_function': g.null_grouping
                                              #      }
                                            }
                           }


# In[6]:

d = g.get_data(data_request_descriptor)
pprint(d)
print(d['arrays']['B30'].shape)



# In[7]:
plotImages(d['arrays']['B30'])


# In[ ]:

type(d['arrays']['B30'])




# In[ ]:



