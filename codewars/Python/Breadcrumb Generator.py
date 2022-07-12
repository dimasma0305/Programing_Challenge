import re
def generate_bc(url, separator):
    # print(url)
    # replace http or https with '' and remove #.*
    ignore = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
    parse_url = re.sub(r'(http|https)://', '', url)
    parse_url = re.sub(r'#.*', '', parse_url)
    parse_url = re.sub(r'\?.*', '', parse_url)
    # print(parse_url)
    parse_url = parse_url.split('/')
    parse_url[-1] = parse_url[-1].split('?')[0]
    parse_url = [i for i in parse_url if i != '']
    if len(parse_url) < 2:
        return '<span class="active">HOME</span>'
    parse_url.pop(0)
    file = parse_url[-1].split('.')[0]
    path = parse_url[:-1]
    
    # print(file)
    if file == 'index':
        try:
            file = parse_url[-2]
            path = parse_url[:-2]
        except:
            return '<span class="active">HOME</span>'
    # print(file)
    
    
    breadcrumb = """<a href="/">HOME</a>%s""" % separator
    plus = []
    for _, c in enumerate(path):
        plus.append(c)
        if len(c) > 30:
            c = [i for i in c.split('-')]
            c = ''.join([i[0] for i in c if i not in ignore])
        breadcrumb += """<a href="/%s/">%s</a>%s""" % ('/'.join(plus), c.upper().replace('-', ' '), separator)
    file = file.split('.')[0].replace("-", " ")
    # print(file)
    if len(file) > 30:
        file = [i for i in file.split(' ')]
        # print(file)
        file = ''.join([i[0] for i in file if i not in ignore])
    breadcrumb += """<span class="active">%s</span>""" % file.upper()
    # return html.escape(breadcrumb)
    return breadcrumb
    
print(generate_bc('http://twitter.de/issues/kamehameha-kamehameha-the-paper-kamehameha/bed-and-paper-and-meningitis-immunity', ':'))