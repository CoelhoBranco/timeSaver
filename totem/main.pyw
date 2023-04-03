import time, json, os, logging
from flask import Flask, render_template, redirect, url_for, request


#from bots import exec

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/index")
def r_home():
    return redirect('/')


@app.route("/video")
def video():
    return render_template('video.html')


@app.route("/result")
def result():
    return render_template('result.html')

@app.route("/teste")
def teste():
    return render_template('teste.html')

@app.route("/api/test")
def test():
    for i in range(10):
        print(i)
        time.sleep(1)
    print('terminou')
    
    #app.redirect('/video')
         
    return  {"route": '/'}
    
    
@app.route("/api/start-bot", methods=['GET'])
def start_bot():
    #print()
    name = request.args.get('name')
    os.system(f'py bots.pyw "{name}" &')
    #exec(name)
    return {'data': request.args.get('name')}
   

@app.route("/api/status-bot")
def status_bot():
    with open('status.json') as f:
        file = json.loads(f.read())
    return file


if __name__ == "__main__":
    try:
        
        #print(app.config['TEMPLATES_AUTO_RELOAD'])
        app.run(debug=True)
        
        #server = Server(app.wsgi_app)
        #server.serve()
    except Exception as e:
        print(e)
    
    
    