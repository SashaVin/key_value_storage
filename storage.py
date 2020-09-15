import argparse
import json
import os
import tempfile


def exit(key):
    with open(storage_path, 'r') as f:
        x = json.load(f)
        d = ', '
        try:
            print(d.join(x[key]))
        except KeyError:
            print()


def check():
    with open(storage_path, 'r') as g:
        try:
            json.load(g)
        except json.decoder.JSONDecodeError:
            with open(storage_path, 'a') as f:
                json.dump({}, f)


def body():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", dest='key')
    parser.add_argument("--val", dest='val')
    parser.add_argument('-n', '--name', type=open, default=storage_path)
    args = parser.parse_args()

    if args.val is not None:
        dct[args.key] = args.val
        with open(storage_path, 'r') as s:
            dict_1 = json.load(s)
            if list(dict_1.keys()).count(args.key) != 0:
                a = dict_1[args.key]
                dict_1[args.key] = []
                dict_1[args.key].append(a)
                dict_1[args.key].append(args.val)
                with open(storage_path, 'w') as f:
                    json.dump(dict_1, f)

            else:
                with open(storage_path, 'w') as f:
                    dict_1.update(dct)
                    json.dump(dict_1, f)
    else:
        exit(args.key)


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
dct = {}

check()
body()
