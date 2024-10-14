import sqlite3
import mysql.connector
import mariadb
import sys


conn = mysql.connector.connect(
    host="10.2.2.122",
    user="root",
    password="admin123",
    database="telefonkatalog"
)


cursor = conn.cursor()


def printmeny():
    print("------------------- Telefonkatalog -------------------")
    print("| 1. Legg til ny person                              |")
    print("| 2. Søk opp person eller telefonnummer              |")
    print("| 3. Vis alle personer                               |")
    print("| 4. Slett lagret person                             |")
    print("| 5. Avslutt                                         |")
    print("------------------------------------------------------")
    menyvalg = input("Skriv inn tall for å velge fra menyen: ")
    utfoermenyvalg(menyvalg)


def utfoermenyvalg(valgttall):
    if valgttall == "1":
        registerperson()
    elif valgttall == "2":
        sokperson()
        printmeny()
    elif valgttall == "3":
        visallepersoner()
    elif valgttall == "4":
        velgslettperson()
    elif valgttall == "5":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if (bekreftelse == "J" or bekreftelse =="j"):
            conn.close()
            exit()
        else:
            printmeny()
    else:
        nyttforsoek = input("Ugyldig tall. Velg tall mellom 1-5: ")
        utfoermenyvalg(nyttforsoek)



def registerperson():
    fornavn = input("Skriv inn fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    telefonnummer = input("Skriv inn telefonnummer: ")
    legg_til_i_db(fornavn, etternavn, telefonnummer)
    
    print("{1} {2} er registrert med telefonnummer {3}"
          .format(fornavn, etternavn, telefonnummer))
    input("Trykk en tast for å gå tilbake til menyen")
    printmeny()


def legg_til_i_db(fornavn, etternavn, telefonnummer):
    cursor.execute("INSERT INTO personer (fornavn, etternavn, telefonnummer) VALUES (?, ?, ?)",
                   (fornavn, etternavn, telefonnummer))
    conn.commit()

    
def slett_fra_db(fornavn, etternavn, telefonnummer):
    cursor.execute("DELETE FROM personer WHERE fornavn=? AND etternavn=? AND telefonnummer=?",
                   (fornavn, etternavn, telefonnummer))
    conn.commit()
    print(fornavn + " " + etternavn + " med telefonnummer " + telefonnummer + " er slettet fra systemet")
    input("Trykk en tast for å fortsette")
    printmeny()
    


def visallepersoner():
    cursor.execute("SELECT * FROM personer")
    resultater = cursor.fetchall()
    if not resultater:
        print("Det er ingen registrerte personer i katalogen")
        input("Trykk en tast for å gå tilbake til menyen")
        printmeny()
    else:
        print("*******************************************"
            "*******************************************")
        for personer in resultater:
            print("* Fornavn: {:15s} Etternavn: {:15s} Telefonnummer: {:8s}"
                    .format(personer[1], personer[2], personer[3]))
        print("*******************************************"
                    "*******************************************")
        input("Trykk en tast for å gå tilbake til menyen")
        printmeny()

def sokperson():
    print("------------------------------------------")
    print("| 1. Søk på fornavn                      |")
    print("| 2. Søk på etternavn                    |")
    print("| 3. Søk på telefonnummer                |")
    print("| 4. Tilbake til hovedmeny               |")
    print("------------------------------------------")
    sokefelt = input("Velg ønsket søk 1-3, eller 4 for å gå tilbake: ")
    if sokefelt == "1":
        navn = input("Fornavn: ")
        finnperson("fornavn", navn)
    elif sokefelt == "2":
        navn = input("Etternavn: ")
        finnperson("etternavn", navn)
    elif sokefelt == "3":
        telefonnummer = input("Telefonnummer: ")
        finnperson("telefonnummer", telefonnummer)
    elif sokefelt == "4":
        printmeny()
    else:
        print("Ugyldig valg. Velg et tall mellom 1-4: ")
        sokperson()

def finnperson(typesok, soketekst):

    if typesok == "fornavn":
        cursor.execute("SELECT * FROM  personer WHERE fornavn=?", (soketekst,))
    elif typesok == "etternavn":
        cursor.execute("SELECT * FROM  personer WHERE etternavn=?", (soketekst,))
    elif typesok == "telefonnummer":
        cursor.execute("SELECT * FROM  personer WHERE telefonnummer=?", (soketekst,))
    
    resultater = cursor.fetchall()

    if not resultater:
        print("Finner ingen personer")
    else:
        for personer in resultater:
            print("{1} {2} har telefonnummer {3}"
                  .format(personer[1], personer[2], personer[3]))
        

def velgslettperson():
    print("****************************************")
    print("| 1. Skriv inn navn + etternavn        |")
    print("| 2. Skriv inn telefonnummer           |")
    print("| 3. Avbryt                            |")
    print("****************************************")
    valgttall = input("Skriv inn tall: ")
    if valgttall == "1":
        fornavn = input("Skriv inn fornavn: ")
        etternavn = input("Skriv inn etternavn: ")
        fullnavn = fornavn + " " + etternavn
        finnslettperson("fullnavn", fullnavn)
    elif valgttall == "2":
        tlf = input("Skriv inn telfonnummer: ")
        finnslettperson("tlf", tlf)
    elif valgttall == "3":
        printmeny()
    else:
        print("Ugyldig tall. Prøv igjen")
        input("Trykk en tast for å fortsette")
        velgslettperson()


def finnslettperson(typesok, soktekst):
    funnet = False
    cursor.execute("SELECT * FROM personer")
    allepersoner = cursor.fetchall()
    if typesok == "fullnavn":
        for personer in allepersoner:
            if personer[1] + " " + personer[2] == soktekst:
                navn = personer[1]
                etternavn = personer[2]
                tlf = personer[3]
                bekreftelse = input("Er du sikker på at du vil slette " + personer[1] + " " + personer[2] + " med telefonnummer " + personer[3] + "? J/N")
                if bekreftelse == "J" or bekreftelse == "j":
                    slett_fra_db(navn, etternavn, tlf)
                else:
                    velgslettperson()
                funnet = True
        if funnet == False:
            print("Fant ikke " + soktekst)
            input("Trykk en tast for å fortsette")
            velgslettperson()
            
    elif typesok == "tlf":
        for personer in allepersoner:
            if personer[3] == soktekst:
                navn = personer[1]
                etternavn = personer[2]
                tlf = personer[3]
                slett_fra_db(navn, etternavn, tlf)
                funnet = True
        if funnet == False:
            print("Fant ingen med telefonnummer " + soktekst)
            input("Trykk en tast for å fortsette")
            velgslettperson()

# def slettperson(navn, etternavn, tlf):
#     gammelttall = len(telefonkatalog)
#     person = [navn, etternavn, tlf]
#     bekreftelse = input("Er du sikker på at du vil slette " + navn + " " + etternavn + " med telefonnummer " + tlf + "? J/N: ")
#     if bekreftelse == "J" or bekreftelse == "j":
#         telefonkatalog.remove(person)
#         skriv_til_fil(fil)
#         if len(telefonkatalog) == gammelttall - 1:
#             print(navn + " " + etternavn + " er slettet fra systemet")
#             input("Trykk en tast for å fortsette")
#             printmeny()
#         else:
#             print("Noe gikk galt")
#     elif bekreftelse == "N" or bekreftelse == "n":
#         printmeny()
#     else:
#         print("Ugyldig bekreftelse, prøv på nytt")
#         slettperson(navn, etternavn, tlf)


printmeny()