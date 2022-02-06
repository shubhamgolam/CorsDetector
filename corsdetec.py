import argparse
import requests


#create the parser
parser = argparse.ArgumentParser()

#add argumnets

parser.add_argument('--subdomain', type=str, help='Single or Multiple Subdomains with spaces', nargs='+')
parser.add_argument('--list', type=str,help='Provide list of subdomains')
parser.add_argument('--out', type=str,help='Provide a output file name')

#parse the argument
args = parser.parse_args()


if args.subdomain:
    print(args.subdomain)



#open the file  > read the subdomains and print them

if args.list:
    file = open(args.list,'r')
    try:
        create = open(args.out,'x')
    except:
        print("File already created. Do you want to overrite it?[yes/no]")
        answer = input()
        if answer == 'yes':
            print('File overwritten')
            create = open(args.out,'w')
        elif answer == 'no':
            print('Give some unique name :)')
            pass

    #make requets to Subdomains with fix origin

    origonheader = {'Origin':'https://evil.com'}
    nullorigin = {'Origin':'null'}

    for x in file:
        y = x.replace('\n','')
        r = requests.get('https://'+y,origonheader["Origin"])
        print(r.url)
