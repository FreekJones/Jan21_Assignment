import cherrypy
import os
from mako.lookup import TemplateLookup

# Configure Mako template lookup
srcdir = os.path.abspath(os.path.dirname(__file__))
lookup = TemplateLookup(directories=[os.path.join(srcdir, "../html")])

class App:
    @cherrypy.expose
    def index(self):
        template = lookup.get_template("index.html")
        return template.render(title="Home Page", name="NAME")

    @cherrypy.expose
    def signup(self):
        template = lookup.get_template("signup.html")
        return template.render(title="Signup", name="NAME")

    @cherrypy.expose
    def posts(self):
        users = [
            "Maksymilian Hewitt", "Chad Green", "Zakaria Glenn", "Salman Erickson",
            "Khadija Rosario", "Jemima Humphrey", "Melvin Kirby", "Lowri Henry",
            "Shawn Lowery", "Gertrude Bradford"
        ]
        posts = [
            {
                "user": user,
                "thumbnail": f"/html/images/avatar{i + 1}.png",
                "time_ago": f"{random.randint(1, 30)} days ago",
                "views": random.randint(0, 1000),
            }
            for i, user in enumerate(users)
        ]
        template = lookup.get_template("posts.html")
        return template.render(title="Posts Page", posts=posts, name="NAME")

if __name__ == "__main__":
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
#https://www.w3schools.com/html/
#https://www.w3schools.com/css/
#https://www.w3schools.com/html/html_styles.asp
#https://www.w3schools.com/css/css_boxmodel.asp
#https://www.w3schools.com/html/html_formatting.asp
#https://www.w3schools.com/html/html_lists.asp
#https://www.w3schools.com/html/html_images.asp
#https://www.w3schools.com/html/html_filepaths.asp
#I also used ChatGPT to help me with some of the code and to explain some concepts
