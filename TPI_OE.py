def cargar_empleados():
    empleados= []
    try:
        with open("empleados.csv", "r", encoding= "utf-8")as archivo:
            next(archivo) # Hace que salte la linea del encabezado
            
            for linea in archivo:
                try:
                
                    legajo, nombre, saldo = linea.strip().split(",")
                    empleado = {
                        "legajo": legajo,
                        "nombre": nombre,
                        "saldo": int(saldo)
                    }

                    
                    empleados.append(empleado)
                
                except ValueError as error: # Maneja el error si en el csv en la columna saldo no hay un int
                    print(f"Ha ocurrido un error de conversion: {error}")
                
                except KeyError as error: # Maneja un error en el csv, por si falta una columna
                    print(f"Falta la columna: {error}")
                

                
        return empleados
    except FileNotFoundError:
        print("El archivo no existe en la ubicación brindada.")

def carga_solicitud():
    solicitudes = []

    try:
        with open("vacaciones.csv", "r", encoding= "utf-8") as archivo:
            next(archivo) # Saltea el encabezado

            for linea in archivo:
                try:
                
                    legajo, fecha, estado= linea.strip().split(",")
                    solicitud = {
                        "legajo": legajo,
                        "fecha": fecha,
                        "estado": estado
                        }
                    solicitudes.append(solicitud)
                
                except ValueError as error: # Maneja un error en el csv, por si falta una columna
                    print(f"Linea con formato incorrecto: {linea.strip()}")
                    
        return solicitudes
        
    except FileNotFoundError:
        print("El archivo no existe en la ubicación brindada.")
    
def validar_legajo(empleados):
        
    while True:

        try:
            id = input("Ingrese su legajo: ")

            if not id.isdigit():
                raise ValueError ("El legajo debe ser numérico.")
        
        except ValueError as error:
            print(error)
            continue # Vuelve al inicio del programa

        for empleado in empleados:
            if empleado["legajo"] == id :
                return id
        
        print ("Legajo no encontrado, intente nuevamente.")

def consultar_saldo(legajo, empleados):
    for empleado in empleados:
        if empleado["legajo"] == legajo:
            if empleado["saldo"] > 0:
                print(f"Saldo disponible, cantidad de dias: {empleado['saldo']}")
                return True
            else:
                return False
            
def SolicitarValidar_Dias(legajo, empleados):
    
    saldo = 0
    
    for empleado in empleados:
        
        if empleado["legajo"] == legajo:
            saldo = empleado["saldo"]

    while True:

        dias=input("¿Cuantos dias de vacaciones querés solicitar?\n ")
        

        if not dias.isdigit():
            print("Error, ingresá un numero entero válido. ")
            continue

        dias = int(dias)

        if dias <= saldo:
            print("Cantidad de dias solicitados válido.")
            return True
        else:
            print("No tenés los días suficientes, intenta con menos.")
            

        


        




