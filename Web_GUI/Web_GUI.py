from flask import Flask, render_template, url_for, request, redirect, session, flash
#import LLLib_Charles_Schwab as lib
import math

app = Flask(__name__)#, template_folder='templates', static_folder='static')

@app.route('/')

def index():

    #This is where you can put python code to run before rendering the template
    # For example, you can fetch data from a database or perform calculations
    myFloat = math.pi

    return render_template('index.html', value=myFloat)


if(__name__ == "__main__"):
    app.run(debug=True)



