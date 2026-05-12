data = input("digite a data: dd/mm/aa: ")
dataFormatada = data.split("/")
dia = dataFormatada[0]
mes = dataFormatada[1]
ano = dataFormatada[2]
if dia > 31 and mes > 5 and mes < 12 and ano >= 2026:
    print("Data agendada com sucesso!!")
    dataFormatada.append(data_ret)
                    