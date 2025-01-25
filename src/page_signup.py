def get():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Signup</title>
        <style>
            body 
            {{
                font-family: Roboto, Libre Franklin;
                margin: 0;
                padding: 0;
                background-color: #f0f0f0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
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
            .signup-popup 
            {{
                background-color: white;
                width: 300px;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                border-radius: 8px;
                text-align: center;
                box-sizing: border-box;
            }}
            .signup-popup input 
            {{
                display: block;
                width: 100%;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
                margin-bottom: 15px;
            }}
            .signup-popup label 
            {{
                text-align: left;
                font-size: 14px;
                margin-bottom: 5px;
                display: block;
            }}
            .signup-popup button 
            {{
                padding: 10px 20px;
                background-color: blue;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
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
        <div class="signup-popup">
            <h2>Signup to be Freek Jones' friend</h2>
            <form>
                <label for="email">Email</label>
                <input type="email" id="email" name="email">
                
                <label for="real-name">Real Name</label>
                <input type="text" id="real-name" name="real-name">
                
                <label for="password">Password</label>
                <input type="password" id="password" name="password">
                
                <label for="dob">Date of Birth</label>
                <input type="date" id="dob" name="dob">
                
                <button type="submit">Sign Up</button>
            </form>
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