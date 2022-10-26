import re

#son una secuencia de caracteres que forman un patron de busqueda,sirve para buscar una cadena de texto caracteres o conincidncias hay de palabras o numeros 

cadena = "vamos aprender expresiones regulares"
print(re.search ("aprender" , cadena))

buscar= "aprender"
textoEncontrado =re.search(buscar , cadena)
print (textoEncontrado.start())
print (textoEncontrado.end())
print (textoEncontrado.span())

cadena2 = "expresiones en Python. Python es un lenguaje de programacion "
textoPython = "Python"
print(re.findall(textoPython, cadena2))
print(len(re.findall(textoPython, cadena2)))