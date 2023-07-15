import re
from unicodedata import normalize

def reverseString(str):
  return str[::-1]


def formattedString(str):
  # Eliminar diacríticos utilizando expresiones regulares y normalización
  formatted_string = re.sub(
    r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
    r"\1", normalize("NFD", str), 0, re.I)

  formatted_string = normalize('NFD', formatted_string)

  return formatted_string


print("""## DETECTOR DE PALABRAS PALÍNDROMO ##\n""")

word = input("Ingresa una palabra: ").lower()

# Eliminamos diacríticos y dieresis 
formatted_word = formattedString(word)

reverse_word = reverseString(formatted_word)

if (formatted_word == reverse_word):
  print(f"La palabra: \"{ word.capitalize() }\" es palindromo.")
else:
  print(f"La palabra: \"{ word.capitalize() }\", no es palindromo.")


"""
- re -> Biblioteca para expresiones regulares
- unicodedata -> biblioteca unicodedata proporciona funciones y datos para trabajar con caracteres Unicode
- normalize -> función para realizar operaciones de manipulación de texto en una cadena con caracteres diacríticos

Desglosemos los diferentes componentes de esta expresión regular:

[^n\u0300-\u036f]: Esta parte define una clase de caracteres negados [^...]. Significa que cualquier carácter que no sea n o que no esté en el rango Unicode \u0300-\u036f será una coincidencia. En resumen, coincide con cualquier carácter que no sea n ni un carácter diacrítico.

n(?!\u0303(?![\u0300-\u036f])): Aquí tenemos una coincidencia condicional. Coincidirá con la letra n solo si no está seguida por el carácter ̃ (tilde) seguido de otro carácter diacrítico. El (?!\u0303(?![\u0300-\u036f])) es un "negative lookahead" (búsqueda hacia adelante negativa) que asegura que no haya un tilde seguido de un carácter diacrítico después de la letra n. Esto evita coincidencias incorrectas en ciertos casos.

[\u0300-\u036f]+: Esta parte coincide con uno o más caracteres diacríticos. El rango Unicode \u0300-\u036f engloba una amplia gama de caracteres diacríticos utilizados en varios idiomas.

En resumen, esta expresión regular busca caracteres diacríticos o la letra n seguida de caracteres diacríticos, pero evita ciertos casos específicos donde la letra n está seguida de un tilde y otro carácter diacrítico.

Es importante tener en cuenta que el contexto en el que se utilice esta expresión regular determinará cómo se aplicará y qué resultados se obtendrán.


# la función re.sub para buscar y reemplazar patrones de expresiones regulares en la cadena str.
# La función normalize("NFD", str) se utiliza para descomponer la cadena s en caracteres Unicode utilizando la forma de normalización NFD (Forma de Normalización de Descomposición).
# La función re.sub reemplaza los caracteres diacríticos y las combinaciones 'n' seguidas de caracteres diacríticos con el contenido capturado en \1, que representa la primera coincidencia capturada en el patrón de expresión regular.
# La opción re.I indica que la coincidencia no distingue entre mayúsculas y minúsculas.
# La función normalize('NFC', formatted_string) se utiliza para normalizar la cadena s utilizando la forma de normalización NFC 
8Forma Normalización de Composición).
"""