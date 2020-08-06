import HHdust

class CreativBO:

    def __init__(self,tyBot,numBt,usrh,servh):
        self.TPBot = tyBot
        self.nNum = numBt
        self.user_id = usrh
        self.service_id = servh

    def SelectorBt(self):

        print("""\n\n\n
        ****************************************************************
        ****************************************************************
        ******1010010**********110101010***************01010************
        *****01010***************01001***************100***001**********
        *****110*****************11010***************011***101**********
        *****0011****************01100**************101*****101*********
        ******010100*************10101*************010*******010********
        ********001010***********10010*************100*******101********
        ***********0101**********01100************010*********100*******
        ************010**********10010************100*********101*******
        ***********1011**********01001***********101***********101******
        ********100101***********10010***********010***********110******
        ******0100100**********100110101********101*************100*****
        ****************************************************************
        ****************************************************************
        ________________________________________________________________
                |HighHBOT|                |V.1.1.5|\n\n""")

        print ("----- Selecione tipo de bot -----\n\n")
        print(" > 1 - Facebook")
        print(" > 2 - Instagram")
        print(" > 3 - Twitter ")

        self.TPBot = int(input("> "))


    #UI Blue
        if (self.TPBot == 1):
            print("\n----- USR_Facebook -----\n")
            print("Cantidad de usuarios:\n ")
            print("A>25")
            print("B>50")
            print("C>100")

            self.nNum = str(input("> "))

            if(self.nNum == "A" or self.nNum == "a"):

                #Genesis code
                Genesis = HHdust.NetFallot()
                Genesis.farmer()

                #lib Code
                libs = HHdust.NetFallot()
                libs.newWin()


            elif(self.nNum == "B" or self.nNum == "b"):

                #Genesis code
                Genesis = HHdust.NetFallot()
                Genesis.farmer()

                #lib Code
                libs = HHdust.NetFallot()
                libs.newWin()

            elif(self.nNum == "C" or self.nNum == "c"):

                #Genesis code
                Genesis = HHdust.NetFallot()
                Genesis.farmer()

                #lib Code
                libs = HHdust.NetFallot()
                libs.newWin()

            else:
                print("selecciona una opcion valida")

        #TP-02
        elif(self.TPBot == 2):
            print("\n----- USR_Instagram-----\n")
            print("Cantidad de usuarios:\n ")
            print("A>25")
            print("B>50")
            print("C>100")

            self.nNum = str(input("> "))

            if(self.nNum == "A" or self.nNum == "a"):

                #Genesis code
                Genesis = HHdust.NetFallot()
                Genesis.farmer()

                #lib Code
                libs = HHdust.NetFallot()
                libs.newWin()

            elif(self.nNum == "B" or self.nNum == "b"):

                #Genesis code
                Genesis = HHdust.NetFallot()
                Genesis.farmer()

                #lib Code
                libs = HHdust.NetFallot()
                libs.newWin()

            elif(self.nNum == "C" or self.nNum == "c"):

                #Genesis code
                Genesis = HHdust.NetFallot()
                Genesis.farmer()

                #lib Code
                libs = HHdust.NetFallot()
                libs.newWin()

            else:
                print("selecciona una opcion valida")

        #TP
        elif(self.TPBot == 3):
            print("\n----- USR_Twitter----\n")
            print("Cantidad de usuarios:\n ")
            print("A>25")
            print("B>50")
            print("C>100")

            self.nNum = str(input("> "))

            if(self.nNum == "A" or self.nNum == "a"):

                #Genesis code
                Genesis = HHdust.NetFallot()
                Genesis.farmer()

                #lib Code
                libs = HHdust.NetFallot()
                libs.newWin()

            elif(self.nNum == "B" or self.nNum == "b"):

                #Genesis code
                Genesis = HHdust.NetFallot()
                Genesis.farmer()

                #lib Code
                libs = HHdust.NetFallot()
                libs.newWin()

            elif(self.nNum == "C" or self.nNum == "c"):

                #Genesis code
                Genesis = HHdust.NetFallot()
                Genesis.farmer()

                #lib Code
                libs = HHdust.NetFallot()
                libs.newWin()

            else:
                print("selecciona una opcion valida")

        else:
            print("selecciona una opcion valida")



