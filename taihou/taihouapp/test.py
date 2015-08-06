import urllib
import urllib.request
import json

url_openapi='http://openapi.exmail.qq.com:12211/openapi'
token_key='token_string'

def http_post(url,values,token):
    data=urllib.parse.urlencode(values).encode(encoding='UTF8')
    req=urllib.request.Request(url,data)
    req.add_header('Authorization',token['token_type']+' '+token['access_token'])
    response=urllib.request.urlopen(req)
    resdata=response.read()
    #print(resdata)
    try:
        return json.loads(resdata.decode('UTF8'))
    except:
        return resdata

def GetToken():
        secret='168203c4d886b1cd6c513bda63465648'
        Admin='476458427'
        url='https://exmail.qq.com/cgi-bin/token'
        values={'grant_type':'client_credentials','client_id':Admin,'client_secret':secret}
        jdata=urllib.parse.urlencode(values).encode(encoding='UTF8')
        req=urllib.request.Request(url,jdata)
        response=urllib.request.urlopen(req)
        resp=response.read()
        ret=json.loads(resp.decode('UTF8'))
        return ret

def CheckAccount(Name):
    token=GetToken()
    values={'email':Name}
    url=url_openapi+'/user/check'
    ret=http_post(url,values,token)
    return ret['List'][0]['Type']

def AddAccount(Name):
    token=GetToken()
    values={'Action':'2',
            'Alias':Name+'@taihou.moe',
            'Name':Name,
            'Gender':'1',
            'Password':'taihou666',
            'PartyPath':'Client',
            'OpenType':0,
            }
    url=url_openapi+'/user/sync'
    ret=http_post(url,values,token)
    print(ret)
    if ret==b'':
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

def GetHTML(Name,auth):
    token=GetToken()
    values={'fun':'bizopenssologin',
            'method':'bizauth',
            'ticket':auth,
            'user':Name+'@taihou.moe',
            'agent':'476458427',
            }
    url='http://exmail.qq.com/cgi-bin/login'
    ret=http_post(url,values,token)
    return ret.decode('GB2312')
