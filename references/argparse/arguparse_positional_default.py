import argparse

parser = argparse.ArgumentParser()
parser.add_argument('blog', nargs='?', default = 'sample')
args = parser.parse_args()

if args.blog == 'sample':
	print('you made it')
else:
	print("you didn't made it")

# python arguparse_positional_default.py sample
# python arguparse_positional_default.py xyz
# python arguparse_positional_default.py