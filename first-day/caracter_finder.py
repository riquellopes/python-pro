from sys import maxunicode
import unicodedata


def procurar_char(palavra):
    """
        Procurar caracter que contenha palavra em seu nome.
        :param palavra: string
        :return Lista com tuplas (caracter, nome do caracter)
        >>> ("♡", 'WHITE HEART SUIT') in procurar_char("suit")
        True
    """
    lista = []
    for x in range(0, maxunicode):
        char = chr(x)
        try:
            name = unicodedata.name(char)
            if palavra.upper() in name.upper():
                lista.append((char, name))
        except ValueError:
            continue
    return lista

if __name__ == "__main__":
    saida = procurar_char("suit")
    print(saida)
