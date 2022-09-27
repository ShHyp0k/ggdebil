import random
from user_agents import parse

def random_user_agent(device):
	if device == "pc":
		user_agent = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36
			Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36
			Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36
			Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36
			Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36
			Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0
			Mozilla/5.0 (Macintosh; Intel Mac OS X 12.0; rv:95.0) Gecko/20100101 Firefox/95.0
			Mozilla/5.0 (X11; Linux i686; rv:95.0) Gecko/20100101 Firefox/95.0
			Mozilla/5.0 (Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0
			Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:95.0) Gecko/20100101 Firefox/95.0
			Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0
			Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0
			Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15
			Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)
			Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)
			Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)
			Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)
			Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)
			Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)
			Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)
			Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko
			Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko
			Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko
			Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko
			Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.43
			Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.43
			Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.23
			Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.23
			Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.23
			Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.23
			Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Vivaldi/4.3
			Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Vivaldi/4.3
			Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Vivaldi/4.3
			Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Vivaldi/4.3
			Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Vivaldi/4.3
			Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 YaBrowser/21.11.0 Yowser/2.5 Safari/537.36"""
		user = random.choice(user_agent.split("\n")).replace("	", "")
		if user == "":
			while True:
				user = random.choice(user_agent.split("\n")).replace("	", "")
				if user == "":
					pass
				else:
					break
		else:
			pass

	elif device == "android":
		android_users = ['Mozilla/5.0 (Linux; Android 10; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550)', 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)']
		user = random.choice(android_users)
		user_agent = parse(user)
		print(user_agent.os)
		print(user_agent.device)
		user_agent = {"OperatingSystem": {'OperatingSystem_family': user_agent.os.family, 'OperatingSystem_version': user_agent.os.version_string}, "Device": {"Device_brand": user_agent.device.brand, "Device_model": user_agent.device.model, "Device_family": user_agent.device.family}}
		print(user_agent)

	return user

def random_gmail():
	return "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for x in range(10)) + "@gmail.com"

def random_name(country):
	if country == "ru":
		ru_names = ["Август", "Авдей", "Аверкий", "Аверьян", "Авксентий", "Автоном", "Агап", "Агафон", "Аггей", "Адам", "Адриан", "Азарий", "Аким", "Александр", "Алексей", "Амвросий", "Амос", "Ананий", "Анатолий", "Андрей", "Андрон", "Андроник", "Аникей", "Аникита", "Анисим", "Антип", "Антонин", "Аполлинарий", "Аполлон", "Арефий", "Аристарх", "Аркадий", "Арсений", "Артемий", "Артем", "Архип", "Аскольд", "Афанасий", "Афиноген", "Бажен", "Богдан", "Болеслав", "Борис", "Борислав", "Боян", "Бронислав", "Будимир", "Вадим", "Валентин", "Валерий", "Валерьян", "Варлаам", "Варфоломей", "Василий", "Вацлав", "Велимир", "Венедикт", "Вениамин", "Викентий", "Виктор", "Викторин", "Виссарион", "Виталий", "Владилен", "Владлен", "Владимир", "Владислав", "Влас", "Всеволод", "Всемил", "Всеслав", "Вышеслав", "Вячеслав", "Гаврила", "Галактион", "Гедеон", "Геннадий", "Георгий", "Герасим", "Герман", "Глеб", "Гордей", "Гостомысл", "Гремислав", "Григорий", "Гурий", "Давыд", "Данила", "Дементий", "Демид", "Демьян", "Денис", "Дмитрий", "Добромысл", "Доброслав", "Дорофей", "Евгений", "Евграф", "Евдоким", "Евлампий", "Евсей", "Евстафий", "Евстигней", "Егор", "Елизар", "Елисей", "Емельян", "Епифан", "Еремей", "Ермил", "Ермолай", "Ерофей", "Ефим", "Ефрем", "Захар", "Зиновий", "Зосима", "Иван", "Игнатий", "Игорь", "Измаил", "Изот", "Изяслав", "Иларион", "Илья", "Иннокентий", "Иосиф", "Ипат", "Ипатий", "Ипполит", "Ираклий", "Исай", "Исидор", "Казимир", "Каллистрат", "Капитон", "Карл", "Карп", "Касьян", "Ким", "Кир", "Кирилл", "Клавдий", "Климент", "Кондрат", "Кондратий", "Конон", "Константин", "Корнил", "Кузьма", "Куприян", "Лавр", "Лаврентий", "Ладимир", "Ладислав", "Лазарь", "Лев", "Леон", "Леонид", "Леонтий", "Лонгин", "Лука", "Лукьян", "Лучезар", "Любим", "Любомир", "Любосмысл", "Макар", "Максим", "Максимильян", "Мариан", "Марк", "Мартын", "Мартьян", "Матвей", "Мефодий", "Мечислав", "Милан", "Милен", "Милий", "Милован", "Мина", "Мир", "Мирон", "Мирослав", "Митофан", "Михаил", "Михей", "Модест", "Моисей", "Мокей", "Мстислав", "Назар", "Наркис", "Натан", "Наум", "Нестор", "Никандр", "Никанор", "Никита", "Никифор", "Никодим", "Николай", "Никон", "Нифонт", "Олег", "Олимпий", "Онуфрий", "Орест", "Осип", "Остап", "Остромир", "Павел", "Панкратий", "Панкрат", "Пантелеймон", "Панфил", "Парамон", "Парфен", "Пахом", "Петр", "Пимен", "Платон", "Поликарп", "Порфирий", "Потап", "Пров", "Прокл", "Прокофий", "Прохор", "Радим", "Радислав", "Радован", "Ратибор", "Ратмир", "Родион", "Роман", "Ростислав", "Рубен", "Руслан", "Рюрик", "Савва", "Савватий", "Савелий", "Самсон", "Самуил", "Светозар", "Святополк", "Святослав", "Севастьян", "Селиван", "Селиверст", "Семен", "Серафим", "Сергей", "Сигизмунд", "Сидор", "Сила", "Силантий", "Сильвестр", "Симон", "Сократ", "Соломон", "Софон", "Софрон", "Спартак", "Спиридон", "Станимир", "Станислав", "Степан", "Стоян", "Тарас", "Твердислав", "Творимир", "Терентий", "Тимофей", "Тимур", "Тит", "Тихон", "Трифон", "Трофим", "Ульян", "Устин", "Фадей", "Федор", "Федосий", "Федот", "Феликс", "Феоктист", "Феофан", "Ферапонт", "Филарет", "Филимон", "Филипп", "Фирс", "Флорентин", "Фока", "Фома", "Фортунат", "Фотий", "Фрол", "Харитон", "Харлампий", "Христофор", "Чеслав", "Эдуард", "Эммануил", "Эмиль", "Эраст", "Эрнест", "Эрнст", "Ювеналий", "Юлиан", "Юлий", "Юрий", "Яков", "Ян", "Якуб", "Януарий", "Ярополк", "Ярослав"]
		return random.choice(ru_names)