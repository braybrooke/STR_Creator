# Defining motor properties to use in combination with ball screws
import numpy as np
import pandas as pd

# Speeds are consistent across columns in the motor maps, max() is merely used to avoid capturing 0 values
m_speeds = pd.read_csv(r'C:\Users\TristanB\Documents\Core Components\STRCreator\m_speed.csv')
max_s_idcs = m_speeds.idxmax()
max_speeds=[]
for jmp in range(0, len(m_speeds.columns)):
    max_speeds.append(m_speeds.iloc[max_s_idcs[jmp]][jmp])

# Capturing the maximum torque values from the motor map for each speed
m_torques = pd.read_csv(r'C:\Users\TristanB\Documents\Core Components\STRCreator\m_torque.csv')
max_t_idcs = m_torques.idxmax()
max_torques=[]
for kr in range(0, len(m_torques.columns)):
    max_torques.append(m_torques.iloc[max_t_idcs[kr]][kr])