from tkinter import *
from fonctionRemplissage import *
from fonctionEcriture import *
from tkinter import messagebox
import os

def majIndex():

    if(cliked.get() == "ARP" or cliked.get() == "SCO"
            or cliked.get() == "1SM" or cliked.get() == "VME" or cliked.get() == "CGR" or cliked.get() == "ALA"
            or cliked.get() == "NS2" or cliked.get() == "AEV" or cliked.get() == "VPT"):
        if validationChamps1(entreeTag.get(), entreeSign.get(), entreeCom.get())== False:
            return False

        if verificationDoublon(entreeTag.get().upper()) == False:
            messagebox.showerror('erreur de libelle', 'le libelle est déja utilisé')

        # elif validationEcriture(cliked.get(), entreeSign.get(), entreeCom.get()) == False:
        #     messagebox.showerror('erreur adressage', 'Concatenation d adresses')
        else:
            tag = entreeTag.get()
            if cliked.get() == "ARP":
                indexARP = remplissageARP(tag.upper(), entreeSign.get(), entreeCom.get())
                saveText(indexARP)

            elif cliked.get() == "SCO":
                indexSCO = remplissageSCO(tag.upper(), entreeSign.get(), entreeCom.get())
                saveText(indexSCO)

            elif cliked.get() == "1SM":
                index1SM = remplissage1SM(tag.upper(), entreeSign.get(), entreeCom.get())
                saveText(index1SM)

            elif cliked.get() == "VME":
                indexVME = remplissageVME(tag.upper(), entreeSign.get(), entreeCom.get())
                saveText(indexVME)

            elif cliked.get() == "VPT":
                indexVPT = remplissageVPT(tag.upper(), entreeSign.get(), entreeCom.get())
                saveText(indexVPT)

            elif cliked.get() == "CGR":
                indexCGR = remplissageCGR(tag.upper(), entreeSign.get(), entreeCom.get())
                saveText(indexCGR)

            elif cliked.get() == "ALA":
                indexALA = remplissageALA(tag.upper(), entreeSign.get(), entreeCom.get())
                saveText(indexALA)

            elif cliked.get() == "NS2":
                indexNS2 = remplissageNS2(tag.upper(), entreeSign.get(), entreeCom.get())
                saveText(indexNS2)

            elif cliked.get() == "AEV":
                indexAEV = remplissageAEV(tag.upper(), entreeSign.get(), entreeCom.get())
                saveText(indexAEV)

            saveExcel(cliked.get(), tag.upper(), entreeSign.get(), entreeCom.get())
            entreeTag.delete("0", "end")
            entreeSign.delete("0", "end")
            entreeCom.delete("0", "end")

    elif cliked.get() == "MA" or cliked.get() == "MT" or cliked.get() == "VMA" or cliked.get() == "TOR":
        if validationChamps2(entreeTag.get(), entreeSign.get()) == False:
            return False

        if verificationDoublon(entreeTag.get().upper()) == False:
            messagebox.showerror('erreur de libelle', 'le libelle est déja utilisé')

        # elif validationEcriture(cliked.get(), entreeSign.get(),"") == False:
        #     messagebox.showerror('erreur adressage', 'Concatenation d adresses')

        else:
            tag = entreeTag.get()
            if cliked.get() == "MA":
                indexMA = remplissageMA(tag.upper(), entreeSign.get())
                saveText(indexMA)
            elif cliked.get() == "MT":
                indexMT = remplissageMA(tag.upper(), entreeSign.get())
                saveText(indexMT)
            elif cliked.get() == "TOR":
                indexTOR = remplissageTOR(tag.upper(), entreeSign.get())
                saveText(indexTOR)
            else:
                indexVMA = remplissageVMA(tag.upper(), entreeSign.get())
                saveText(indexVMA)

            # saveExcel(cliked.get(), tag.upper(), entreeSign.get(),"")
            entreeTag.delete("0", "end")
            entreeSign.delete("0", "end")
            entreeCom.delete("0", "end")

def ouvrirIndex():
    os.startfile("Modbus.txt")

def ouvrirExcel():
    os.startfile("tablesModbus.xlsx")

def exctraction():

    try:
        monFichier = open(entreextract.get(), "r")

    except OSError:
        messagebox.showerror('erreur ', 'fichier non trouvé')
        entreextract.delete("0", "end")
        return False

    tab = []
    tabMot = []
    tabTag = []
    dictSignALA = {}
    dictComALA = {}
    dictSignCGR = {}
    dictComCGR = {}
    dictSignVME = {}
    dictComVME = {}
    dictSignVPT = {}
    dictComVPT = {}
    dictSign1SM = {}
    dictCom1SM = {}
    dictSignARP = {}
    dictComARP = {}
    dictSignSCO = {}
    dictComSCO = {}
    dictSignMA = {}
    dictSignMT = {}
    dictSignNS2 = {}
    dictComNS2 = {}
    dictSignAEV = {}
    dictComAEV = {}
    dictSignVMA = {}
    dictSignTOR = {}

    validation = True
    verification = True

    effaceur = "%MW"

    for ligne in monFichier.readlines():
        for carac in range(len(ligne)):
            if ligne[carac] == '\t' or ligne[carac] == '\n':
                mot = "".join(tab)
                if len(mot) > 3:
                    tabMot.append(mot)
                tab = []
            else:
                tab.append(ligne[carac])
        if len(tabMot) != 0:
            for x in range(len(tabMot[0])):
                if (tabMot[0])[x] == "_":
                    tag = "".join(tabTag)
                    tabTag = []
                    break
                else:
                    tabTag.append((tabMot[0])[x])

            for x in range(len(effaceur)):
                tabMot[1] = tabMot[1].replace(effaceur[x], "")

            if tabMot[2] == "UDT_ST_SIGNALISATIONS_ARP_NF":
                dictSignARP[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_MOYEN_CONDUITE_ARP_NF":
                dictComARP[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_MOYEN_CONDUITE_SCO":
                dictComSCO[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_SCO":
                dictSignSCO[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_MA":
                dictSignMA[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_TOR":
                dictSignTOR[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_VMA":
                dictSignVMA[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_MT":
                dictSignMT[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_1SM":
                dictSign1SM[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_MOYEN_CONDUITE_1SM":
                dictCom1SM[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_MOYEN_CONDUITE_NS2":
                dictComNS2[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_NS2":
                dictSignNS2[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_VME":
                dictSignVME[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_MOYEN_CONDUITE_VME":
                dictComVME[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_VPT":
                dictSignVPT[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_MOYEN_CONDUITE_VPT":
                dictComVPT[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_CGR":
                dictSignCGR[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_MOYEN_CONDUITE_CGR":
                dictComCGR[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_ALA":
                dictSignALA[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_MOYEN_CONDUITE_ALA":
                dictComALA[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_SIGNALISATIONS_AEV":
                dictSignAEV[tag] = str(tabMot[1])

            elif tabMot[2] == "UDT_ST_MOYEN_CONDUITE_AEV":
                dictComAEV[tag] = str(tabMot[1])

        tabMot = []

    if bool(dictComARP) == True and bool(dictSignARP) == True:
        sheet = "ARP"
        for key in dictComARP.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSignARP[key], dictComARP[key]) == False:
            #     validation = False

            else :
                # saveExcel(sheet, key, dictSignARP[key], dictComARP[key])
                text = remplissageARP(key, dictSignARP[key], dictComARP[key])
                saveText(text)

    if bool(dictComSCO) == True and bool(dictSignSCO) == True :
        sheet = "SCO"
        for key in dictComSCO.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSignSCO[key], dictComSCO[key]) == False:
            #     validation = False

            else :
                # saveExcel(sheet, key, dictSignSCO[key], dictComSCO[key])
                text = remplissageSCO(key, dictSignSCO[key], dictComSCO[key])
                saveText(text)

    if bool(dictSignVMA) == True :
        # sheet = "VMA"
        for key in dictSignVMA.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSignMA[key], "") == False:
            #     validation = False

            else:
                # saveExcel(sheet, key, dictSignMA[key], "")
                text = remplissageVMA(key, dictSignVMA[key])
                saveText(text)

    if bool(dictSignTOR) == True :
        for key in dictSignTOR.keys():
            if verificationDoublon(key) == False:
                verification = False

            else:
                text = remplissageTOR(key, dictSignTOR[key])
                saveText(text)

    if bool(dictSignMA) == True :
        sheet = "MA"
        for key in dictSignMA.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSignMA[key], "") == False:
            #     validation = False

            else:
                # saveExcel(sheet, key, dictSignMA[key], "")
                text = remplissageMA(key, dictSignMA[key])
                saveText(text)

    if bool(dictSignMT) == True  :
        sheet = "MT"
        for key in dictSignMT.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSignMT[key], "") == False:
            #     validation = False

            else:
                # saveExcel(sheet, key, dictSignMT[key], "")
                text = remplissageMA(key, dictSignMT[key])
                saveText(text)

    if bool(dictCom1SM) == True and bool(dictSign1SM) == True :
        sheet = "1SM"
        for key in dictCom1SM.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSign1SM[key], dictCom1SM[key]) == False:
            #     validation = False

            else :
                # saveExcel(sheet, key, dictSign1SM[key], dictCom1SM[key])
                text = remplissage1SM(key, dictSign1SM[key], dictCom1SM[key])
                saveText(text)

    if bool(dictComNS2) == True and bool(dictSignNS2) == True :
        sheet = "NS2"
        for key in dictComNS2.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSignNS2[key], dictComNS2[key]) == False:
            #     validation = False

            else :
                # saveExcel(sheet, key, dictSignNS2[key], dictComNS2[key])
                text = remplissageNS2(key, dictSignNS2[key], dictComNS2[key])
                saveText(text)

    if bool(dictComVME) == True and bool(dictSignVME) == True :
        sheet = "VME"
        for key in dictComVME.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSignVME[key], dictComVME[key]) == False:
            #     validation = False

            else :
                # saveExcel(sheet, key, dictSignVME[key], dictComVME[key])
                text = remplissageVME(key, dictSignVME[key], dictComVME[key])
                saveText(text)

    if bool(dictComVPT) == True and bool(dictSignVPT) == True :
        sheet = "VPT"
        for key in dictComVPT.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSignVME[key], dictComVME[key]) == False:
            #     validation = False

            else :
                # saveExcel(sheet, key, dictSignVPT[key], dictComVPT[key])
                text = remplissageVPT(key, dictSignVPT[key], dictComVPT[key])
                saveText(text)

    if bool(dictComCGR) == True and bool(dictSignCGR) == True :
        sheet = "CGR"
        for key in dictComCGR.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSignCGR[key], dictComCGR[key]) == False:
            #     validation = False

            else :
                # saveExcel(sheet, key, dictSignCGR[key], dictComCGR[key])
                text = remplissageCGR(key, dictSignCGR[key], dictComCGR[key])
                saveText(text)

    if bool(dictComALA) == True and bool(dictSignALA) == True :
        sheet = "ALA"
        for key in dictComALA.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSignALA[key], dictComALA[key]) == False:
            #     validation = False

            else :
                # saveExcel(sheet, key, dictSignALA[key], dictComALA[key])
                text = remplissageALA(key, dictSignALA[key], dictComALA[key])
                saveText(text)

    if bool(dictComAEV) == True and bool(dictSignAEV) == True :
        sheet = "AEV"
        for key in dictComAEV.keys():
            if verificationDoublon(key) == False:
                verification = False

            # elif validationEcriture(key, dictSignAEV[key], dictComAEV[key]) == False:
            #     validation = False

            else :
                # saveExcel(sheet, key, dictSignAEV[key], dictComAEV[key])
                text = remplissageAEV(key, dictSignAEV[key], dictComAEV[key])
                saveText(text)

    # if validation == False or verification == False:
    #     messagebox.showwarning("attention", "les objets contenant des libelles redondants ou des chevauchements"
    #                                         " d'adresses n'ont pas ete ajoutés")

    entreextract.delete("0", "end")


#Creation de la page d'acceuil
monInterface = Tk()
monInterface.title("Index Unity-Panorama")
monInterface.geometry('480x600')
monInterface.configure(background="#4B8BBE")
monInterface.resizable(height=False, width=False)

#Creation liste déroulante
listeDeroulante = [
    "ARP",
    "SCO",
    "MA",
    "MT",
    "1SM",
    "VME",
    "VPT",
    "CGR",
    "ALA",
    "NS2",
    "AEV",
    "VMA",
    "TOR"
]
titrePrincipal = Label(monInterface , text="Interface Table Echanges UNITY PANORAMA", bg="yellow")
titrePrincipal.place(height=50, width=400, x=40, y=5)
cliked = StringVar()
cliked.set(listeDeroulante[0])

drop = OptionMenu(monInterface, cliked, *listeDeroulante)
drop.place(height=30, width=300, x=90, y=75)

libelleTag = Label(monInterface, text="Tag de l'objet :", bg="#4B8BBE").place(height=30, width=150, x=90, y=125)
entreeTag = Entry(monInterface)
entreeTag.place(height=30, width=100, x=270, y=125)

libelleCom = Label(monInterface, text="Adresse  commandes :%MW", bg="#4B8BBE").place(height=30, width=170, x=100, y=160)
entreeCom = Entry(monInterface)
entreeCom.place(height=30, width=100, x=270, y=160)

libelleSign = Label(monInterface, text="Adresse Signalisations :%MW", bg="#4B8BBE").place(height=30, width=170, x=100, y=195)
entreeSign = Entry(monInterface)
entreeSign.place(height=30, width=100, x=270, y=195)

libelleextract = Label(monInterface, text="Entrer le nom.txt", bg="#4B8BBE").place(height=30, width=100, x=190, y=510)
entreextract = Entry(monInterface)
entreextract.place(height=30, width=100, x=190, y=485)

boutonAjouter = Button(monInterface, text="ajouter l'objet", command=majIndex).place(height=30, width=150, x=165, y=240)
boutonAfficherIndex = Button(monInterface, text="afficher la table d'index", command=ouvrirIndex).place(height=30, width=150, x=85, y=280)
boutonAfficherExcel = Button(monInterface, text="afficher Excel", command=ouvrirExcel).place(height=30, width=150, x=240, y=280)
boutonExtraire = Button(monInterface, text="ajouter à partir d'une extraction ", command=exctraction).place(height=30, width=200, x=140, y=450)

canText = Canvas(monInterface, bg="#4B8BBE")
imgText = PhotoImage(file="Capturetext.PNG")
canText.create_image(30, 30, image=imgText)
canText.place(height=60, width=60, x=120, y=320)

canExcel = Canvas(monInterface, bg="#4B8BBE")
imgExcel = PhotoImage(file="Captureexcel.PNG")
canExcel.create_image(40, 30, image=imgExcel)
canExcel.place(height=60, width=60, x=290, y=320)

canUnity = Canvas(monInterface, bg="#4B8BBE")
imgUnity = PhotoImage(file="CaptureUnity.PNG")
canUnity.create_image(30, 30, image=imgUnity)
canUnity.place(height=60, width=60, x=25, y=145)

canPanorama = Canvas(monInterface, bg="#4B8BBE")
imgPanorama = PhotoImage(file="CapturePanorama.PNG")
canPanorama.create_image(40, 20, image=imgPanorama)
canPanorama.place(height=40, width=80, x=380, y=155)


#Affichage de la page
monInterface.mainloop()