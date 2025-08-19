import codecs

from numpy.matlib import empty


def delete_html_tags(html_file: str, result_file='cleaned.txt') -> None:

    inside_tag = False
    result = []

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    for char in html:
        if char == "<":
            inside_tag = True
        elif char == ">":
            inside_tag = False
        elif not inside_tag:
            result.append(char)

        empty_lines = []
        for line in "".join(result).splitlines():
            if line.strip():
                empty_lines.append(line.strip())


    with codecs.open(result_file, 'w', 'utf-8') as f:
        f.write("\n".join(empty_lines))


delete_html_tags("draft.html")



