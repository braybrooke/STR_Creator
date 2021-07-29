# Combining the ball screw and motor properties to satisfy static requirements

import pandas as pd
import Static_Requirements
import ball_screw_lib
import motor_properties
import math
import strc_fns

balls = ball_screw_lib.balls
ForceFilteredBS = balls[balls.Ca>9500].head()
print(ForceFilteredBS)


# Maximum axial force attainable from the motor-bs combination

# Define a limit based on the motor properties to select the bs from (what's the static requirement, how much
# pitch and Ca do we need in the bs to allow for this?) (Ca must be greater than the requirement, pitch must
# work in combination with the motor properties to allow enough torque to be generated)