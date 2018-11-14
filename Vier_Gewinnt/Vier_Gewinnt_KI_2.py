from random import *
from Vier_Gewinnt_KI import KI
from Vier_Gewinnt_Klasse import viergewinntklasse
import copy

class VierGewinnt_KI_2:
	def __init__(self,eigeneSpielsteinfarbe,fremdesteinfarbe):
		self.__Spielfeld = [["w" for x in range(7)] for y in range(6)]
		self.__eigeneSpielsteinfarbe = eigeneSpielsteinfarbe
		self.__fremdeSpielsteinfarbe = fremdesteinfarbe
		self.__RestSpielzuege = None
		self.__Spielzug = ""
		self.__VierGewinntKlasse = None
		
	def setSpielfeld(self,Spielfeld):
		self.__Spielfeld = copy.deepcopy(Spielfeld)

	def setRestspielzuege(self,zuege):
		self.__RestSpielzuege = zuege

	def Spielzuggenerieren(self):
		steine = 0
		for element in self.__Spielfeld:
			if element == "w":
				steine +=1
		spalte=[0,0,0,0,0,0,0]
		xy =0
		while xy < 8:
			self.__VierGewinntKlasse = viergewinntklasse(self.__Spielfeld,steine)
			self.__VierGewinntKlasse.setSpielzug(0)
			self.__VierGewinntKlasse.ausführen()
			Game0 = Game(self.__eigeneSpielsteinfarbe,self.__fremdeSpielsteinfarbe,steine-1,self.__VierGewinntKlasse.getArray())
			if Game0.start() == True:
				spalte[0] = Game0.getAusgang()
			xy+=1

		b = max(spalte)
		return spalte.index(b)

class Game:
	def __init__(self,eigenefarbe,fremdefarbe,restzuege,spielfeld = [["w" for x in range(7)] for y in range(6)]):
		self.__eigeneSpielsteinfarbe = eigenefarbe
		self.__fremdeSpielsteinfarbe = fremdefarbe
		self.__Ausgang = ""
		self.__VierGewinntKlasse = viergewinntklasse(spielfeld,restzuege)
		self.KI_1 = KI(eigenefarbe,fremdefarbe)
		self.KI_2 = KI(fremdefarbe,eigenefarbe)

	def getAusgang(self):
		return self.__Ausgang

	def start(self):
		self.spielen()
		if self.__eigeneSpielsteinfarbe == "gr":
			if self.__VierGewinntKlasse.getSpielstandGelb() < self.__VierGewinntKlasse.getSpielstandGruen():
				self.__Ausgang = self.__VierGewinntKlasse.getSpielstandGruen()
				return True
			elif self.__VierGewinntKlasse.getSpielstandGelb() > self.__VierGewinntKlasse.getSpielstandGruen():
				return False
		elif self.__eigeneSpielsteinfarbe == "ge":
			if self.__VierGewinntKlasse.getSpielstandGelb() > self.__VierGewinntKlasse.getSpielstandGruen():
				self.__Ausgang = self.__VierGewinntKlasse.getSpielstandGruen()
				return True
			elif self.__VierGewinntKlasse.getSpielstandGelb() < self.__VierGewinntKlasse.getSpielstandGruen():
				return Falsealse


	def spielen(self):
		x = 0
		while x < 100:
			while self.__VierGewinntKlasse.getSpielbeendet() == False:
				if self.__VierGewinntKlasse.getRestSpielzüge() %2 == 0 and self.__VierGewinntKlasse.getSpielbeendet() == False:
					self.KI_1.setSpielfeld(self.__VierGewinntKlasse.getArray())
					self.__VierGewinntKlasse.setSpielzug(self.KI_1.Spielzuggenerieren())
					self.__VierGewinntKlasse.ausführen()

				if self.__VierGewinntKlasse.getRestSpielzüge() %2 == 1 and self.__VierGewinntKlasse.getSpielbeendet() == False:
					self.KI_2.setSpielfeld(self.__VierGewinntKlasse.getArray())
					self.__VierGewinntKlasse.setSpielzug(self.KI_2.Spielzuggenerieren())
					self.__VierGewinntKlasse.ausführen()
			self.__VierGewinntKlasse.neuesMatch()
			x+=1

