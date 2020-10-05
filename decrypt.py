from cryptography.fernet import Fernet
import os

def load_key():
    """
        Función que carga la clave
    """
    return open('key.key','rb').read()

def decrypt(items, key):
    """
        Función para desencriptar
    """
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(item, 'wb') as file:
            file.write(decrypted_data)

if __name__ == '__main__': #esta condición siempre se cumple por lo tanto metemos
    #ruta
    path_to_encrypt = 'C:\\Users\\Jarvis\\Desktop\\Proyectos\\ramson'
    #remuevo el archivo de rescate
    os.remove(path_to_encrypt+'\\'+'rescate.txt')

    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+ item for item in items] # le sumo a la ruta el archivo por cada item de la lista de items -> 'C:\\Users\\Jarvis\\Desktop\\Proyectos\\ramson' + \\ 1.txt

    key = load_key()

    decrypt(full_path, key) #ejecuto la desencriptación
