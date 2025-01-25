from mako.lookup import TemplateLookup
import os
import random
import datetime

srcdir = os.path.abspath(os.path.dirname(__file__))
lookup = TemplateLookup(directories=[os.path.join(srcdir, "../html")])

def generate_posts():
    users = [
        "Maksymilian Hewitt", "Chad Green", "Zakaria Glenn", "Salman Erickson",
        "Khadija Rosario", "Jemima Humphrey", "Melvin Kirby", "Lowri Henry",
        "Shawn Lowery", "Gertrude Bradford"
    ]
    posts = []
    for i, user in enumerate(users):
        x = datetime.timedelta(minutes=random.randrange(500000))  
        days_ago = x.days
        hours_ago = int(x.seconds / 3600)
        minutes_ago = int((x.seconds % 3600) / 60)
        time_ago = f"{days_ago} days, {hours_ago} hours, and {minutes_ago} minutes ago"
        
        posts.append({
            "user": user,
            "thumbnail": f"/html/images/avatar{i + 1}.png",
            "time_ago": time_ago,
            "views": random.randint(0, 1000),
        })
    return posts

def render_posts(name):
    posts = generate_posts()
    template = lookup.get_template("posts.html")
    return template.render(title="Posts Page", posts=posts, name=name)
    

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