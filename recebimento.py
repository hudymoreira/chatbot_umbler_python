import subprocess
import json

idChat = ""
#token = "" 
#organizationId = ""

comando =  " curl -X 'GET' " 
comando += " 'https://app-utalk.umbler.com/api/v1/chats/{}/?organizationId={}' ".format(idChat,organizationId)
comando += "  -H 'accept: text/plain' "
comando += "  -H 'Authorization: Bearer {}'".format(token)

p = subprocess.Popen(comando, stdout=subprocess.PIPE, shell=True)
saida = p.communicate()[0].decode("utf-8")
resposta = json.loads(saida)
print(resposta['lastMessage']['content'])
