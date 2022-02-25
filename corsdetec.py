import argparse
import requests
import os
import sys
import time
from requests.packages import urllib3
from concurrent.futures import ThreadPoolExecutor

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#create the parser
parser = argparse.ArgumentParser()

#add argumnets

parser.add_argument('--subdomain', type=str, help='Single or Multiple Subdomains with spaces', nargs='+')
parser.add_argument('--list', type=str,help='Provide list of subdomains with --out file')
parser.add_argument('--out', type=str,help='Provide a output file name')
parser.add_argument('--N', action='store_true',help='Check for NULL origin') #we just want the flag -N hence the action is store_true
#parse the argument
args = parser.parse_args()

start = time.perf_counter()

def make_requests(readfile):


    originheader = {}


    if (args.list or args.subdomain) and args.N:
        originheader['Origin'] = 'null'
        origin = originheader['Origin']

    else:
        originheader['Origin'] = 'https://evil.com'
        origin = originheader['Origin']



    # Route the traffic through proxies like burpsuite
    proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}


    if args.list:
        with open(args.out,'a') as a:
                r = requests.get('https://'+readfile, proxies=proxies,headers=originheader,verify=False)
                ACAO = r.headers.get('Access-Control-Allow-Origin')
                ACAC = r.headers.get('Access-Control-Allow-Credentials')

                checkcors(ACAO,ACAC,origin,a,readfile)


    if args.subdomain:
        r = requests.get('https://'+readfile,proxies=proxies,headers=originheader,verify=False)
        ACAO = r.headers.get('Access-Control-Allow-Origin')
        ACAC = r.headers.get('Access-Control-Allow-Credentials')

        checkcors(ACAO,ACAC,origin,None,readfile)



def checkcors(ACAO,ACAC,origin,*giveme):


    a = giveme[0]
    domain = giveme[1]


    if ACAO == origin and ACAC is None:
        if args.list:
            a.write(domain+'\n')
            a.write(f'ACAO is {ACAO}')
            a.write('Only ACAO is reflected'+'\n')

        else:
            print(domain)
            print(f'ACAO is {ACAO}')
            print('Only ACAO is reflected\n')

    elif ACAO == '*' and ACAC is None:
        if args.list:
            a.write(domain+'\n')
            a.write('Wildcart Supported'+'\n')

        else:
            print(domain)
            print('Wildcart Supported\n')

    elif ACAO == '*' and ACAC == 'true':
        if args.list:
            a.write(domain+'\n')
            a.write('ACAO is * and Creds is True' +'\n')

        else:
            print(domain)
            print('ACAO is * and Creds is True\n')

    elif ACAO == origin and ACAC == 'true':
        if args.list:
            a.write(domain+'\n')
            a.write('Possible CORS Misconfiguration'+'\n')

        else:
            print(domain)
            print('Possible CORS Misconfiguration\n')

    else:
        if args.list:
            a.write(domain+'\n')
            a.write('No reflection' + '\n' )

        else:
            print(domain)
            print('No reflection\n')



if args.subdomain:
    data =  args.subdomain
    with ThreadPoolExecutor(max_workers=30) as executor:
        executor.map(make_requests,data)




#open the file  > read the subdomains and print them
def list_action():
        with open(args.list,'r') as f:
            file = f.read()
        file = file.split('\n')
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
                    os.remove(args.out)


                elif answer == 'no':
                    print('Give some unique name :)')
                    sys.exit()
                else:
                    print('Please make your decision')
                    sys.exit()
        return file


if args.list:
    with ThreadPoolExecutor(max_workers=30) as executor:
        executor.map(make_requests,list_action())

#print('Total time:',time.perf_counter()-start)
