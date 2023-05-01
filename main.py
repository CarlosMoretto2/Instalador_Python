import pyautogui
import time
import win32com.client as win32
from win32api import GetKeyState 
from win32con import VK_NUMLOCK 
import os

package = manual = chrm = firf = adbr = winr = anyd = offc = result =  None

print("=======================================\n")
print("         Automação de processo         ")
print("Prefeitura Municipal de Jaguariúna 2023\n")
print("=======================================")

print("\n\nLembre-se de desabilitar a solicitação de acesso nível ADM do windows, aperte win e digite UAC!")
print("\n\nCaso a instalação dê algum erro, insira M/m para habilitar a instalação manual")

package = input("\n\nDeseja instalar o pacote de software padrão? Chrome, Firefox, Winrar, Adobe Reader, AnyDesk, Office. \nResponder com s/n/m: ")

if package in ['M', 'm']:

        os.system('cls') or None

        print("=======================================\n")
        print("         Automação de processo         ")
        print("              Modo Manual              \n")
        print("=======================================\n\n")

        manual = input("\n\nDeseja instalar o pacote de software padrão de maneira manual? Chrome, Firefox, Winrar, Adobe Reader, AnyDesk, Office. \nResponder com s/n: ")

        if manual in ['S' , 's']:
                pyautogui.hotkey('winleft', 'r')
                pyautogui.write('cmd')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write("winget install Google.Chrome && winget install 9NZVDKPMR9RD && winget install RARLab.WinRAR && winget install XPDP273C0XHQH2 && widget install AnyDeskSoftwareGmbH.AnyDesk && winget install 9WZDNCRD29V9")
                pyautogui.press('enter')

        elif manual in ['N', 'n']:
                os.system('cls') or None

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
                        result = chrm + firf + winr + adbr + anyd + offc
                elif offc in ['N', 'n']:
                        offc = ""
                        result = chrm + firf + winr + adbr + anyd + offc
                        result = result[:-3]
                
                pyautogui.hotkey('winleft', 'r')
                pyautogui.press('delete')
                pyautogui.write('cmd')
                pyautogui.press('enter')
                pyautogui.write(''+result)
                pyautogui.press('enter')

        else: 
                print('Insira um parâmetro válido.')

elif package in ['S', 's']:
    
        pyautogui.hotkey('winleft', 'r')
        pyautogui.write('powershell')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe')
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.write('taskkill /f /im powershell.exe')
        pyautogui.press('enter')



        pyautogui.pause = 1.0

        pyautogui.hotkey('winleft', 'r')
        pyautogui.write('cmd')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write("winget install Google.Chrome && winget install Mozilla.Firefox && winget install RARLab.WinRAR && winget install Adobe.Acrobat.Reader.64-bit && widget install AnyDeskSoftwareGmbH.AnyDesk && winget install Microsoft.Office")
        pyautogui.press('enter')


elif package in ['N', 'n']: 
        os.system('cls') or None

        print("=======================================\n")
        print("         Automação de processo         ")
        print("          Escolha customizada          \n")
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
                firf = "winget install Mozilla.Firefox && "
        elif firf in ['N', 'n']:
                firf = ""

        if winr in ['S', 's']:  
                winr = "winget install RARLab.WinRAR && "
        elif winr in ['N', 'n']:
                winr = ""

        if adbr in ['S', 's']:  
                adbr = "winget install Adobe.Acrobat.Reader.64-bit && "
        elif adbr in ['N', 'n']:
                adbr = ""

        if anyd in ['S', 's']:  
                anyd = "winget install AnyDeskSoftwareGmbH.AnyDesk && "
        elif anyd in ['N', 'n']:
                anyd = ""

        if offc in ['S', 's']:  
                offc = "winget install Microsoft.Office"
                result = chrm + firf + winr + adbr + anyd + offc
                                
        elif offc in ['N', 'n']:
                offc = ""
                
                result = chrm + firf + winr + adbr + anyd + offc
                result = result[:-3]
                
        else: 
                print('Insira um parâmetro válido.')

        pyautogui.hotkey('winleft', 'r')
        pyautogui.write('powershell')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe')
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.write('taskkill /f /im powershell.exe')
        pyautogui.press('enter')

        pyautogui.hotkey('winleft', 'r')
        pyautogui.press('delete')
        pyautogui.write('cmd')
        pyautogui.press('enter')
        pyautogui.write(''+result)
        pyautogui.press('enter')
else: 
        print("Insira um parâmetro válido")


    








