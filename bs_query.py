# Query ball screw library for items matching requirements

import Static_Requirements
import ball_screw_lib

balls = ball_screw_lib.balls
ForceA = Static_Requirements.ForceA

bs_fltrd = balls[balls.Ca>ForceA].head()
print(bs_fltrd)
