import docx

data = docx.Document("project.docx").paragraphs
print(data[43].text=="附录1 ")