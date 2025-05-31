from flask_restful import Resource
from flask import request
class sustitucion(Resource):
    def post(self):
        alfabeto = {
            'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I',
            'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O',
            'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U',
            'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A',
            'Y': 'B', 'Z': 'C',
        }

        data = request.get_json()
        texto = data.get("texto")
        if not texto:
            return {"error": "No se proporcionó texto para cifrar"}, 400

        texto = texto.upper()
        cifrado = ""
        for i in texto:
            if i in alfabeto:
                cifrado += alfabeto[i]
            else:
                cifrado += i

        return {"resultado": cifrado}, 200

class decodificacicion(Resource):
    def post(self):
        alfabeto = {
            'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F',
            'J': 'G', 'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L',
            'P': 'M', 'Q': 'N', 'R': 'O', 'S': 'P', 'T': 'Q', 'U': 'R',
            'V': 'S', 'W': 'T', 'X': 'U', 'Y': 'V', 'Z': 'W', 'A': 'X',
            'B': 'Y', 'C': 'Z'
        }


        data = request.get_json()
        texto = data.get("texto")
        if not texto:
            return {"error": "No se proporcionó texto para cifrar"}, 400

        texto = texto.upper()
        cifrado = ""
        for i in texto:
            if i in alfabeto:
                cifrado += alfabeto[i]
            else:
                cifrado += i

        return {"resultado": cifrado}, 200


        
        