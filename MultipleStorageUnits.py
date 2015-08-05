# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 08:56:10 2015

@author: woo409
"""



# In[1]:

get_ipython().magic(u'pylab')
#%pylab inline
#import mpld3; mpld3.enable_notebook() 


# In[2]:
import calendar
from datetime import datetime, date, timedelta
from gdf import GDF
from pprint import pprint
from _gdfutils import dt2secs, secs2dt
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
       cax = ax.imshow(data, interpolation='nearest', aspect = 'equal')
       #fig.colorbar(cax)
       plot_count += 1
    fig.tight_layout()
    plt.show()
    
def plotColorMesh(arrays):
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
       cax = ax.pcolormesh(data, origin='upper') #, interpolation='nearest', aspect = 'equal')
       #fig.colorbar(cax)
       plot_count += 1
    fig.tight_layout()
    plt.show()

def plotContourf(the_data, band):
    data_t = the_data['arrays'][band]
    lat = the_data['indices']['X']
    lon = the_data['indices']['Y']
    time = the_data['indices']['T']
    num_t = data_t.shape[0]
    num_rowcol = math.ceil(math.sqrt(num_t))
    fig = plt.figure()
    fig.clf()
    plot_count = 1
    for i in range(data_t.shape[0]):
       data = data_t[i]
       ax = fig.add_subplot(num_rowcol,num_rowcol,plot_count)
       plt.contourf(lat, lon, data, 64)
       plot_count += 1
    fig.tight_layout()
    plt.show()

# In[4]:

g = GDF()
g.debug = False


# In[5]:

start_date = dt2secs(date(year=2010,month=1,day=1))
end_date = dt2secs(date(year=2010, month=1, day=18))
data_request_descriptors = []
data_request_descriptors.append( {'storage_type': 'LS5TM',
                               'variables': ('B30',),
                               'dimensions': {'X': {'range': (140.0, 141.0)},
                                              'Y': {'range': (-36.0, -35.0)},
                                              'T': {'range': (start_date, end_date),
                                              #      'array_range': (0, 4)
                                                    #'crs': 'SSE', # Seconds since epoch
                                                    #'grouping_function': g.null_grouping
                                                   }
                                            }
                           })
data_request_descriptors.append({'storage_type': 'LS5TM',
                               'variables': ('B30',),
                               'dimensions': {'X': {'range': (140.0, 141.0)},
                                              'Y': {'range': (-35.0, -34.0)},
                                              'T': {'range': (start_date, end_date),
                                              #      'array_range': (0, 4)
                                                    #'crs': 'SSE', # Seconds since epoch
                                                    #'grouping_function': g.null_grouping
                                                   }
                                            }
                           })
data_request_descriptors.append({'storage_type': 'LS5TM',
                               'variables': ('B30',),
                               'dimensions': {'X': {'range': (141.0, 142.0)},
                                              'Y': {'range': (-36.0, -35.0)},
                                              'T': {'range': (start_date, end_date),
                                              #      'array_range': (0, 4)
                                                    #'crs': 'SSE', # Seconds since epoch
                                                    #'grouping_function': g.null_grouping
                                                   }
                                            }
                           })
data_request_descriptors.append( {'storage_type': 'LS5TM',
                               'variables': ('B30',),
                               'dimensions': {'X': {'range': (141.0, 142.0)},
                                              'Y': {'range': (-35.0, -34.0)},
                                              'T': {'range': (start_date, end_date),
                                              #      'arra_range': (0, 4)
                                                    #'crs': 'SSE', # Seconds since epoch
                                                    #'grouping_function': g.null_grouping
                                                   }
                                            }
                           })


# In[6]:
#for data_request_descriptor in data_request_descriptors:
#    d = g.get_data(data_request_descriptor)
#    print "d shape: " , d['arrays']['B30'].shape
    #plotContourf(d, 'B30')
#    plotImages(d['arrays']['B30'])
#   pprint(d)

# In[ ]:

big_descriptor = {'storage_type': 'LS5TM',
                               'variables': ('B30',),
                               'dimensions': {'X': {'range': (140.0+0.75, 142.0)},
                                              'Y': {'range': (-36.0+0.75, -34.0)},
                                              'T': {'range': (start_date, end_date),
                                              #      'array_range': (0, 4)
                                                    #'crs': 'SSE', # Seconds since epoch
                                                    #'grouping_function': g.null_grouping
                                                   }
                                            }
                           }
                           
d_all = g.get_data(big_descriptor)
d_all['arrays']['B30'].shape
plotImages(d_all['arrays']['B30'])
#plotContourf(d_all, 'B30')                           