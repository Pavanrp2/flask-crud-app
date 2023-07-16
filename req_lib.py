from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route('/user')
def user():
    name = request.args.get('name')
    surname = request.args.get('surname')
    speciality = request.args.get('speciality')
    return '''<h1> Name of the user : {}</h1>
              <h1> Surname of the user : {}</h1>
              <h1> Speciality of the user : {}</h1>'''.format(name , surname , speciality)


@app.route('/form_example' , methods = ['POST' , 'GET'])
def form_example():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        return '''<h1>New user created successfully</h1>
                   <h4>Name of the candidate : {} <br><br>
                   Surname of the candidate is :{}</h4>'''.format(name , surname)

    
    return ''' <form method = "POST">
                Name <input type="text" name = "name">
                Surname <input type="text" name = "surname">
                <input type="SUbmit">
                '''

if __name__ == '__main__':
    app.run(debug=True , port=5000)