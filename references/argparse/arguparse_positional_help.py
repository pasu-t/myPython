import argparse

parser = argparse.ArgumentParser()
parser.add_argument('blog', default = 'sample', help = 'best blog name here')
args = parser.parse_args()

if args.blog == 'sample':
	print('you made it')
else:
	print("you didn't made it")

# python arguparse_positional_help.py sample
# python arguparse_positional_help.py xyz
# python arguparse_positional_help.py