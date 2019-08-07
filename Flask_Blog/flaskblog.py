from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/test')
def test():
    print(request.form)
    return render_template('test.html')

# Read for understanding the return type of request.form: https://werkzeug.palletsprojects.com/en/0.15.x/datastructures/
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == "POST":
        # Request the forms to return the inputs in form of dictionary
        pins_dict = request.form.to_dict() # Output: dict_keys(['dp0', 'dp3', 'dp6', 'ap0', 'ap4'])

        # Create an empty list for digital pins
        digital_pins = []
        # Create an empty list for analog pins
        analog_pins = []

        # print(pins_dict.keys()) # Debugging

        # Append the pin numbers in their appropriate lists
        for pin in list(pins_dict.keys()):
            if('dp' in pin):
                digital_pins.append(int(pin[2:]))
            elif('ap' in pin):
                analog_pins.append(int(pin[2:]))
        
        # Debugging
        # print(digital_pins)
        # print(analog_pins)

        from testArduino import testWrite
        testWrite(digital_pins, analog_pins)
    return render_template('upload.html')


@app.route('/user/<username>')
def profile(username):
    print(f'The username is {username}')
    return f'<h1>{username}<h1>'


if __name__ == "__main__":
    app.run(debug=True)
