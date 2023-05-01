print("=======================================\n")
print("         Automação de processo         ")
print("           Manual customizado          \n")
print("=======================================\n\n")

chrm = input("Deseja instalar o Chrome?\nResponder com s/n: ")
firf = input("Deseja instalar o Firefox?\nResponder com s/n: ")
winr = input("Deseja instalar o Winrar?\nResponder com s/n: ")
adbr = input("Deseja instalar o Adobe Reader?\nResponder com s/n: ")
anyd = input("Deseja instalar o AnyDesk?\nResponder com s/n: ")
offc = input("Deseja instalar o Office?\nResponder com s/n: ")
                
if chrm in ['S', 's']:  
    chrm = "winget install Google.Chrome && "
elif chrm in ['N', 'n']:
    chrm = ""

if firf in ['S', 's']:  
    firf = "winget install 9NZVDKPMR9RD && "
elif firf in ['N', 'n']:
    firf = ""

if winr in ['S', 's']:  
    winr = "winget install RARLab.WinRAR && "
elif winr in ['N', 'n']:
    winr = ""

if adbr in ['S', 's']:  
        adbr = "winget install XPDP273C0XHQH2 && "
elif adbr in ['N', 'n']:
        adbr = ""

if anyd in ['S', 's']:  
        anyd = "winget install AnyDeskSoftwareGmbH.AnyDesk && "
elif anyd in ['N', 'n']:
        anyd = ""

if offc in ['S', 's']:  
        offc = "winget install 9WZDNCRD29V9"
elif offc in ['N', 'n']:
        offc = ""
        result = chrm + firf + winr + adbr + anyd + offc
        print(result)
        result = result[:-3]
        print(result)