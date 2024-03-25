import json
import os


def generate_sample_JSON(mission="igwn_gwalert", alert_type="initial"):
    path = os.path.join(os.path.split(__file__)[0], mission)
    samples = os.listdir(path=path)
    alert_type = alert_type.lower()
    print(samples)
    for sample in samples:
        sample_type = sample.split("-")[1].split(".")[0]
        sample_type = sample_type.lower()
        if sample_type == alert_type:
            with open(os.path.join(path, sample), 'r') as file:
                record = json.load(file)
            return record
    record = {}
    print('no match record.')
    return record

