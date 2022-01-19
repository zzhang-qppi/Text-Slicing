import docx

def __write_in_txt(word_path, txt_path):
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
    __write_in_txt(word_path, txt_path)
    txt = open(txt_path, mode="r")
    totaldict = {'}f ':[[],[]], '}c ':[[],[]]}
    for i in txt.readlines():
        i = i.strip('\n')
        try:
            a = i[3:5]
            b = i[6:-1]
            totaldict[i[:3]][0].append(a)
            totaldict[i[:3]][1].append(b)
        except KeyError:
            None
    print(totaldict)

if __name__ == "__main__":
    data_slicing("project.docx","text.txt")
