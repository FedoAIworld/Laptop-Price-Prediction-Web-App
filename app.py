from flask import Flask, request, render_template
from model_prep import Price_Prediction

# initialize the flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    For rendering results on HTML GUI
    """
    brand = int( request.form['brand'])
    typename = int(request.form['typename'])
    ram = int(request.form['ram'])
    opsys = int(request.form['opsys'])
    weight = float(request.form['weight'])
    touchscreen = int(request.form['touchscreen'])
    ips = int(request.form['ips'])
    inches = float(request.form['inches'])
    resolution = str(request.form['resolution'])
    cpu = int(request.form['cpu'])
    gpu = int(request.form['gpu'])
    hdd = int(request.form['hdd'])
    ssd = int(request.form['ssd'])

    model_prep = Price_Prediction(brand, typename, ram, opsys, weight, touchscreen, ips, inches, resolution, cpu, gpu, hdd, ssd)
    prediction = (round(float(model_prep.final_prediction[0]),2))

    return render_template('predict.html', prediction_text = 'The predicted laptop price is in the range of €{} and €{}'.format(prediction-100, prediction+100))
    

if __name__ == "__main__":
    app.run()