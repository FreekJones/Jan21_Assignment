import cherrypy
import os
import random
import page_index
import page_signup
import page_posts

# List of first names for the greeting
FIRST_NAMES = [
    "Emilia", "Mia", "Norma", "Mustafa", "Talia",
    "Axel", "Aiden", "Rosa", "Zaki", "Stevie"
]

class App:
    @cherrypy.expose
    def index(self):
        # Retrieve or set a random name for the session
        random_name = self.get_or_set_session_name()
        return page_index.render_index(random_name)

    @cherrypy.expose
    def signup(self):
        # Retrieve or set a random name for the session
        random_name = self.get_or_set_session_name()
        return page_signup.render_signup(random_name)

    @cherrypy.expose
    def posts(self):
        # Retrieve or set a random name for the session
        random_name = self.get_or_set_session_name()
        return page_posts.render_posts(random_name)

    def get_or_set_session_name(self):
        if "name" not in cherrypy.session:
            cherrypy.session["name"] = random.choice(FIRST_NAMES)
        return cherrypy.session["name"]

if __name__ == "__main__":
    # CherryPy configuration
    srcdir = os.path.abspath(os.path.dirname(__file__))
    cherrypy.config.update({
        "tools.sessions.on": True,                # Enable session management
        "tools.sessions.storage_type": "ram",     # Store sessions in RAM
        "tools.sessions.timeout": 5,              # Minutes until session timeout
        "tools.sessions.persistent": False,       # Expire cookies when the browser closes
    })
    cherrypy.quickstart(
        App(),
        "/",
        {
            "/html": {
                "tools.staticdir.on": True,
                "tools.staticdir.dir": os.path.join(srcdir, "../html"),
            }
        },
    )
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
