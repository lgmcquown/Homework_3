def ParseEle(ElementData):
    Symbol = ElementData[0] 
    Eledict[Symbol] = {"MM" : ElementData[1], "Z" : ElementData[2], "rho" : ElementData[3]}
    NumIsos = ElementData[4]
