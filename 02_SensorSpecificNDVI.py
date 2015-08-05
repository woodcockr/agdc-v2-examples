# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:03:49 2015

@author: 
"""

from pprint import pprint
from datetime import datetime
from analytics import Analytics
from execution_engine import ExecutionEngine
from analytics_utils import plot

a = Analytics()
e = ExecutionEngine()

dimensions = {'X': {'range': (147.0, 148.0)}, 'Y': {'range': (-37.0, -36.0)}, 'T': {'range': (1262304000.0, 1325375999.999999)}, }
arrays = a.createArray('LS5TM', ['B40',], dimensions, 'get_data')
#ndvi = a.applyBandMath(arrays, '((array1 - array2) / (array1 + array2))', 'ndvi')

e.executePlan(a.plan)

plot(e.cache['get_data'])

