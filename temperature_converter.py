from flask import Flask

app = Flask(__name__)

@app.route('/c')
@app.route('/c/<celsius>')
def c_to_f(celsius=0):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return '{:.2f} F'.format(fahrenheit)


@app.route('/f')
@app.route('/f/<fahrenheit>')
def f_to_c(fahrenheit=0):
    celsius = 5 / 9 * (float(fahrenheit) - 32)
    return '{:.2f} C'.format(celsius)


if __name__ == '__main__':
    app.run()

