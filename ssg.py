import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from sky6 import dada
    dada()
elif bit == '32bit':
    from sky7 import dada
    dada()

