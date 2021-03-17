import fileinput, argparse

parser = argparse.ArgumentParser()
parser.add_argument('version')
with fileinput.FileInput('kernel-metadata.json', inplace=True) as file:
    for line in file:
        print(line.replace('VERSION', parser.parse_args().version), end='')
