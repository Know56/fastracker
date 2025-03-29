import os
import datetime
import pyfiglet

# Activar secuencias ANSI en Windows para colores
os.system("")  
 
info = "This tool is in beta phase, it has been programmed by Fsociety."

# Banner con estilo verde brillante
print("\033[32m")
print("""
  _____     ____  _   ____        ____ _    _____      
 |  ___|_ _/ ___|| |_|  _ \ __ _ / ___| | _| ____|_ __ 
 | |_ / _` \___ \| __| |_) / _` | |   | |/ /  _| | '__| 
 |  _| (_| |___) | |_|  _ < (_| | |___|   <| |___| |   
 |_|  \__,_|____/ \__|_| \_\__,_|\____|_|\_\_____|_|   
                                                  
  Type 'help' to see available commands.
""")
print("\033[0m")  # Reset de colores

print("\033[1;36m")
print("1-RAT generator")
print("\033[0m")

# Función para mostrar "WE SEE YOU ALL" con estilo
def show_wds_message():
    try:
        ascii_art = pyfiglet.figlet_format("WE SEE YOU ALL", font="small_caps")
    except pyfiglet.FontNotFound:
        ascii_art = pyfiglet.figlet_format("WE SEE YOU ALL", font="slant")  # Fuente alternativa

    print("\033[1;31m" + ascii_art + "\033[0m")  # Texto en rojo brillante

while True:
    userinput = input("\033[1;32mftck> \033[0m").strip().split()
    
    if not userinput:
        continue
    
    command = userinput[0].lower()
    args = userinput[1:]

    if command == "exit":
        print("\033[1;31mBye!\033[0m")  # Texto rojo brillante al salir
        break
    elif command == "1":
        print("\033[31m")
        print("""                                                      
      -------------                -------------      
    ------------------          ------------------    
  ---------------------        ---------------------  
 ------..........--------    --------..........------ 
-----..............------    ------..............-----
----................------  ------................----
---.................--------------.................---
---............------------------------............---
----.........----------------------------.........----
 ----......--------------------------------......---- 
  ----....----------------------------------....----  
   ------------------------------------------------   
     --------------------------------------------     
         -------------------------------------        
         ----------+##+--------+##+----------         
         ---------######------######---------         
          --------######------######---------         
          --------######------######--------          
           -------+####+------+####+-------           
            ------------------------------            
             ----------------------------             
            +++-----------..-----------+++            
   ++++++++++++++++++--........--++++++++++++++++++   
+++++++++++++++++++----........----+++++++++++++++++++
++++   +++++++       ---......---       +++++++   ++++
     ++++++             ------             ++++++     
    +++++                                    +++++    
     ++                                        ++     
              
              ____      _  _____ ____ 
             |  _ \    / \|_   _/ ___|
             | |_) |  / _ \ | || |  _ 
             |  _ <  / ___ \| || |_| |
             |_| \_\/_/   \_\_| \____|
                 """)
        print("\033[0m")
       
                          

    elif command == "info":
        print(info)
    elif command == "clear":
        os.system("cls" if os.name == "nt" else "clear")
    elif command == "ls":
        os.system("dir" if os.name == "nt" else "ls")
    elif command == "wds":
        show_wds_message()
    elif command == "whoami":
        os.system("whoami")
    elif command == "date":
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    elif command == "mkdir":
        if args:
            os.makedirs(args[0], exist_ok=True)
            print(f"Directorio '{args[0]}' creado.")
        else:
            print("Uso: mkdir <nombre>")
    elif command == "rm":
        if args:
            target = args[0]
            if os.path.isdir(target):
                os.rmdir(target)
                print(f"Directorio '{target}' eliminado.")
            elif os.path.isfile(target):
                os.remove(target)
                print(f"Archivo '{target}' eliminado.")
            else:
                print(f"No se encontró '{target}'.")
        else:
            print("Uso: rm <archivo/directorio>")
    elif command == "echo":
        print(" ".join(args))
    elif command == "help":
        print("\033[1;36m")  # Texto cyan brillante
        print("""
Comandos disponibles:
- info      → Información del programa
- clear     → Limpia la pantalla
- ls        → Lista archivos en la carpeta actual
- wds       → Mensaje especial "WE SEE YOU ALL"
- whoami    → Muestra el usuario actual
- date      → Muestra la fecha y hora actual
- mkdir X   → Crea un directorio X
- rm X      → Elimina un archivo/directorio X
- echo X    → Muestra el texto X
- exit      → Salir del programa
""")
        print("\033[0m")  # Reset de colores
    else:
        print(f"\033[1;31mComando desconocido: {command}. Escribe 'help' para ver los comandos disponibles.\033[0m")
