#gera angulos a partir do tsv em output_angle.tsv

import csv
import numpy as np
import math

input_file = 'C:/Users/clara/Downloads/Fisioterapia (Cod tsv)/output/Coluna/output_file_points_Coluna.tsv'
output_angle = 'C:/Users/clara/Downloads/Fisioterapia (Cod tsv)/angulos/Coluna/ang_Coluna_tsv.tsv'

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
            x1, y1, z1 = map(float, row[44:47])  # ponto medio CM gerado por new_points_coluna
            x2, y2, z2 = map(float, row[47:50])  # ponto medio AC gerado por new_points_coluna
            x3, y3, z3 = map(float, row[50:53])  # ponto medio TMF gerado por new_points_coluna

            ponto1 = [x1, y1, z1]
            ponto2= [x2, y2, z2]
            ponto3 = [x3, y3, z3]

            flexao_cabeca = calculate_angle(ponto1, ponto2, ponto3)

            #////////////////////////////////////////////////////////////////////////////////////////

            # flexao tronco
            x11, y11, z11 = map(float, row[47:50])  # ponto medio AC gerado por new_points_coluna
            x22, y22, z22 = map(float, row[53:56])  # ponto medio EIAS gerado por new_points_coluna
            x33, y33, z33 = map(float, row[50:53])  # ponto medio TMF gerado por new_points_coluna

            ponto11 = [x11, y11, z11]
            ponto22= [x22, y22, z22]
            ponto33 = [x33, y33, z33]

            flexao_tronco = calculate_angle(ponto11, ponto33, ponto22)
            
            #///////////////////////////////////////////////////////////////////////////////////////




            new_row = ["flexao cabeca:", flexao_cabeca, "flexao tronco:", flexao_tronco]

            writer.writerow(new_row)



        count += 1
