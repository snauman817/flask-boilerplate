from flask import Flask, request


# this is our factory
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    else:
        app.config.from_mapping(test_config)

    # The route place to respond to a certain request (this one accepts GET, HEAD, OPTIONS)
    @app.route('/')
    def index():
        return 'This is a flask-boilerplate project, not to be used in production.'

    @app.route('/hello')
    def hello():
        print(request.args)
        print(type(request.args))

        # # loops through all query parameters, and grabs the key and value of each query parameter
        # for key, value in request.args.items():
        #     print(f"{key}: {value}")

        name = request.args.get('name', 'World')
        return f"Hello {name}!"
    
    @app.route('/number/<int:n>')
    def number(n):
        return f"Number: {n}"

    return app