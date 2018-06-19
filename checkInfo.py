import urllib
import ast
import datetime
import time

print '-----------------------------------------------'
print '                 Jenkins API'
print '-----------------------------------------------\n'

print 'Iniciando o job "Check info"...'
triggerURL = 'http://localhost:8080/job/Check%20info/build?token=stringDeAutenticacao'
urllib.urlopen(triggerURL)
time.sleep(10)

print 'Job iniciado!'
print '\n\n'
print 'Obtendo informacoes sobre o job...\n'

jenkinsAPI = "http://localhost:8080/job/Check%20info/api/python?token=stringDeAutenticacao"
jobInfo = ast.literal_eval(urllib.urlopen(jenkinsAPI).read()) 

jobName = jobInfo["displayName"]
jobBuilds = jobInfo["builds"]

print "--------------------------------------"
print "Build         Data          Resultado"
print "--------------------------------------"
for i in range(0, 5):
    buildURL = jobBuilds[i]["url"] + "api/python?token=stringDeAutenticacao"
    buildInfo = ast.literal_eval(urllib.urlopen(buildURL).read())
    
    timestamp = datetime.datetime.fromtimestamp(buildInfo["timestamp"]/1000).strftime('%d/%m/%Y %H:%M:%S')
    
    if buildInfo["result"] is None:
        result = "Rodando"
    else:
        result = buildInfo["result"]

    print ' ' + str(buildInfo["number"]) + '    ' + timestamp + '   ' + result