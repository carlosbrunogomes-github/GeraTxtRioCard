import PySimpleGUI as sg

layout = [
		[sg.Text(22*' ' + 'Cole as Matrículas abaixo'), sg.Text(42*' ' + 'Cole os Valores abaixo')],
		[sg.Multiline(size=(45, 20), key='MultilineMatriculas'), sg.Multiline(size=(45, 20), key='MultilineTotais')],
		[sg.Text('Digite o Nome do Arquivo:    '), sg.Input(size=(45, 1), key='NomeArquivo')],
		[sg.Text('Digite o Caminho do Arquivo:'), sg.Input(size=(45, 1), key='CaminhoArquivo')],
		[sg.Button('Ok'), sg.Button('Cancel')]
	]


window = sg.Window('Geração de Arquivo de VT', layout)

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel':
		break

	values['CaminhoArquivo'] = values['CaminhoArquivo'] + "\\" + values['NomeArquivo'] + ".txt"

	matriculas = values['MultilineMatriculas'].split('\n')
	for i in range(len(matriculas)):
		matriculas[i] = matriculas[i].strip()
		
	totais = values['MultilineTotais'].split('\n')
	for i in range(len(totais)):
		totais[i] = totais[i].strip('R$ ')
		if totais[i][-3] == '.' or totais[i][-3] == ',':
			totais[i] = totais[i][:-3] + totais[i][-2:]
		if '.' in totais[i] or ',' in totais[i]:
			totais[i] = totais[i][:-6] + totais[i][-5:]

	linha_01 = "0000101PEDIDO01.0003686998000118"
	sequencia = []
	cargas = []
	total_cargas = []
	trailler = []
	total_cargas.append(totais[-1])
	totais.remove(totais[-1])

	for i in range(len(matriculas)):
		sequencia.append(i + 2)
		sequencia[i] = str(sequencia[i])

	for j in range(len(sequencia)):
		if len(sequencia[j]) < 5:
			sequencia[j] = (5 - len(sequencia[j])) * '0' + sequencia[j] + '02'

	for j in range(len(matriculas)):
		if len(matriculas[j]) < 15:
			matriculas[j] = matriculas[j] + (15 - len(matriculas[j])) * ' '

	for i in range(len(totais)):
		if len(totais[i]) < 8:
			totais[i] = (8 - len(totais[i])) * '0' + totais[i]

	total_linhas = len(matriculas) + 2
	total_linhas = str(total_linhas)
	trailler.append(total_linhas)

	for j in range(len(trailler)):
		if len(trailler[j]) < 5:
			trailler[j] = (5 - len(trailler[j])) * '0' + trailler[j]

	trailler[0] = trailler[0] + '99'

	if len(total_cargas[0]) < 10:
		total_cargas[0] = (10 - len(total_cargas[0])) * '0' + total_cargas[0]

	trailler[0] = trailler[0] + total_cargas[0]

	with open(values['CaminhoArquivo'], 'w') as f:
		print(linha_01, file=f)
		for j in range(len(totais)):
			print(sequencia[j], matriculas[j], totais[j], sep='', file=f)
		print(trailler[0], file=f)

	print('Verifique o diretório onde os arquivos matriculas.txt e totais.txt estão.')
	print('Arquivo recarga.txt gerado!!!')

window.close()
