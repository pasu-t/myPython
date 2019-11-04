import argparse

parser = argparse.ArgumentParser()
parser.add_argument('blog', help = 'Name the blog here')
parser.add_argument('-w', '--writer', help = 'name of the writer')
args = parser.parse_args()

if args.blog == 'sample':
	print('you made it')
if args.writer == 'pasu':
	print('technical author')

# python arguparse_optional_positional.py sample
# python arguparse_optional_positional.py sample -w pasupati
# python arguparse_optional_positional.py sample -w pasu