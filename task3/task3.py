import sys
import json


def read_values(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return {item['id']: item['value'] for item in data['values']}


def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def fill_with_value(test_data, values_map):
    if isinstance(test_data, list):
        return [fill_with_value(item, values_map) for item in test_data]

    if isinstance(test_data, dict):
        if 'id' in test_data and 'value' in test_data:
            test_data['value'] = values_map.get(test_data['id'], '')

        if 'values' in test_data:
            test_data['values'] = fill_with_value(test_data['values'], values_map)

    return test_data


def make_report(values_path, tests_path, report_path):
    values_map = read_values(values_path)
    with open(tests_path, 'r') as f:
        tests_data = json.load(f)

    tests_data['tests'] = fill_with_value(tests_data['tests'], values_map)

    write_json(report_path, tests_data)


make_report(sys.argv[1], sys.argv[2], sys.argv[3])
