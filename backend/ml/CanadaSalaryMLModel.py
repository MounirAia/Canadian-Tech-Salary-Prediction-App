from typing import Dict

import joblib
import pandas as pd


class CanadaSalaryMLModel:
    model = None

    @staticmethod
    def _getModel():
        if (CanadaSalaryMLModel.model == None):
            CanadaSalaryMLModel.model = joblib.load("ml/Canada.joblib")

        return CanadaSalaryMLModel.model

    @staticmethod
    def predict(parameters: Dict[str, str]):
        model = CanadaSalaryMLModel._getModel()
        input = {}
        for key in parameters:
            input[key] = [parameters[key]]

        input = pd.DataFrame(input)

        yearlyCadSalary = model.predict(input)
        hourlyCadSalary = (yearlyCadSalary*1.33)/(12*4*5*8)

        output = {
            "yearly": round(list(yearlyCadSalary)[0], 2),
            "hourly": round(list(hourlyCadSalary)[0], 2)
        }

        return output
