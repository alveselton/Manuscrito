import pywhatkit as kit

def print_manuscrito():
    kit.text_to_handwriting(
        "Em quatro jogos, Rogerio\n"
        "Ceni usa 23 jogadores no\n"
        "Sao Paulo e confia em meio - campo\n"
        "made in Cotia", rgb=(1, 2, 255))

if __name__ == '__main__':
    print_manuscrito()
