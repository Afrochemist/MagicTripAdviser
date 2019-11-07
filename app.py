from flask import Flask, render_template, url_for

app = Flask(__name__)



#### Initial Page ####
@app.route('/')
def index():
    return render_template('index.html')




#### Sign Up ####
@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

#### Sign In ####

@app.route('/signIn')
def signIn():
    return render_template('signIn.html')



if __name__ == '__main__':
    app.run(debug=True)


#### Sign Up ####



#### Sign In ####