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

dimensions = {'X': {'range': (147.968, 148.032)}, 'Y': {'range': (-36.032, -35.968)}, 'T': {'range': (1262304000.0, 1325375999.999999)}, }
ndvi = a.applySensorSpecificBandMath('LS5TM', 'ndvi', dimensions, 'step1_get_data', 'step2_ndvi')
result = e.executePlan(a.plan)

plot(e.cache['ndvi'])

