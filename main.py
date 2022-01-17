import docx

def __write_in_txt(word_document, txt_path):
    for lines in word_document:
        if lines.text != "附录1 ":
            lines.clear()
        else:
            lines.clear()
            break
#删除附录1前的内容（未修改原文档）
    txt = open(txt_path, mode="w")
    for lines in word_document:
        if lines.text != "":
            txt.write(lines.text+"\n")
#创建txt并写入附录1中的字符
    txt.close()
    return txt

def data_slicing(source_path, txt_path):
    data = docx.Document(source_path).paragraphs
    txt = __write_in_txt(data, txt_path)
    
if __name__ == "__main__":
    data_slicing("project.docx","text.txt")
