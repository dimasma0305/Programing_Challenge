import html

def generate_bc(url, separator):
    parse_url = url.split('/')
    parse_url[-1] = parse_url[-1].split('?')[0]
    parse_url = [i for i in parse_url if i != '']
    parse_url.pop(0)
    path = parse_url[:-1]
    file = parse_url[-1]
    # print(path)
    # print(file)
    breadcrumb = """<a href="/">HOME</a>%s""" % separator
    for i, c in enumerate(path):
        breadcrumb += """<a href="/%s/">%s</a>%s""" % (c, c.upper(), separator)
    if file != '' and file != file.split('.')[0]:
        breadcrumb += """<span class="active">%s</span>""" % file.split('.')[0].upper()
    # return html.escape(breadcrumb)
    return breadcrumb
    
print(generate_bc('mysite.com/pictures/holidays.html?testing', ':'))