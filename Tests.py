import tkinter as tk

#--------------------------------- testa jautājumi ------------------------------#
jautajumi = [
#--------------------------------- 1 ------------------------------#
    {
        "jautajums": "Kādi ir Python mainīgo definēšanas noteikumi?",
        "varianti": ["Jāsākas ar burtu vai ciparu.",
                    "Var saturēt tikai burtus, ciparus un pasvītrojumus.",
                    "Drīkst sākties ar ciparu.",
                    "Nedrīkst sakrist ar kādu no Python atslēgvārdiem."],
        "atbildes": {"Var saturēt tikai burtus, ciparus un pasvītrojumus.", "Nedrīkst sakrist ar kādu no Python atslēgvārdiem."}
    },
#--------------------------------- 2 ------------------------------#
     {
        "jautajums": "Kādas (Case) metodes izmanto mainīgo definēšanai Python valodā?",
        "varianti": ["Pascal Case.",
                    "Kebab case.",
                    "Middot case.",
                    "Snake Case."],
        "atbildes": {"Pascal Case.", "Snake Case."}
    },
#--------------------------------- 3 ------------------------------#
     {
        "jautajums": "Kuri ir patiesi apgalvojumi par Python mainīgo veidiem?",
        "varianti": ["Visi ārpus funkcijas deklarētie mainīgie ir globālie mainīgie.",
                    "Python nodrošina atslēgvārdu “local”, lai funkcijas iekšpusē izmantotu lokālo mainīgo.",
                    "Visi ārpus funkcijas deklarētie mainīgie ir lokālie mainīgie.",
                    "Globālos mainīgos var izmantot gan funkcijas iekšpusē, gan ārpusē."],
        "atbildes": {"Visi ārpus funkcijas deklarētie mainīgie ir globālie mainīgie.", "Globālos mainīgos var izmantot gan funkcijas iekšpusē, gan ārpusē."}
    },
#--------------------------------- 4 ------------------------------#
     {
        "jautajums": "Nosaki pareizos datu tipu piešķiršanas pierakstus.",
        "varianti": ["Boolean x = False",
                    "x = set((“viens”, “divi”, “trīs”))",
                    "x = b“Sveiki!”",
                    "x = list((“viens”, “divi”, “trīs”))"],
        "atbildes": {"x = set((“viens”, “divi”, “trīs”))", "x = b“Sveiki!”", "x = list((“viens”, “divi”, “trīs”))"}
    },
#--------------------------------- 5 ------------------------------#
     {
        "jautajums": "Kuriem Python atslēgvārdiem un/vai funkcijām ir pareizs pieraksts?",
        "varianti": ["print[]",
                    "type()",
                    "del()",
                    "del"],
        "atbildes": {"type()", "del"}
    },
#--------------------------------- 6 ------------------------------#
     {
        "jautajums": "Kuri ir patiesi liegumi par mainīgajiem Python programmēšanas valodā?",
        "varianti": ["Mainīgie ir jādeklarē ar konkrētu tipu, un to tips nevar mainīties pēc iestatīšanas.",
                    "Python valodā ir komandas mainīgā deklarēšanai.",
                    "Mainīgais tiek izveidots brīdī, kad tam pirmo reizi piešķir vērtību.",
                    "Mainīgais ir identifikators un tiek izmantots vērtības saglabāšanai."],
        "atbildes": {"Mainīgais tiek izveidots brīdī, kad tam pirmo reizi piešķir vērtību.", "Mainīgais ir identifikators un tiek izmantots vērtības saglabāšanai."}
    },
#--------------------------------- 7 ------------------------------#
     {
        "jautajums": "Izvēlies patiesos apgalvojumus par mainīgo izvadīšanu.",
        "varianti": ["Ja ar print() mēģina izvadīt dažādu tipu mainīgos izmantojot operatoru (+), Python parādīs kļūdu.",
                    "Skaitļiem rakstzīme (+) darbojas kā matemātiskais operators.",
                    "Ar print() var izvadīt dažādu tipa mainīgos, ja atdala tos ar komatu.",
                    "Nevar izmantot operatoru (+), lai izvadītu vairākus mainīgos."],
        "atbildes": {"Ja ar print() mēģina izvadīt dažādu tipu mainīgos izmantojot operatoru (+), Python parādīs kļūdu.", "Skaitļiem rakstzīme (+) darbojas kā matemātiskais operators.", "Ar print() var izvadīt dažādu tipa mainīgos, ja atdala tos ar komatu."}
    },
#--------------------------------- 8 ------------------------------#
     {
        "jautajums": "Atzīme pareizi piederošos atslēgvārdus konkrētajam datu tipam.",
        "varianti": ["Kartēšanas tipi: set, frozenset",
                    "Kopas tips: dict",
                    "Binārie tipi: bytes, bytearray, memoryview",
                    "Tukšuma tips: NoneType"],
        "atbildes": {"Binārie tipi: bytes, bytearray, memoryview", "Tukšuma tips: NoneType"}
    },
#--------------------------------- 9 ------------------------------#
    {
        "jautajums": "Kuros variantos ir pareizi paziņots par iegūto datu tipu?",
        "varianti": ["<class (int)>",
                    "<class 'complex'>",
                    "<class (str)>",
                    "<class 'frozenset'>"],
        "atbildes": {"<class 'complex'>", "<class 'frozenset'>"}
    },
#--------------------------------- 10 ------------------------------#
    {
        "jautajums": "Kuri ir pareizi nosacījumi par Python mainīgo vērtību piešķiršanu?",
        "varianti": ["Var piešķirt vienu un to pašu vērtību vairākiem mainīgajiem vienā rindā.",
                    "Mainīgajiem var tikai piešķirt vērtības atsevišķi katrā rindā.",
                    "Python ļauj piešķirt vairākas vērtības vairākiem mainīgajiem vienā rindā.",
                    "Mainīgajiem nevar piešķirt vairākas vērtības vienā rindā."],
        "atbildes": {"Var piešķirt vienu un to pašu vērtību vairākiem mainīgajiem vienā rindā.", "Python ļauj piešķirt vairākas vērtības vairākiem mainīgajiem vienā rindā."}
    }
]

#--------------------------------- programmas logs ------------------------------#
root = tk.Tk()
root.title("Elektroniskais tests")
root.geometry("800x450")  
root.resizable(False, False) 
root.configure(bg='#EEEEEE')

# Krāsas un fonti
BG_KRASA    = "#F0F0F0"
POGA_BG      = "#D9D9D9"
POGA_FG      = "#333333"
VIRSRAKSTS_FG    = "#004466"
FONTS_VIRSRAKSTS  = ('Verdana', 20, 'bold')
FONTS_POGA    = ('Verdana', 12, 'bold')
FONTS_JAUT  = ('Verdana', 14, 'bold')

root.mainloop()
