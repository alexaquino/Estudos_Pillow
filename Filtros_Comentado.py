#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageFilter
import math
from random import randrange

# Obtendo Imagem Original
imagem_original = Image.open("apollo_10_RGB.jpg")
# Convertendo Imagem Original para o modo RGB
imagem = imagem_original.convert('RGB')
imagem.show()
#print(imagem.format, imagem.size, imagem.mode)

# Obtendo tamanho das componentes x, y
# Image.width e Image.height
largura, altura = imagem.size


# Escala de Cinza {
def cinza():
    print("Processando escala de cinza...")
    # Percorrendo Matriz de Pixels
    for x in range(largura):
        for y in range(altura):
            # Obtendo componente RGB do pixel atual
            R, G, B = imagem.getpixel((x, y))
            # Aplicando o padrão de vídeo digital ITU-R 601-2
            L = int((R * 299/1000) + (G * 587/1000) + (B * 114/1000))
            imagem.putpixel((x, y), (L, L, L))
    # Exibindo imagem modificada
    imagem.show()
#}
#cinza()


# Negativo {
def negativo():
    print("Processando negativo...")
    # Convertendo em escala de cinza
    #cinza()
    # Percorrendo Matriz de Pixels
    for x in range(largura):
        for y in range(altura):
            # Obtendo componente RGB pixel atual
            R, G, B = imagem.getpixel((x, y))
            # Modificando componentes RGB do pixel atual
            imagem.putpixel((x, y), (255 - R, 255 - G, 255 - B))
    # Exibindo imagem modificada
    imagem.show()
#}
#negativo()

# Binarização {
def binarizacao(limiar):
    print("Processando binarização...")
    # Convertendo em escala de cinza
    #cinza()
    # Percorrendo Matriz de Pixels
    for x in range(largura):
        for y in range(altura):
            # Obtendo componentes RGB pixel atual
            R, G, B = imagem.getpixel((x, y))
            # Modificando componentes RGB do pixel atual
            if ((R + G + B) / 3 <= limiar):
                imagem.putpixel((x, y), (0, 0, 0))
            else:
                imagem.putpixel((x, y), (255, 255, 255))
    # Exibindo imagem modificada
    imagem.show()
#}
#binarizacao(120)


# histograma() {
def histograma():
    print("Processando histograma...")
    # Convertendo em escala de cinza
    cinza()
    intensidade = []
    # Percorrendo Matriz de Pixels
    for x in range(largura):
        for y in range(altura):
            R, G, B = imagem.getpixel((x, y))
            intensidade.append(R);

    Xmin = min(intensidade)
    Xmax = max(intensidade)
    print({x:intensidade.count(x) for x in set(intensidade)})
    return Xmin, Xmax
#}
#histograma()


# realce() {
def realce():
    print("Processando realce...")
    # Obtendo Xmin e Xmax baseado no histograma
    Xmin, Xmax = histograma()
    # Aplicando os cálculos
    a = 255 / (Xmax - Xmin)
    b = -a * Xmin
    # Percorrendo Matriz de Pixels
    for x in range(largura):
        for y in range(altura):
            # Obtendo componentes RGB do pixel atual
            R, G, B = imagem.getpixel((x, y))
            # Aplicando os cálculos para obter nova componente
            Y = int(a * R + b)
            # Modificando componentes do pixel atual
            imagem.putpixel((x, y), (Y, Y, Y))
    # Exibindo imagem modificada
    imagem.show()
#}
#realce()


# Média {
def media_3x3():
    print("Processando média 3x3...")
    # Convertendo em escala de cinza
    #cinza()
    # Percorrendo Matriz de Pixels
    for x in range(1, largura - 2):
        for y in range(1, altura - 2):
            # Obtendo componentes RGB da vizinhança do pixel atual(mascara 3x3)
            R0, G0, B0 = imagem.getpixel((x - 1, y - 1))
            R1, G1, B1 = imagem.getpixel((x, y - 1))
            R2, G2, B2 = imagem.getpixel((x + 1, y - 1))
            R3, G3, B3 = imagem.getpixel((x - 1, y))
            R4, G4, B4 = imagem.getpixel((x, y))
            R5, G5, B5 = imagem.getpixel((x + 1, y))
            R6, G6, B6 = imagem.getpixel((x - 1, y + 1))
            R7, G7, B7 = imagem.getpixel((x, y + 1))
            R8, G8, B8 = imagem.getpixel((x + 1, y + 1))
            # Aplicando os cálculos para obter a média
            R = int((R0 + R1 + R2 + R3 + R4 + R5 + R6 + R7 + R8) / 9)
            G = int((G0 + G1 + G2 + G3 + G4 + G5 + G6 + G7 + G8) / 9)
            B = int((B0 + B1 + B2 + B3 + B4 + B5 + B6 + B7 + B8) / 9)
            # Modificando componentes RGB do pixel atual
            imagem.putpixel((x, y), (R, G, B))
    # Exibindo imagem modificada
    imagem.show()
#}
#media_3x3()


# Mediana {
def mediana_3x3():
    print("Processando mediana 3x3...")
    # Convertendo em escala de cinza
    #cinza()
    # Percorrendo Matriz de Pixels
    for x in range(1, largura - 2):
        for y in range(1, altura - 2):
            # Obtendo componentes RGB da "vizinhança" (3x3)
            R0, G0, B0 = imagem.getpixel((x - 1, y - 1))
            R1, G1, B1 = imagem.getpixel((x, y - 1))
            R2, G2, B2 = imagem.getpixel((x + 1, y - 1))
            R3, G3, B3 = imagem.getpixel((x - 1, y))
            R4, G4, B4 = imagem.getpixel((x, y))
            R5, G5, B5 = imagem.getpixel((x + 1, y))
            R6, G6, B6 = imagem.getpixel((x - 1, y + 1))
            R7, G7, B7 = imagem.getpixel((x, y + 1))
            R8, G8, B8 = imagem.getpixel((x + 1, y + 1))
            # Ordenando os valores e obtendo a mediana
            R = [R0, R1, R2, R3, R4, R5, R6, R7, R8]
            G = [G0, G1, G2, G3, G4, G5, G6, G7, G8]
            B = [G0, B1, B2, B3, B4, B5, B6, B7, B8]
            R.sort()
            G.sort()
            B.sort()
            # Modificando componentes RGB do pixel atual
            imagem.putpixel((x, y), (R[4], G[4], B[4]))
    # Exibindo imagem modificada
    imagem.show()
#}
#mediana_3x3()


# Ruído sal_pimenta {
def sal_pimenta():
    print("Processando ruído sal e pimenta...")
    # Convertendo imagem para tons de cinza
    #cinza()
    # Modificando pixels aleatoriamente
    for x in range(largura * randrange(largura)):
        if (x % 2 == 0):
            imagem.putpixel((randrange(largura), randrange(altura)), (0, 0, 0))
        else:
            imagem.putpixel((randrange(largura), randrange(altura)), (255, 255, 255))
    # Exibindo imagem modificada
    imagem.show()
#}
#sal_pimenta()


# Ruído gausiano {
def gausino():
    print("Processando ruído gausiano...")
    # Convertendo imagem para tons de cinza
    #cinza()
    # Modificando pixels aleatoriamente
    for x in range(largura * randrange(largura)):
        imagem.putpixel((randrange(largura), randrange(altura)), (randrange(255), randrange(255), randrange(255)))
    # Exibindo imagem modificada
    imagem.show()
#}
#gausino()


# Filtro Gaussiano {
def filtro_gaussiano():
    print("Processando filtro gausiano...")
    # Percorrendo Matriz de Pixels
    for x in range(1, largura - 2):
        for y in range(1, altura - 2):
            # Obtendo componentes RGB da mascara (3x3)
            R1, G1, B1 = imagem.getpixel((x, y))
            R2, G2, B2 = imagem.getpixel((x, y + 1))
            R3, G3, B3 = imagem.getpixel((x, y - 1))
            R4, G4, B4 = imagem.getpixel((x + 1, y))
            R5, G5, B5 = imagem.getpixel((x - 1, y))
            R6, G6, B6 = imagem.getpixel((x - 1, y - 1))
            R7, G7, B7 = imagem.getpixel((x + 1, y + 1))
            R8, G8, B8 = imagem.getpixel((x + 1, y - 1))
            R9, G9, B9 = imagem.getpixel((x - 1, y + 1))
            # Aplicando os cálculos (mascara [1 2 1] [2 4 2] [1 2 1])
            R = int(((R1 * 4) + (2 * (R2 + R3 + R4 + R5)) + (1 * (R6 + R7 + R8 + R9))) / 16)
            G = int(((G1 * 4) + (2 * (G2 + G3 + G4 + G5)) + (1 * (G6 + G7 + G8 + G9))) / 16)
            B = int(((B1 * 4) + (2 * (B2 + B3 + B4 + B5)) + (1 * (B6 + B7 + B8 + B9))) / 16)
            # Modificando componentes RGB do pixel atual
            imagem.putpixel((x, y), (R, G, B))
    # Exibindo imagem modificada
    imagem.show()
#}
#filtro_gaussiano()


# Sobel {
def sobel():
    print("Processando operador de sobel...")
    #Convertendo imagem para tons de cinza
    cinza()
    # Percorrendo Matriz de Pixels
    for x in range(1, largura - 2):
        for y in range(1, largura - 2):
            # Obtendo componentes RGB da mascara (3x3)
            R0, G0, B0 = imagem.getpixel((x - 1, y - 1))
            R1, G1, B1 = imagem.getpixel((x, y - 1))
            R2, G2, B2 = imagem.getpixel((x + 1, y - 1))
            R3, G3, B3 = imagem.getpixel((x - 1, y))
            R4, G4, B4 = imagem.getpixel((x, y))
            R5, G5, B5 = imagem.getpixel((x + 1, y))
            R6, G6, B6 = imagem.getpixel((x - 1, y + 1))
            R7, G7, B7 = imagem.getpixel((x, y + 1))
            R8, G8, B8 = imagem.getpixel((x + 1, y + 1))
            # Convolução (mascara horizontal)
            eixo_x = (-1 * R0) + (1 * R2) + (-2 * R3) + (2 * R5) + (-1 * R6) + (1 * R8)
            #eixo_x = eixo_x / 4
            # Convolução (mascara vertica)
            eixo_y = (-1 * R0) + (-2 * R1) + (-1 * R2) + (1 * R6) + (2 * R7) + (1 * R8)
            #eixo_y = eixo_x / 4
            # Obtendo valor de gradiente
            gradiente = math.sqrt((eixo_x ** 2) + (eixo_y ** 2))
            # Modificando componentes RGB do pixel atual
            imagem.putpixel((x, y), (int(gradiente), int(gradiente), int(gradiente)))
    # Exibindo imagem modificada
    imagem.show()
#}
#sobel()
#teste = imagem.filter(ImageFilter.CONTOUR)
#teste.show()


# roberts {
def roberts():
    print("Processando operador de roberts...")
    #Convertendo imagem para tons de cinza
    cinza()
    # Percorrendo Matriz de Pixels
    for x in range(1, largura - 2):
        for y in range(1, largura - 2):
            # Obtendo componentes RGB da mascara (3x3)
            R0, G0, B0 = imagem.getpixel((x - 1, y - 1))
            R1, G1, B1 = imagem.getpixel((x, y - 1))
            R2, G2, B2 = imagem.getpixel((x + 1, y - 1))
            R3, G3, B3 = imagem.getpixel((x - 1, y))
            R4, G4, B4 = imagem.getpixel((x, y))
            R5, G5, B5 = imagem.getpixel((x + 1, y))
            R6, G6, B6 = imagem.getpixel((x - 1, y + 1))
            R7, G7, B7 = imagem.getpixel((x, y + 1))
            R8, G8, B8 = imagem.getpixel((x + 1, y + 1))
            # Convolução (mascara horizontal)
            eixo_x = (-1 * R2) + (1 * R4)
            #eixo_x = eixo_x / 4
            # Convolução (mascara vertica)
            eixo_y = (-1 * R0)
            #eixo_y = eixo_x / 4
            # Obtendo valor de gradiente
            gradiente = math.sqrt((eixo_x ** 2) + (eixo_y ** 2))
            # Modificando componentes RGB do pixel atual
            imagem.putpixel((x, y), (int(gradiente), int(gradiente), int(gradiente)))
    # Exibindo imagem modificada
    imagem.show()
#}
#roberts()


# prewitt {
def prewitt():
    print("Processando operador de prewitt...")
    #Convertendo imagem para tons de cinza
    cinza()
    # Percorrendo Matriz de Pixels
    for x in range(1, largura - 2):
        for y in range(1, largura - 2):
            # Obtendo componentes RGB da mascara (3x3)
            R0, G0, B0 = imagem.getpixel((x - 1, y - 1))
            R1, G1, B1 = imagem.getpixel((x, y - 1))
            R2, G2, B2 = imagem.getpixel((x + 1, y - 1))
            R3, G3, B3 = imagem.getpixel((x - 1, y))
            R4, G4, B4 = imagem.getpixel((x, y))
            R5, G5, B5 = imagem.getpixel((x + 1, y))
            R6, G6, B6 = imagem.getpixel((x - 1, y + 1))
            R7, G7, B7 = imagem.getpixel((x, y + 1))
            R8, G8, B8 = imagem.getpixel((x + 1, y + 1))
            # Convolução (mascara horizontal)
            eixo_x = (-1 * R0) + (1 * R2) + (-1 * R3) + (1 * R5) + (-1 * R6) + (1 * R8)
            #eixo_x = eixo_x / 4
            # Convolução (mascara vertica)
            eixo_y = (-1 * R0) + (-1 * R1) + (-1 * R2) + (1 * R6) + (1 * R7) + (1 * R8)
            #eixo_y = eixo_x / 4
            # Obtendo valor de gradiente
            gradiente = math.sqrt((eixo_x ** 2) + (eixo_y ** 2))
            # Modificando componentes RGB do pixel atual
            imagem.putpixel((x, y), (int(gradiente), int(gradiente), int(gradiente)))
    # Exibindo imagem modificada
    imagem.show()
#}
#prewitt()
