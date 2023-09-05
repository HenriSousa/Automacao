import os
import datetime
from shutil import copyfile

# Diretorios
caminhoBackupsFrom = "./home/valcann/backupsFrom"
caminhoBackupsTo = "./home/valcann/backupsTo"

# Caminho dos log's
caminhoLogFrom = os.path.join(caminhoBackupsFrom, 'backupsFrom.log')
caminhoLogTo = os.path.join(caminhoBackupsTo, 'backupsTo.log')

# Mostrar todos os arquivos
mostrarArquivos = os.listdir(caminhoBackupsFrom)

# Data atual e data limite de 3 dias
dataAtual = datetime.datetime.now()
dataLimite = dataAtual - datetime.timedelta(days=3)

# Cria o arquivo de log caso não exista
if not os.path.exists(caminhoLogFrom):
    open(caminhoLogFrom, 'w').close()

if not os.path.exists(caminhoLogTo):
    open(caminhoLogTo, 'w').close()

# Abre os arquivos log's para inserir informações
with open(caminhoLogFrom, 'a') as logFrom, \
        open (caminhoLogTo, 'a') as logTo:
    #Passa em todos os arquivos dentro da pasta (/home/valcann/backupsFrom)
    for arquivo in mostrarArquivos:
        caminhoArquivo = os.path.join(caminhoBackupsFrom, arquivo)

        infoArquivo = os.stat(caminhoArquivo) # Retorna os Status do arquivo
        tamanho = infoArquivo.st_size # Retorna o tamanho do arquivo
        dataCriacao = datetime.datetime.fromtimestamp(infoArquivo.st_ctime) # Retorna a data que o arquivo foi criado
        dataModificacao = datetime.datetime.fromtimestamp(infoArquivo.st_mtime) # Retorna a data de modificao

        #Escreve no arquivo .txt
        logFrom.write(f"Nome: {arquivo}\n")
        logFrom.write(f"Tamanho: {tamanho}\n")
        logFrom.write(f"Data de Criação: {dataCriacao}\n")
        logFrom.write(f"Data da Última Modificação: {dataModificacao}\n\n")

        #Quando o arquivo for menor ou igual a 3 dias ele vai ser copiado para (/home/valcann/backupsTo)
        if dataCriacao >= dataLimite:
            copyfile(caminhoArquivo, os.path.join(caminhoBackupsTo, arquivo))
            logTo.write(f"Arquivo copiado para {caminhoBackupsTo}: {arquivo}\n")
        #Quando o arquivo for maior que 3 dias ele vai ser removido do local (/home/valcann/backupsFrom)
        else:
            os.remove(caminhoArquivo)
            logFrom.write(f"Arquivo removido de {caminhoBackupsFrom}: {arquivo}\n")

print("Operação realizada com Sucesso!")
