from flask_restful import Resource
from flask import request

alfabeto = {
    'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I',
    'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O',
    'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U',
    'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A',
    'Y': 'B', 'Z': 'C',
}
alfabeto2 = {
    'A': 'O', 'B': 'P', 'C': 'Q', 'D': 'R', 'E': 'S', 'F': 'T',
    'G': 'U', 'H': 'V', 'I': 'W', 'J': 'X', 'K': 'Y', 'L': 'Z',
    'M': 'A', 'N': 'B', 'O': 'C', 'P': 'D', 'Q': 'E', 'R': 'F',
    'S': 'G', 'T': 'H', 'U': 'I', 'V': 'J', 'W': 'K', 'X': 'L',
    'Y': 'M', 'Z': 'N'
}
class polialfabetica(Resource):
    def post(self):
        data = request.get_json()
        texto = data.get("texto")
        if not texto:
            return {"error": "No se proporcionó texto para cifrar"}, 400

        texto = texto.upper()
        cifrado = ""
        for indice, letra in enumerate(texto):
            if indice % 2 == 0:
                if letra in alfabeto:
                    cifrado += alfabeto[letra]
                else:
                    cifrado += letra
            else:
                if letra in alfabeto2:
                    cifrado += alfabeto2[letra]
                else:
                    cifrado += letra
        return {"resultado": cifrado}, 200

class decodificacion(Resource):
    def post(self):
        inverso = {valor: clave for clave, valor in alfabeto.items()}
        inverso2 = {valor: clave for clave, valor in alfabeto2.items()}
        data = request.get_json()
        texto = data.get("texto")
        if not texto:
            return {"error": "No se proporcionó texto para cifrar"}, 400

        texto = texto.upper()
        cifrado = ""
        for indice, letra in enumerate(texto):
            if indice % 2 == 0:
                if letra in inverso:
                    cifrado += inverso[letra]
                else:
                    cifrado += letra
            else:
                if letra in inverso2:
                    cifrado += inverso2[letra]
                else:
                    cifrado += letra
        return {"resultado": cifrado}, 200


        