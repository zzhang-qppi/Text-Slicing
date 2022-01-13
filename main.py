import docx

data = docx.Document("project.docx").paragraphs


def __write_in_txt(word_document):
    for lines in word_document:
        if lines.text != "附录1 ":
            lines.clear()
        else:
            lines.clear()
            break
    return word_document

data = __write_in_txt(data,)
