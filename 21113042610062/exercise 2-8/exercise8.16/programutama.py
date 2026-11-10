import greeting
greeting.greet('Budi')

from greeting import greet
greet('iyan')

from greeting import greet as g
g('Andi')

import greeting as gt
gt.greet('abi')

from greeting import *
greet('mubarok')