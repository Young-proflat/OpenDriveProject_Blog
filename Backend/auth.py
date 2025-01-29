from flask_restx import Resource, Namespace, fields
from flask import request, jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import JWTManager, access_token, access_refresh_token,jwt_required

auth_ns = Namsespace('auth', description='Namespace for authentication requests')


signup_model = auth_ns.model(
    "signup", 
    {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
        "role": fields.String()
    }
)

login_model = auth_ns.model(
    "login",
    {
        "usename": fields.String(),
        "password": fields.String()
    }
)


@auth_ns.route('/signup')
class SignupForm(Resource):
    
    @auth_ns.expect(signup_model)
    def post(self): 
        data = request.get_json()

        username = data.get('username') 
        user = User.query.filter_by(username=username).first()

        if user is not None:
            return jsonify({"message": f"Username {username} already exist"})
        
        new_user = User(
            username = data.get('username'),
            email = data.get('email'),
            password = generate_password_hash(data.get('password')),
            role = data.get('role')
        )
        new_user.save()
        return jsonify({"message": f"{username} account created successfully"})



@auth_ns.route('/login')
class LoginForm(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username = username).first()

        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid username or password provided'})

        access_token = create_access_token(identity = username)
        refresh_token = create_refresh_token(identity = username)

        return jsonify ({"access_token": access_token, "refresh_token": refresh_token})
