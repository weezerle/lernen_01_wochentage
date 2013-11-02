print "Weekdaypruefong"
print "Bitte eine Jahreszahl eingeben:"
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
        print "Tag des Herren"
    else:
        print "Tag der Erkenntnis"


def jahrestagessumme(tag,monat,jahr):
    anzahljahrestage=0
    for i in range(1900,jahr-1):
        if istSchaltjahr(i):
            anzahljahrestage+=365
        else:
            anzahljahrestage+=366
    return anzahljahrestage+jahrestag(tag,monat,jahr)

def jahrestag(tag,monat,jahr):
    return tag + monatstagesumme(tag,monat,jahr)
    
def monatstagesumme(tag,monat,jahr):
    print tag,'.',monat,'.',jahr
    anzahlmonatstage=0

    for i in range(monat-1):
#        print "egal", monatstage[i]
        anzahlmonatstage+=monatstage[i]

#    if monat > 2:
#        if istSchaltjahr(jahr):
#            anzahlmonatstage+=1
#    elif monat == 2 and tag == 29:
#        if istSchaltjahr(jahr):
#            anzahlmonatstage+=1
    if anzahlmonatstage >= 60:
        if istSchaltjahr(jahr):
            anzahlmonatstage+=1
    else:
        print "nix"

    return anzahlmonatstage


doof = 0
while doof == 0:
    try:
        testjahr = int(raw_input('> '))
        doof=1
    except ValueError:
        print "Bist Du zu doof fuer ne Zahl zu erkennen?"

print "Bitte eine Monat eingeben:"
doof = 0
while doof == 0:
    try:
        testmonat = int(raw_input('> '))
        doof=1
    except ValueError:
        print "Bist Du zu doof fuer ne Zahl zu erkennen?"

print "Bitte einen Tag (Zahl) eingeben:"
doof = 0
while doof == 0:
    try:
        testtag = int(raw_input('> '))
        doof=1
    except ValueError:
        print "Bist Du zu doof fuer ne Zahl zu erkennen?"

def istSchaltjahr(jahreszahl):
    if jahreszahl%4==0:
        if jahreszahl%100==0 and not jahreszahl%400==0:
            print jahreszahl, "ist kein Schaltjahr!"
            return False
        else:
            print jahreszahl, "ist ein Schaltjahr!"
            return True
    else:
        print jahreszahl, "sollte kein Schaltjahr sein."
        return False


# istSchaltjahr(testjahr)
print jahrestag(testtag, testmonat, testjahr)
bestimmung(jahrestagessumme(testtag, testmonat, testjahr))

# for tach in wochentage:
#    print tach
