import subprocess
import json

urlEnvio = "https://app-utalk.umbler.com/api/v1/messages/simplified/"
token = "" 
fromPhone = ""
organizationId = ""

telefone = "11900000000"

mensagem = "Teste de envio 12345"

comando  = "curl -X 'POST' "
comando += " '{}'  ".format(urlEnvio)
comando += "  -H 'accept: text/plain' "
comando += "  -H 'Authorization: Bearer {}' ".format(token)
comando += "  -H 'Content-Type: multipart/form-data' "
comando += "  -F 'ToPhone=+55{}' ".format(telefone)
comando += "  -F 'FromPhone={}' ".format(fromPhone)
comando += "  -F 'OrganizationId={}' ".format(organizationId)
comando += "  -F 'Message={}' ".format(mensagem)

p = subprocess.Popen(comando, stdout=subprocess.PIPE, shell=True)
saida = p.communicate()[0].decode("utf-8")
retorno = json.loads(saida)

print(retorno)

print(retorno["chat"]["id"])
