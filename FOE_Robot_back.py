# ==================== DÉFINITION DES RÉGLAGLES ==================================================
from random import randint
world_list = [3,15,16] 
Settings.ActionLogs = False
Settings.LogTime = True
Settings.MinSimilarity = .8
setFindFailedResponse(SKIP)


# ===================== DÉFINITION DU MESSAGE D'AVERTISSEMENT DE SCRIPT EN EXÉCUTION =============
from javax.swing import JFrame as JF
from javax.swing import JTextArea as JTA
from java.awt import Color as JC
from java.awt import Font as JFONT
box = JF()
box.setAlwaysOnTop(True);
#box.setUndecorated(True);
msg = JTA("ATTENTION - SCRIPT EN COURS D'EXECUTION - VEUILLEZ EVITER DE TOUCHER A LA SOURIS"); #\n
msg.setEditable(False);
msg.setBackground(JC.yellow)
msg.setFont(JFONT("Dialog", JFONT.PLAIN, 40));
box.getContentPane().add(msg)
box.pack()
box.setLocation(0,0)



# ==================== DÉFINITION DES FONCTIONS =============================================
def seek_click(target,reg = SCREEN):
	if reg.exists(target,0):
		reg.click(target)
		return 1
	else:
		return 0
def wait_click(target,timeout = FOREVER,reg = SCREEN):
	if timeout == FOREVER:
		while not reg.exists(target,5):
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
def move_view(x,y,COLLECT_PROOF = 0):
	if seek_click(Pattern("1483362735914.png").exact()):
		wait(1)
		type(Key.ENTER)
		wait(1)
	if exists(Pattern("1479301630898.png").targetOffset(0,400)):# approx center of window
		mouseMove(getLastMatch())
		if COLLECT_PROOF:#On commence par un mini drag-drop pour ne pas collecter au lieu de déplacer l'écran
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
def open_world(current_world):
	#openApp("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --new-window https://fr0.forgeofempires.com/page/'") 
	print("Started world " + str(current_world) + " @ " + time.strftime("%Y-%m-%d %H:%M:%S"))
	chrome = App("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --new-window https://fr0.forgeofempires.com/page/'")
	while 1:
		seek_click(Pattern("1486001679249.png").exact())
		chrome.open()
		s=10
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
			s *= wait_click(Pattern("1476869730378-1.png").targetOffset(0,22),20) # Attendre l'affichage de la ville
		if s:
			break
		else:
			log("[W" + str(current_world) + "] Load retry...")
			type("w",Key.CTRL)
			wait(1)
	wait(.5)
	seek_click("1476785522783.png") # X - close popup
def close_world():
	seek_click("1477882546743.png")
	seek_click("1482667306801.png")
	seek_click("1476785522783.png")
	wait_click("1476785554780.png") #PwrOff button
	wait_click("1482202331015.png",5) #Déconnexion 
	wait(1)
	type("w",Key.CTRL)
	wait(2)
def treasure_hunt():
	seek_click("1476784990496.png")
	seek_click("1476869339766.png")
	seek_click("1477938159435.png")
	seek_click("1488319007746.png")
	exists("1481796872768.png",5)
	if seek_click(Pattern("1481912728830.png").targetOffset(-20,0)): #Ouvrir et repartir ->doit être relancé dans 5 minutes
		wait_click("1476785383350.png")# OK - close popup
		wait_click("1482667306801.png",1.5)# OK - close popup
		print("    Treasure hunt started in world " + str(current_world) + " @ " + time.strftime("%Y-%m-%d %H:%M:%S")+" Waiting 5 minutes before continuing")
		log("[W" + str(current_world)+"] Hunt launched")
		#wait_click(Pattern("1481819304806.png").targetOffset(-19,0)) # Attendre les 5 minutes et click ouvrir et continuer
		#print("    Treasure hunt advanced in world " + str(current_world) + " @ " + time.strftime("%Y-%m-%d %H:%M:%S"))
		#log("[W" + str(current_world)+"] Hunt advanced")
		#wait_click("1476785383350.png")# OK - close popup
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
	seek_click(Pattern("1477045257278.png").exact())
	find(Pattern("1477651422181.png").exact().targetOffset(30,-50))
	contacts_bar= Region(getLastMatch().x+35,getLastMatch().y-25,730,160)
	contacts_bar.highlight(1)
	mmd = Settings.MoveMouseDelay
	Settings.MoveMouseDelay = .25
	POMO_count = 0
	BEER_count = 0
	for player_group in ['amis', 'guilde', 'voisins']:
		if player_group == 'amis':
			wait_click("1476799810011.png")
		elif player_group == 'guilde':
			wait_click("1476799836040.png")
		elif player_group == 'voisins':
			wait_click("1476799858711.png")
		wait(1)
		wait_click("1477647782557.png")# Atteindre la fin de la liste
		wait(1)
		j=0
		while j<20:
			if contacts_bar.exists(Pattern("1481797004836.png").exact(),1):
				list = sorted(contacts_bar.findAll(Pattern("1481797004836.png").similar(0.90)), key=lambda m:m.x)
				for each in list:
					seek_click("1482667306801.png") # Fermer - close popup
					click(each)
					POMO_count += 1
					wait_click("1482667306801.png",2) # Fermer - close popup
				wait(1)
			if player_group == 'amis':
				if contacts_bar.exists(Pattern("1479983497731.png").similar(0.90).targetOffset(0,-7),1):
					list = sorted(contacts_bar.findAll(Pattern("1479983497731.png").similar(0.90).targetOffset(0,-7)), key=lambda m:m.x)
					for each in list:
						click(each)
						BEER_count +=1
						wait_click("1482667306801.png",5) # Fermer - close popup
					wait(1)
			if contacts_bar.exists(Pattern("1481798353811.png").exact(),0):
				break # if first in list is found, don't continue
			wait_click("1477647886523.png") #Next page 
			j+=1
	Settings.MoveMouseDelay = mmd
	print("    " + str(POMO_count) + " POMO completed in world " + str(current_world) + " @ " + time.strftime("%Y-%m-%d %H:%M:%S"))
	if POMO_count:
		log("[W" + str(current_world)+"] " + str(POMO_count) + " POMO done. ")
	if BEER_count:
		log("[W" + str(current_world)+"] " + str(BEER_count) + " BEER drunk.")
	wait_click("1477571713803.png")
def POMO_hist():
	wait_click("1476869730378.png")# Top-Left icon
	wait_click("1477044921973.png") #Nouvelles
	wait_click(Pattern("1477044943329.png").similar(0.80)) #Afficher l'historique 
	wait("1477533342918.png",10)
	POMO_count = 0
	i=30
	while i > 0:
		if exists(Pattern("1477255971342.png").exact(),1):
			list = sorted(findAll(Pattern("1477255971342.png").similar(0.90)), key=lambda m:m.y)
			for each in list:
				click(each)
				POMO_count += 1
				wait(1.5)
				seek_click("1482667306801.png") # Fermer - close popup
			wait(1)
		seek_click("1477045089139.png") #Next page
		wait(.25)
		i -= 1
	seek_click("1476785522783.png")# X - close popup
	print("    " + str(POMO_count) + " POMO completed in world " + str(current_world) + " @ " + time.strftime("%Y-%m-%d %H:%M:%S"))
	log("[W" + str(current_world)+"] " + str(POMO_count) + " POMO done. ")
	wait(1)
def tavern():
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
	#reg.highlight(1)
	count=0
	while reg.exists(target,3):
		list = reg.findAll(target)
		if not list == None:
			list = sorted(list, key=lambda m:m.x)
			drag(list[0])
			for each in list:
				hover(each)
				count+=1
			dropAt(getLastMatch())
		seek_click(Pattern("1482262392369.png").similar(0.80))
		seek_click(Pattern("1476785522783.png").exact())
	return count

def launch_prod(target,option = Pattern("1482230896918.png").exact(),reg=SCREEN):
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
					if seek_click(Pattern("1483896950530-1.png").exact(),prod_title) or seek_click(Pattern("1483897020289-1.png").exact(),prod_title) or seek_click(Pattern("1483897062260-1.png").exact(),prod_title) or seek_click(Pattern("1488318799094.png").exact(),prod_title): #
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
	militaty_picked += collect(Pattern("1488319168166.png").similar(0.80).targetOffset(0,80))#military
	robery_cleared += collect(Pattern("1489077703725.png").targetOffset(0,90))#probery (thunder icon)
	box_picked += collect(Pattern("1476976977709-1.png").similar(0.80).targetOffset(0,80))
	coin_picked += collect(Pattern("1476977050669-1.png").similar(0.75).targetOffset(10,79))
	supply_picked += collect(Pattern("1482292482984.png").similar(0.80).targetOffset(-3,90))
	prod_launched += launch_prod(Pattern("1482460710090.png").similar(0.65).targetOffset(0,80)) 

def city_walkaround():
	global box_picked
	global coin_picked
	global supply_picked
	global prod_launched
	global robery_cleared
	global militaty_picked
	box_picked = 0
	coin_picked = 0
	supply_picked = 0
	prod_launched = 0
	robery_cleared = 0
	militaty_picked = 0
	wait(1)
	type(" ",Key.ALT)
	type("x") #maximize windows
	wheel(Pattern("1479301630898.png").targetOffset(0,400),WHEEL_DOWN,3)
	SCREEN.h -= 150
	SCREEN.w -= 150
	SCREEN.x = 100
	SCREEN.highlight(2)
	seek_click(Pattern("1477571713803-2.png").exact())
	move_view(-800,-400,1)
	move_view(-800,-400)
	tavern()
	move_view(450,100) 
	move_view(450,100)
	seek_click(Pattern("1477571713803-2.png").exact())
	screen_collect_and_launch()#box_picked,coin_picked,supply_picked,prod_launched)
	move_view(0,300) 
	move_view(0,300)
	screen_collect_and_launch()#box_picked,coin_picked,supply_picked,prod_launched)
	move_view(500,0) 
	move_view(500,0)
	screen_collect_and_launch()#box_picked,coin_picked,supply_picked,prod_launched)
	move_view(0,-300)
	move_view(0,-300)
	screen_collect_and_launch()#box_picked,coin_picked,supply_picked,prod_launched)
	wait(1)
	log("[W"+str(current_world)+"] G:"+str(box_picked)+"  C:"+str(coin_picked)+"  S:"+str(supply_picked)+"  L:"+str(prod_launched))
	type(" ",Key.ALT)
	type("r") #restore windows size
	SCREEN.h += 150
	SCREEN.x = 0
	SCREEN.w += 150
	

# ==================== DÉBUT DU PROGRAMME =============================================
POMO_skip=0
box.setVisible(True)
while 1:
	msg.setText("ATTENTION - SCRIPT EN COURS D'EXECUTION - VEUILLEZ EVITER DE TOUCHER A LA SOURIS")
	msg.setBackground(JC.red)
	next_run = 20
	for current_world in world_list:
		open_world(current_world)
		treasure_hunt()
		city_walkaround()
		if not POMO_skip:
			POMO_full()
		close_world()
	print("last completion : " + time.strftime("%Y-%m-%d %H:%M:%S"))
	if not POMO_skip:
		POMO_skip = 3
	else:
		POMO_skip -= 1
	msg.setText("SCRIPT EN VEILLE - Prochaine exécution dans " + str(next_run) + " minutes.")
	msg.setBackground(JC.green)
	if not POMO_skip:
		log("Done, next(POMO): " + str(next_run) + "m")
	else:
		log("Done, next(quick): " + str(next_run) + "m")
	while next_run > 1:
		msg.setText("SCRIPT EN VEILLE - Prochaine execution dans " + str(next_run) + " minutes.")
		wait(60)
		next_run -= 1
	countdown = 60
	msg.setBackground(JC.yellow)
	while countdown > -1:
		msg.setText("ATTENTION ! LE SCRIPT SE LANCERA DANS " + str(countdown) + " SECONDES.")
		countdown -= 1
		wait(1)        