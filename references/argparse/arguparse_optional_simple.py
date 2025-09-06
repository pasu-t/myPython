import argparse

parser = argparse.ArgumentParser()
'''
With the -- before the optional parameter name, we can define optional parameters in any order.
The method for passing default values, help messages and data types for optional parameters is same as in positional parameters. 
Just a point to be noted, if no value is passed to an optional argument, it is assigned a value of None for the program.
'''
parser.add_argument('--blog', help = 'Best blog name here')
args =parser.parse_args()

if args.blog == 'sample':
    print('You made it!')


# python arguparse_optional_simple.py sample
# python arguparse_optional_simple.py --blog sample
# python arguparse_optional_simple.py --blog text