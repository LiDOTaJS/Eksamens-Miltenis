import random
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

jaut_kopa = 10  # kopējais jautājumu skaits

#--------------------------------- globālie mainīgie ------------------------------#
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

# Nejauša jautājumu secība un skaitītāji
jaut_seciba = random.sample(range(len(jautajumi)), jaut_kopa)
jaut_indekss = 0
pirmo_reizi = True
pareiz_pirmaja_reiz = 0

# --------------------------------- rāmju pārejas funkcija---------------------------------
def parad_logu(frame):
    #Parāda tikai izvēlēto rāmi.
    for f in (sakuma_logs, jaut_logs, rezultatu_logs):
        f.pack_forget()
    frame.pack(fill='both', expand=True)

# --------------------------------- pogu funkcijas ---------------------------------
def aizvert_prog():
    #Aizver programmu.
    root.destroy()

def ielade_jaut():
    #Atjauno jautājuma tekstu un pārveido opciju secību.
    global tagad_opcijas, mainigo_saraksts

    # noņem iepriekšējās pārbaudes pogas
    for logriks in jaut_logs.winfo_children():
        if isinstance(logriks, tk.Checkbutton):
            logriks.destroy()

    data = jautajumi[jaut_seciba[jaut_indekss]]
    jaut_virsraksts.config(text=f"{jaut_indekss+1}. {data['jautajums']}")

    # sajauc opcijas un izveido jaunas
    tagad_opcijas = data["varianti"].copy()
    random.shuffle(tagad_opcijas)
    mainigo_saraksts = []
    for opcijas in tagad_opcijas:
        mainigais = tk.IntVar()
        parbaude = tk.Checkbutton(jaut_logs, text=opcijas, variable=mainigais,
                             font=('Verdana', 12), bg=BG_KRASA)
        parbaude.pack(anchor='w', padx=40, pady=3)
        mainigo_saraksts.append(mainigais)

    pazinojums.config(text="")    

def sakt_testu():
    #Inicializē un sāk jaunu izstrādātu testu.
    global jaut_indekss, pirmo_reizi, pareiz_pirmaja_reiz, jaut_seciba
    jaut_indekss = 0
    pirmo_reizi = True
    pareiz_pirmaja_reiz = 0
    jaut_seciba = random.sample(range(len(jautajumi)), jaut_kopa)
    ielade_jaut()
    parad_logu(jaut_logs)

def nakamais_jaut():
    #Ielādē nākamo jautājumu vai beidz testu, rādot rezultātu.
    global jaut_indekss, pirmo_reizi
    jaut_indekss += 1
    if jaut_indekss < jaut_kopa:
        pirmo_reizi = True
        pazinojums.config(text="")
        ielade_jaut()
    else:
        parad_rezultatu()

def parad_rezultatu():
    #Rāda rezultātu logu ar pareizo atbilžu skaitu.
    rezultatu_teksts.config(
        text=f"No {jaut_kopa} jautājumiem, tu {pareiz_pirmaja_reiz} atbildēji pareizi ar pirmo reizi.")
    parad_logu(rezultatu_logs)

# --------------------------------- Sākuma izvēlne ---------------------------------
sakuma_logs = tk.Frame(root, bg=BG_KRASA)
virsraksts = tk.Label(sakuma_logs,
                       text="Elektroniskais tests\n\nMainīgie, datu tipi, pamatdarbības ar tiem \nPython programmēšanas valodā",
                       font=FONTS_VIRSRAKSTS, fg=VIRSRAKSTS_FG, bg=BG_KRASA, justify="center")
virsraksts.pack(pady=(60,20))

poga_sakt = tk.Button(sakuma_logs, text="Sākt", width=20, height=2,
                      bg=POGA_BG, fg=POGA_FG, font=FONTS_POGA, command=sakt_testu)
poga_sakt.pack(pady=10)
poga_apturet = tk.Button(sakuma_logs, text="Iziet", width=20, height=2,
                     bg=POGA_BG, fg=POGA_FG, font=FONTS_POGA, command=aizvert_prog)
poga_apturet.pack()

# --------------------------------- Jautājumu logs ---------------------------------
jaut_logs = tk.Frame(root, bg=BG_KRASA)
jaut_virsraksts = tk.Label(jaut_logs, text="", font=FONTS_JAUT,
                          fg=VIRSRAKSTS_FG, bg=BG_KRASA, wraplength=700, justify="left")
jaut_virsraksts.pack(pady=20)

apstiprinat_poga = tk.Button(jaut_logs, text="Apstiprināt", width=15, height=1,
                       bg=POGA_BG, fg=POGA_FG, font=FONTS_POGA)
apstiprinat_poga.pack(pady=10)

pazinojums = tk.Label(jaut_logs, text="", font=('Verdana', 12),
                          fg="red", bg=BG_KRASA)
pazinojums.pack(pady=5)

# --------------------------------- Rezultātu logs ---------------------------------
rezultatu_logs = tk.Frame(root, bg=BG_KRASA)
rezultatu_teksts = tk.Label(rezultatu_logs, text="", font=FONTS_JAUT,
                       fg=VIRSRAKSTS_FG, bg=BG_KRASA)
rezultatu_teksts.pack(pady=40)

poga_uz_sakumu = tk.Button(rezultatu_logs, text="Atgriezties uz sākumu", width=20, height=2,
                     bg=POGA_BG, fg=POGA_FG, font=FONTS_POGA)
poga_uz_sakumu.pack()

# --------------------------------- Programmas palaišana ---------------------------------
parad_logu(sakuma_logs)
root.mainloop()
