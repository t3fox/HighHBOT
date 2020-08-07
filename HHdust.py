from hhUI import CreativBO
import time
import subprocess
import shutil

class NetFallot(CreativBO):

    def __init__(self):
        pass

    def farmer(self,nhbo,dirhhbo):

        while True:

            for n in range(1,nhbo):

                fileUName = "mrBlue"
                flfinal = ".py"
                flnumb = n

                #JefeEscoba = False
                dirBO = shutil.copy("theUsr.py","C:/Users/t3fox/Desktop/IT/{}{}{}{}".format(dirhhbo,fileUName,flnumb,flfinal))
                print("\n\t----- Generando Nuevo_Usuario -----")
                time.sleep(.5)

            print("\n\n----- Proceso Terminado -----\n\n")
            break


    def newWin(self):

    # LibService=C://ruta/libreria.tx

        time.sleep(2)

        subprocess.call("cls",shell=True)
        print("\n\t\n---- Cargando librerias -----\n\n")

        self.user_id = input("\nLib usuarios.txt :> ")
        time.sleep(1)

        self.service_id = input("\nLib service.txt :> ")

        subprocess.call("cls",shell=True)

        print("\n\nDir usuarios.txt : ",self.user_id)
        print("\nDir service.txt : ",self.service_id)

        print("\n\t\n---- Asignando Identidad -----\n\n")




