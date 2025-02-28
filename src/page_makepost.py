from mako.lookup import TemplateLookup
import os
import cherrypy  

srcdir = os.path.abspath(os.path.dirname(__file__))
lookup = TemplateLookup(directories=[os.path.join(srcdir, "../html")])

def render_makepost():
    """Render the Make Post page using Mako."""
    name = cherrypy.session.get("name", "Guest")  
    template = lookup.get_template("makepost.html")
    return template.render(title="Make a Post", name=name)