# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hi():
#     return 'Hii, there!'

# def a(name):
#     return 'This is state %s. %s' % (name, name)
# app.add_url_rule('/hi/<name>','',a)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port='5000',debug=True)

# ------------------------------------------



# from flask import Flask, redirect, url_for

# app = Flask(__name__)

# def user(name):
#     if name == 'admin':
#         return redirect(url_for('admin'))
#     else:
#         return redirect(url_for('guest', guest = name))

# def admin():
#     return 'Hello Admin'

# def guest(guest):
#     return 'Your are enterd as %s .' %guest

# app.add_url_rule('/user/<name>','user',user)
# app.add_url_rule('/admin/','admin',admin)
# app.add_url_rule('/guest/<guest>','guest',guest)

# if __name__ == '__main__':
#     app.run()


# ---------------------Use of GET_POST (Methods)----------------------



# from flask import Flask, redirect, url_for, request
# app = Flask(__name__)

# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' % name

# @app.route('/login/', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['name']
#         print("args ==  "+str(request.args.get('name')))
#         return redirect(url_for('success', name = user))
#     else:
#         print("args  ==  "+str(request.args.get('name')))
#         user = request.args.get('name')
#         return redirect(url_for('success', name = user))

# if __name__ == '__main__':
#     app.run(debug = True)

# ------------------SEND SERVER DATA TO TEMPLATE--------------------------

# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def index():
#     dict = {'phy':50,'che':60,'maths':70}
#     return render_template('form.html',name = dict)

# if __name__ == '__main__':
#     app.run(debug=True)

# ----------------STATIC FILE ACCESS--------------------

# from flask import Flask, redirect, render_template, request

# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def index():
#     # print(request.form)
#     return render_template('index.html',result = request.form)

# @app.route('/form/')  
# def data():
#     return render_template('form.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# ----------------COOKIE--------------------

# from flask import Flask, request, render_template, make_response

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/cookie/',methods=['POST','GET'])
# def cookie():
#     if request.method == 'POST':
#         user = request.form['id']
#         resp = make_response( render_template('form.html'))
#         resp.set_cookie('id', user)

#         return resp

# @app.route('/getcookie')
# def getcookie():
#     name = request.cookies.get('id')
#     return '<h1> Welcome '+ name + '</h1>'

# if __name__ == '__main__':
#     app.run(debug=True)

# ----------------SESSION--------------------

# from flask import Flask, url_for, redirect, session, request

# app = Flask(__name__)
# app.secret_key = 'mySession'

# @app.route('/')
# def index():
#     if 'username' in session:
#         user = session['username']
#         return 'You are login as '+user
#     return 'You are not Login.'

# @app.route('/login/' , methods=['POST','GET'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form method='POST'>
#             username: <input type='text' name='username' />
#             <input type='submit' value='Login' />
#         </form>
#     '''

# @app.route('/logout/')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)

# ----------------ABORT--------------------

# from flask import Flask, redirect, abort, render_template, url_for, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/login/', methods=['GET','POST'])
# def login():
#     if 'POST' in request.method:
#         if request.form['name'] == 'admin':
#             return 'Welcome '+str(request.form['name'])
#         else:
#             return abort(401)


# if __name__ == '__main__':
#     app.run(debug=True)

# ----------------FILE UPLOAD--------------------

from flask import Flask, redirect, request, render_template, abort
import os
# from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'templates/'


@app.route('/')
def index():
    # print("PATH = "+str(os.path.join('/templates',f.filename)))
    return render_template('index.html')

@app.route('/upload/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)