import json

def isInt(var):
    if isinstance(var, int):
        return True
    return False

def isStr(var):
    if isinstance(var, str):
        return True
    return False

def isBool(var):
    if isinstance(var, bool):
        return True
    return False

def isUrl(var):
    if isinstance(var, str) and (var.startswith('http://') or var.startswith('https://')):
        return True
    return False

def isEvent(var):
    if isinstance(var, str) and (var == 'itemBuyEvent' or var == 'itemViewEvent'):
        return True
    return False

def Error(type, key, count_el, t):
    err_msg = ''
    if type == 1:
        err_msg = f"Элемент {count_el} (timestamp = {t}): Ошибка {type} - Поля \"{key}\" нет в элементе {count_el}"
    elif type == 2:
        err_msg = f"Элемент {count_el} (timestamp = {t}): Ошибка {type} - Поле \"{key}\" не включено в схему fields"
    elif type == 3:
        err_msg = f"Элемент {count_el} (timestamp = {t}): Ошибка {type} - Поле \"{key}\" должно быть типа \"{fields[key]}\""
    return err_msg

# Main
fields = {
    'timestamp': 'int',
    'referer': 'string (url)',
    'location': 'string (url)',
    'remoteHost': 'string',
    'partyId': 'string',
    'sessionId': 'string',
    'pageViewId': 'string',
    'eventType': 'string (itemBuyEvent или itemViewEvent)',
    'item_id': 'string',
    'item_price': 'int',
    'item_url': 'string (url)',
    'basket_price': 'string',
    'detectedDuplicate': 'bool',
    'detectedCorruption': 'bool',
    'firstInSession': 'bool',
    'userAgentName': 'string'
}

# Читаем файл
#with open('site_response.json', encoding='utf8') as f:
with open('site_response_err.json', encoding='utf8') as f:
    templates = json.load(f)

# Список ошибок
error = []

count_el = 0
for el in templates:
    count_el += 1
    for key in el:
        if key in fields:
            # Проверка int
            if fields[key] == 'int' and not isInt(el[key]):
                error.append(Error(3, key, count_el, el['timestamp']))
            # Проверка string
            if fields[key] == 'string' and not isStr(el[key]):
                error.append(Error(3, key, count_el, el['timestamp']))
            # Проверка string (url)
            if fields[key] == 'string (url)' and not isUrl(el[key]):
                error.append(Error(3, key, count_el, el['timestamp']))
            # Проверка string (itemBuyEvent или itemViewEvent)
            if fields[key] == 'string (itemBuyEvent или itemViewEvent)' and not isEvent(el[key]):
                error.append(Error(3, key, count_el, el['timestamp']))
            # Проверка типа bool
            if fields[key] == 'bool' and not isBool(el[key]):
                error.append(Error(3, key, count_el, el['timestamp']))
        else:
            error.append(Error(2, key, count_el, el['timestamp']))

    # Проверяем, что все поля из fields указаны во всех элементах json-а
    for key in fields:
        if key not in el:
            error.append(Error(1, key, count_el, el['timestamp']))

# Вывод ошибок
if len(error) > 0:
    print("Ошибки в json-е: ")
    for err in error:
        print(err)
else:
    print("Ошибок в json-е нет")