# Static requirements for the STR
# Maximum duty forces (axial and radial), speed, travel
# This replaces a duty cycle for development/basic calculation

import numpy as np
import pandas as pd
from matplotlib.pyplot import plot, show, grid
import matplotlib.pyplot as plt
import strc_fns

duty_cycle = pd.read_csv(r'C:\Users\TristanB\Documents\Core Components\STRCreator\duty_cycle.csv')
duty_cycle.sort_values(by=['Rack speed'])

rack_speed = duty_cycle['Rack speed'].tolist()
rack_speed = [abs(ip) for ip in rack_speed] # Absolute values since the performance is not direction dependent
rack_force = duty_cycle['Rack force'].tolist()
rack_force = [abs(an) for an in rack_force] # Absolute values since the performance is not direction dependent

plt.scatter(rack_speed, rack_force);
grid(True);
show()

# strc_fns.envelope(rack_speed,rack_force)