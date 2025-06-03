from flask import request
from flask_restful import Resource

# Diccionario del alfabeto para conversión
alfabeto = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
    'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
    'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
    'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
    'Y': 24, 'Z': 25,
}

# Lista para conversión inversa (más eficiente que usar list(alfabeto.keys())[indice])
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class Vegenere(Resource):
    def post(self):
        try:
            data = request.get_json()
            
            # Validaciones de entrada
            if not data:
                return {"error": "No se recibieron datos JSON válidos"}, 400
            
            texto = data.get("texto")
            clave = data.get("clave", "CLAVE")  # Clave por defecto
            
            if not texto:
                return {"error": "No se proporcionó texto para cifrar"}, 400
            
            if not isinstance(texto, str):
                return {"error": "El texto debe ser una cadena"}, 400
            
            if not isinstance(clave, str):
                return {"error": "La clave debe ser una cadena"}, 400
            
            # Validar que la clave solo contenga letras
            clave = clave.upper()
            if not all(c in alfabeto for c in clave):
                return {"error": "La clave debe contener solo letras del alfabeto"}, 400
            
            if len(clave) == 0:
                return {"error": "La clave no puede estar vacía"}, 400
            
            # Proceso de cifrado
            texto = texto.upper()
            cifrado = ""
            
            # Repetir la clave para que coincida con la longitud del texto
            clave_repetida = (clave * (len(texto) // len(clave) + 1))[:len(texto)]
            print(f"Clave repetida: {clave_repetida}")  # Debugging
            for i, char in enumerate(texto):
                if char in alfabeto:
                    desplazamiento = alfabeto[clave_repetida[i]]
                    indice_cifrado = (alfabeto[char] + desplazamiento) % 26
                    cifrado += letras[indice_cifrado]
                else:
                    # Preservar caracteres que no son letras (espacios, números, puntuación)
                    cifrado += char
            
            return {
                "texto_original": data.get("texto"),
                "resultado": cifrado,
                "clave_utilizada": clave,
                "metodo": "Cifrado de Vigenère"
            }, 200
            
        except Exception as e:
            return {"error": f"Error interno del servidor: {str(e)}"}, 500

class vegenereDescifrar(Resource):
    def post(self):
        try:
            data = request.get_json()
            
            # Validaciones de entrada
            if not data:
                return {"error": "No se recibieron datos JSON válidos"}, 400
            
            texto_cifrado = data.get("texto")
            clave = data.get("clave", "CLAVE")
            
            if not texto_cifrado:
                return {"error": "No se proporcionó texto para descifrar"}, 400
            
            if not isinstance(texto_cifrado, str):
                return {"error": "El texto debe ser una cadena"}, 400
            
            if not isinstance(clave, str):
                return {"error": "La clave debe ser una cadena"}, 400
            
            # Validar que la clave solo contenga letras
            clave = clave.upper()
            if not all(c in alfabeto for c in clave):
                return {"error": "La clave debe contener solo letras del alfabeto"}, 400
            
            if len(clave) == 0:
                return {"error": "La clave no puede estar vacía"}, 400
            
            # Proceso de descifrado
            texto_cifrado = texto_cifrado.upper()
            descifrado = ""
            
            # Repetir la clave para que coincida con la longitud del texto
            clave_repetida = (clave * (len(texto_cifrado) // len(clave) + 1))[:len(texto_cifrado)]
            
            for i, char in enumerate(texto_cifrado):
                if char in alfabeto:
                    desplazamiento = alfabeto[clave_repetida[i]]
                    # Para descifrar, restamos el desplazamiento
                    indice_descifrado = (alfabeto[char] - desplazamiento) % 26
                    descifrado += letras[indice_descifrado]
                else:
                    # Preservar caracteres que no son letras
                    descifrado += char
            
            return {
                "texto_cifrado": data.get("texto"),
                "resultado": descifrado,
                "clave_utilizada": clave,
                "metodo": "Descifrado de Vigenère (Poligráfico)"
            }, 200
            
        except Exception as e:
            return {"error": f"Error interno del servidor: {str(e)}"}, 500