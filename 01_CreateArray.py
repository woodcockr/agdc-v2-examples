"""
Created on Tue Jul 14 14:45:06 2015


"""

#1. Create array
from analytics import Analytics
from execution_engine import ExecutionEngine
from analytics_utils import plot

a = Analytics()
e = ExecutionEngine()

dimensions = {'X': {'range': (147.968, 148.032)}, 'Y': {'range': (-36.032, -35.968)}, 'T': {'range': (1262304000.0, 1325375999.999999)}, }
arrays = a.createArray('LS5TM', ['B40'], dimensions, 'get_data')

e.executePlan(a.plan)

plot(e.cache['get_data'])
