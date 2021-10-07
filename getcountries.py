from process import FormatAsCSVTable, GetAllSubValues

srcFolder = "MinecraftSpeedrunExtractCountries/"

names = []
countries = []

filename = srcFolder + input("filepath: ")
debug = input('should debug? ').lower() == 'yes'
with open(filename,'rt',encoding='UTF-8') as file:
    str_res = file.read()
    #names = GetAllValues(str_res,'<a class="link-username nobr nounderline" href="https://www.speedrun.com/',startChar='/',endChar='"',debug=debug)
    #names = list(filter(None, names))
    countries = GetAllSubValues(str_res,'data-original-title',debug=debug)

with open(srcFolder + "MinecraftData.csv",'wt') as file:
    file.write('"Countries"\n')
    file.write(FormatAsCSVTable([countries]))
