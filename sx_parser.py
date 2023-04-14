#python 3.8.10
version = '0.1'
import csv

if __name__ == "__main__":
    first = False
    sx_data = []
    with open('sxc-all-transactions.csv') as csv_file:
        for line in csv_file:
            if first:
                first = False
            else:
                data = line.split(",")
                sx_data.append(data)

csv_first_line = "Type", "Buy Amount", "Buy Currency", "Sell Amount", "Sell Currency", "Fee", "Fee Currency", "Exchange", "Trade-Group", "Comment", "Date"

transactions = {}
ct_data = []
for e in sx_data:
    if e[3] == 'Grifo':
        line = ['Airdrop', str(e[4]), str(e[2]),'' ,'' ,'' ,'' , 'Southxchange','' ,'' ,e[1] ]
        ct_data.append(line)
    elif e[3] == 'Depósito':
        line = ['Depósito', str(e[4]), str(e[2]),'' ,'' ,'' ,'' , 'Southxchange','' ,'' ,e[1] ]
        ct_data.append(line)
    elif e[3] == 'Extracción':
        line = ['Retirada', '', '', float(e[4]) * (-1), str(e[2]),'' ,'' , 'Southxchange','' ,'' ,e[1] ]
        ct_data.append(line)
    elif e[3] == 'Operación':
        if not e[12] in transactions:
            transactions[e[12]] = {}
        if float(e[4]) > 0:
            transactions[e[12]]['Buy Amount'] = e[4]
            transactions[e[12]]['Buy Currency'] = e[2]
            transactions[e[12]]['Date'] = e[1]
        if float(e[4]) < 0:
            transactions[e[12]]['Sell Amount'] = float(e[4]) * (-1)
            transactions[e[12]]['Sell Currency'] = e[2]
            transactions[e[12]]['Date'] = e[1]
    elif e[3] == 'Comisión':
        if e[12] == '':
            line = ['Otros gastos', '', '', float(e[4]) * (-1), str(e[2]),'' ,'' , 'Southxchange','' ,'' ,e[1] ]
            ct_data.append(line)
        else:
            if not e[12] in transactions:
                transactions[e[12]] = {}
            transactions[e[12]]['Fee'] = e[4] * (-1)
            transactions[e[12]]['Fee Currency'] = e[2]
            transactions[e[12]]['Date'] = e[1]

for key, value in transactions.items():
    if len(value) != 7:
        print(f'Faltan valores: {value}')
    line = ['Operación', value["Buy Amount"], value["Buy Currency"], value["Sell Amount"] , value["Sell Currency"] ,'' ,'' , 'Southxchange','' ,'' , value["Date"]]
    ct_data.append(line)

with open('sx_cointracking.csv', mode='w') as file:
    transaction_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    transaction_writer.writerow(csv_first_line)
    for e in ct_data:
        transaction_writer.writerow(e)