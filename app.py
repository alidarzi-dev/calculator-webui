from flask import Flask, render_template, request

app = Flask(__name__)

# List to store recent calculations
recent_calculations = []

@app.route('/')
def index():
    return render_template('index.html', recent_calculations=recent_calculations)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        global recent_calculations  # Declare recent_calculations as a global variable
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        else:
            result = "Error: Invalid operation"

        # Add the calculation to the list of recent calculations
        recent_calculations.insert(0, f"{num1} {operation} {num2} = {result}")
        # Keep only the last 5 calculations
        recent_calculations = recent_calculations[:5]

        return render_template('index.html', result=f"Result: {result}", recent_calculations=recent_calculations)
    except ValueError:
        return render_template('index.html', result="Error: Invalid input", recent_calculations=recent_calculations)

if __name__ == '__main__':
    app.run(debug=True)
