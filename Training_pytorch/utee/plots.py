import matplotlib.pyplot as plt
import pandas as pd

def plotting(data, LTP, LTD):

    df = pd.read_csv(data)

    x = df.iloc[:, 0]
    y = df.iloc[:, 2]

    plt.plot(x, y, 'o-', markersize=3)

    plt.title('LTP ' + LTP + ' / ' + 'LTD ' + LTD)
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')

    plt.savefig(data + '_' + LTP + '_' + LTD + '.png', dpi=300)

'''
data = str(input('Input data name: '))
LTPn = str(input('Input LTP: '))
LTDn = str(input('Input LTD: '))
plots(data, LTPn, LTDn)
'''
