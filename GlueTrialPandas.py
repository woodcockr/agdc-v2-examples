# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 08:56:10 2015

@author: woo409
"""
# In[2]:
from glue.core import Data, DataCollection
from glue.qt.glue_application import GlueApplication
from datetime import datetime, date, timedelta
from gdf import GDF
from gdf import dt2secs, secs2dt
from analytics import Analytics
from execution_engine import ExecutionEngine

# In[4]:

a = Analytics()
e = ExecutionEngine()
g = GDF()
g.debug = False


# In[5]:

start_date = dt2secs(date(year=2010,month=1,day=1))
end_date = dt2secs(date(year=2010, month=1, day=18))
data_request_descriptor = {'storage_type': 'LS5TM',
                               'variables': ('B40',),
                               'dimensions': {'X': {'range': (149.0699, 149.152)},
                                              'Y': {'range': (-35.3117, -35.2842)},
                                              #'T': {'range': (start_date, end_date),
                                              #      'array_range': (0, 4)
                                                    #'crs': 'SSE', # Seconds since epoch
                                                    #'grouping_function': g.null_grouping
                                              #     }
                                            }
                           }


# In[]:
arrays = a.createArray('LS5TM', ['B20', 'B30'], data_request_descriptor['dimensions'], 'get_data')
ndvi = a.applyBandMath(arrays, '((array1 + array2)/2.0)', 'ndvi')
pq_data = a.createArray('LS5TMPQ', ['PQ'], data_request_descriptor['dimensions'], 'pq_data')
mask = a.applyCloudMask(ndvi, pq_data, 'mask')
result = e.executePlan(a.plan)


# In[6]:
#d = g.get_data(data_request_descriptor)
#print "d shape: " , d['arrays']['B40'].shape
#plotContourf(d, 'B30')
#plotImages(d['arrays']['B30'])

# In[ ]:


# In[ ]:
my_data1 = Data(label='LS5TM')
#my_data1.add_component(d['arrays']['B20'], label='B20')
my_data1.add_component(e.cache['mask']['array_result']['mask'], label='NDVI')
#my_data1.add_component(d['arrays']['B10'], label='B10')

collection = DataCollection([my_data1,])
#collection.merge(my_data1,my_data2,my_data3)
app = GlueApplication(collection)
app.start()

