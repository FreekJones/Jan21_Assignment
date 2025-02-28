from mako.lookup import TemplateLookup
import os
import cherrypy  # Import Cherrypy to access session data

srcdir = os.path.abspath(os.path.dirname(__file__))
lookup = TemplateLookup(directories=[os.path.join(srcdir, "../html")])

def render_makepost():
    """Render the Make Post page using Mako."""
    name = cherrypy.session.get("name", "Guest")  # Get session name, default to "Guest"
    template = lookup.get_template("makepost.html")
    return template.render(title="Make a Post", name=name)