from flask import Flask, render_template, url_for

app = Flask(__name__)



#### Initial Page ####
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title="Welcome Page")




#### Sign Up ####
@app.route('/signUp')
def signUp():
    return render_template('signUp.html', title="Sign up Page")



#### Sign In ####

@app.route('/signIn')
def signIn():
    return render_template('signIn.html', title="Sign In Page")



#### Payment Page
@app.route('/payment')
def payment():
    return render_template('payment.html', title='Payment Page')


if __name__ == '__main__':
    app.run(debug=True)


#### Sign Up ####



#### Sign In ####