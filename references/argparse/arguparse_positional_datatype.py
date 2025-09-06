import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('number', help = 'Enter a number to triple it')
parser.add_argument('number', help = 'Enter a number to triple it', type = int)
args = parser.parse_args()
print(args.number*3)

# python arguparse_positional_datatype.py 11