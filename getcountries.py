import string
from numbers import Number as number

def RemoveFromStr(_str:string,lowerIndex:number,upperIndex:number):
    return _str[:lowerIndex] + _str[upperIndex:]

def GetString(_str:string,index:number=0, startChar='"', endChar='"'):
    indexes = []
    for i in range(index,len(_str)):
        if (len(indexes) == 1):
            if (_str[i] == endChar):
                indexes.append(i)
                break
        if (_str[i] == startChar):
            indexes.append(i)
        if (len(indexes) > 1):
            break
    res = _str[indexes[0]+1:indexes[1]]
    return res

def GetAllValues(_str:string, value:string, startChar='"', endChar='"', debug=False):
    gotallvalues=False
    values = []
    count = 0
    while not gotallvalues:
        count+=1
        if (debug):
            print(f'At Value: {count}')
        try:
            currentIndex = _str.index(value)
            values.append(GetString(_str,currentIndex + len(value),startChar,endChar))
            _str = RemoveFromStr(_str,currentIndex,currentIndex + len(values[-1]) + len(value))
        except ValueError:
            gotallvalues = True
    return values

def GetLowestLength(Lists) -> number:
    length = 10000000000000000000000000000000000000000000
    for list in Lists:
        if (len(list) < length):
            length = len(list)
    return length


def FormatAsCSVTable(Lists) -> string:
    length = GetLowestLength(Lists)
    res = ''
    for index in range(0,length):
        for list in Lists:
            res += f'"{list[index]}",'
        res = res[0:-1]
        res += '\n'
    return res






names = []
countries = []

filename = input("filepath: ")
debug = input('should debug? ').lower() == 'yes'
with open(filename,'rt',encoding='UTF-8') as file:
    str_res = file.read()
    #names = GetAllValues(str_res,'<a class="link-username nobr nounderline" href="https://www.speedrun.com/',startChar='/',endChar='"',debug=debug)
    #names = list(filter(None, names))
    countries = GetAllValues(str_res,'data-original-title',debug=debug)

with open("MinecraftData.csv",'wt') as file:
    file.write('"Countries"\n')
    file.write(FormatAsCSVTable([countries]))
