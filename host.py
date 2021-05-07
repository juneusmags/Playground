from flask import Flask, render_template 
app = Flask(__name__)  


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/render_route')
def render():
    return render_template('index.html')


@app.route('/play/<x>/<choose_color>')
def combine_all(x,choose_color):
    return render_template('index.html',num_from_host = int(x), colorf=choose_color)


































if __name__=="__main__":   
    app.run(debug=True)    