from flask import Flask, Blueprint, render_template

# Declare a Flask App
app = Flask(__name__)


# Created a Blueprint
basic_controller = Blueprint(
    "basic_controller",
    __name__,
    url_prefix="/",
    template_folder="template-assets/templates",
    static_folder="template-assets/assets",
    static_url_path="assets"
)



@basic_controller.route('/', methods=['GET'])
@basic_controller.route('/registration', methods=['GET'])
def registration():
    return render_template("auth/registration.html")


@basic_controller.route('/login', methods=['GET'])
def login():
    return render_template("auth/login.html")


@basic_controller.route('/forgot-password', methods=['GET'])
def forgotPassword():
    return render_template("auth/forgot-password.html")


@basic_controller.route('/set-password', methods=['GET'])
def setPassword():
    return render_template("auth/set-password.html")


@basic_controller.route('/otp', methods=['GET'])
def otp():
    return render_template("auth/otp.html")


@basic_controller.route("/reset-success", methods=['GET'])
def resetSuccess():
    return render_template('auth/reset-success.html')


# Register the Blueprint
app.register_blueprint(basic_controller)


if __name__ == '__main__':
    app.run(debug=True)