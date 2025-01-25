import cherrypy
import os.path

# Importing the pages
import page_index
import page_signup
import page_posts

class App:
    @cherrypy.expose
    def index(self):
        return page_index.get()
    
    @cherrypy.expose
    def signup(self):
        return page_signup.get()
    
    @cherrypy.expose
    def posts(self):
        return page_posts.get()

srcdir = os.path.abspath(os.path.dirname(__file__))

app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": 
        {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{srcdir}/../html"
        }
    }
)

#I used the following resources to help me with this project:
#https://www.w3schools.com/html/
#https://www.w3schools.com/css/
#https://www.w3schools.com/html/html_styles.asp
#https://www.w3schools.com/css/css_boxmodel.asp
#https://www.w3schools.com/html/html_formatting.asp
#https://www.w3schools.com/html/html_lists.asp
#https://www.w3schools.com/html/html_images.asp
#https://www.w3schools.com/html/html_filepaths.asp
#I also used ChatGPT to help me with some of the code and to explain some concepts
