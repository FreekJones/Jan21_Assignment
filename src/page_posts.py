import random

def get():
    users = [
        "Maksymilian Hewitt", "Chad Green", "Zakaria Glenn", "Salman Erickson",
        "Khadija Rosario", "Jemima Humphrey", "Melvin Kirby", "Lowri Henry",
        "Shawn Lowery", "Gertrude Bradford"
    ]
    
    posts_html = "".join([
        f"""
        <div class="post-item" style="background-color: {'lightblue' if i % 2 == 0 else 'white'}; padding: 10px; border-bottom: 1px solid #ccc;">
            <img src="/html/images/avatar{i + 1}.png" alt="Thumbnail" style="width: 64px; height: 64px; margin-right: 10px; border-radius: 4px;">
            <div>
                <p><strong>Post: {i + 1}</strong></p>
                <p>User: {user}</p>
                <p>Time Ago: {random.randint(1, 30)} days ago</p>
                <p>Views: {random.randint(0, 1000)} views</p>
            </div>
        </div>
        """
        for i, user in enumerate(users)
    ])
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Posts Page</title>
        <style>
            body 
            {{
                font-family: Roboto, Libre Franklin;
                margin: 0;
                padding: 0;
                background-color: #f0f0f0;
            }}
            .header 
            {{
                background-color: blue;
                color: white;
                padding: 20px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                z-index: 1000;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .navigation 
            {{
                display: flex;
                gap: 15px;
            }}
            .nav-link 
            {{
                color: white;
                text-decoration: none;
                font-weight: bold;
            }}
            .nav-link:hover 
            {{
                text-decoration: underline;
            }}
            .greeting 
            {{
                font-size: 18px;
                white-space: nowrap;
                margin-left: auto;
                margin-right: 40px;
                text-align: right;
            }}
            .content 
            {{
                padding: 100px 20px;
            }}
            .posts-container 
            {{
                max-height: 500px;
                overflow-y: auto;
                padding: 10px;
                background-color: #fff;
                border-radius: 8px;
            }}
            .post-item 
            {{
                display: flex;
                margin-bottom: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <nav class="navigation">
                <a href="/" class="nav-link">Home</a>
                <a href="/signup" class="nav-link">Signup</a>
                <a href="/posts" class="nav-link">Posts</a>
            </nav>
            <span class="greeting">Hello, NAME</span>
        </div>
        <div class="content">
            <h1 class="posts-title">User Posts</h1>
            <div class="posts-container">
                {posts_html}
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

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