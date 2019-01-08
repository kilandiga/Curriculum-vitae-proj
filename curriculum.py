from curriculumClasses import Opleiding
from curriculumClasses import Werk
from curriculumClasses import Computer_vaardigheden
from curriculumClasses import Taal_vaardigheden
from turtle import *
from tkinter import *
from datetime import date

def Bedankt():
    print("bedankt voor de interesse")

#opleidingen
School = ["BEHAALD AAN","staat", "Karel De Grote Hogeschool", "Pito Stabroek", "Pito Stabroek"]
Jaren = [2013, 2012, 2009, 2009]
Richtingen = ["RICHTINGEN", "Bedrijfsbeheer", "Informaticabeheer", "VCA", "Mechanische Vormgevingstechnieken"]
Diplomas = ["BEHAALD OF NIET 1/0", True, False, True, True]
#Werkplaatsen

Werkervaring1 = Werk("G4S", 2015, "heden", "Technieker ademlucht, Chauffeur, Installateur mobiele camera systemen",
                     "Te weinig uitdaging en ben hier nog steeds bezig")
Werkervaring2 = Werk("DnD Computers", 2014, 2015, "Magazijn Beheerder", "Was te ver voor elke dag te doen")
Werkervaring3 = Werk("Ergo Pro (bijberoep)", 2013, 2015, "Begeleider van commerciële teams in de financiële sector",
                     "Te weinig tijd")
Werkervaring4 = Werk("VF Europe", 2013, 2013, "Magazijn medewerker", "Einde contract")
Werkervaring5 = Werk("De Ronde en Drubbel", 2011, 2012, "Onderhoudstechnieker Vorkliften", "Verlies grote klant")
Werkervaring6 = Werk("Case New Holland", 2011, 2011, "CNC machine Operator", "Niet wat ik er van had verwacht")
Werkervaring7 = Werk("Hessen Natie", 2010, 2011, "Magazijn Medewerker BASF V-Project",
                     "Einde V-Project + einde contract hessen natie met BASF")
Werkervaring8 = Werk("Voith ermo", 2009, 2010, "Flensmonteur", "Veel thuisgezeten wegens einde projecten")

#Computer vaardigheden
Vaardigheid1 = Computer_vaardigheden("Word", "Zeer goed")
Vaardigheid2 = Computer_vaardigheden("Excel", "goed")
Vaardigheid3 = Computer_vaardigheden("PowerPoint", "goed")
Vaardigheid4 = Computer_vaardigheden("Autocad", "goed")
Vaardigheid5 = Computer_vaardigheden("Outlook", "goed")
Vaardigheid6 = Computer_vaardigheden("CNC", "goed")
Vaardigheid7 = Computer_vaardigheden("SQL", "Basis")
Vaardigheid8 = Computer_vaardigheden("Java", "Basis")
Vaardigheid9 = Computer_vaardigheden("Javascript", "Basis")
Vaardigheid10 = Computer_vaardigheden("Python", "Basis")
Vaardigheid11 = Computer_vaardigheden("CCNA", "Basis")

#TaalVaardigheden
Taal_vaardigheden.Taal = ["+Nederlands (moedertaal)+", "+--------Engels-------+", "+--------Frans--------+",
                               "+--------Duits--------+"]
Taal_vaardigheden.Spreken = ["+-------Vloeiend-------+", "+------Zeer goed------+", "+--------Goed---------+",
                               "+-------Voldoende------+", "+--------Matig--------+", "+-------Noties--------+"]
Taal_vaardigheden.Schrijven = ["+-------Vloeiend-------+", "+------Zeer goed------+", "+--------Goed---------+",
                               "+-------Voldoende------+", "+--------Matig--------+", "+-------Noties--------+"]
Taal_vaardigheden.Lezen = ["+-------Vloeiend-------+", "+------Zeer goed------+", "+--------Goed---------+",
                               "+-------Voldoende------+", "+--------Matig--------+", "+-------Noties--------+"]

GeboorteDatum = date(1989, 12, 9)
Vandaag = date.today()
Jaren = date.today().year - GeboorteDatum.year - ((Vandaag.month, Vandaag.day) <
                                                  (GeboorteDatum.month, GeboorteDatum.day))

Naam = "Naam = Vlegels Mike"
Leeftijd = ("Leeftijd =" + str(Jaren))
Adres = "Adres = Gillis Damaesstraat 70"
GSM = "GSM : 0471201945"
E_Mail = "E-mail = vlegels.mike@gmail.com"
Geboorte = "Geboortedatum = 09 December 1989 (Ekeren)"
Nationaliteit = "Nationaliteit = Belg"
Rijbewijs = "Rijbewijs = B, Vorklift, C"
Hobbys = {"Coach Softball team", "Softball speler 1ste klas", "Gaming in team verband", "medewerker Tempo Happening"}
