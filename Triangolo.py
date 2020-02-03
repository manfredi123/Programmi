import math
from math import *
def triangolo(lato1 = 0, lato2 = 0, lato3 = 0, alpha = 0, beta = 0, gamma = 0):

    print("Inserisci i dati che hai di un triangolo per trovare il perimetro")
    print("  LEGENDA")
    print("-----------\n")
    print("lato1 = il lato di sotto\nlato2 = il lato a destra\nlato3 = il lato a sinistra\nalpha = l'angolo in basso a sinistra\nbeta = l'angolo in basso a destra\ngamma = l'angolo in alto")
    print("Ricorda di inserire gli angoli in gradi\n\n")
    dati = []#Ogni dato viene inserito in questa lista

    while len(dati) != 3:#Quando la lista contiene 3 elementi il codice dentro while si ferma

        selezionelato = input("Inserisci l per lato, a per angolo\n")#lato o angolo

        if selezionelato == "l":
            lato = int(input("Lato 1, 2, 3? Attenzione se selezioni due volte lo stesso lato andrai a cancellare il dato precedente\n"))
                  # int --> l'input deve essere un numero senza virgola quindi 1 o 2 o 3
            if lato == 1:#se preme 1
                L1 = float(input("Che lunghezza per il lato 1:?\n"))#float --> la lunghezza è un numero con o senza virgola
                lato1 += L1 #Sommo a lato 1 la lunghezza L1 inserita dall'utente
                dati.append("lato1" + str(lato1))#E aggiungo alla lista il dato inserito

            if lato == 2: #Se preme 2
                L2 = float(input("Che lunghezza per il lato 2:?\n"))
                lato2 += L2
                dati.append("lato2" + str(lato2))

            if lato == 3:#Se preme 3
                L3 = float(input("Che lunghezza per il lato 3:?\n"))
                lato3 += L3
                dati.append("lato3" + str(lato3))

        elif selezionelato == "a":#Se sceglie a quindi angolo

            angolo = input("Alpha, Beta, Gamma\n?")#Quale angolo

            if angolo == "Alpha" or angolo == "alpha": #Se sceglie alpha
                A = float(input("Che ampiezza per l'angolo Alpha:\n?"))#Quale ampiezza in gradi?
                alpha += radians(A)#Aggiungo ad alpha il valore che inserisce l'utente convertito in radianti (asin e acos prendono i dati in radianti non in gradi)
                dati.append("Alpha" + str(alpha))#Aggiungo alla lista il dato inserito

            if angolo == "Beta" or angolo == "beta":#Se sceglie beta
                B = float(input("Che ampiezza per l'angolo Beta:\n?"))
                beta += radians(B)
                dati.append("Beta" + str(beta))

            if angolo == "Gamma" or angolo == "gamma":#Se sceglie gamma
                G = float(input("Che ampiezza per l'angolo Gamma:\n?"))
                gamma += radians(G)
                dati.append("Gamma" + str(gamma))
            #Appena ci saranno 3 dati dentro la lista "dati" il codice sopra smette di funzionare
        #E il programma inizia a controllare quale dato è diverso da 0(quindi quale dato è stato inserito)
        if lato1 != 0 and alpha != 0 and beta != 0:
            gamma += 180 - degrees(alpha) - degrees(beta)
            lato2 += (lato1 / sin(gamma)) * sin(alpha)
            lato3 += (lato2 / sin(alpha)) * sin(beta)
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2)) #Round serve ad arrotondare, il numero accanto dice quanti numeri dopo la virgola vogliamo

        elif lato1 != 0 and alpha != 0 and gamma != 0:
            beta += 180 - degrees(alpha) - degrees(gamma)
            lato2 += (lato1 / sin(gamma)) * sin(alpha)
            lato3 += (lato1 / sin(gamma)) * sin(beta)
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato1 != 0 and beta != 0 and gamma != 0:
            alpha += 180 - degrees(beta) - degrees(gamma)
            lato2 += (lato1 / sin(gamma)) * sin(alpha)
            lato3 += (lato1 / sin(gamma)) * sin(beta)
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato2 != 0 and alpha != 0 and beta != 0:
            gamma += 180 - degrees(alpha) - degrees(beta)
            lato1 += (lato2 / sin(alpha)) * sin(gamma)
            lato3 += (lato1 / sin(gamma)) * sin(beta)
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato2 != 0 and alpha != 0 and gamma != 0:
            beta += 180 - degrees(alpha) - degrees(gamma)
            lato1 += (lato2 / sin(alpha)) * sin(gamma)
            lato3 += (lato1 / sin(gamma)) * sin(beta)
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato2 != 0 and beta != 0 and gamma != 0:
            alpha += 180 - degrees(beta) - degrees(gamma)
            lato1 += (lato2 / sin(alpha)) * sin(gamma)
            lato3 += (lato1 / sin(gamma)) * sin(beta)
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato3 != 0 and alpha != 0 and beta != 0:
            gamma += 180 - degrees(alpha) - degrees(beta)
            lato1 += (lato3 / sin(beta)) * sin(gamma)
            lato2 += (lato1 / sin(gamma)) * sin(alpha)
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato3 != 0 and alpha != 0 and gamma != 0:
            beta += 180 - degrees(alpha) - degrees(gamma)
            lato1 += (lato3 / sin(beta)) * sin(gamma)
            lato2 += (lato1 / sin(gamma)) * sin(alpha)
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato3 != 0 and beta != 0 and gamma != 0:
            alpha += 180 - degrees(gamma) - degrees(beta)
            lato1 += (lato3 / sin(beta)) * sin(gamma)
            lato2 += (lato1 / sin(gamma)) * sin(alpha)
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro, 2))

        elif lato1 != 0 and lato2 != 0 and alpha != 0:#carnot #GIUSTO
            sgamma = (sin(alpha) / lato2) * lato1
            gamma += asin(sgamma)
            beta += 180 - degrees(gamma) - degrees(alpha)
            lato3 += sqrt(lato1 ** 2 + lato2 ** 2 - 2*(lato1 * lato2 * cos(beta)))#sqrt è la radice quadrata
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro, 2))

        elif lato1 != 0 and lato2 != 0 and beta != 0:
            lato3 += sqrt(lato1 ** 2 + lato2 ** 2 - 2*(lato1 * lato2 * cos(beta)))
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato1 != 0 and lato2 != 0 and gamma != 0:#??
            salfa = (sin(gamma) / lato1) * lato2
            alpha += asin(salfa)
            beta += 180 - degrees(gamma) - degrees(alpha)
            lato3 += sqrt(lato1 ** 2 + lato2 ** 2 - 2*(lato1 * lato2 * cos(beta)))
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato1 != 0 and lato3 != 0 and alpha != 0:
            lato2 += sqrt(lato1 ** 2 + lato3 ** 2 - 2*(lato1 * lato3 * cos(alpha)))
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato1 != 0 and lato3 != 0 and beta != 0:#??
            sgamma = (sin(beta) / lato3) * lato1
            gamma += asin(sgamma)
            alpha += 180 - degrees(beta) - degrees(gamma)
            lato2 += (lato3 / sin(beta)) * sin(alpha)
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato1 != 0 and lato3 != 0 and gamma != 0:#??
            sbeta = (sin(gamma) / lato1) * lato3
            print(sbeta)
            beta += asin(sbeta)
            alpha += 180 - degrees(gamma) - degrees(beta)
            lato2 += sqrt(lato1 ** 2 + lato3 ** 2 - 2*(lato1 * lato3 * cos(alpha)))
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato2 != 0 and lato3 != 0 and alpha != 0:#??
            sbeta = (sin(alpha) / lato2) * lato3
            beta += asin(sbeta)
            gamma += 180 - degrees(alpha) - degrees(beta)
            lato1 += (lato2 / sin(alpha)) * sin(gamma)
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato2 != 0 and lato3 != 0 and beta != 0:#??
            salfa = (sin(beta) / lato3) * lato2
            alpha += asin(salfa)
            gamma += 180 - degrees(alpha) - degrees(beta)
            lato1 += sqrt(lato2 ** 2 + lato3 ** 2 - 2*(lato2 * lato3 * cos(gamma)))
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato2 != 0 and lato3 != 0 and gamma != 0:
            lato1 += sqrt(lato2 ** 2 + lato3 ** 2 - 2 * (lato2 * lato3 * cos(gamma)))
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif lato1 != 0 and lato2 != 0 and lato3 != 0:
            perimetro = lato1 + lato2 + lato3
            return "Il perimetro è: {}".format(round(perimetro,2))

        elif alpha != 0 and beta != 0 and gamma != 0:
            return "Con questi dati non posso calcolare il perimetro. Inserisci almeno un lato"



#asin = Return the arc sine of x, in radians.
#acos = Return the arc cosine of x, in radians

print(triangolo())