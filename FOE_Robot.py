# ==================== DÉFINITION DES RÉGLAGLES ==============================================================
from random import randint
world_list = [3,15,16] 
Settings.ActionLogs = False
Settings.LogTime = True
Settings.MinSimilarity = .8
setFindFailedResponse(SKIP)

# ==================== DÉFINITION DES FONCTIONS ==============================================================
def seek_click(target,reg = SCREEN):
	if current_world==0:
		return 0
	if reg.exists(target,0):
		reg.click(target)
		return 1
	else:
		return 0
def wait_click(target,timeout = FOREVER,reg = SCREEN):
	if timeout == FOREVER:
		while not reg.exists(target,5):
			if current_world==0:
				return 0
			mouseMove(randint(-99,99),randint(-99,99)) #Bouge un peu la souris au cas ou la cible est cachee
			if seek_click(Pattern("1483362735914.png").exact()):
				wait(1)
				type(Key.ENTER)
				wait(1)
		click(getLastMatch())
	else:	
		if reg.exists(target,timeout):
			click(getLastMatch())
			return 1
		else:
			if seek_click(Pattern("1483362735914.png").exact()):
				wait(1)
				type(Key.ENTER)
				wait(1)
			return 0
		
def log(entry = ""):
	with open("D:\Dropbox\Fun\FOE\Macro\FOE_Robot.sikuli\log.txt","a") as file:
		file.write("["+time.strftime("%Y-%m-%d %H:%M:%S")+"] ")
		file.write(entry)
		file.write("\n")
def clearlog():
	with open("D:\Dropbox\Fun\FOE\Macro\FOE_Robot.sikuli\log-archive.txt","a") as archive, open("D:\Dropbox\Fun\FOE\Macro\FOE_Robot.sikuli\log.txt","r") as current:
		archive.write(current.read())
	with open("D:\Dropbox\Fun\FOE\Macro\FOE_Robot.sikuli\log.txt","w") as file: 
		file.write("["+time.strftime("%Y-%m-%d %H:%M:%S")+"] ")
		file.write("New session launched. See log-archive.txt for previous entries")
		file.write("\n")
def clearRemote():
	with open("D:\Dropbox\Fun\FOE\Macro\FOE_Robot.sikuli\ifttt.txt","w") as remote:
		remote.write("")# Vide le fichier de remote avant de commencer

def move_view(x,y,COLLECT_PROOF = 0):
	if pause_check():
		return
	if seek_click(Pattern("1483362735914.png").exact()):
		wait(1)
		type(Key.ENTER)
		wait(1)
	if exists(Pattern("1479301630898.png").similar(0.95).targetOffset(0,450)):# approx center of window
		mouseMove(getLastMatch())
		if COLLECT_PROOF:#On commence par un mini drag-drop pour ne pas collecter au lieu de déplacer l écran
			mouseDown(Button.LEFT)
			wait(.25)
			mouseMove(-50,-50)
			wait(.25)
			mouseMove(getLastMatch())
			wait(.25)
			mouseUp(Button.LEFT)
			wait(.25)
		# maintenant le déplacement demandé
		mouseDown(Button.LEFT)
		mouseMove(-x,-y)
		mouseUp(Button.LEFT)
		return 1
	else:
		return 0
def open_world():
	global current_world
	status.setText("Ouverture de W" + str(current_world))
	print("Started world " + str(current_world) + " @ " + time.strftime("%Y-%m-%d %H:%M:%S"))
	#chrome = App("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --new-window https://fr0.forgeofempires.com/page/")
	while 1:
		if current_world==0:
			return
		seek_click(Pattern("1486001679249.png").exact())
		chrome = App.open("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --new-window https://fr0.forgeofempires.com/page/'")
		s=10
		wait(1)
		type("0",Key.CTRL)
		while s:
			if wait_click(Pattern("1481120160133.png").targetOffset(-80,-115),1):
				wait(.25)
				type(Key.DOWN)
				wait(1)
				type(Key.ENTER)
				wait(1)
				type(Key.ENTER)
			if wait_click("1476753469907.png",1):
				break
			s -=1
		wait(1)
		if  s and current_world == 3: #'C':
			s *= wait_click(Pattern("1476781840604.png").similar(0.90),10)
		elif s and current_world == 15: #'P':
			s *= wait_click(Pattern("1476781898555.png").similar(0.90),10)
		elif s and current_world == 16: #'Q':
			s *= wait_click(Pattern("1476781977706.png").similar(0.90),10)
		if s:
			s *= wait_click(Pattern("1491750295812.png").targetOffset(0,20),20) # Attendre affichage de la ville
		if s:
			wheel(Pattern("1479301630898.png").similar(0.95).targetOffset(0,400),WHEEL_DOWN,3) # S'assurer que l'échelle est au plus grand
			break
		else:
			log("[W" + str(current_world) + "] Load retry...")
			type("w",Key.CTRL)
			wait(1)
	wait(.5)
	
	if seek_click(Pattern("1491559904471.png").exact().targetOffset(0,-20)):#Reprendre les négociations "1491559852719.png" #--> Alternative possible
		log("[W" + str(current_world)+"] Nego started...")
		pause()
	if seek_click(Pattern("1491559592013.png").exact().targetOffset(0,-20)):#Continuer le combat
		log("[W" + str(current_world)+"] Battle started...")
		pause()
		
	
	seek_click("1476785522783.png") # X - close popup
def close_world():
	global current_world
	#global chrome
	status.setText("Fermeture de W" + str(current_world))
	seek_click("1477882546743.png")
	seek_click("1482667306801.png")
	seek_click("1476785522783.png")
	wait_click(Pattern("1476785554780.png").exact(),2) #PwrOff button
	wait_click("1482202331015.png",5) #Déconnexion 
	wait_click(Pattern("1476753469907.png").targetOffset(0,-100),3) 
	wait(1)
	App.focus("Forge of Empires - Google Chrome")
	type("w",Key.CTRL)
	wait(2)
def treasure_hunt():
	global next_run
	if pause_check():
		return
	status.setText("W" + str(current_world)+": Chasse aux tresors")
	seek_click("1476784990496.png")
	seek_click("1476869339766.png")
	seek_click("1477938159435.png")
	seek_click("1488319007746.png")
	seek_click("1498122013437.png")
	exists("1481796872768.png",5)
	if seek_click(Pattern("1481912728830.png").targetOffset(-20,0)): #Ouvrir et repartir ->doit être relancé dans 5 minutes
		wait_click("1476785383350.png")# OK - close popup
		wait_click("1482667306801.png",1.5)# OK - close popup
		print("    Treasure hunt started in world " + str(current_world) + " @ " + time.strftime("%Y-%m-%d %H:%M:%S")+" Waiting 5 minutes before continuing")
		log("[W" + str(current_world)+"] Hunt launched")
		next_run = 5 # Next run apres 5 minutes
	elif seek_click(Pattern("1481819304806.png").targetOffset(-19,0)): #Ouvrir et continuer
		print("    Treasure hunt advanced in world " + str(current_world) + " @ " + time.strftime("%Y-%m-%d %H:%M:%S"))
		log("[W" + str(current_world)+"] Hunt advanced")
		wait_click("1476785383350.png")# OK - close popup
		wait_click("1482666296968.png",1.5)# OK - close popup
		wait_click("1476785522783.png",2)# X - close popup
	seek_click("1476785383350.png")# OK - close popup
	seek_click("1476785522783.png")# X - close popup
def POMO_full():
	if pause_check():
		return
	status.setText("W" + str(current_world)+": POMO")
	seek_click("1492459151799.png")# Fermer - close popup
	seek_click(Pattern("1476785522783.png").exact())# X - close popup
	seek_click(Pattern("1477045257278.png").exact())
	move_view(-800,400)
	move_view(-800,400)
	find(Pattern("1477651422181.png").exact().targetOffset(30,-50))
	contacts_bar= Region(getLastMatch().x+35,getLastMatch().y-25,730,160)
	contacts_bar.highlight(1)
	mmd = Settings.MoveMouseDelay
	Settings.MoveMouseDelay = .25
	POMO_count = 0
	BEER_count = 0
	for player_group in ['amis', 'guilde', 'voisins']:
		seek_click("1492459151799.png")# Fermer - close popup
		seek_click("1476785383350.png")# OK - close popup
		seek_click("1482667306801.png") # Fermer - close popu
		seek_click(Pattern("1493020958360.png").exact().targetOffset(0,-120),contacts_bar)# menu contextuel - close
		if player_group == 'amis':
			wait_click("1476799810011.png")
			status.setText("W" + str(current_world)+": POMO - Amis")
		elif player_group == 'guilde':
			wait_click("1476799836040.png")
			status.setText("W" + str(current_world)+": POMO - Guilde")
		elif player_group == 'voisins':
			wait_click("1476799858711.png")
			status.setText("W" + str(current_world)+": POMO - Voisins")
		wait(1)
		wait_click(Pattern("1477647782557.png").exact())# Atteindre la fin de la liste
		wait(1)
		j=0
		while j<22:
			if pause_check():
				break
			if contacts_bar.exists(Pattern("1481797004836.png").similar(0.90),1):
				list = sorted(contacts_bar.findAll(Pattern("1481797004836.png").similar(0.90)), key=lambda m:m.x)
				for each in list:
					if pause_check():
						return
					wait_click("1482667306801.png",2) # Fermer - close popup
					#seek_click("1492459151799.png")# Fermer - close popup
					#seek_click("1476785383350.png")# OK - close popup
					#seek_click(Pattern("1493020958360.png").exact().targetOffset(0,-120),contacts_bar)# menu contextuel - close
					click(each)
					POMO_count += 1
				wait(1)
				seek_click(Pattern("1482667306801.png").exact()) # Fermer - close popup
				seek_click(Pattern("1492459151799.png").exact())# Fermer - close popup
				seek_click("1476785383350.png")# OK - close popup
				seek_click(Pattern("1493020958360.png").exact().targetOffset(0,-120),contacts_bar)# menu contextuel - close
			if player_group == 'amis':
				if contacts_bar.exists(Pattern("1479983497731.png").similar(0.90).targetOffset(0,-7),1):
					list = sorted(contacts_bar.findAll(Pattern("1479983497731.png").similar(0.90).targetOffset(0,-7)), key=lambda m:m.x)
					for each in list:
						click(each)
						BEER_count +=1
						wait_click(Pattern("1482667306801.png").similar(0.80),5) # Fermer - close popup
						seek_click(Pattern("1492459151799.png").exact())# X - close popup
					wait(1)
			if contacts_bar.exists(Pattern("1481798353811.png").exact(),0):
				break # if first in list is found, don t continue
			wait_click(Pattern("1477647886523.png").exact()) #Previous page 
			j+=1
	Settings.MoveMouseDelay = mmd
	if POMO_count:
		log("[W" + str(current_world)+"] " + str(POMO_count) + " POMO done. ")
	if BEER_count:
		log("[W" + str(current_world)+"] " + str(BEER_count) + " BEER drunk.")
	wait_click("1477571713803.png")
def tavern():
	if pause_check():
		return
	status.setText("W" + str(current_world)+": Service de la Taverne")
	move_view(-800,-400,1)
	move_view(-800,-400)
	if seek_click(Pattern("1479984544343.png").targetOffset(0,170)):
		if wait_click("1481796612169.png",5):
			empty_chairs = 0
			if exists(Pattern("1480992060925.png").exact()):
				mm = findAll(Pattern("1480992060925.png").exact())
				for m in mm:
					empty_chairs +=1
			if empty_chairs < 2:
				if seek_click("1481796684024.png"):
					log("[W" + str(current_world)+"] Tavern cash in")
			else:
				log("[W" + str(current_world)+"] Tavern: " + str(empty_chairs) + " places")
		wait_click("1476785522783.png")

def collect(target,reg= SCREEN):
	#if pause_check():
	#	return 0
	#reg.highlight(1)
	count=0
	loops=0
	dy=0
	while reg.exists(target,3) and loops<6:
		if loops > 0:
			dy += 10
		list = reg.findAll(target)
		if not list == None:
			list = sorted(list, key=lambda m:m.x)
			drag(list[0].getTarget().above(dy))
			for each in list:
				hover(each)
				count+=1
			dropAt(getLastMatch())
		loops +=1
		seek_click(Pattern("1482262392369-2.png").similar(0.80))
		seek_click(Pattern("1476785522783-2.png").exact())
	return count

def launch_prod(target,option = Pattern("1482230896918.png").exact(),reg=SCREEN):
	#if pause_check():
	#	return 0
	mmd = Settings.MoveMouseDelay
	Settings.MoveMouseDelay = .25
	#reg.highlight(1)
	count=0
	launch_error=0
	while reg.exists(target,1) and launch_error < 5:
		list = findAll(target.similar(0.50))
		if not list == None:
			for each in list:
				click(each)
				if exists(Pattern("1482230675160-1.png").exact(),4):
					prod_title = Region(getLastMatch().x-700,getLastMatch().y-20,720,50)
					#prod_title.highlight(1)
					if seek_click(Pattern("1483896950530-1.png").exact(),prod_title) or seek_click(Pattern("1483897020289-1.png").exact(),prod_title) or seek_click(Pattern("1483897062260-1.png").exact(),prod_title) or seek_click(Pattern("1488318799094.png").exact(),prod_title) or seek_click(Pattern("1492994678597.png").exact(),prod_title): #
						seek_click(Pattern("1483892809767-1.png").exact())
						wait(.25)
					else:
						if wait_click(option,1): # launch option (time)
							wait(.25)
							if exists(option,.25):
								seek_click("1482230675160.png")
								launch_error += 1
							else:
								count += 1
						elif wait_click(Pattern("1482230896918.png").exact(),1): # if choosen time option is not availible, choose 8h
							wait(.25)
							if exists(Pattern("1482230896918.png").exact(),.25):
								seek_click(Pattern("1482230675160.png").exact())# "X"
								launch_error += 1
							else:
								count += 1
				else:
					launch_error += 1
				seek_click(Pattern("1482230675160.png").exact())# "X"
				
	Settings.MoveMouseDelay = mmd
	return count

def screen_collect_and_launch():#(box_picked,coin_picked,supply_picked,prod_launched):
	global box_picked
	global coin_picked
	global supply_picked
	global prod_launched
	global robery_cleared
	global militaty_picked
	if pause_check():
		return
	status.setText("W" + str(current_world)+": Recolte - Militaires")
	militaty_picked += collect("1494790916031.png")#militaryPattern("1488319168166.png").similar(0.80).targetOffset(0,80)
	status.setText("W" + str(current_world)+": Recolte - Pillages")
	robery_cleared += collect(Pattern("1489077703725.png").targetOffset(0,90))#probery (thunder icon)
	status.setText("W" + str(current_world)+": Recolte - Boites")
	box_picked += collect(Pattern("1476976977709-1.png").similar(0.80).targetOffset(0,80))
	status.setText("W" + str(current_world)+": Recolte - Pieces")
	coin_picked += collect(Pattern("1476977050669-1.png").similar(0.75).targetOffset(10,79))
	status.setText("W" + str(current_world)+": Recolte - Marchandises")
	supply_picked += collect(Pattern("1482292482984.png").similar(0.80).targetOffset(-3,90))
	status.setText("W" + str(current_world)+": Lancement des productions")
	prod_launched += launch_prod(Pattern("1482460710090.png").similar(0.65).targetOffset(0,80)) 

def city_walkaround():
	global box_picked
	global coin_picked
	global supply_picked
	global prod_launched
	global robery_cleared
	global militaty_picked
	if pause_check():
		return 0
	box_picked = 0
	coin_picked = 0
	supply_picked = 0
	prod_launched = 0
	robery_cleared = 0
	militaty_picked = 0
	#wait(1)
	type(" ",Key.ALT)
	wait(.5)
	type("x") #maximize windows
	wait(.5)
	SCREEN.setH(SCREEN.h - 150)
	SCREEN.setW(SCREEN.w - 150)
	SCREEN.setX(100)
	SCREEN.highlight(2)
	seek_click(Pattern("1477571713803-2.png").exact())
	tavern()
	move_view(450,100) 
	move_view(450,100)
	seek_click(Pattern("1477571713803-2.png").exact())
	screen_collect_and_launch()
	move_view(0,300) 
	move_view(0,300)
	screen_collect_and_launch()
	move_view(500,0) 
	move_view(500,0)
	screen_collect_and_launch()
	move_view(0,-300)
	move_view(0,-300)
	screen_collect_and_launch()
	wait(1)
	counters=[robery_cleared,militaty_picked,box_picked,coin_picked,supply_picked,prod_launched]
	units=[" Robery"," Military unit"," Box"," Coin"," Supply"," Prod launched"]
	log_entries=0
	for i in range(1,6):
		if counters[i]:
			log("[W"+str(current_world)+"] "+str(counters[i])+units[i])
			log_entries+=1
	if not log_entries:
		log("[W"+str(current_world)+"] Nothing to pick")
	type(" ",Key.ALT)
	type("r") #restore windows size
	SCREEN.setH(SCREEN.h + 150)
	SCREEN.setW(SCREEN.w + 150)
	SCREEN.setX(0)
	
def pause_check():
	global current_world
	global next_run
	if current_world == 0:
		return 1
	if seek_click(Pattern("1491312792534.png").exact()): #fenêtre qui apparait car connecté ailleur
		log("[W"+str(current_world)+"Connection lost, restart at " + time.strftime("%H:%M",time.localtime+60*str(next_run)))
		status.setText("W" + str(current_world)+": Connection lost")
		next_run = 30
		#close_world()
		App.focus("Forge of Empires - Google Chrome")
		type("w",Key.CTRL)
		current_world = 0
		msg.setText("SCRIPT MIS EN PAUSE - Prochaine exécution dans " + str(next_run) + " minutes.")
		msg.setBackground(JC.green)
		return 1
		
	with open("D:\Dropbox\Fun\FOE\Macro\FOE_Robot.sikuli\ifttt.txt","r") as remote_file:
		if "PAUSE" in remote_file:
			clearRemote()
			log("Pause requested remotely, restart at " + time.strftime("%H:%M",time.localtime+60*str(next_run)))
			status.setText("Pause requested remotely")
			next_run = 30
			#close_world()
			App.focus("Forge of Empires - Google Chrome")
			type("w",Key.CTRL)
			current_world = 0
			msg.setText("SCRIPT MIS EN PAUSE (remote) - Prochaine exécution dans " + str(next_run) + " minutes.")
			msg.setBackground(JC.green)
			resumeButton.setEnabled(True)
			return 1
					

def pause_click(event):
	pause()

def pause():
	global next_run
	global current_world
	#global chrome
	if current_world == 0:
		next_run += 30
		countdown=0
		status.setText("30 minutes ajoutees")
		log("30 min delay ... Next run at " + time.strftime("%H:%M",time.localtime+60*str(next_run)))
		msg.setText("SCRIPT EN VEILLE - Prochaine execution dans " + str(next_run) + " minutes.")
		msg.setBackground(JC.green)
	else:
		next_run = 30
		current_world = 0
		log("waiting 30 min ...Next run at " + time.strftime("%H:%M",time.localtime+60*str(next_run)))
		msg.setText("SCRIPT MIS EN PAUSE - Prochaine exécution dans " + str(next_run) + " minutes.")
		msg.setBackground(JC.green)
		resumeButton.setEnabled(True)
		App.focus("Forge of Empires - Google Chrome")
		type("w",Key.CTRL)

def resume(event):
	global next_run
	global countdown
	next_run = 0
	countdown = 0

# ===================== DÉFINITION DU MESSAGE D AVERTISSEMENT DE SCRIPT EN EXÉCUTION =============
from javax.swing import JFrame, JTextArea, JButton, JPanel
from java.awt import Color as JC
from java.awt import Font as JFONT

box = JFrame('FOE Robot', defaultCloseOperation = JFrame.EXIT_ON_CLOSE)
box.setAlwaysOnTop(True)
layout = JPanel()
layout.setLayout(None)
box.add(layout)
msg = JTextArea("ATTENTION - SCRIPT EN COURS D'EXECUTION - VEUILLEZ EVITER DE TOUCHER A LA SOURIS"); #\n
msg.setEditable(False)
msg.setBackground(JC.yellow)
msg.setFont(JFONT("Dialog", JFONT.PLAIN, 25))
msg.setBounds(0,0,1250,50)
layout.add(msg)
status = JTextArea(text = ""); #\n
status.editable = False
status.wrapStyleWord = True
status.lineWrap = True
status.setBackground(JC.white)
status.setFont(JFONT("Dialog", JFONT.PLAIN, 15))
status.setBounds(1550,0,250,50)
layout.add(status)
pauseButton = JButton('Pause (+30 min.)',actionPerformed = pause_click)
pauseButton.setBounds(1250,0,150,50)
layout.add(pauseButton)
resumeButton = JButton('Lancer maintenant',actionPerformed = resume)
resumeButton.setBounds(1400,0,150,50)
layout.add(resumeButton)
box.pack()
box.setSize(1800, 100)
box.setLocation(0,0)
box.visible = True
		
# ============================== DÉBUT DU PROGRAMME =========================================================
current_world=0
POMO_skip=0
next_run = .25
clearlog()
clearRemote()

while 1:
	resumeButton.setEnabled(True)
	status.setText(" ")
	while next_run > 0:
		countdown= min(60,60*next_run)
		while countdown>0:
			if next_run > 1:
				msg.setBackground(JC.green)
				msg.setText("SCRIPT EN VEILLE - Prochaine execution dans " + str(next_run) + " minutes.")
			else:
				msg.setBackground(JC.yellow)
				msg.setText("ATTENTION ! LE SCRIPT SE LANCERA DANS " + str(countdown) + " SECONDES.")
			wait(1)
			countdown -=1
			with open("D:\Dropbox\Fun\FOE\Macro\FOE_Robot.sikuli\ifttt.txt","r") as remote_file:
				if "PAUSE" in remote_file:
					clearRemote()
					next_run += 30
					msg.setText("SCRIPT MIS EN PAUSE (remote) - Prochaine exécution dans " + str(next_run) + " minutes.")
					log("Paused remotely, Next run at " + time.strftime("%H:%M",time.localtime+60*str(next_run)))
					status.setText("Pause requested remotely")
				elif "RESUME" in remote_file:
					clearRemote() 
					next_run = 0
					countdown = 0
					log("Resumed remotely...")
					#msg.setBackground(JC.yellow)
					#msg.setText("ATTENTION ! LE SCRIPT SE LANCERA DANS " + str(countdown) + " SECONDES.")
					status.setText("Resumed remotely")
			if next_run <= 0:
				break
		next_run -= 1
	next_run = 20
	msg.setText("ATTENTION - SCRIPT EN COURS D'EXECUTION - VEUILLEZ EVITER DE TOUCHER A LA SOURIS")
	msg.setBackground(JC.red)
	resumeButton.setEnabled(False)
	
	for current_world in world_list:
		open_world()
		treasure_hunt()
		city_walkaround()
		if not POMO_skip:
			POMO_full()
			treasure_hunt()
		if pause_check():
			break
		close_world()
	if current_world : # pas égal 0 donc pas interrompu
		if not POMO_skip:
			POMO_skip = 3
		else:
			POMO_skip -= 1
		if not POMO_skip:
			log("Done, next(POMO): " + time.strftime("%H:%M",time.localtime+60*str(next_run)))
		else:
			log("Done, next(quick): " + time.strftime("%H:%M",time.localtime+60*str(next_run)))
	current_world = 0
#End of while 1 loop --> start again