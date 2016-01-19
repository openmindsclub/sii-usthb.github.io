# import yaml
from markdown import markdown
from jinja2 import Environment, FileSystemLoader
# from time import sleep
# import os


def renderIndex():

    # Loading the template
    templateLoader = FileSystemLoader(searchpath="./templates/")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template("index.base.html")
    rendered = template.render()

    # Rendering the output
    result = open('index.html', 'w')
    result.write(rendered)
    result.close()


def renderLearnMore():
    # Loading the data
    f = open('README.md')
    contribute = f.read()
    contribute = markdown(contribute)
    f.close()

    # Loading the template
    templateLoader = FileSystemLoader(searchpath="./templates/")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template("learnmore.base.html")
    rendered = template.render(markdown=contribute)

    # Rendering the output
    result = open('learnmore.html', 'w')
    result.write(rendered)
    result.close()


if __name__ == "__main__":

    renderIndex()
    renderLearnMore()
