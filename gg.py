import yaml
from markdown import markdown
from jinja2 import Environment, FileSystemLoader
from time import sleep
import os


def renderIndex():
    # Loading the data
    f = open('data/projects.yml')
    dataMap = yaml.safe_load(f)
    f.close()

    # Loading the template
    templateLoader = FileSystemLoader(searchpath="./templates/")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template("index.base.html")
    rendered = template.render(links=dataMap, landing=True)

    # Rendering the output
    result = open('output/index.html', 'w')
    result.write(rendered)
    result.close()


def renderContrib():
    # Loading the data
    f = open('data/contribute.md')
    contribute = f.read()
    contribute = markdown(contribute)
    f.close()

    # Loading the template
    templateLoader = FileSystemLoader(searchpath="./templates/")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template("contrib.base.html")
    rendered = template.render(markdown=contribute)

    # Rendering the output
    result = open('output/contrib.html', 'w')
    result.write(rendered)
    result.close()


def renderOther():
    # Loading the data
    f = open('data/other.yml')
    other = yaml.safe_load(f)
    f.close()

    # Loading the template
    templateLoader = FileSystemLoader(searchpath="./templates/")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template("other.base.html")
    rendered = template.render(otherData=other)

    # Rendering the output
    result = open('output/other.html', 'w')
    result.write(rendered)
    result.close()


if __name__ == "__main__":
    # Put your pictures in "projectImages/" folder
    # they'll be copied to the right place
    os.system("cp projectImages/* output/images/projects/")

    # Put the three next lines into a while loop
    # if you want not to execute this code each time
    # you want to refresh

    # while(1):
    renderIndex()
    renderContrib()
    renderOther()
    sleep(2)

    # Might wanna add a simple http server instead
