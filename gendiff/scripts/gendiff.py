import argparse
import json


def generate_diff(path_to_file1, path_to_file2):
    first_file = json.load(open(path_to_file1))
    second_file = json.load(open(path_to_file2))
    diff = '{\n'
    set_of_keys = set(first_file.keys()) | set(second_file.keys())
    for key in set_of_keys:
        if first_file.get(key) == second_file.get(key):
            diff += '    {}: {}\n'.format(key, first_file[key])
            continue
        elif first_file.get(key) and second_file.get(key):
            diff += '  + {}: {}\n'.format(key, second_file[key])
            diff += '  - {}: {}\n'.format(key, first_file[key])
            continue
        elif first_file.get(key):
            diff += '  - {}: {}\n'.format(key, first_file[key])
            continue
        else:
            diff += '  + {}: {}\n'.format(key, second_file[key])
    diff += '}'
    return diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        help='set format of output',
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()

