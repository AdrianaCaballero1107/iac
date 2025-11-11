# Importamos los módulos necesarios de la librería cryptography y del sistema operativo
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom  # Para generar datos aleatorios seguros (clave e IV)

# ------------------------------------------------------------
# Función para generar una clave y un vector de inicialización (IV)
# ------------------------------------------------------------
def generar_clave_y_iv():
    """Genera una clave AES de 32 bytes (AES-256) y un IV de 16 bytes"""
    key = urandom(32)  # 32 bytes = 256 bits, para AES-256
    iv = urandom(16)   # 16 bytes (128 bits), tamaño estándar del bloque AES
    return key, iv


# ------------------------------------------------------------
# Función para encriptar texto
# ------------------------------------------------------------
def encriptar(texto_plano, key, iv):
    """Encripta texto plano usando AES en modo CBC."""
    
    # Crear el objeto Cipher con el algoritmo AES, modo CBC y el backend por defecto
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()  # Objeto que realizará la encriptación

    # Convertir el texto a bytes
    texto_plano_bytes = texto_plano.encode('utf-8')

    # --- Padding ---
    # El algoritmo AES trabaja con bloques de 16 bytes.
    # Si el texto no es múltiplo de 16, se le agrega "padding" (relleno)
    padding_length = 16 - (len(texto_plano_bytes) % 16)
    padding = bytes([padding_length]) * padding_length
    texto_a_cifrar = texto_plano_bytes + padding

    # Encriptar el texto con el objeto encryptor
    texto_cifrado = encryptor.update(texto_a_cifrar) + encryptor.finalize()
    return texto_cifrado


# ------------------------------------------------------------
# Función para desencriptar texto
# ------------------------------------------------------------
def desencriptar(texto_cifrado, key, iv):
    """Desencripta texto cifrado usando AES en modo CBC."""
    
    # Crear el objeto Cipher con los mismos parámetros que se usaron para cifrar
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()  # Objeto que realizará la desencriptación

    # Desencriptar el texto cifrado
    texto_desencriptado_con_padding = decryptor.update(texto_cifrado) + decryptor.finalize()

    # --- Quitar el padding ---
    # El último byte indica cuántos bytes de padding se añadieron
    padding_length = texto_desencriptado_con_padding[-1]
    texto_desencriptado = texto_desencriptado_con_padding[:-padding_length]

    # Convertir los bytes a texto legible (UTF-8)
    return texto_desencriptado.decode('utf-8')


# ------------------------------------------------------------
# --- Ejemplo de uso del programa ---
# ------------------------------------------------------------

# 1. Generar clave y vector de inicialización (IV)
key, iv = generar_clave_y_iv()

# 2. Texto original a encriptar
texto_original = "Adriana Caballero Manuel"

# 3. Encriptar el texto original
texto_encriptado = encriptar(texto_original, key, iv)
print(f"Texto encriptado: {texto_encriptado}")

# 4. Desencriptar el texto encriptado
texto_desencriptado = desencriptar(texto_encriptado, key, iv)
print(f"Texto desencriptado: {texto_desencriptado}")
