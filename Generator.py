import pandas as pd
import datetime
from slugify import slugify

now = datetime.datetime.now()

df = pd.DataFrame([
        {'package': 'PEPTize', 'student': 'Yashvant Singh', 'level': 'Level 1'}
        # {'package': 'PlaceMe Mechanical', 'student': 'Rajeev Kumar', 'level': 'Level 2'},
        # {'package': 'N2N Python', 'student': 'Gaurav Singh', 'level': 'Level 2'},
        # {'package': 'PEPTize', 'student': 'Rakesh Sharma', 'level': 'Level 3'},
    ])

import pdfkit
