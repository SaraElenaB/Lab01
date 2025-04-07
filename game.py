import random

from domanda import Domanda

class Player:
    def __init__(self, nickname):
        self.nickname=nickname
        self.punteggio=0

    def incrementa_punteggio(self):
        self.punteggio+=1

    def __str__(self):
        return f"{self.nickname} {self.punteggio}"

#-------------------------------------------------------------------------------------------------------------
def carica_domande(file):
    domande={}    #dizionario: associa ad una chiave i suoi valori

    with open(file, "r", encoding="utf.8") as f:
        tutte_righe = f.readlines()   #leggi tutte le righe e le salvi in una lista
        righe=[]
        for riga in tutte_righe:
            riga_pulita = riga.strip()  #rimuovi spazi vuoti e newline()
            if riga_pulita:
                righe.append(riga_pulita)

    for i in range( 0, len(righe), 6):
        domanda = Domanda( righe[i], righe[i+1], righe[i+2], righe[i+3 : i+6]  ) #da : a
        #ancora nessuna domanda per quel livello
        if domanda.livello not in domande:
            domande[domanda.livello]=[]
        domande[domanda.livello].append(domanda)

    return domande

#-------------------------------------------------------------------------------------------------------------
class Game:
    def __init__(self, domande):
        self.domande=domande    #dizionario con domande per livello
        self.livello=0          #livello iniziale
        self.giocatore=None     #inizializzato durante il gioco

    def gioco(self):
        while self.livello in self.domande:
            domanda = random.choice(self.domande[self.livello])
            if not self.ch

