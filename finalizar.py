import subprocess
import json

token = ""
sectorId = ""
memberId = ""
channelId = ""
organizationId = ""

idChat = ""

comando =  " curl -X 'PUT' " 
comando += " 'https://app-utalk.umbler.com/api/v1/chats/{}/?organizationId={}' ".format(idChat,organizationId)
comando += " -H 'accept: text/plain' "
comando += " -H 'Authorization: Bearer {}' ".format(token)
comando += " -H 'Content-Type: application/json' "
comando += " -d '{"
comando += " \"open\": false,"
comando += " \"sectorId\": \"{}\",".format(sectorId)
comando += " \"memberId\": \"{}\", ".format(memberId)
comando += " \"channelId\": \"{}\",".format(channelId)
comando += " \"private\": true,"
comando += " \"mute\": true }'"

p = subprocess.Popen(comando, stdout=subprocess.PIPE, shell=True)
saida = p.communicate()[0].decode("utf-8")
resposta = json.loads(saida)
print(resposta)
