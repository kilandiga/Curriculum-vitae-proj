class Opleiding:
    def __init__(self, school, richting, jaar, diploma):
        self.school = [school]
        self.richting = [jaar]
        self.jaar = [richting]
        self.diploma = [diploma]


class Werk:
    def __init__(self, werkgever, jaar_Begin, jaar_eind, job_inhoud, reden_vertrek):
        self.werkgever = werkgever
        self.jaar = jaar_Begin
        self.jaar_eind = jaar_eind
        self.job_inhoud = job_inhoud
        self.reden_vertrek = reden_vertrek


class Taal_vaardigheden:
    def __init__(self, Taal, Spreken, Schrijven, Lezen):
        self.Taal = [Taal]
        self.Spreken = [Spreken]
        self.Schrijven = [Schrijven]
        self.Lezen = [Lezen]

    def add_Taal (self, Taal):
        self.Taal.append(Taal)
    def add_Spreken(self, Spreken):
        self.Spreken.append(Spreken)
    def add_Schrijven(self, Schrijven):
        self.Schrijven.append(Schrijven)
    def add_Lezen(self, Lezen):
        self.Schrijven.append(Lezen)


class Computer_vaardigheden:
    def __init__(self, programma, vaardigheid):
        self.programma = programma
        self.vaardigheid = vaardigheid
