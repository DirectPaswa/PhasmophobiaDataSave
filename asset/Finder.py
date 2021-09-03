import os
import getpass
user = getpass.getuser()

PATH = f'C:\\Users\\{user}\\AppData\\LocalLow\\Kinetic Games\\Phasmophobia'
fileNameStuff = 'saveData.txt'

def searchFile(fileName):
    for root, dirs, files in os.walk(PATH):
        print('Looking in:',root)
        for Files in files:
            try:
                found = Files.find(fileName)
                # print(found)
                if found != -1:
                    print(PATH, files)
                    print(fileName, 'Found\n')

                    global filePATH
                    filePATH = os.path.join(PATH, fileNameStuff)
                    l = os.path.isdir(PATH)
                    p = os.path.isfile(filePATH)
                    print(l + 'Directory Path Found/Exist')
                    print('-\/-\/-\/-')
                    print(p + 'File Path Found/Exist')

                    break
            except:
                print('Worked!')
                


