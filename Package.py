import urllib.request 


import os
import sys
import requests

relative = os.getcwd()
folder = 'asset'
new_relative = f'{relative}/' + folder

sys.path.insert(0, new_relative)

import asset.Finder
from asset.Finder import searchFile
from time import sleep



url = 'https://phasmosave.com/saveData.txt'



fileName2 = 'SaveFile.es3'
fileName3 = 'SaveFile.es3.tmp.bak'

print('This may take some time. Please be patient')

searchFile('saveData.txt')

joinedFile = asset.Finder.filePATH
fileArea = os.path.dirname(asset.Finder.filePATH)

delete1 = os.path.join(fileArea, fileName2)
delete2 = os.path.join(fileArea, fileName3)
sleep(2)
if os.path.exists(delete1):
    print('Found SaveFile.es3') 
    os.remove(delete1)
    print('Removed')
else:
    print('Skipping Step 2...')
sleep(1)
if os.path.exists(delete2):
    print('Found SaveFile.es3.tmp') 
    os.remove(delete2)
    print('Removed')
else:
    print('Skipping Step 3...')
sleep(1)
if os.path.exists(joinedFile):
    print('Found old saveData.txt') 
    os.remove(joinedFile)
    print('Removing old saveData')
else:
    print('Skipping Step 4...')
sleep(1)
r = requests.get(url)
full = r.content

with open(joinedFile, 'wb') as f:
    f.write(full)

print(f'Wrote file into {fileArea}')
print('Checking file is there....')

if os.path.exists(joinedFile):
    print('Success!')

else: 
    print('Failed?')
    
sleep(3)
exit()

