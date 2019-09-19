import csv

def proc(entrada):
    with open(entrada, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open('resultado.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file)
            new_file.write("Data,Hora,Vazao,Totalizador\n")

            while True:
                try:
                    # começo do set
                    line = csv_file.readline()
                    # separação da data e hora
                    linha_data = line[6:8] + "/" + line[3:5] + "/" + line[0] + line[1] + "," + line[9:17]
                    # pula o valor SYS
                    line = csv_file.readline()
                    line = csv_file.readline()
                    # filtra o conteúdo de Flow para pegar apenas o valor
                    valor = ''.join([n for n in line if n.isdigit()])
                    linha_data = linha_data + "," + valor
                    line = csv_file.readline()
                    # filtra o conteúdo de Net totalizer para pegar apenas o valor
                    valor = ''.join([n for n in line if n.isdigit()])
                    linha_data = linha_data + "," + valor
                    # pula para o próximo valor de leitura
                    line = csv_file.readline()
                    line = csv_file.readline()
                    line = csv_file.readline()
                    line = csv_file.readline()
                    print(linha_data)
                    new_file.write(linha_data + '\n')
                    # line = csv_file.readline( )
                    # csv_writer.writerow(linha_data)
                except EOFError:
                    print("Arquivo processado com sucesso")
                    break
                except IndexError:
                    print("Arquivo processado com sucesso 2")
                    break


entrada = input("Digite aqui o nome do arquivo de origem dos dados:")
proc(entrada)
print("Arquivo convertido com Sucesso!\n\n\n")
entrada = input("Pressione qualquer tecla para sair")