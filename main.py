import docx

data = docx.Document("project.docx").paragraphs


#删除非附录文本
for lines in data:
    if lines.text != "附录1 ":
        lines.clear()
    else:
        lines.clear()
        break



