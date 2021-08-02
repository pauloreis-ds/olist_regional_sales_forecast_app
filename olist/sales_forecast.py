import joblib
from pandas import DataFrame
# from statsmodels.tsa.arima.model import ARIMA
from .olist_utils import *


class OlistSales:
    def __init__(self):
        directory = Directory(__file__)
        self.arima = joblib.load(os.path.join(directory.MODEL_DIR, "olist_arima_models_by_region.joblib"))
        self.valid_regions = ['midwest', 'north', 'northeast', 'south', 'southeast',
                              'centro oeste', 'norte', 'nordeste', 'sul', 'sudeste',
                              'all', 'todas']

    def get_forecast(self, region='all'):
        region = region.strip(" ").lower()
        if region in ['all', 'todas', '']:
            return self.get_sales_forecast()
        if self.validate_region(region):
            return self.arima[translate_region(region)].forecast(3).tolist()
        else:
            raise ValueError(f"Invalid Region. Current Valid regions: {self.valid_regions}")

    def validate_region(self, region):
        if region in self.valid_regions:
            return True
        if not region:
            print("not: ", region)
            return True
        else:
            return False

    def get_sales_forecast(self):
        preds = {}
        for region in self.arima.keys():
            preds[region] = self.arima[region].forecast(3)
        return list(DataFrame(data=preds).sum(axis=1))