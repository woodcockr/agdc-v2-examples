# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:08:14 2015

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
arrays = a.createArray('LS5TM', ['B40'], dimensions, 'get_data')
median_t = a.applyGenericReduction(arrays, ['T'], 'median(array1)', 'medianT')

result = e.executePlan(a.plan)

plot(e.cache['medianT'])
