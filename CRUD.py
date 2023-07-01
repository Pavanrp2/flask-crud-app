from flask import Flask , request , jsonify

app = Flask(__name__)

user_Data = [
    {
        "user_id" : 1,
        "user_name" : "Pavan",
        "last_name" : "Patil",
        "age" : 24
    },
    {
        "user_id" : 2,
        "user_name" : "Basvaraj",
        "last_name" : "Patil",
        "age" : 25
    }
]


@app.route("/")
def index():
    return "This is Flask"


#read operation : Get all users
@app.route("/allUsers")
def allUsers():
    return jsonify(user_Data)


#read operation : Get a specific User by their id
@app.route('/user_id/<int:user_id>', methods = ['GET'])
def update(user_id):
    for item in user_Data:
        if item["user_id"] == user_id:
            return item
            response = {"message" : "User found successfully"}
    return "User not found"


#create a new user : 
@app.route("/addUser", methods = ['POST'])
def addUser():
    data = request.get_json()
    print(data)
    user_Data.append(data)
    response = {'message' : 'POST request received successfully'}
    return 'Successfully added new user'


# update operation : Update existing data 
@app.route('/update_user/<int:user_id>' , methods = ['PUT'])
def update_user(user_id):
    for item in user_Data:
        if item['user_id'] == user_id:
            item['user_name'] = request.json['user_name']
            item['last_name'] = request.json['last_name']
            item['age'] = request.json['age']
            return item
    return {'message' : 'book not found chinna'}


#Delete operation : Delete existing data 
@app.route('/delete/<int:user_id>' , methods = ['DELETE'])
def delete_user(user_id):
    for item in user_Data:
        if item['user_id'] == user_id:
            user_Data.remove(item)
            return {'message' : 'successfully deleted user'}
    return 'user not found '


if __name__ == "__main__":
    app.run(debug=True , port=2000)





