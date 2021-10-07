import string
from numbers import Number as number

def CutFromStr(_str: string, lowerIndex: number, upperIndex: number):
    return _str[:lowerIndex] + _str[upperIndex:]

def GetSubString(_str: string, index: number = 0, startChar='"', endChar='"'):
    indexes = []
    for i in range(index, len(_str)):
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

def GetCSVValue(_str: string, index: number = 0):
    indexes = []
    for i in range(0, len(_str)):
        if (_str[i] == ',' or i == 0):
            if (index != 0):
                index-=1
                continue
            indexes.append(i)
        if (len(indexes) > 1):
            break
    res = _str[indexes[0]+1:indexes[1]]
    return res

def GetAllSubValues(_str: string, value: string, startChar='"', endChar='"', debug=False):
    gotallvalues = False
    values = []
    count = 0
    while not gotallvalues:
        count += 1
        if (debug):
            print(f'At Value: {count}')
        try:
            currentIndex = _str.index(value)
            values.append(GetSubString(_str, currentIndex +
                          len(value), startChar, endChar))
            _str = CutFromStr(_str, currentIndex,
                              currentIndex + len(values[-1]) + len(value))
        except ValueError:
            gotallvalues = True
    return values

def GetLowestLength(Collections) -> number:
    length = 10000000000000000000000000000000000000000000
    for collection in Collections:
        if (len(collection) < length):
            length = len(collection)
    return length

def FormatAsCSVTable(Collections) -> string:
    length = GetLowestLength(Collections)
    res = ''
    for index in range(0, length):
        for collection in Collections:
            res += f'"{collection[index]}",'
        res = res[0:-1]
        res += '\n'
    return res
