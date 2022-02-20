import argparse
import requests
import os
import sys

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#create the parser
parser = argparse.ArgumentParser()

#add argumnets

parser.add_argument('--subdomain', type=str, help='Single or Multiple Subdomains with spaces', nargs='+')
parser.add_argument('--list', type=str,help='Provide list of subdomains with --out file')
parser.add_argument('--out', type=str,help='Provide a output file name')

#parse the argument
args = parser.parse_args()

def make_requests(*takeall):
    #takeall is tuple of tuple ((a,zzz),) with file and (sub,) for subdomain
    rrr = takeall[0] #take the first value from tuple
    a = rrr[1]#take the file write object


    originheader = {'Origin':'https://evil.com'}
    nullorigin = {'Origin':'null'}

    origin = originheader.get('Origin')

    # Route the traffic through proxies
    proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}


    if args.list:
        zzz = rrr[0]
        for x in zzz:
            y = x.replace('\n','')
            a.write(y + '\n')

            r = requests.get('https://'+y, proxies=proxies,headers=originheader,verify=False)
            ACAO = r.headers.get('Access-Control-Allow-Origin')
            ACAC = r.headers.get('Access-Control-Allow-Credentials')

            checkcors(ACAO,ACAC,origin,a,y)


    if args.subdomain:
        r = requests.get('https://'+rrr[0],proxies=proxies,headers=originheader,verify=False)
        ACAO = r.headers.get('Access-Control-Allow-Origin')
        ACAC = r.headers.get('Access-Control-Allow-Credentials')

        checkcors(ACAO,ACAC,origin,rrr,None)



def checkcors(ACAO,ACAC,origin,*giveme):
    #same tuple logic here

    a= giveme[0]
    domain = giveme[1]


    if ACAO == origin and ACAC is None:
        if args.list:
            a.write(f'ACAO is {ACAO}')
            a.write('Only ACAO is reflected\n')

        else:
            print(f'ACAO is {ACAO}')
            print('Only ACAO is reflected\n')

    elif ACAO == '*' and ACAC is None:
        if args.list:
            a.write('Wildcart Supported\n')

        else:
            print('Wildcart Supported\n')

    elif ACAO == '*' and ACAC == 'true':
        if args.list:
            a.write('ACAO is * and Creds is True' +'\n')

        else:
            print('ACAO is * and Creds is True\n')

    elif ACAO == origin and ACAC == 'true':
        if args.list:
            a.write('Possible CORS Misconfiguration'+'\n')

        else:
            print('Possible CORS Misconfiguration\n')

    else:
        if args.list:
            a.write('No reflection' + '\n' )

        else:
            print('No reflection\n')


if args.subdomain:
    for subs in args.subdomain:
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
                    print('\n')
                    create = open(args.out,'w')
                    create.close()

                    a = open(args.out,'a')

                    return file, a

                elif answer == 'no':
                    print('Give some unique name :)')
                    sys.exit()
                else:
                    print('Please make your decision')
                    sys.exit()



if args.list:
    make_requests(list_action())
