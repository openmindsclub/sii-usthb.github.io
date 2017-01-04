## A website for sharing SII Master's materials 

This is a static website generated with a simple python script (Because other static web generators are too complex for the needs of the project. ). 
It is open for anyone to contribute. 

------------------------------------------------

## F. A. Q.


##### Why is the website in english?
Because you need to get familiar with the language. That's how all the materials out there are written.

#### Are the files viruses free?
Don't ask about viruses, you're embarassing yourself. (Hint: use Linux)

#### How can I add other files?
It depends, each generation might have their own way of sharing the files. Try asking your class representative or send an email to *sii.usthb.website@gmail.com*.

------------------------------------------------

## Technically details:

The project is really easy, you can even ignore everything and only check the *Data/* folder for modifications. 
It's structured as follows:


* *generate.py*: One python program to generate the website using [jinja2](http://jinja.pocoo.org/) templating. 
* *template/*: contains the Jinja2 templates.
* *Data/*: contains the yaml files for the "semester" pages ([semesterOne](https://sii-usthb.github.io/One.html), [semesterTwo](https://sii-usthb.github.io/Two.html), [semesterThree](https://sii-usthb.github.io/Three.html)) generation. You do not need to know about *yaml*, just follow the simple syntax of the files.

Install the requirements via: ```pip install -r requirements.txt```

------------------------------------------------
<a name="contact"></a> 
## I want to contribute:

If you want to enrich the content with some files or propose something you can:

1. Making a pull request to the [github project](http://github.com/sii-usthb/sii-usthb.github.io).
2. Create a [new github issues](https://github.com/sii-usthb/sii-usthb.github.io/issues)
3. Send an email to **sii.usthb.website@gmail.com**

PS: Any other type of contribution is welcomed! 

------------------------------------------------

### License: 

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
