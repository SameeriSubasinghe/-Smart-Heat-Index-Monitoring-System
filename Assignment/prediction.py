import pickle
from datetime import date, timedelta
import json


def get_prediction():
    filename = 'model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    today = date.today()
    f_date = today + timedelta(days=365)
    p_date = today + timedelta(days=-365)

    f_predictions = loaded_model.predict(today, f_date)
    f_date_lst = []
    for i in range(0, len(f_predictions)):
        dt = f_predictions.index[i].to_timestamp()
        f_date_lst.append(str(dt).split()[0])

    f_val_lst = []
    for i in range(0, len(f_predictions)):
        f_val_lst.append(f_predictions[i])

    f_data_dict = {
        'date': f_date_lst,
        'data': f_val_lst
    }

    p_predictions = loaded_model.predict(p_date, today)
    p_date_lst = []
    for i in range(0, len(p_predictions)):
        dt = p_predictions.index[i].to_timestamp()
        p_date_lst.append(str(dt).split()[0])

    p_val_lst = []
    for i in range(0, len(p_predictions)):
        p_val_lst.append(p_predictions[i])

    p_data_dict = {
        'date': p_date_lst,
        'data': p_val_lst
    }

    with open("forecast.json", "w") as outfile:
        json.dump(f_data_dict, outfile)

    with open("previous.json", "w") as outfile:
        json.dump(p_data_dict, outfile)


if __name__ == '__main__':
    get_prediction()
