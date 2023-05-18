def index():
    with open('templates/index.html') as template:
        return template.read()


def about():
    with open('templates/about.html') as template:
        return template.read()


def error_404():
    with open('templates/404.html') as template:
        return template.read()


def error_405():
    with open('templates/405.html') as template:
        return template.read()
