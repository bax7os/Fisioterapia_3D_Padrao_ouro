import csv
import glob
# Function to calculate the midpoint between two sets of xyz values
def calculate_midpoint(x1, y1, z1, x2, y2, z2):
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    midpoint_z = (z1 + z2) / 2
    return round(midpoint_x, 3), round(midpoint_y, 3), round(midpoint_z, 3)


# output file names
output_file_points = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv/projeto-fisioterapia-3D/output/MMSS/output_file_points_MMSS.tsv'
# Especifica o diretório onde os arquivos TSV estão
diretorio = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv/projeto-fisioterapia-3D/input/MMSS'
# Busca por todos os arquivos TSV no diretório especificado
arquivos_tsv = glob.glob(f'{diretorio}/*.tsv')
# Verifica se há pelo menos um arquivo TSV na pasta
if arquivos_tsv:
    # Assume que estamos usando o primeiro arquivo encontrado
    input_file = arquivos_tsv[0]


# Read the input TSV file and create an output TSV file
with open(input_file, 'r') as tsv_in, open(output_file_points, 'w', newline='') as tsv_out:
    reader = csv.reader(tsv_in, delimiter='\t')
    writer = csv.writer(tsv_out, delimiter='\t')
    # Pula as linhas do cabeçalho
    for i in range(10):
        next(reader, None)
    for row in reader:

        
        #ponto medio do cotovelo DIREITO EM_D e EL_D
        #_____________________________________________________________________________________________________________
        x1, y1, z1 = map(float, row[35:38]) #EM_D 
        x2, y2, z2 = map(float, row[38:41]) #EL_D 

        midpoint_xC_D, midpoint_yC_D, midpoint_zC_D = calculate_midpoint(x1, y1, z1, x2, y2, z2)
        #_____________________________________________________________________________________________________________


        #/////////////////////////////////////////////////////////////////////////////////////////////////////////////

        
        #ponto medio do pulso DIREITO PEU_D e PER_D
        #_____________________________________________________________________________________________________________
        x11, y11, z11 = map(float, row[17:20]) # PEU_D
        x22, y22, z22 = map(float, row[23:26]) # PER_D

        midpoint_xP_D, midpoint_yP_D, midpoint_zP_D = calculate_midpoint(x11, y11, z11, x22, y22, z22)
        #_____________________________________________________________________________________________________________


        #/////////////////////////////////////////////////////////////////////////////////////////////////////////////


        #ponto medio do cotovelo ESQUERDO EM_E e EL_E
        #_____________________________________________________________________________________________________________

        x111, y111, z111 = map(float, row[35:38]) #EM_E
        x222, y222, z222 = map(float, row[44:47]) #EL_E

        midpoint_xC_E, midpoint_yC_E, midpoint_zC_E = calculate_midpoint(x111, y111, z111, x222, y222, z222)
        #_____________________________________________________________________________________________________________


        #ponto medio do pulso ESQUERDO PER_E PEU_E
        #_____________________________________________________________________________________________________________

        x14, y14, z14 = map(float, row[20:23]) # PER_E
        x24, y24, z24 = map(float, row[47:50]) # PEU_E

        midpoint_xP_E, midpoint_yP_E, midpoint_zP_E = calculate_midpoint(x14, y14, z14, x24, y24, z24)
        

        #ponto medio da pelve DIREITA EIAS_D EIAS_E
        #_____________________________________________________________________________________________________________

        x1111, y1111, z1111 = map(float, row[2:5]) # EIAS_D
        x2222, y2222, z2222 = map(float, row[5:8]) # EIAS_E

        midpoint_xPE_D, midpoint_yPE_D, midpoint_zPE_D = calculate_midpoint( x1111, y1111, z1111, x2222, y2222, z2222)

        #ponto medio da pelve ESQUERDA EIPS_D EIPS_E
        #_____________________________________________________________________________________________________________

        x1112, y1112, z1112 = map(float, row[8:11]) # EIPS_D
        x22222, y22222, z22222 = map(float, row[11:14]) # EIPS_E

        midpoint_xPE_E, midpoint_yPE_E, midpoint_zPE_E = calculate_midpoint( x1112, y1112, z1112, x22222, y22222, z22222)
        
        # Append the midpoint xyz values to the row (COTOVELO_D 50:53) (PULSO_D 53:56) (COTOVELO_E 56:59) (PULSO_E 59:62) (PELVE_D 62:65) (PELVE_E 65:68)
        row.extend([midpoint_xC_D, midpoint_yC_D, midpoint_zC_D, 
                    midpoint_xP_D, midpoint_yP_D, midpoint_zP_D,
                    midpoint_xC_E, midpoint_yC_E, midpoint_zC_E,
                    midpoint_xP_E, midpoint_yP_E, midpoint_zP_E,
                    midpoint_xPE_D, midpoint_yPE_D, midpoint_zPE_D,
                    midpoint_xPE_E, midpoint_yPE_E, midpoint_zPE_E])

        # Write the updated row to the output file
        writer.writerow(row)
        
        