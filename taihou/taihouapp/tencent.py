import urllib
import urllib2
import json
from taihouapp.models import Account
from django.core.cache import cache

url_openapi='http://openapi.exmail.qq.com:12211/openapi'
token_key='token_string'

def http_post(url,values,token):
    data=urllib.urlencode(values).encode(encoding='UTF8')
    req=urllib2.Request(url,data)
    req.add_header('Authorization',token['token_type']+' '+token['access_token'])
    response=urllib2.urlopen(req)
    resdata=response.read()
    #print(resdata)
    try:
        return json.loads(resdata.decode('UTF8'))
    except:
        return resdata

def GetToken():
    token=cache.get(token_key)
    if token:
        return token
    else:
        secret='168203c4d886b1cd6c513bda63465648'
        Admin='476458427'
        url='https://exmail.qq.com/cgi-bin/token'
        values={'grant_type':'client_credentials','client_id':Admin,'client_secret':secret}
        jdata=urllib.urlencode(values).encode(encoding='UTF8')
        req=urllib2.Request(url,jdata)
        response=urllib2.urlopen(req)
        resp=response.read()
        ret=json.loads(resp.decode('UTF8'))
        cache.set(token_key,ret,int(ret['expires_in']))
        return ret

def CheckAccount(Name):
    token=GetToken()
    values={'email':Name+"@taihou.moe"}
    url=url_openapi+'/user/check'
    ret=http_post(url,values,token)
    ret=ret['List'][0]['Type']
    if ret!=0:
        Account.objects.get_or_create(AccountName=Name.lower())
    return ret
        
def AddAccount(Name):
    token=GetToken()
    values={'Action':'2',
            'Alias':Name.lower()+'@taihou.moe',
            'Name':Name,
            'Gender':'1',
            'Password':'taihou666',
            'PartyPath':'Client',
            'OpenType':1,
            }
    url=url_openapi+'/user/sync'
    ret=http_post(url,values,token)
    if ret==b'':
        p=Account(AccountName=Name.lower(),LoginAuth=True)
        p.save()
        return True
    else:
        return False
    
def AutoLogin(Name):
    token=GetToken()
    values={'Alias':Name+'@taihou.moe'}
    url=url_openapi+'/mail/authkey'
    ret=http_post(url,values,token)
    #print(ret)
    auth=ret['auth_key']
    return auth;
