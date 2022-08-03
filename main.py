import flask
from flask_cors import CORS
import utils.functions.functions as funcs

app = flask.Flask(__name__)
CORS(app)


@app.route('/VehicleSummary/<string:registration>', methods=['GET'])
def vehicle_data_request(registration):
    information = funcs.get_vehicle_details(registration)
    return information.to_dict()


# app.run(host='hexreports.com')
app.run()



