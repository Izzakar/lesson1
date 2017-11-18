def get_answer():
	question = input()	
	answer = {'Привет':'И тебе привет!', 'Как дела?': 'Лучше всех!'}
	question.lower()
	if 	answer.get(question) is None:
		return ('Повтори ещё раз,пожалуйста.')
	return answer.get(question)
print(get_answer())