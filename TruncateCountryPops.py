

from process import GetSubString
from process import GetSubString

srcFolder = "MinecraftSpeedrunExtractCountries/"
fileName = "countrypopdata"
ext = ".csv"

with open(srcFolder + fileName + ext, "r") as input:
    with open(srcFolder + fileName + '_truncated' + ext, "w") as output:
        # iterate all lines from file
        currentcountry = ''
        for line in input:
            country = GetSubString(line.strip("\n"),startChar=',',endChar=',')
            if country != currentcountry:
                currentcountry = country
                output.write(line)
