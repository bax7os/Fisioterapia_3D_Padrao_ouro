import csv
import glob
import os

# Function to calculate the midpoint between two sets of xyz values
def calculate_midpoint(x1, y1, z1, x2, y2, z2):
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    midpoint_z = (z1 + z2) / 2
    return round(midpoint_x, 3), round(midpoint_y, 3), round(midpoint_z, 3)


# Especifica o diretório onde os arquivos TSV estão
diretorio = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv/projeto-fisioterapia-3D/input/MMSS'
# Busca por todos os arquivos TSV no diretório especificado
arquivos_tsv = glob.glob(f'{diretorio}/*.tsv')

for input_file in arquivos_tsv:
    # Define o nome do arquivo de saída com base no nome do arquivo de entrada
    nome_arquivo = os.path.basename(input_file)
    output_file_points = os.path.join('D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv/projeto-fisioterapia-3D/output/MMSS', f'output_file_points_{nome_arquivo}')

    with open(input_file, 'r') as tsv_in, open(output_file_points, 'w', newline='') as tsv_out:
        reader = csv.reader(tsv_in, delimiter='\t')
        writer = csv.writer(tsv_out, delimiter='\t')
        for i in range(10):
            next(reader, None)
        for row in reader:
                    # ponto medio do cotovelo DIREITO EM_D e EL_D
                    x1, y1, z1 = map(float, row[38:41])  # EM_D
                    x2, y2, z2 = map(float, row[41:44])  # EL_D
                    midpoint_xC_D, midpoint_yC_D, midpoint_zC_D = calculate_midpoint(x1, y1, z1, x2, y2, z2)
                    
                    # ponto medio do pulso DIREITO PEU_D e PER_D
                    x11, y11, z11 = map(float, row[47:50])  # PEU_D
                    x22, y22, z22 = map(float, row[44:47])  # PER_D
                    midpoint_xP_D, midpoint_yP_D, midpoint_zP_D = calculate_midpoint(x11, y11, z11, x22, y22, z22)
                    
                    # ponto medio do cotovelo ESQUERDO EM_E e EL_E
                    x111, y111, z111 = map(float, row[26:29])  # EM_E
                    x222, y222, z222 = map(float, row[29:32])  # EL_E
                    midpoint_xC_E, midpoint_yC_E, midpoint_zC_E = calculate_midpoint(x111, y111, z111, x222, y222, z222)
                    
                    # ponto medio do pulso ESQUERDO PER_E e PEU_E
                    x14, y14, z14 = map(float, row[32:35])  # PER_E
                    x24, y24, z24 = map(float, row[35:38])  # PEU_E
                    midpoint_xP_E, midpoint_yP_E, midpoint_zP_E = calculate_midpoint(x14, y14, z14, x24, y24, z24)
                    
                    # ponto medio da pelve DIREITA EIAS_D e EIAS_E
                    x1111, y1111, z1111 = map(float, row[14:17])  # EIAS_D
                    x2222, y2222, z2222 = map(float, row[17:20])  # EIAS_E
                    midpoint_xPE_D, midpoint_yPE_D, midpoint_zPE_D = calculate_midpoint(x1111, y1111, z1111, x2222, y2222, z2222)
                    
                    # ponto medio da pelve ESQUERDA EIPS_D e EIPS_E
                    x1112, y1112, z1112 = map(float, row[8:11])  # EIPS_D
                    x22222, y22222, z22222 = map(float, row[11:14])  # EIPS_E
                    midpoint_xPE_E, midpoint_yPE_E, midpoint_zPE_E = calculate_midpoint(x1112, y1112, z1112, x22222, y22222, z22222)
                    
                    # Adiciona os pontos médios à linha
                    #[50:53] ponto medio do cotovelo DIREITO EM_D e EL_D [53:56] ponto medio do pulso DIREITO PEU_D e PER_D
                    #[56:59] ponto medio do cotovelo ESQUERDO EM_E e EL_E [59:62] ponto medio do pulso ESQUERDO PER_E e PEU_E
                    #[62:65] ponto medio da pelve DIREITA EIAS_D e EIAS_E [65:68] ponto medio da pelve ESQUERDA EIPS_D e EIPS_E
                    row.extend([midpoint_xC_D, midpoint_yC_D, midpoint_zC_D,
                                midpoint_xP_D, midpoint_yP_D, midpoint_zP_D,
                                midpoint_xC_E, midpoint_yC_E, midpoint_zC_E,
                                midpoint_xP_E, midpoint_yP_E, midpoint_zP_E,
                                midpoint_xPE_D, midpoint_yPE_D, midpoint_zPE_D,
                                midpoint_xPE_E, midpoint_yPE_E, midpoint_zPE_E])
                    
                    # Escreve a linha atualizada no arquivo de saída
                    writer.writerow(row)