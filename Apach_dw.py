

from time import sleep
from pyrsistent import b
from sqlalchemy import false


i = 1
a = '# '

while i <= 20:
    
    sleep(1)
    
    a = a + '# '
    i = i + 1
   
#new
print("Fertig")

