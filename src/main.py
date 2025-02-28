import cherrypy
import os
import random
import page_index
import page_signup
import page_posts
import page_makepost  # Import Mako rendering for makepost
import io
import PIL.Image
import json

# List of first names for the greeting
FIRST_NAMES = [
    "Emilia", "Mia", "Norma", "Mustafa", "Talia",
    "Axel", "Aiden", "Rosa", "Zaki", "Stevie"
]

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

recent_post = {"title": "", "filename": ""}  # Store the most recent post's metadata

def check_image(data):
    """Check if the uploaded file is a valid image."""
    try:
        MAXSIZE = 4096
        tmp = io.BytesIO(data)
        with PIL.Image.open(tmp, formats=["JPEG", "PNG"]) as img:
            if img.width > MAXSIZE or img.height > MAXSIZE:
                return False
        return True
    except (PIL.UnidentifiedImageError, PIL.DecompressionBombError):
        return False

class App:
    @cherrypy.expose
    def index(self):
        """Displays the most recent post if available."""
        random_name = self.get_or_set_session_name()
        return page_index.render_index(random_name, recent_post["title"], recent_post["filename"])

    @cherrypy.expose
    def signup(self):
        """Signup page."""
        random_name = self.get_or_set_session_name()
        return page_signup.render_signup(random_name)

    @cherrypy.expose
    def posts(self):
        """Posts page."""
        random_name = self.get_or_set_session_name()
        return page_posts.render_posts(random_name)

    @cherrypy.expose
    def makepost(self):
        """Render the make post page using Mako."""
        return page_makepost.render_makepost()

    @cherrypy.expose
    def upload(self, title, image):
        """Handles post uploads."""
        if not title.strip():
            return json.dumps({"ok": False, "reason": "Title cannot be empty."})

        image_data = image.file.read()
        
        if not check_image(image_data):
            return json.dumps({"ok": False, "reason": "Invalid image format or size."})

        # Save the image
        filename = os.path.join(UPLOAD_FOLDER, image.filename)
        with open(filename, "wb") as f:
            f.write(image_data)

        # Store metadata
        recent_post["title"] = title.strip()
        recent_post["filename"] = image.filename

        return json.dumps({"ok": True})

    @cherrypy.expose
    def mostrecent(self):
        """Serves the most recent uploaded image or a default question mark image."""
        default_image_path = os.path.join("html", "images", "QuestionMark.jpg")

        if not recent_post["filename"]:
            cherrypy.response.headers["Content-Type"] = "image/jpeg"
            return open(default_image_path, "rb").read()

        image_path = os.path.join(UPLOAD_FOLDER, recent_post["filename"])
        if not os.path.exists(image_path):
            cherrypy.response.headers["Content-Type"] = "image/jpeg"
            return open(default_image_path, "rb").read()

        cherrypy.response.headers["Content-Type"] = "image/jpeg"
        return open(image_path, "rb").read()

    def get_or_set_session_name(self):
        """Handles session-based user greetings."""
        if "name" not in cherrypy.session:
            cherrypy.session["name"] = random.choice(FIRST_NAMES)
        return cherrypy.session["name"]

if __name__ == "__main__":
    srcdir = os.path.abspath(os.path.dirname(__file__))
    cherrypy.config.update({
        "tools.sessions.on": True,
        "tools.sessions.storage_type": "ram",
        "tools.sessions.timeout": 5,
        "tools.sessions.persistent": False,
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
