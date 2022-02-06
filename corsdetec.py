import argparse


#create the parser
parser = argparse.ArgumentParser()

#add argumnets

parser.add_argument('--subdomain', type=str, help='Single or Multiple Subdomains with spaces', nargs='+')
parser.add_argument('--list', type=str,help='Provide list of subdomains')

#parse the argument
args = parser.parse_args()


if args.subdomain:
    print(args.subdomain)



#open the file  > read the subdomains and print them

if args.list:
    file = open(args.list)
    next(file)
    print(file.read())
    file.close()

    #deded
