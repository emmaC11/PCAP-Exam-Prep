# 1 - importing module as a whole
import math
import random

import math, random

# 2 - accessing entities from import syntax above
import my_module

test = my_module.entityname

 # 3 - importing individual entities

from math import pi
from module import function1, function2

print(function1())
print(function2)

# 4 - import all entities in a module
from math import *

# 5 - change name of imported entity

import module as mod
from module import entity as e
from module import entity1 as e1, entity2 as e2
from math import pi as p



