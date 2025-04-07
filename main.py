import random
from operator import attrgetter


class Domanda:
    def __init__(self, testo, livello, corretta, sbagliata1, sbagliata2, sbagliata3):
        self.testo = testo
        self.livello = livello
        self.corretta = corretta
        self.sbagliata1 = sbagliata1
        self.sbagliata2 = sbagliata2
        self.sbagliata3 = sbagliata3

class Player:
    def __init__(self, nickname, punteggio):
        self.nickname = nickname
        self.punteggio = punteggio

class Game:
    def __init__(self, listaDomande):
        self.listaDomande = listaDomande

    def gioco(self):
        livelloMax=0

        for domanda in listaDomande: #perchè self.listsDomande???
            if int(domanda.livello) > livelloMax:
                livelloMax = int(domanda.livello)

        livelloAttuale=0
        for i in range(0, livelloMax+1): #da livello 0 e si ferma raggiunto il livelloMax
            listaDomandeLivelloAttuale = self.getListaDomandeLivelloAttuale(livelloAttuale)
            random.shuffle(listaDomandeLivelloAttuale)

            listaRisposte=[domanda.corretta, domanda.sbagliata1, domanda.sbagliata2, domanda.sbagliata3]
            random.shuffle(listaRisposte)

            print(f"Livello {livelloAttuale}) {domanda.testo}")
            cnt=1
            for risposta in listaRisposte:
                print(f"    {cnt} {risposta}")
                cnt+=1

            rispostaInserita = int(input("Inserire una risposta: "))

            indexCorretta= listaRisposte.index(domanda.corretta)
            if rispostaInserita == indexCorretta+1:
                print(f"Risposta corretta!\n")
                livelloAttuale+=1
                continue
            else:
                print(f"Risposta sbagliata! La risposta corretta era: {indexCorretta+1}\n")
                print(f"Hai totalizzato {livelloAttuale} punti! \n")
                nickname = input("Inserisci il tuo nickname: ")
                return nickname, livelloAttuale

        print(f"Hai totalizzato {livelloAttuale} punti! \n")
        nickname = input("Inserisci il tuo nickname: ")
        return nickname, livelloAttuale


    def getListaDomandeLivelloAttuale(self, livelloAttuale):
        lista=[]
        for domanda in listaDomande:
            if domanda.livello==livelloAttuale:
                lista.append(domanda)
        return lista

listaDomande=[]
listaGiocatori=[]
nomefile="domande.txt"
file=open(nomefile,"r", encoding="utf-8")

cnt=1
for line in file:
    if line=="":
        raise IOError

    if cnt==7:
        cnt=1
        continue

    if cnt==1:
        testo=line.strip()
    elif cnt==2:
        livello=line.strip()
    elif cnt==3:
        corretta=line.strip()
    elif cnt==4:
        sbagliata1=line.strip()
    elif cnt==5:
        sbagliata2=line.strip()
    elif cnt==6:
        sbagliata3=line.strip()

    domanda=Domanda(testo, livello, corretta, sbagliata1, sbagliata2, sbagliata3)
    listaDomande.append(domanda)
    cnt+=1
file.close()

scelta=input("\nVuoi giocare?")
if scelta=="si":
    game = Game(listaDomande)
    (nickname, punti) = game.gioco()
    print(f"Bravo {nickname}, hai totalizzato {punti} punti!\n")
    player = Player(nickname, int(punti))
    esiste=False

    for p in listaGiocatori:
        if p.nickname==player.nickname:
            esiste=True
            p.punteggio=punti

    if not esiste:
        listaGiocatori.append(player)

    listaGiocatoriOrdinata = sorted( listaGiocatori, key=attrgetter("punteggio"), reverse=True)
    fileScritto = open("punti.txt","w", encoding="utf-8")
    for giorcatore in listaGiocatoriOrdinata:
        fileScritto.write( giorcatore.nickname + " " + str(giorcatore.punteggio) + "\n")

else:
    print("Gioco terminato!")




