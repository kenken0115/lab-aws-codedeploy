import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainmenu():

    return """
    <html>
    <body>
    <center><h1>!!!!!!Hello World!!!!!!! from AWS CodeDeploy.</h1><br/>
    <h2>Piper for Partner 2022 Day4 at Dell co.</h2>
    </body>
    </html>"""

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=80)
