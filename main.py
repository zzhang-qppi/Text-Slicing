# -*- coding: utf-8 -*-

import docx
import matplotlib.pyplot as plt
import numpy as np

def write_in_txt(word_path, txt_path):
#    for lines in word_document:
#        if lines.text != "附录1 ":
#            lines.clear()
#        else:
#            lines.clear()
#            break
    data = docx.Document(word_path).paragraphs
    txt = open(txt_path, mode="w+")
    for lines in data:
        txt.write(lines.text+"\n")

def data_slicing(word_path, txt_path):
    write_in_txt(word_path, txt_path)
    txt = open(txt_path, mode="r")
    totaldict = {'}f':[[],[]], '}c':[[],[]]}
    for i in txt.readlines():
        i = i.strip('\n')
        i_spl = i.split(' ')
        try:
            totaldict[i_spl[0]][0].append(int(i_spl[1]))
            totaldict[i_spl[0]][1].append(float(i_spl[2]))
        except KeyError:
            None
    for keys in totaldict:
        totaldict[keys] = np.asarray(totaldict[keys])
    return totaldict

def data_graphing(word_path, txt_path):
    data = data_slicing(word_path, txt_path)
    fig = plt.figure()
    fig, axs = plt.subplots(len(data), 2, layout='constrained')
    for i in range(0, len(data)):
        data_1 = data[list(data.keys())[i]][0]
        data_2 = data[list(data.keys())[i]][1]
        axs[i, 0].scatter(range(0, len(data_1)), data_1, s=5)
        axs[i, 0].set_title(list(data.keys())[i]+ ' 1')
        axs[i, 1].scatter(range(0, len(data_2)), data_2, s=5)
        axs[i, 1].set_title(list(data.keys())[i]+ ' 2')
    return fig

if __name__ == "__main__":
    fig = data_graphing("project.docx","text.txt")
    plt.savefig('scatter_plot.jpeg')
    plt.show()
