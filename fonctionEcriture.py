import pandas as pd
from tkinter import messagebox
from styleframe import StyleFrame, Styler


def verificationDoublon(tag):
    monExcelARP = pd.read_excel("tablesModbus.xlsx", sheet_name="ARP")
    monExcelSCO = pd.read_excel("tablesModbus.xlsx", sheet_name="SCO")
    monExcelMA = pd.read_excel("tablesModbus.xlsx", sheet_name="MA_MT")
    monExcel1SM = pd.read_excel("tablesModbus.xlsx", sheet_name="1SM")
    monExcelNS2 = pd.read_excel("tablesModbus.xlsx", sheet_name="NS2")
    monExcelVME = pd.read_excel("tablesModbus.xlsx", sheet_name="VME")
    monExcelCGR = pd.read_excel("tablesModbus.xlsx", sheet_name="CGR")
    monExcelAEV = pd.read_excel("tablesModbus.xlsx", sheet_name="AEV")


    tabD = [pd.DataFrame(monExcelARP), pd.DataFrame(monExcelSCO), pd.DataFrame(monExcelMA), pd.DataFrame(monExcel1SM),
            pd.DataFrame(monExcelNS2), pd.DataFrame(monExcelVME), pd.DataFrame(monExcelCGR), pd.DataFrame(monExcelAEV)]

    for tab in tabD:
        for index in range(len(tab)):
            if str(tab.loc[index, "Libelle"]) == str(tag):
                return False
    return True


def validationChamps1(tag, sign, com):
    if((tag == "")|(sign == "")|(com == "")):
        messagebox.showerror('erreur de champ', 'Tous les champs doivent etre renseignés')
        return False

    if ((sign.isdigit() == False) | (com.isdigit() == False)):
        messagebox.showerror('erreur de champ', 'Les champs "adresse commandes" et "adresses"ignalisations" doivent etre des nombres')
        return False
    else:
        return True


def validationChamps2(tag, sign):
    if((tag == "")|(sign == "")):
        messagebox.showerror('erreur de champ', 'Tous les champs doivent etre renseignés')
        return False

    if ((sign.isdigit() == False)):
        messagebox.showerror('erreur de champ', 'Les champs "adresse commandes" et "adresses"ignalisations" doivent etre des nombres')
        return False
    else:
        return True


def validationEcriture(model, adresseSign, adresseCom):
    monExcelARP = pd.read_excel("tablesModbus.xlsx", sheet_name="ARP")
    monExcelSCO = pd.read_excel("tablesModbus.xlsx", sheet_name="SCO")
    monExcelMA = pd.read_excel("tablesModbus.xlsx", sheet_name="MA_MT")
    monExcel1SM = pd.read_excel("tablesModbus.xlsx", sheet_name="1SM")
    monExcelVME = pd.read_excel("tablesModbus.xlsx", sheet_name="VME")
    monExcelCGR = pd.read_excel("tablesModbus.xlsx", sheet_name="CGR")
    monExcelALA = pd.read_excel("tablesModbus.xlsx", sheet_name="ALA")
    monExcelNS2 = pd.read_excel("tablesModbus.xlsx", sheet_name="NS2")
    monExcelAEV = pd.read_excel("tablesModbus.xlsx", sheet_name="AEV")

    tabD = [pd.DataFrame(monExcelARP), pd.DataFrame(monExcelSCO), pd.DataFrame(monExcelMA),
            pd.DataFrame(monExcel1SM), pd.DataFrame(monExcelVME), pd.DataFrame(monExcelCGR), pd.DataFrame(monExcelALA),
            pd.DataFrame(monExcelNS2), pd.DataFrame(monExcelAEV)]

    carEfface = "%MW"

    for tab in tabD:
        if model == "ARP" or model == "SCO":
            if (-3 < (int(adresseSign) - int(adresseCom)) <3):
                return False

            for index in range(len(tab)):
                if pd.isnull(tab.loc[index, "Commande"]):
                    valstrCom = "0"
                    valstrSign = str(tab.loc[index, "Signalisation"])
                else:
                    valstrSign = str(tab.loc[index, "Signalisation"])
                    valstrCom = str(tab.loc[index, "Commande"])

                for x in range(len(carEfface)):
                    valstrSign = valstrSign.replace(carEfface[x], "")
                    valstrCom = valstrCom.replace(carEfface[x], "")

                if ((-3 < (int(adresseSign)) - int(valstrCom) < 3)
                        | ((-3 < (int(adresseSign)) - int(valstrSign) < 3))
                        | ((-2 < (int(adresseCom)) - int(valstrSign) < 2))
                        | ((-2 < (int(adresseCom)) - int(valstrCom) < 2))):
                    return False

        elif model == "MA" or model == "MT":
            for index in range(len(tab)):

                if pd.isnull(tab.loc[index, "Commande"]):
                    valstrCom = "0"
                    valstrSign = str(tab.loc[index, "Signalisation"])
                else:
                    valstrSign = str(tab.loc[index, "Signalisation"])
                    valstrCom = str(tab.loc[index, "Commande"])

                for x in range(len(carEfface)):
                    valstrSign = valstrSign.replace(carEfface[x], "")
                    valstrCom = valstrCom.replace(carEfface[x], "")


                if ((-10 < (int(adresseSign)) - int(valstrCom) < 10)
                        | ((-10 < (int(adresseSign)) - int(valstrSign) < 10))):
                    return False

        elif model == "1SM" or model == "VME" or model == "CGR" or model == "ALA":
             if (-1 < (int(adresseSign) - int(adresseCom)) <1):
                return False

             for index in range(len(tab)):
                if pd.isnull(tab.loc[index, "Commande"]):
                    valstrCom = "0"
                    valstrSign = str(tab.loc[index, "Signalisation"])
                else:
                    valstrSign = str(tab.loc[index, "Signalisation"])
                    valstrCom = str(tab.loc[index, "Commande"])

                for x in range(len(carEfface)):
                    valstrSign = valstrSign.replace(carEfface[x], "")
                    valstrCom = valstrCom.replace(carEfface[x], "")

                if ((-2 < (int(adresseSign)) - int(valstrCom) < 2)
                        | ((-2 < (int(adresseSign)) - int(valstrSign) < 2))
                        | ((-1 < (int(adresseCom)) - int(valstrSign) < 1))
                        | ((-1 < (int(adresseCom)) - int(valstrCom) < 1))):
                    return False

        elif model == "NS2":
             if (-1 < (int(adresseSign) - int(adresseCom)) <1):
                return False

             for index in range(len(tab)):
                if pd.isnull(tab.loc[index, "Commande"]):
                    valstrCom = "0"
                    valstrSign = str(tab.loc[index, "Signalisation"])
                else:
                    valstrSign = str(tab.loc[index, "Signalisation"])
                    valstrCom = str(tab.loc[index, "Commande"])

                for x in range(len(carEfface)):
                    valstrSign = valstrSign.replace(carEfface[x], "")
                    valstrCom = valstrCom.replace(carEfface[x], "")

                if ((-2 < (int(adresseSign)) - int(valstrCom) < 2)
                        | ((-1 < (int(adresseSign)) - int(valstrSign) < 1))
                        | ((-2 < (int(adresseCom)) - int(valstrSign) < 2))
                        | ((-2 < (int(adresseCom)) - int(valstrCom) < 2))):
                    return False

        elif model == "AEV":
             if (-3 < (int(adresseSign) - int(adresseCom)) <3):
                return False

             for index in range(len(tab)):
                if pd.isnull(tab.loc[index, "Commande"]):
                    valstrCom = "0"
                    valstrSign = str(tab.loc[index, "Signalisation"])
                else:
                    valstrSign = str(tab.loc[index, "Signalisation"])
                    valstrCom = str(tab.loc[index, "Commande"])

                for x in range(len(carEfface)):
                    valstrSign = valstrSign.replace(carEfface[x], "")
                    valstrCom = valstrCom.replace(carEfface[x], "")

                if ((-3< (int(adresseSign)) - int(valstrCom) < 3)
                        | ((-3 < (int(adresseSign)) - int(valstrSign) < 3))
                        | ((-2 < (int(adresseCom)) - int(valstrSign) < 2))
                        | ((-1 < (int(adresseCom)) - int(valstrCom) < 1))):
                    return False

    return True


def saveExcel(sheet, tag, sign, com):

    if sheet == "MA" or sheet == "MT":
        sheet = "MA_MT"

    monExcelARP = pd.read_excel("tablesModbus.xlsx", sheet_name="ARP")
    monExcelSCO = pd.read_excel("tablesModbus.xlsx", sheet_name="SCO")
    monExcelMA = pd.read_excel("tablesModbus.xlsx", sheet_name="MA_MT")
    monExcel1SM = pd.read_excel("tablesModbus.xlsx", sheet_name="1SM")
    monExcelVME = pd.read_excel("tablesModbus.xlsx", sheet_name="VME")
    monExcelVPT = pd.read_excel("tablesModbus.xlsx", sheet_name="VPT")
    monExcelCGR = pd.read_excel("tablesModbus.xlsx", sheet_name="CGR")
    monExcelALA = pd.read_excel("tablesModbus.xlsx", sheet_name="ALA")
    monExcelNS2 = pd.read_excel("tablesModbus.xlsx", sheet_name="NS2")
    monExcelAEV = pd.read_excel("tablesModbus.xlsx", sheet_name="AEV")

    DfARP = pd.DataFrame(monExcelARP)
    DfSCO = pd.DataFrame(monExcelSCO)
    DfMA = pd.DataFrame(monExcelMA)
    Df1SM = pd.DataFrame(monExcel1SM)
    DfVME = pd.DataFrame(monExcelVME)
    DfVPT = pd.DataFrame(monExcelVPT)
    DfCGR = pd.DataFrame(monExcelCGR)
    DfALA = pd.DataFrame(monExcelALA)
    DfNS2 = pd.DataFrame(monExcelNS2)
    DfAEV = pd.DataFrame(monExcelAEV)

    sfARP = StyleFrame(DfARP)
    sfSCO = StyleFrame(DfSCO)
    sfMA = StyleFrame(DfMA)
    sf1SM = StyleFrame(Df1SM)
    sfVME = StyleFrame(DfVME)
    sfVPT = StyleFrame(DfVPT)
    sfCGR = StyleFrame(DfCGR)
    sfALA = StyleFrame(DfALA)
    sfNS2 = StyleFrame(DfNS2)
    sfAEV = StyleFrame(DfAEV)

    sfARP.apply_headers_style(Styler(bg_color='#00008000', bold=True, font='Calibri', font_size=11))
    sfARP.set_column_width(columns=["Libelle", "Signalisation", "Commande"], width=40)
    sfSCO.apply_headers_style(Styler(bg_color='#00008000', bold=True, font='Calibri', font_size=11))
    sfSCO.set_column_width(columns=["Libelle", "Signalisation", "Commande"], width=40)
    sfMA.apply_headers_style(Styler(bg_color='#00008000', bold=True, font='Calibri', font_size=11))
    sfMA.set_column_width(columns=["Libelle", "Signalisation", "Commande"], width=40)
    sf1SM.apply_headers_style(Styler(bg_color='#00008000', bold=True, font='Calibri', font_size=11))
    sf1SM.set_column_width(columns=["Libelle", "Signalisation", "Commande"], width=40)
    sfVME.apply_headers_style(Styler(bg_color='#00008000', bold=True, font='Calibri', font_size=11))
    sfVME.set_column_width(columns=["Libelle", "Signalisation", "Commande"], width=40)
    sfVPT.apply_headers_style(Styler(bg_color='#00008000', bold=True, font='Calibri', font_size=11))
    sfVPT.set_column_width(columns=["Libelle", "Signalisation", "Commande"], width=40)
    sfCGR.apply_headers_style(Styler(bg_color='#00008000', bold=True, font='Calibri', font_size=11))
    sfCGR.set_column_width(columns=["Libelle", "Signalisation", "Commande"], width=40)
    sfALA.apply_headers_style(Styler(bg_color='#00008000', bold=True, font='Calibri', font_size=11))
    sfALA.set_column_width(columns=["Libelle", "Signalisation", "Commande"], width=40)
    sfNS2.apply_headers_style(Styler(bg_color='#00008000', bold=True, font='Calibri', font_size=11))
    sfNS2.set_column_width(columns=["Libelle", "Signalisation", "Commande"], width=40)
    sfAEV.apply_headers_style(Styler(bg_color='#00008000', bold=True, font='Calibri', font_size=11))
    sfAEV.set_column_width(columns=["Libelle", "Signalisation", "Commande"], width=40)

    DfModif = pd.read_excel("tablesModbus.xlsx", sheet_name=sheet)
    dernierIndice = (len(DfModif.index))

    if ((sheet == "ARP") or (sheet == "SCO") or (sheet == "1SM") or (sheet == "VPT")
            or (sheet == "VME") or (sheet == "CGR") or (sheet == "ALA") or (sheet == "NS2") or (sheet == "AEV")):
        l_row = [tag, "%MW"+sign, "%MW"+com]

    else:
        l_row = [tag, "%MW"+sign, ""]

    DfModif.loc[dernierIndice] = l_row

    sfModif = StyleFrame(DfModif)
    sfModif.apply_headers_style(Styler(bg_color='#00008000', bold=True, font='Calibri', font_size=11))
    sfModif.set_column_width(columns=["Libelle", "Signalisation", "Commande"], width=40)

    excel_writer = StyleFrame.ExcelWriter('tablesModbus.xlsx')
    sfARP.to_excel(excel_writer, sheet_name='ARP')
    sfSCO.to_excel(excel_writer, sheet_name='SCO')
    sfMA.to_excel(excel_writer, sheet_name='MA_MT')
    sf1SM.to_excel(excel_writer, sheet_name='1SM')
    sfVME.to_excel(excel_writer, sheet_name='VME')
    sfVPT.to_excel(excel_writer, sheet_name='VPT')
    sfCGR.to_excel(excel_writer, sheet_name='CGR')
    sfALA.to_excel(excel_writer, sheet_name='ALA')
    sfNS2.to_excel(excel_writer, sheet_name='NS2')
    sfAEV.to_excel(excel_writer, sheet_name='AEV')
    sfModif.to_excel(excel_writer, sheet_name=sheet)
    excel_writer.save()


def saveText(texte):
    file = open("Modbus.txt", "a")
    file.write(texte)
    file.close()
