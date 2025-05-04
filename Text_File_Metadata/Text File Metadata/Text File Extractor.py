#Extract metadata from .txt files and record the metadata in .txt files.

#Copyright (c) 2023, Sourceduty

#This software is free and open-source; anyone can redistribute it and/or modify it.

import os
import sys

path = 'Folder1'

contents = []

for filename in filter(lambda p: p.endswith(".txt"), os.listdir(path)):
    filepath = os.path.join(path, filename)
    with open(filepath, mode='r') as f:
        contents += [f.read()]
        
with open('Metadata.txt', 'w') as f:
    sys.stdout = f
    print (contents)