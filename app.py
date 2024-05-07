from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


#hack 1
@app.route("/users", methods=["GET"])
def users():
    return jsonify (
        {
            'payload': 'success'
        }
    )



#hack 2
@app.route("/user", methods=["POST"])
def user():
    return jsonify (
        {
            'payload': 'success'
        }
    )



#hack 3
@app.route("/user", methods=["DELETE"])
def delete_user():
   if request.method == 'DELETE':
       response = {'payload': 'success'}
       return jsonify(response)
   

   

#hack 4
@app.route("/user", methods=["PUT"])
def put_user():
       response = {'error': False, 'payload': 'success'}
       return jsonify(response)
    
   



#hack 5
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    if request.method == 'GET':
        response = {'payload': []}
        return jsonify(response)
    



#hack 6
@app.route('/api/v1/user', methods=['POST'])
def add_user():
    email = request.args.get('email')
    name = request.args.get('name')

    
    payload = {
        'payload': {
            'email': email,
            'name': name
        }
    }

    
    return jsonify(payload)



#hack 7
@app.route('/api/v1/user/add', methods=['POST'])
def post_user():
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')

    
    payload = {
        'payload': {
            'email': email,
            'name': name,
            'id': id
        }
    }

    
    return jsonify(payload)



#hack 8
@app.route("/api/v1/user/create", methods=["POST"])
def create_user():
    if request.method == "POST":
        data = request.get_json()
        email = data.get('email')
        name = data.get('name')
        id = data.get('id')

        response = {
            'payload': {
                'email': email,
                'name': name,
                'id': id
            }
        }

        return jsonify(response)
    else:
        return jsonify({'error': 'Method Not Allowed'}), 405
    

                        

if __name__ == "__main__":
    app.run(debug=True)