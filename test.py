import random
import re

url = 'https://blog.stephane-robert.info/docs/developper/programmation/python/dictionnaire/'

new_url = re.sub(r"[:./\\]", "", url)

print(new_url)