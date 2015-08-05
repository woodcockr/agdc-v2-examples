# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 08:56:10 2015

@author: woo409
"""

# In[1]:

#get_ipython().magic(u'pylab')
# %pylab inline
# import mpld3; mpld3.enable_notebook()

# In[2]:
import calendar
from datetime import datetime, date, timedelta
from gdf import GDF
from pprint import pprint
from gdf import dt2secs, secs2dt
import matplotlib.pyplot as plt

# In[4]:

g = GDF()
g.debug = False


# In[5]:

start_date = dt2secs(date(year=2010, month=1, day=1))
end_date = dt2secs(date(year=2010, month=1, day=18))
data_request_descriptor = {'storage_type': 'LS5TM',
                           'variables': ('B40', 'B30',),
                           'dimensions': {'X': {'range': (147.875, 148.125)},
                                          'Y': {'range': (-37.0 + 0.875, -36.0 + 0.125)},
                                          # 'T': {'range': (start_date, end_date),
                                          #      'array_range': (0, 4)
                                          # 'crs': 'SSE', # Seconds since epoch
                                          # 'grouping_function': g.null_grouping
                                          #     }
                                          }
                           }



# In[6]:
d = g.get_data(data_request_descriptor)
print "d shape: ", d['arrays']['B30'].shape
# plotContourf(d, 'B30')
# plotImages(d['arrays']['B30'])

# In[ ]:
from glue.core import Data, DataCollection
from glue.qt.glue_application import GlueApplication

44  # In[ ]:
my_data1 = Data(x=d['arrays']['B40'], label='B40')

collection = DataCollection([my_data1, ])
# collection.merge(my_data1,my_data2,my_data3)
app = GlueApplication(collection)
app.start()
