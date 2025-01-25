import cherrypy
import os
import random
from mako.lookup import TemplateLookup

# Set up the template lookup
srcdir = os.path.abspath(os.path.dirname(__file__))
lookup = TemplateLookup(directories=[os.path.join(srcdir, "../html")])

# List of first names to use for the greeting
FIRST_NAMES = [
    "Emilia", "Mia", "Norma", "Mustafa", "Talia",
    "Axel", "Aiden", "Rosa", "Zaki", "Stevie"
]

class App:
    @cherrypy.expose
    def index(self):
        # Retrieve or set a random name for the session
        random_name = self.get_or_set_session_name()
        template = lookup.get_template("index.html") # Render the index page
        return template.render(title="Home Page", name=random_name)

    @cherrypy.expose
    def signup(self):
        # Retrieve or set a random name for the session
        random_name = self.get_or_set_session_name()
        template = lookup.get_template("signup.html")
        return template.render(title="Signup", name=random_name)

    @cherrypy.expose
    def posts(self):
        # Generate random posts from a list of random users
        users = [
            "Maksymilian Hewitt", "Chad Green", "Zakaria Glenn", "Salman Erickson",
            "Khadija Rosario", "Jemima Humphrey", "Melvin Kirby", "Lowri Henry",
            "Shawn Lowery", "Gertrude Bradford"
        ]
        posts = [
            {
                "user": user,
                "thumbnail": f"/html/images/avatar{i + 1}.png",
                "time_ago": f"{random.randint(1, 364)} days ago",
                "views": random.randint(0, 1000),
            }
            for i, user in enumerate(users)
        ]
        # Retrieve or set a random name for the session
        random_name = self.get_or_set_session_name()
        template = lookup.get_template("posts.html")
        return template.render(title="Posts Page", posts=posts, name=random_name)

    def get_or_set_session_name(self):
        """
        Retrieve the session name or set it if it doesn't exist.
        """
        if "name" not in cherrypy.session:
            # Generate a random name and store it in the session
            cherrypy.session["name"] = random.choice(FIRST_NAMES)
        return cherrypy.session["name"]

if __name__ == "__main__":
    cherrypy.config.update({
        "tools.sessions.on": True,                # Enable session management
        "tools.sessions.storage_type": "ram",     # Use in-memory session storage
        "tools.sessions.timeout": 5,             # Session timeout in minutes
        "tools.sessions.persistent": False,      # Session cookie expires on browser close
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
