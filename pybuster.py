import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
s = requests.Session()

lista=[]
def buster(url):
    global lista
    retries=Retry(total=5,backoff_factor=0.1,status_forcelist=[ 500,502,503,504])
    try:
        r=requests.get(url, max_retries=retries)
        if str(r)=='<Response [404]>':
            pass
        elif str(r)=='<Response [403]>':
            #'<a target="_blank" href="'+url+'"><em><font font color="#D2738A">'+url+' </a> </font>'
            tp='<a target="_blank" href="'+url+'"><em><font font color="#D2738A">'+url+'</a> </font> <p>FORBIDDEN</p>'
            #tp='URL = '+url+' # FORBIDDEN\n'
            print(url+' # '+str(r))
            lista.append(tp)
            return lista
        else:
            tp='<a target="_blank" href="'+url+'"><em><font font color="#D2738A">'+url+'</a> </font> <p>OK (response 200)</p>'
            #tp='URL = '+url+' # FORBIDDEN\n'
            print(tp)
            lista.append(tp)
            return lista

    except requests.exceptions.ConnectionError:
        print('Connection refused, skipping')

    except:
        pass

def sdir(url, wl):
    #wl=input('Wordlist: ')
    with open(wl, mode='r') as f:
        f=f.readlines()
    print('Wordlist imported successfully')
    cont=0



    for l in range(len(f)):
        f[l]=f[l].replace('\n','')

    i=url
    if 'http://' in i:
        pass
    else:
        i='http://'+i

    if i[-1]=='/':
        pass
    else:
        i=i+'/'



    print(i)

    for e in f:
        cont+=1
        url=i+str(e)
        buster(url)
        if '.html' in url:
            pass
        else:
            url2=i+str(e)+'.html'
            buster(url2)

        if '.php' in url:
            pass
        else:
            url3=i+str(e)+'.php'
            buster(url3)


        print(f"{cont/len(f)*100:.3f} %", end="\r")
        if cont/len(f)*100==100:
            global lista
            return lista

def sub(url, wl):
    #wl=input('Wordlist: ')
    with open(wl, mode='r') as f:
        f=f.readlines()
    print('Wordlist imported successfully')
    cont=0


    for l in range(len(f)):
        f[l]=f[l].replace('\n','')

    i=url
    if 'http://' in i:
        pass
    else:
        i='http://'+i

    if i[-1]=='/':
        pass
    else:
        i=i+'/'


    print(i)
    cont=0
    for e in f:
        cont+=1
        url=i[:7]+str(e)+'.'+i[7:]
        buster(url)

        print(f"{cont/len(f)*100:.3f} %", end="\r")
