def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}<{tag}>')
    return wrap_text

print_h1 = html_tag('h1')
print_h2 = html_tag('h2')
print_p = html_tag('p')

print_h1('test headline')
print_h2('another headline')
print_p('paragraph ')


