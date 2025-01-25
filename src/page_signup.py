from mako.lookup import TemplateLookup
import os

srcdir = os.path.abspath(os.path.dirname(__file__))
lookup = TemplateLookup(directories=[os.path.join(srcdir, "../html")])

def render_signup(name):
    template = lookup.get_template("signup.html")
    return template.render(title="Signup", name=name)


#I used the following resources to help me with this project:
#https://docs.cherrypy.dev/en/latest/pkg/cherrypy.lib.sessions.html
#https://www.w3schools.com/html/
#https://www.w3schools.com/css/
#https://www.w3schools.com/html/html_styles.asp
#https://www.w3schools.com/css/css_boxmodel.asp
#https://www.w3schools.com/html/html_formatting.asp
#https://www.w3schools.com/html/html_lists.asp
#https://www.w3schools.com/html/html_images.asp
#https://www.w3schools.com/html/html_filepaths.asp
#I also used ChatGPT to help me with some of the code and to explain some concepts