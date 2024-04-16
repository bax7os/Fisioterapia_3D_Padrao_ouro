import csv
import glob
# Function to calculate the midpoint between two sets of xyz values
def calculate_midpoint(x1, y1, z1, x2, y2, z2):
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    midpoint_z = (z1 + z2) / 2
    return round(midpoint_x, 3), round(midpoint_y, 3), round(midpoint_z, 3)
# output file names
output_file_points = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv/projeto-fisioterapia-3D/output/Coluna/output_file_points_Coluna.tsv'
# Especifica o diretório onde os arquivos TSV estão
diretorio = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv/projeto-fisioterapia-3D/input/Coluna'

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

        #ponto medio  CM_D e CM_E
        #_____________________________________________________________________________________________________________
        x1, y1, z1 = map(float, row[23:26]) #CM_D
        x2, y2, z2 = map(float, row[26:29]) #CM_E

        midpoint_xCM, midpoint_yCM, midpoint_zCM = calculate_midpoint(x1, y1, z1, x2, y2, z2)
        #_____________________________________________________________________________________________________________


        #/////////////////////////////////////////////////////////////////////////////////////////////////////////////

        #ponto medio AC_D e AC_E
        #_____________________________________________________________________________________________________________
        x11, y11, z11 = map(float, row[35:38]) #AC_D
        x22, y22, z22 = map(float, row[38:41]) #AC_E

        midpoint_xAC, midpoint_yAC, midpoint_zAC = calculate_midpoint(x11, y11, z11, x22, y22, z22)
        #_____________________________________________________________________________________________________________


        #/////////////////////////////////////////////////////////////////////////////////////////////////////////////


        #ponto medio TMF_D e TMF_E
        #_____________________________________________________________________________________________________________
        x13, y13, z13 = map(float, row[2:5]) #TMF_D
        x23, y23, z23 = map(float, row[5:8]) #TMF_E

        midpoint_xTMF, midpoint_yTMF, midpoint_zTMF = calculate_midpoint(x13, y13, z13, x23, y23, z23)
        #_____________________________________________________________________________________________________________


        #/////////////////////////////////////////////////////////////////////////////////////////////////////////////


        #ponto medio  EIAS_D e EIAS_E
        #_____________________________________________________________________________________________________________
        x14, y14, z14 = map(float, row[41:44]) #EIAS_D
        x24, y24, z24 = map(float, row[8:11]) #EIAS_E

        midpoint_xEIAS, midpoint_yEIAS, midpoint_zEIAS = calculate_midpoint(x14, y14, z14, x24, y24, z24)
        #_____________________________________________________________________________________________________________



        # Append the midpoint xyz values to the row (CM 44:47) (AC 47:50) (TMF 50:53) (EIAS 53:56)
        row.extend([midpoint_xCM, midpoint_yCM, midpoint_zCM, 
                    midpoint_xAC, midpoint_yAC, midpoint_zAC,
                    midpoint_xTMF, midpoint_yTMF, midpoint_zTMF,
                    midpoint_xEIAS, midpoint_yEIAS, midpoint_zEIAS])
        


        # Write the updated row to the output file
        writer.writerow(row)
