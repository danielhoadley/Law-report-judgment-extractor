# Extracts metadata and judgment blocks from ICLR report XML

from bs4 import BeautifulSoup
import os
import io

for catchword in catchwords:
    zero_level = catchword.strip('\n')
    zeros.append(zero_level)

# Read the XML

directory = '/Users/danielhoadley/PycharmProjects/trainer/'

# Open each XML file
for filename in os.listdir(directory):
    if filename.endswith(".xml"):

        f = open(filename)
        file = f.read()
        soup = BeautifulSoup(file, "lxml") #load content of file into bs4
        judgment = str(soup.find('judgments')) #extract <judgments>
        metadata = str(soup.find('metadata')) #extract <judgments>

        # Write judgment to file
        with io.open('[JO]' + filename, 'w+', encoding='utf-8') as g:
            g.write(metadata)
            g.write(judgment)





