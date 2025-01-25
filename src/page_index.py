def get():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home Page</title>
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
                box-sizing: border-box;
            }}
            .navigation 
            {{
                display: flex;
                gap: 15px;
                flex-grow: 1;
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
                margin-right: 20px;
                text-align: right;
            }}
            .content 
            {{
                padding: 100px 20px 20px;
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
            <h1>Welcome to the Home of Freek Jones</h1>
        </div>
    </body>
    </html>
    """


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