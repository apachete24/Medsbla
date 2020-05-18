from funciones import *
import time
import pprint

pp = pprint.PrettyPrinter(indent=4, compact=True, width=42)
option = "0"

while option != "5":

    print(
            """
        * * * * * * * * * * * * * * * * * * * *
        *                                     *
        *   1)Get Interfaces configuration    *
        *                                     *
        *   2)New Loopback Interface          *
        *                                     *
        *   3)Remove Logical Interface        *
        *                                     *
        *   4)Show ip Route                   *
        *                                     *
        *   5)Exit                            *
        *                                     *
        * * * * * * * * * * * * * * * * * * * *
            """
        )

    option = input(">>>>>")
# mostrar configuracion de las interfaces
    if (option == "1"):
       print("En proceso...")

# añadir interfaz
    elif (option == "2"):
        
        number = input("Interface number: ")
        ip = input("Ip address: ")
        mask = input("Netmask: ")
        description = input("Descripcion: ")
        try:
            reply = new_if(number, ip, mask, description)
        except:
            print("An error has occurred during request\n. Check your input information")
            time.sleep(5)


#eliminar interfaz
    elif (option == "3"):
        name = input("Interface name: ")
        remove_if(name)



# no es lo que se pedía, pero pensé que mejor que nada es
    elif (option == "4"):
        output = ssh_command("show ip route")
        pp.pprint(output)




    elif (option == "5"):
        print("See you soon ;) ")
        break




    else:
        print("***********************OPCIÓN INCORRECTA*************************")
        time.sleep(2.5)

 