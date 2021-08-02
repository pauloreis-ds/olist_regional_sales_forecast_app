from olist.sales_forecast import OlistSales
from flask import Flask, request, Response
import os

olist_sales = OlistSales()
app = Flask(__name__)


@app.route("/olist/forecast", methods=['POST'])
def forecast_sales():
    region = request.get_json()
    try:
        predictions = olist_sales.get_forecast(str(region['region']))
    except Exception as exception:
        predictions = None
        error = exception

    if predictions:
        return f"{predictions}"
    else:
        # response = Response(f"{error}", status=406, mimetype='application/json')
        return f" {error}"


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)

