## Welcher Wochentag?
#

wochentage = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
monatstage = [31,28,31,30,31,30,31,31,30,31,30,31]

def bestimmung(anzahl):
    if anzahl%7 == 1:
        print "Montag"
    elif anzahl%7 == 2:
        print "Dienstag"
    elif anzahl%7 == 3:
        print "Mittwoch"
    elif anzahl%7 == 4:
        print "Donnerstag"
    elif anzahl%7 == 5:
        print "Freitag"
    elif anzahl%7 == 6:
        print "Samstag"
    elif anzahl%7 == 0:
        print "Sonntag"
    else:
        print "Das darf nicht sein."

def jahrestagessumme(tag,monat,jahr):
    anzahljahrestage=0
    for i in range(1900,jahr-1):
        if istSchaltjahr(i):
            anzahljahrestage+=365
        else:
            anzahljahrestage+=366
    return anzahljahrestage+tag+monatstagesumme(tag,monat,jahr)
    #return anzahljahrestage+jahrestag(tag,monat,jahr)

"""
def jahrestag(tag,monat,jahr):
    return tag + monatstagesumme(tag,monat,jahr)
"""

def monatstagesumme(tag,monat,jahr):
    #print tag,'.',monat,'.',jahr
    anzahlmonatstage=0

    for i in range(monat-1):
        anzahlmonatstage+=monatstage[i]
    if anzahlmonatstage >= 60:
        if istSchaltjahr(jahr):
            anzahlmonatstage+=1
    return anzahlmonatstage


## Ueberpruefung ob Schaltjhr oder nicht

def istSchaltjahr(jahreszahl):
    if jahreszahl%4==0:
        if jahreszahl%100==0 and not jahreszahl%400==0:
            # print jahreszahl, "ist kein Schaltjahr!"
            return False
        else:
            # print jahreszahl, "ist ein Schaltjahr!"
            return True
    else:
        # print jahreszahl, "sollte kein Schaltjahr sein."
        return False


## Hier wird das zu pruefende Datum abgefragt

print "Bitte eine Jahreszahl eingeben:"
doof = 0
while doof == 0:
    try:
        testjahr = int(raw_input('> '))
        doof=1
    except ValueError:
        print "Bitte eine Jahreszahl eingeben."

print "Bitte eine Monat eingeben:"
doof = 0
while doof == 0:
    try:
        testmonat = int(raw_input('> '))
        doof=1
    except ValueError:
        print "Bitte eine Monatszahl eingeben."

print "Bitte einen Tag (Zahl) eingeben:"
doof = 0
while doof == 0:
    try:
        testtag = int(raw_input('> '))
        doof=1
    except ValueError:
        print "Bitte eine Tageszahl eingeben."

## Hier werden dann die obigen Funktionen aufgerufen

print "Summe vor Bestimmung:", jahrestagessumme(testtag, testmonat, testjahr)
bestimmung(jahrestagessumme(testtag, testmonat, testjahr))
print "Werte:", testtag, testmonat, testjahr

