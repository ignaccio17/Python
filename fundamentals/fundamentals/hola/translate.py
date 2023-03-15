#En cmd
# pip install googletrans==4.0.0-rc1


from googletrans import Translator

translator = Translator()

# Ingresa el texto que deseas traducir
texto_a_traducir = input("Ingresa el texto que deseas traducir: ")

# Ingresa el idioma al que deseas traducir el texto
idioma_destino = input("Ingresa el idioma al que deseas traducir el texto: ")

# Traduce el texto al idioma deseado
texto_traducido = translator.translate(texto_a_traducir, dest=idioma_destino)

# Imprime el resultado
print(texto_traducido.text)