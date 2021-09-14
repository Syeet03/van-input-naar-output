#Lucas van Pelt, 99057303, Pizza Calculator

#Prijzen van de Selami pizza
MediumSelamiPrijs  = 6.95
ItalianSelamiPrijs = 8.70
LargeSelamiPrijs   = 11.95
XXLSelamiPrijs     = 12.95
ColaPrijs          = 1.95
FantaPrijs         = 1.95
FuzeTeaPrijs       = 1.95
RedBullPrijs       = 2.50
WaterPrijs         = 1.50

#Menukaart voor de Pizza Selami
print("____________PRIJSKAART PIZZA SELAMI____________")
print("----------------Medium, 25 cm----------------")
print("--------------------€6.95--------------------")
print("=================================================")
print("---------------Italian, 30 cm---------------")
print("--------------------€8.70-------------------")
print("=================================================")
print("----------------Large, 35 cm----------------")
print("-------------------€11.95-------------------")
print("=================================================")
print("-----------------XXL, 40 cm-----------------")
print("-------------------€12.95-------------------")
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
print("_________________DRANKJES_________________")
print("--------- Cola, Fanta, FuzeTea---------")
print("------------------€1.95------------------")
print("=================================================")
print("----------------Red Bull----------------")
print("-----------------€2.50-----------------")
print("=================================================")
print("------------------Water------------------")
print("-----------------€1.50-----------------")

#Hoeveelheden die besteld worden
hoeveelMediumSelami  = int(input("Aantal Medium Selami Pizza's:  "))
hoeveelItalianSelami = int(input("Aantal Italian Selami Pizza's: "))
hoeveelLargeSelami   = int(input("Aantal Large Selami Pizza's:   "))
hoeveelXXLSelami     = int(input("Aantal XXL Selami Pizza's:     "))
hoeveelCola          = int(input("Aantal Cola:                   "))
hoeveelFanta         = int(input("Aantal Fanta:                  "))
hoeveelFuzeTea       = int(input("Aantal FuzeTea:                "))
hoeveelRedBull       = int(input("Aantal Red Bull:               "))
hoeveelWater         = int(input("Aantal Water:                  "))

#Prijs en aantal van de bestelde pizza's worden opgeteld
TotaalMediumSelami  = (MediumSelamiPrijs  * hoeveelMediumSelami)
TotaalItalianSelami = (ItalianSelamiPrijs * hoeveelItalianSelami)
TotaalLargeSelami   = (LargeSelamiPrijs   * hoeveelLargeSelami)
TotaalXXLSelami     = (XXLSelamiPrijs     * hoeveelXXLSelami)
TotaalCola          = (ColaPrijs          * hoeveelCola)
TotaalFanta         = (FantaPrijs         * hoeveelFanta)
TotaalFuzeTea       = (FuzeTeaPrijs       * hoeveelFuzeTea)
TotaalRedBull       = (RedBullPrijs       * hoeveelRedBull)
TotaalWater         = (WaterPrijs         * hoeveelWater)

#Alle hoeveelheden bestelde pizza's worden bij elkaar opgeteld
TotaalBestelling = (TotaalMediumSelami + TotaalItalianSelami + TotaalLargeSelami + TotaalXXLSelami + TotaalCola + TotaalFanta + TotaalFuzeTea + TotaalRedBull + TotaalWater)

#Prijs per pizza maat
print("Totale prijs Medium Selami Pizza:    " + " €" + str(TotaalMediumSelami))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs Italian Selami Pizza:   " + " €" + str(TotaalItalianSelami))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van Large Selami Pizza: " + " €" + str(TotaalLargeSelami))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van XXL Selami Pizza:   " + " €" + str(TotaalXXLSelami))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van Cola:               " + " €" + str(TotaalCola))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van Fanta:              " + " €" + str(TotaalFanta))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van FuzeTea:            " + " €" + str(TotaalFuzeTea))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van Red Bull:           " + " €" + str(TotaalRedBull))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van Water:              " + " €" + str(TotaalWater))
print("==============================================================")

#Totaal te betalen bedrag
print("Te betalen bedrag: " + "€" + str(TotaalBestelling))