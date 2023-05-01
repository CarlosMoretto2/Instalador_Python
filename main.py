import pyautogui
import time
import win32com.client as win32
from win32api import GetKeyState 
from win32con import VK_NUMLOCK 
import os

print("=======================================\n")
print("         Automação de processo         ")
print("Prefeitura Municipal de Jaguariúna 2023\n")
print("=======================================")

print("\n\nLembre-se de desabilitar a solicitação de acesso nível ADM do windows, aperte win e digite UAC!")

package = input("\n\nDeseja instalar o pacote de software padrão? Chrome, Firefox, Winrar, Adobe Reader, AnyDesk, Office. \nResponder com s/n: ")

if package in ['S', 's']:
    
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
        anyd = "widget install AnyDeskSoftwareGmbH.AnyDesk && "
elif anyd in ['N', 'n']:
         anyd = ""

if offc in ['S', 's']:  
        offc = "winget install Microsoft.Office"
elif offc in ['N', 'n']:
        offc = ""
    
result = chrm + firf + winr + adbr + anyd + offc

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


    


    








