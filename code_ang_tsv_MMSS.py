#gera angulos a partir do tsv em output_angle.tsv

import csv
import numpy as np
import math
input_file = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv/projeto-fisioterapia-3D/output/MMSS/output_file_points_MMSS.tsv'
output_angle = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv/projeto-fisioterapia-3D/angulos/MMSS/ang_MMSS_tsv.tsv'

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
    frame = 0
    count = 0
    for row in reader:

        

        if count % 3 == 0:
            # abertura no ombro Ângulo entre retas formadas por AC_D/AC_E e CM_D/CM_E
            x1, y1, z1 = map(float, row[50:53])  # cotovelo direito gerado por new_points
            x2, y2, z2 = map(float, row[32:35])  # OMBRO direito (AC_D)
            x3, y3, z3 = map(float, row[14:17])  # ombro esquerdo (AC_E)

            ponto1 = [x1, y1, z1]
            ponto2= [x2, y2, z2]
            ponto3 = [x3, y3, z3]

            ang_abd_ombro_direito = calculate_angle(ponto1, ponto2, ponto3) #calcula abertura no ponto do meio
            



            #/////////////////////////////////////////////////////

            # Abducao ombro esquerdo C_E AC_E AC_D
            x12, y12, z12 = map(float, row[56:59])  # cotovelo esquerdo gerado por new_points
            x22, y22, z22 = map(float, row[14:17])  # OMBRO direito (AC_E)
            x32, y32, z32 = map(float, row[32:35])  # ombro esquerdo (AC_D)

            ponto1 = [x12, y12, z12]
            ponto2= [x22, y22, z22]
            ponto3 = [x32, y32, z32]

            ang_abd_ombro_esquerdo = calculate_angle(ponto1, ponto2, ponto3) #calcula abertura no ponto do meio
            
            #/////////////////////////////////////////////////////

            # Flexao cotovelo direito PER/PEU EM/EL e AC_E

            x13, y13, z13 = map(float, row[53:56])  # Pulso DIREITO gerado por new points   
            x23, y23, z23 = map(float, row[50:53])  # COTOVELO DIREITO gerado por new points 
            x33, y33, z33 = map(float, row[32:35])  # OMBRO direito (AC_D)

            ponto1 = [x13, y13, z13]
            ponto2= [x23, y23, z23]
            ponto3 = [x33, y33, z33]

            ang_flex_cotovelo_direito = calculate_angle(ponto1, ponto2, ponto3)


            #///////////////////////////////////////////////////////////
            
            # Flexao cotovelo esquerdo PER/PEU EM/EL e AC_E

            x14, y14, z14 = map(float, row[59:62])  # Pulso ESQUERDO gerado por new points   
            x24, y24, z24 = map(float, row[56:59])  # COTOVELO ESQUERDO gerado por new points 
            x34, y34, z34 = map(float, row[14:17])  # OMBRO esquerdo (AC_E)

            ponto1 = [x14, y14, z14]
            ponto2= [x24, y24, z24]
            ponto3 = [x34, y34, z34]

            ang_flex_cotovelo_esquerdo = calculate_angle(ponto1, ponto2, ponto3)


            #///////////////////////////////////////////////////////////

            # Flexao Ombro direito 
            
            x15, y15, z15 = map(float, row[56:59])  # ponto medio EM_D EL_D
            x25, y25, z25 = map(float, row[32:35])  # AC_D
            x35, y35, z35 = map(float, row[62:65])  # PELVE_D

            ponto1 = [x15, y15, z15]
            ponto2= [x25, y25, z25]
            ponto3 = [x35, y35, z35]

            ang_flex_ombro_direito = calculate_angle(ponto1, ponto2, ponto3)

            #//////////////////////////////////////////////////////////

            # Flexao Ombro esquerdo
            
            x16, y16, z16 = map(float, row[56:59])  # ponto medio EM_E EL_E
            x26, y26, z26 = map(float, row[14:17])  # AC_E
            x36, y36, z36 = map(float, row[65:68])  # PELVE_E
            ponto14 = [x16, y16, z16]
            ponto24= [x26, y26, z26]
            ponto34 = [x36, y36, z36]

            ang_flex_ombro_esquerdo = calculate_angle(ponto14, ponto24, ponto34)




            new_row = [frame,"abd ombro direito:", ang_abd_ombro_direito, "flex cotovelo direito:", ang_flex_cotovelo_direito, "flex cotovelo esquerdo:", ang_flex_cotovelo_esquerdo,
                       "abd ombro esquerdo:", ang_abd_ombro_esquerdo, "flex ombro direito:", ang_flex_ombro_direito, "flex ombro esquerdo:", ang_flex_ombro_esquerdo]
            frame += 1
            writer.writerow(new_row)
            

        count += 1



