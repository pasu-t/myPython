import argparse

parser = argparse.ArgumentParser()
# what if the descriptive name of the optional parameters in our scripts grows long. Fortunately, we can assign a short name to parameters as well
parser.add_argument('-b', '--blog', help = 'Best blog name here')
args =parser.parse_args()

if args.blog == 'sample':
    print('You made it!')

# python arguparse_optional_shortname.py -b sample
# python arguparse_optional_shortname.py -b text