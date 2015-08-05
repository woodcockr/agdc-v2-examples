# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:27:20 2015

@author: 
"""

from pprint import pprint
from datetime import datetime
from analytics import Analytics
from execution_engine import ExecutionEngine
from analytics_utils import plot

a = Analytics()
e = ExecutionEngine()

dimensions = {'X': {'range': (147.968, 148.032)}, 'Y': {'range': (-36.032, -35.968)}, 'T': {'range': (1262304000.0, 1325375999.999999)}, }
arrays = a.createArray('LS5TM', ['B40', 'B30'], dimensions, 'get_data')
ndvi = a.applyBandMath(arrays, '((array1 - array2) / (array1 + array2))', 'ndvi')
arrays2 = a.createArray('LS5TM', ['B40', 'B30'], dimensions, 'get_data2')
ndvi2 = a.applyBandMath(arrays2, '((array1 - array2) / (array1 + array2))', 'ndvi2')
average = a.applyBandMath([ndvi, ndvi2], '((array1 + array2) / 2)', 'average')
pq_data = a.createArray('LS5TMPQ', ['PQ'], dimensions, 'pq_data')
mask = a.applyCloudMask(average, pq_data, 'mask')
result = e.executePlan(a.plan)

plot(e.cache['mask'])
