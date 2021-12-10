import process as _

filename = "data.html"

searchfor = '<td class="nobr center hidden-sm-u'

res = []
with open(filename,'rt',encoding='UTF-8') as file:
    str_res = file.read()
    res = _.GetAllSubValues(str_res,searchfor,'p','t')

for i in range(0,len(res)):
    res[i] = res[i][20:]
for i in range(0,len(res)):
    res[i] = res[i][:-18]

with open("minesweeperRunData.csv",'wt') as file:
    file.write('"Time Of Run In Seconds"\n')
    file.write(_.FormatAsCSVTable([res]))

print(res)