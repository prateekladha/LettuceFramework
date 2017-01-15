'''
	Return ordered JSON in ascending order of keys
'''
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


'''
	Remove key from JSON
'''
def removeKey(key, parent, jsonObject):
	if parent is not None or (parent.strip().lower() != ""):
			parentKeys = parent.strip().split('/')
			flag = 0
			for parentKey in parentKeys:
				if jsonObject is not None and parentKey in jsonObject:
					njsonObject = jsonObject[parentKey];
					if isinstance(njsonObject, dict): #JsonObject
						continue;
					elif isinstance(njsonObject, list): #JsonArray
						for index in njsonObject:
							index = removeKey(key, parent, index)
					else:
						njsonObject.pop(key, None)
					flag = 1
			
			if flag == 0 and jsonObject is not None:
				jsonObject.pop(key, None)						
	else:
		jsonObject.pop(key, None)
	return jsonObject


'''
	Get key value from JSON
'''
def getKeyValue(key, parent, jsonObject, lst):
	if lst is None:
		lst = []
	if parent is not None or (parent.strip().lower() != ""):
			parentKeys = parent.strip().split('/')
			flag = 0
			for parentKey in parentKeys:
				if jsonObject is not None and parentKey in jsonObject:
					njsonObject = jsonObject[parentKey];
					if isinstance(njsonObject, dict): #JsonObject
						continue;
					elif isinstance(njsonObject, list): #JsonArray
						for index in njsonObject:
							index = getKeyValue(key, parent, index, lst)
					else:
						lst.append(njsonObject[key])
					flag = 1
			
			if flag == 0 and jsonObject is not None:
				lst.append(jsonObject[key])						
	else:
		lst.append(jsonObject[key])
	return lst