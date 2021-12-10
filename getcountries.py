from process import FormatAsCSVTable, GetAllSubValues

srcFolder = "MinecraftSpeedrunExtractCountries/"

names = []
countries = []

filename = srcFolder + input("filepath: ")
debug = input('should debug? ').lower() == 'yes'
with open(filename,'rt',encoding='UTF-8') as file:
    str_res = file.read()
    countries = GetAllSubValues(str_res,'data-original-title',debug=debug)

with open(srcFolder + "MinecraftData.csv",'wt') as file:
    file.write('"Countries"\n')
    file.write(FormatAsCSVTable([countries]))
