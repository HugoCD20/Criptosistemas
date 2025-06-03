from flask import request
from flask_restful import Resource
import numpy as np

class Poligrafica(Resource):
    def post(self):
        data= request.get_json()
        if not data:
            return {"error": "No hay datos"}, 400

        # Extraer los datos necesarios del JSON
        texto = data.get("texto")
        clave = data.get("clave",[3, 2, 5, 7])

        # Funciones auxiliares para el cifrado Hill

        def limpiar_texto(texto):
            return ''.join([c for c in texto.upper() if c.isalpha()])

        def texto_a_numeros(texto):
            return [ord(c) - ord('A') for c in texto]

        def numeros_a_texto(nums):
            return ''.join([chr(n % 26 + ord('A')) for n in nums])

        def cifrar_hill(texto, clave):
            texto = limpiar_texto(texto)
            n = int(len(clave) ** 0.5)
            matriz_clave = np.array(clave).reshape((n, n))
            while len(texto) % n != 0:
                texto += 'X'
            texto_nums = texto_a_numeros(texto)
            texto_cifrado = []
            for i in range(0, len(texto_nums), n):
                bloque = np.array(texto_nums[i:i+n])
                cifrado = np.dot(matriz_clave, bloque) % 26
                texto_cifrado.extend(cifrado)
            return numeros_a_texto(texto_cifrado)

        # Validar y convertir la clave
        if not isinstance(clave, list):
            return {"error": "La clave debe ser una lista de números"}, 400

        n = int(len(clave) ** 0.5)
        if n * n != len(clave):
            return {"error": "La clave debe tener una longitud cuadrada perfecta"}, 400

        try:
            texto_cifrado = cifrar_hill(texto, clave)
        except Exception as e:
            return {"error": f"Error al cifrar: {str(e)}"}, 400

        return {"resultado": texto_cifrado}, 200