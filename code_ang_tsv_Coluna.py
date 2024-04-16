#gera angulos a partir do tsv em output_angle.tsv

import csv
import numpy as np
import math

input_file = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv/projeto-fisioterapia-3D/output/Coluna/output_file_points_Coluna.tsv'
output_angle = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv/projeto-fisioterapia-3D/angulos/Coluna/ang_Coluna_tsv.tsv'

def calculate_angle(point1, point2, point3):
    # Calculate vectors from point2 to point1 and point2 to point3
    vector1 = [point1[0] - point2[0], point1[1] - point2[1], point1[2] - point2[2]]
    vector2 = [point3[0] - point2[0], point3[1] - point2[1], point3[2] - point2[2]]

    # Calculate the dot product of the two vectors
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

    # Calculate the magnitudes of the two vectors
    magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
    magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vector2))

    # Calculate the angle in radians
    angle_radians = math.acos(dot_product / (magnitude1 * magnitude2))

    # Convert radians to degrees
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees



count = 0
#funçao que calcula o comprimento de um vetor
def modulo_vetor(x, y, z):
                
    v = (x**2 + y**2 + z**2)**0.5
                
    return v
            
'''funçao que retona um vetor normalizado, ou seja, um vetor na mesma direção mas com norma igual a 1'''
def normaliza_vetor(x, y, z):
                
    aux = modulo_vetor(x, y, z)
                
    v = [x/aux, y/aux, z/aux]
                
    return v

'''funçao que recebe como parametro as coordenadas de dois pontos, 
que sao os extremos das duas retas, ou seja, esses dois pontos definem essa reta. ela retorna a direção da reta no espaço'''
def calcula_inclinacao(x1, y1, z1, x2, y2, z2):
                
    vetor_diretor = [(x2 - x1), (y2 - y1), (z2 - z1)]
                
    return normaliza_vetor(*vetor_diretor)
                
'''função recebe as coordenadas de 4 pontos, 2 de uma reta (final e inicial) e 2 de outra'''
def angulo_de_flexao(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
                
    inclinacao_reta1 = calcula_inclinacao(x1, y1, z1, x2, y2, z2)
    inclinacao_reta2 = calcula_inclinacao(x3, y3, z3, x4, y4, z4)
                
    produto_escalar = 0.0
                
    for v1, v2 in zip(inclinacao_reta1, inclinacao_reta2):
        produto_escalar += v1 * v2
             
    angulo = math.acos(produto_escalar)

    return math.degrees(angulo)
#
# explicar csv_out
#
# Read the input TSV file and create an output TSV file

with open(input_file, 'r') as tsv_in, open(output_angle, 'w', newline='') as tsv_out:
    reader = csv.reader(tsv_in, delimiter='\t')
    writer = csv.writer(tsv_out, delimiter='\t')

    count = 0
    for row in reader:

        if count % 3 == 0:
            
            # flexao cabeca
            x1_, y1_, z1_ = map(float, row[20:23])  # GA 
            x2_, y2_, z2_ = map(float, row[47:50])  # ponto medio AC gerado por new_points_coluna
            x3_, y3_, z3_ = map(float, row[50:53])  # ponto medio TMF gerado por new_points_coluna

            ponto1 = [x1_, y1_, z1_]
            ponto2= [x2_, y2_, z2_]
            ponto3 = [x3_, y3_, z3_]

            flexao_cabeca = calculate_angle(ponto1, ponto2, ponto3)

            #////////////////////////////////////////////////////////////////////////////////////////

            # flexao tronco
            x11, y11, z11 = map(float, row[47:50])  # ponto medio AC gerado por new_points_coluna
            x22, y22, z22 = map(float, row[53:56])  # ponto medio EIAS gerado por new_points_coluna
            x33, y33, z33 = map(float, row[50:53])  # ponto medio TMF gerado por new_points_coluna

            ponto11 = [x11, y11, z11]
            ponto22= [x22, y22, z22]
            ponto33 = [x33, y33, z33]

            flexao_tronco = calculate_angle(ponto11, ponto22, ponto33)
            
            #///////////////////////////////////////////////////////////////////////////////////////

             # rotação tronco
            X, Y, Z = map(float, row[35:38])  # AC_D
            X1, Y1, Z1 = map(float, row[38:41])  # AC_E
            X2, Y2, Z2 = map(float, row[41:44]) #EIAS_D
            X3, Y3, Z3 = map(float, row[8:11]) #EIAS_E


        

               

            ponto111 = [X, Y, Z ]
            ponto222= [X1, Y1, Z1]
            ponto333 = [X2, Y2, Z2]
            ponto4 = [X3, Y3, Z3]
  
            x_inicial, y_inicial, z_inicial = ponto222
            x_final, y_final, z_final = ponto111
            x1_inicial, y1_inicial, z1_inicial = ponto4
            x1_final, y1_final, z1_final = ponto333


            rotacao_tronco = angulo_de_flexao(x_inicial, y_inicial, z_inicial, x_final, y_final, z_final, x1_inicial, y1_inicial, z1_inicial, x1_final, y1_final, z1_final  )
            
            #///////////////////////////////////////////////////////////////////////////////////////


            new_row = ["flexao cabeca:", flexao_cabeca, "flexao tronco:", flexao_tronco, "rotacao tronco:", rotacao_tronco]

            writer.writerow(new_row)



        count += 1
