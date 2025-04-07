import random

class Domanda:
    def __init__(self, richiesta, livello, corretta, errate):
        self.richiesta=richiesta
        self.livello=int(livello)
        self.corretta=corretta
        self.errate=errate                   #si da per scontato che sia una lista --> viene creata in un passaggio successivo
        self.risposte= [corretta] + errate   #crea lista di corretta + lista (precedentemente creata) di errate
        random.shuffle(self.risposte)        #shuffle mischia le risposte

    def mostraDomanda(self):
        print(f"Livello {self.livello}) {self.richiesta}")
        for i in range(len(self.risposte)):
            print( f"     {i}. {self.risposte[i]}")

    def verificaRisposta(self, scelta):
        return self.corretta == self.risposte[scelta-1]

