from core.language import Language, LanguageChange
from volodnian.greater_volodnian import GreaterVolodnian
from core.chronos import *

WestVolodnian = Language('West Volodnian', 'WVol')

LanguageChange(GreaterVolodnian, WestVolodnian, 
    ('Velar Merger',
        ('N', 'g') 
    ),
)