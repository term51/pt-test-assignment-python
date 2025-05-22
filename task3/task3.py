import sys
import json


def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def get_value_by_id(data, val_id):
    for item in data:
        if item['id'] == val_id:
            return item['value']

    return None


def set_value(tests_data, values_data):
    for test in tests_data:
        value = get_value_by_id(values_data['values'], test['id'])
        test['value'] = value
        if 'values' in test and len(test['values']) > 0:
            set_value(test['values'], values_data)


def make_report(values_path, tests_path, report_path):
    with open(values_path) as f:
        values_data = json.load(f)

    with open(tests_path, 'r') as f:
        tests_data = json.load(f)

    set_value(tests_data['tests'], values_data)

    write_json(report_path, tests_data)


make_report(sys.argv[1], sys.argv[2], sys.argv[3])
