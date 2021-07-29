# Ball screws have properties from catalogues
# Ball screw library can be queried for items matching logical requests (Ca > 3kN for example)

class ball_screw:
    def __init__(self, name, OD, pitch, Ca):
        self.name = name
        self.OD = OD
        self.pitch = pitch
        self.Ca = Ca

import pandas as pd
balls = pd.read_csv(r'C:\Users\TristanB\Documents\Core Components\STRCreator\ball_screw_library.csv')