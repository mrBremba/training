empty = dict()
dialoge={'привет': 'И тебе привет!', 'как твои дела?': 'Нормально', 'тогда пока': 'Пока'}

def get_answer(key,d):
	return d.get(key)

print(get_answer('ПриВеТ'.lower(), dialoge))
print(get_answer('как твои дела?'.lower(), dialoge))
print(get_answer('тогда пока'.lower(), dialoge))