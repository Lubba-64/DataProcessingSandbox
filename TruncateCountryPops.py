

from process import GetCSVValue, GetSubString
from process import GetSubString

srcFolder = "MinecraftSpeedrunExtractCountries/"
fileName = "countrypopdata"
ext = ".csv"

with open(srcFolder + fileName + ext, "r") as input:
    with open(srcFolder + fileName + '_truncated' + ext, "w") as output:
        # iterate all lines from file
        currentcountry = ''
        for line in input:
            country = GetCSVValue(line.strip("\n"),1)
            year = 0
            try:
                year = int(GetCSVValue(line.strip("\n"),4))
            except ValueError:
                continue
            if country != currentcountry and year >= 2015 and year < 2016:
                currentcountry = country
                output.write(line)
