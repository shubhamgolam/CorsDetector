import argparse
import requests
import os
import sys


#create the parser
parser = argparse.ArgumentParser()

#add argumnets

parser.add_argument('--subdomain', type=str, help='Single or Multiple Subdomains with spaces', nargs='+')
parser.add_argument('--list', type=str,help='Provide list of subdomains with --out file')
parser.add_argument('--out', type=str,help='Provide a output file name')

#parse the argument
args = parser.parse_args()

def make_requests(zzz):
    originheader = {'Origin':'https://evil.com'}
    nullorigin = {'Origin':'null'}


    for x in zzz:
        y = x.replace('\n','')
        r = requests.get('https://'+y)
        print(r.status_code)



if args.subdomain:
    array_sub = []
    i = 0
    for subs in args.subdomain:
        array_sub.append(subs)
        make_requests(subs)




#open the file  > read the subdomains and print them
def list_action():
        file = open(args.list,'r')
        if not args.out:
            print('Please provide --out txt file')
            sys.exit()
        else:
            if os.path.exists(args.out):
                print("File already created. Do you want to overrite it?[yes/no]")
                answer = input()
                if answer == 'yes':
                    print('File will be overwritten')
                    print('\n\n')
                    create = open(args.out,'w')
                    return file
                elif answer == 'no':
                    print('Give some unique name :)')
                    sys.exit()
                else:
                    print('Please make your decision')
                    sys.exit()

if args.list:
    make_requests(list_action())
