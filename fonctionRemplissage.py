def remplissageARP(Tag, adresse_signalisation_MCP, adresse_commande_MCP):
      return (
              Tag +"\n"+
              Tag+"_CONS_POS\t#AI/word:"+
              str(adresse_signalisation_MCP)+"\n"+
              Tag + "_MM\t#AI/word:" +
              str(int(adresse_signalisation_MCP)+1) + "\n"+
              Tag + "_DEF_CONS_POS\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-1" "\n" +
              Tag + "_DEF_MM\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-2" "\n" +
              Tag + "_DFdCF\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-3" "\n" +
              Tag + "_A_Prio_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-4" "\n" +
              Tag + "_MODE_A\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-5" "\n" +
              Tag + "_For_A\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-6" "\n" +
              Tag + "_For_M\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-7" "\n" +
              Tag + "_PAIR\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-8" "\n" +
              Tag + "_DEF_MAT\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-9" "\n" +
              Tag + "_IND\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-10" "\n" +
              Tag + "_DEF_REGL_MM\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-11" "\n" +
              Tag + "_SDISCf\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-12" "\n" +
              Tag + "_POSF\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-13" "\n" +
              Tag + "_LIMIT_OUV\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-14" "\n" +
              Tag + "_CHOIX_COM\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 2) + "-15" "\n" +
              Tag + "_ConsO\t#AO/word:" +
              str(int(adresse_commande_MCP)) + "\n" +
              Tag + "_KAM\t#AO/bool:" +
              str(int(adresse_commande_MCP) +1) + "-0" "\n" +
              Tag + "_VAL\t#AO/bool:" +
              str(int(adresse_commande_MCP) + 1) + "-1" "\n" +
              Tag + "_ACQ\t#AO/bool:" +
              str(int(adresse_commande_MCP) + 1) + "-2"+"\n" +
              "\n"  )


def remplissageSCO(Tag, adresse_signalisation_MCP, adresse_commande_MCP):
      return (
              Tag +"\n"+
              Tag+"_ConsO\t#AO/float:"+
              str(adresse_commande_MCP)+"\n"+
              Tag + "_VAL\t#AO/bool:" +
              str(int(adresse_commande_MCP)+2) + "-0"+ "\n"+
              Tag + "_KAMP\t#AO/bool:" +
              str(int(adresse_commande_MCP) + 2) + "-8" "\n" +
              Tag + "_Mesu_R\t#AI/float:" +
              str(int(adresse_signalisation_MCP)) +  "\n" +
              Tag + "_Cons_Reg\t#AI/float:" +
              str(int(adresse_signalisation_MCP)+ 2) +  "\n" +
              Tag + "_Cons_Pos\t#AI/float:" +
              str(int(adresse_signalisation_MCP) + 4) +  "\n" +
              Tag + "_Def_Mesu_R\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 6) + "-0" "\n" +
              Tag + "_Mode_A\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 6) + "-1" "\n" +
              Tag + "_Def_Cons\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 6) + "-2" "\n" +
              Tag + "_For_A\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 6) + "-3" "\n" +
              Tag + "_For_M\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 6) + "-4" "\n" +
              Tag + "_CHOIX_COM\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 6) + "-5" "\n" +
              "\n"
            )


def remplissageMA(Tag, adresse_signalisation_MCP):
      return (
              Tag +"\n"+
              Tag + "_MIN\t#AI/float:" +
              str(adresse_signalisation_MCP) + "\n" +
              Tag + "_MAX\t#AI/float:" +
              str(int(adresse_signalisation_MCP) + 2) + "\n" +
              Tag + "_Seu1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 4) + "-0" "\n" +
              Tag + "_Seu2\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 4) + "-1" "\n" +
              Tag + "_Seu3\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 4) + "-2" "\n" +
              Tag + "_Seu4\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 4) + "-3" "\n" +
              Tag + "_Seu5\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 4) + "-4" "\n" +
              Tag + "_Seu6\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 4) + "-5" "\n" +
              Tag + "_Def_Mesu_R\t#AI/bool:" +
              str(int(adresse_signalisation_MCP) + 4) + "-6" "\n" +
              Tag + "_Mesu_R\t#AI/float:" +
              str(int(adresse_signalisation_MCP) + 5) +"\n" +
              Tag + "_SeuilChaine1\t#AI/float:" +
              str(int(adresse_signalisation_MCP) + 7) +"\n" +
              Tag + "_SeuilChaine2\t#AI/float:" +
              str(int(adresse_signalisation_MCP) + 9) +"\n" +
              Tag + "_SeuilChaine3\t#AI/float:" +
              str(int(adresse_signalisation_MCP) + 11) +"\n" +
              Tag + "_SeuilChaine4\t#AI/float:" +
              str(int(adresse_signalisation_MCP) + 13) + "\n" +
              Tag + "_SeuilChaine5\t#AI/float:" +
              str(int(adresse_signalisation_MCP) + 15) +"\n" +
              Tag + "_SeuilChaine6\t#AI/float:" +
              str(int(adresse_signalisation_MCP) + 17) + "\n"+
              "\n"
            )


def remplissageTOR(Tag, adresse_signalisation_MCP):
      return (
              Tag +"\n"+
              Tag + "_SEUIL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-0" "\n" +
              Tag + "_SEUIL_DEF\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-8" "\n" +
              "\n"
            )


def remplissage1SM(Tag, adresse_signalisation_MCP, adresse_commande_MCP):
      return (
              Tag +"\n"+
              Tag + "_ACQ\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-1" "\n" +
              Tag + "_KE\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-2" "\n" +
              Tag + "_KH\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-3" "\n" +
              Tag + "_KVAL\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-4" "\n" +
              Tag + "_KAM\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-5" "\n" +
              Tag + "_ETAT_ENCL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-0" "\n" +
              Tag + "_ETAT_DECL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-1" "\n" +
              Tag + "_AUTO\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-2" "\n" +
              Tag + "_DEF_MAT\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-3" "\n" +
              Tag + "_IND\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-4" "\n" +
              Tag + "_CHOIX_COM\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-5" "\n" +
              Tag + "_STTLE_E\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-7" "\n" +
              Tag + "_STTLE_H\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-8" "\n" +
              Tag + "_SDISC_E\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-9" "\n" +
              Tag + "_SDISC_H\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-10" "\n" +
              Tag + "_DEF_POS_0\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-11" "\n" +
              Tag + "_DEF_POS_1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-12" "\n" +
              Tag + "_PUP\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-13" "\n" +
              Tag + "_PUC\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-14" "\n" +
              Tag + "_CC_E\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-15" "\n" +
              Tag + "_CC_H\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-0" "\n" +
              Tag + "_VERR_ENCL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-1" "\n" +
              Tag + "_VERR_DECL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-2" "\n" +
              Tag + "_A_PRIO_ENCL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-3" "\n" +
              Tag + "_A_PRIO_DECL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-4" "\n" +
              Tag + "_FOR_A\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-5" "\n" +
              Tag + "_FOR_M\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-6" "\n" +
              Tag + "_PR_OR\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-7" "\n" +
              "\n"

            )


def remplissageVME(Tag, adresse_signalisation_MCP, adresse_commande_MCP):
      return (
              Tag +"\n"+
              Tag + "_ACQ\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-0" "\n" +
              Tag + "_KO\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-1" "\n" +
              Tag + "_KF\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-2" "\n" +
              Tag + "_KVAL\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-3" "\n" +
              Tag + "_KAM\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-4" "\n" +
              Tag + "_POSO\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-0" "\n" +
              Tag + "_POSF\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-1" "\n" +
              Tag + "_AUTO\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-2" "\n" +
              Tag + "_DEF_MAT\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-3" "\n" +
              Tag + "_IND\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-4" "\n" +
              Tag + "_CHOIX_COM\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-5" "\n" +
              Tag + "_STTLE_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-7" "\n" +
              Tag + "_STTLE_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-8" "\n" +
              Tag + "_SDISC_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-9" "\n" +
              Tag + "_SDISC_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-10" "\n" +
              Tag + "_D_FDC_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-11" "\n" +
              Tag + "_D_FDC_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-12" "\n" +
              Tag + "_DEF_POS_0\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-13" "\n" +
              Tag + "_DEF_POS_1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-14" "\n" +
              Tag + "_PUP\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-15" "\n" +
              Tag + "_PUC\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-0" "\n" +
              Tag + "_CC_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-1" "\n" +
              Tag + "_CC_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-2" "\n" +
              Tag + "_VERR_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-3" "\n" +
              Tag + "_VERR_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-4" "\n" +
              Tag + "_A_PRIO_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-5" "\n" +
              Tag + "_A_PRIO_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-6" "\n" +
              Tag + "_FOR_A\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-7" "\n" +
              Tag + "_FOR_M\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-8" "\n" +
              "\n"

            )


def remplissageVPT(Tag, adresse_signalisation_MCP, adresse_commande_MCP):
      return (
              Tag +"\n"+
              Tag + "_ACQ\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-0" "\n" +
              Tag + "_KO\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-1" "\n" +
              Tag + "_KF\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-2" "\n" +
              Tag + "_KVAL\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-3" "\n" +
              Tag + "_KAM\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-4" "\n" +
              Tag + "_POSO\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-0" "\n" +
              Tag + "_POSF\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-1" "\n" +
              Tag + "_AUTO\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-2" "\n" +
              Tag + "_DEF_MAT\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-3" "\n" +
              Tag + "_IND\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-4" "\n" +
              Tag + "_CHOIX_COM\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-5" "\n" +
              Tag + "_AUTORI_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-6" "\n" +
              Tag + "_STTLE_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-7" "\n" +
              Tag + "_STTLE_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-8" "\n" +
              Tag + "_D_FDC_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-9" "\n" +
              Tag + "_D_FDC_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-10" "\n" +
              Tag + "_DEF_POS_0\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-11" "\n" +
              Tag + "_DEF_POS_1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-12" "\n" +
              Tag + "_PAIR\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-13" "\n" +
              Tag + "_PUC\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-14" "\n" +
              Tag + "_CC_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-15" "\n" +
              Tag + "_CC_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-0" "\n" +
              Tag + "_VERR_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-1" "\n" +
              Tag + "_VERR_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-2" "\n" +
              Tag + "_A_PRIO_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-3" "\n" +
              Tag + "_A_PRIO_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-4" "\n" +
              Tag + "_FOR_A\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-5" "\n" +
              Tag + "_FOR_M\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-6" "\n" +
              Tag + "_SDISC_O\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-7" "\n" +
              Tag + "_SDISC_F\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-8" "\n" +
              "\n"

            )


def remplissageCGR(Tag, adresse_signalisation_MCP, adresse_commande_MCP):
      return (
              Tag +"\n"+
              Tag + "_ACQ\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-0" "\n" +
              Tag + "_KC_AR\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-1" "\n" +
              Tag + "_KC_R1\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-2" "\n" +
              Tag + "_KVAL\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-4" "\n" +
              Tag + "_KAM\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-5" "\n" +
              Tag + "_AR\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-0" "\n" +
              Tag + "_ES_R1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-1" "\n" +
              Tag + "_CHOIX_COM\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-2" "\n" +
              Tag + "_AUTO\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-3" "\n" +
              Tag + "_R_DEF\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-4" "\n" +
              Tag + "_IND\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-5" "\n" +
              Tag + "_GROUP_A\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-6" "\n" +
              Tag + "_TTLE_AR\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-7" "\n" +
              Tag + "_TTLE_R1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-8" "\n" +
              Tag + "_SDISC_R1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-9" "\n" +
              Tag + "_SDISC_AR\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-10" "\n" +
              Tag + "_CC_R1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-11" "\n" +
              Tag + "_CC_AR\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-12" "\n" +
              Tag + "_ACT_A\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-13" "\n" +
              Tag + "_VERR_CH_AR\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-14" "\n" +
              Tag + "_VERR_CH_R1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-15" "\n" +
              Tag + "_A_PRIO_CH_AR\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-0" "\n" +
              Tag + "_A_PRIO_CH_R1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+1) + "-1" "\n" +
              "\n"
            )


def remplissageALA(Tag, adresse_signalisation_MCP, adresse_commande_MCP):
      return (
              Tag +"\n"+
              Tag + "_ACQ_MEMO\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-0" "\n" +
              Tag + "_ALA\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-0" "\n" +
              Tag + "_ALAINH\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-8" "\n" +
              Tag + "_GRAVITE\t#AI/WORD:" +
              str(int(adresse_signalisation_MCP)+1) + "\n" +
              "\n"
            )


def remplissageNS2(Tag, adresse_signalisation_MCP, adresse_commande_MCP):
      return (
              Tag +"\n"+
              Tag+"_BASC\t#AO/bool:"+
              str(adresse_commande_MCP) + "-0"+ "\n"+
              Tag + "_PRIO_C1_C2\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-1"+ "\n"+
              Tag + "_VAL\t#AO/bool:" +
              str(int(adresse_commande_MCP)) + "-2" "\n" +
              Tag + "_IND_BASC\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-0" + "\n"+
              Tag + "_PRIO_C1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-1" + "\n"+
              Tag + "_PRIO_C2\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-2" + "\n"+
              Tag + "_CHOIX_COM\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)) + "-3" + "\n"+
              "\n"
            )


def remplissageAEV(Tag, adresse_signalisation_MCP, adresse_commande_MCP):
      return (
              Tag +"\n"+
              Tag + "_CONSO\t#AO/word:" +
              str(int(adresse_commande_MCP)) +"\n" +
              Tag + "_ACQ\t#AO/bool:" +
              str(int(adresse_commande_MCP)+1) + "-1" "\n" +
              Tag + "_KE\t#AO/bool:" +
              str(int(adresse_commande_MCP)+1) + "-2" "\n" +
              Tag + "_KH\t#AO/bool:" +
              str(int(adresse_commande_MCP)+1) + "-3" "\n" +
              Tag + "_KVAL\t#AO/bool:" +
              str(int(adresse_commande_MCP)+1) + "-4" "\n" +
              Tag + "_KAM\t#AO/bool:" +
              str(int(adresse_commande_MCP)+1) + "-5" "\n" +
              Tag + "_CONS_VAR\t#AI/word:" +
              str(int(adresse_signalisation_MCP)) + "\n" +
              Tag + "_MM\t#AI/word:" +
              str(int(adresse_signalisation_MCP)+1) + "\n" +
              Tag + "_ETAT_ENCL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-0" "\n" +
              Tag + "_ETAT_DECL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-1" "\n" +
              Tag + "_AUTO\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-2" "\n" +
              Tag + "_DEF_MAT\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-3" "\n" +
              Tag + "_IND\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-4" "\n" +
              Tag + "_CHOIX_COM\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-5" "\n" +
              Tag + "_STTLE_E\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-7" "\n" +
              Tag + "_STTLE_H\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-8" "\n" +
              Tag + "_SDISC_E\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-9" "\n" +
              Tag + "_SDISC_H\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-10" "\n" +
              Tag + "_DEF_POS_0\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-11" "\n" +
              Tag + "_DEF_POS_1\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-12" "\n" +
              Tag + "_PUP\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-13" "\n" +
              Tag + "_PUC\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-14" "\n" +
              Tag + "_CC_E\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+2) + "-15" "\n" +
              Tag + "_CC_H\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+3) + "-0" "\n" +
              Tag + "_VERR_ENCL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+3) + "-1" "\n" +
              Tag + "_VERR_DECL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+3) + "-2" "\n" +
              Tag + "_A_PRIO_ENCL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+3) + "-3" "\n" +
              Tag + "_A_PRIO_DECL\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+3) + "-4" "\n" +
              Tag + "_FOR_A\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+3) + "-5" "\n" +
              Tag + "_FOR_M\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+3) + "-6" "\n" +
              Tag + "_PR_OR\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+3) + "-7" "\n" +
              Tag + "_SDISC_MM\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+3) + "-8" "\n" +
              Tag + "_DEF_VAR\t#AI/bool:" +
              str(int(adresse_signalisation_MCP)+3) + "-9" "\n" +
              "\n"

            )


def remplissageVMA(Tag, adresse_signalisation_MCP):
        return (
                    Tag + "_POS_O\t#AI/bool:" +
                    str(int(adresse_signalisation_MCP)) + "-0" "\n" +
                    Tag + "_POS_F\t#AI/bool:" +
                    str(int(adresse_signalisation_MCP)) + "-1" "\n" +
                    Tag + "_POS_I\t#AI/bool:" +
                    str(int(adresse_signalisation_MCP)) + "-2" "\n" +
                    Tag + "_DEF_POS_1\t#AI/bool:" +
                    str(int(adresse_signalisation_MCP)) + "-3" "\n" +
                    Tag + "_DEF_MAT\t#AI/bool:" +
                    str(int(adresse_signalisation_MCP)) + "-4" "\n" +
                    Tag + "_D_FDC_F\t#AI/bool:" +
                    str(int(adresse_signalisation_MCP)) + "-5" "\n" +
                    Tag + "_D_FDC_O\t#AI/bool:" +
                    str(int(adresse_signalisation_MCP)) + "-6" "\n" +
                    "\n"
      )
