from flask import Flask,jsonify,request,abort

app = Flask(__name__)
app.secret_key='123456789'

# solo local
db = [
	{
		'id' : '001',
		'name' : 'Danny Julca',
		'title' : 'Computer Science'
	},
	{
		'id' : '002',
		'name' : 'Persona2',
		'title' : 'Title2'
	},
	{
		'id' : '003',
		'name' : 'Persona3',
		'title' : 'Title3'
	}
]

@app.route("/")
def hello():
	return "Hola ;)"

@app.route('/db/user',methods=['GET'])
def dbUser_get():
	return jsonify({'user':db})

@app.route('/db/user',methods=['POST'])
def dbUser_post():
	u = {
		'id' : request.json['id'],
		'name' : request.json['name'],
		'title' : request.json['title']
	}
	db.append(u)
	return jsonify(u)

@app.route('/db/user/<userId>',methods=['GET'])
def dbUserId_get(userId):
	user = [ u for u in db if u['id'] == userId ] 
	return jsonify({'user':user})

@app.route('/db/user/<userId>',methods=['PUT'])
def dbUserId_put(userId): 
	user = [ u for u in db if u['id'] == userId ]
	if len(user) == 0:
		abort(404)
	
	if 'name' in request.json : 
		user[0]['name'] = request.json['name'] 
	if 'title' in request.json:
		user[0]['title'] = request.json['title'] 
	return jsonify({'user':user[0]})

@app.route('/db/user/<userId>',methods=['DELETE'])
def dbUserId_delete(userId):
	user = [ u for u in db if u['id'] == userId ]
	if len(user) == 0:
		abort(404)
	
	db.remove(user[0])
	return jsonify({'response':'Success'})


if __name__ == "__main__":
	app.run(debug=True,port=5000)
