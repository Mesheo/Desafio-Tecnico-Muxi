import os
import shutil

diretorioMAIN = os.path.abspath('.')

#Função para criar as pastas do diretório de carga
def criar_pastas():
    f = 'f'
    print('Criando as pastas do diretório de carga...')

    os.mkdir('load')
    os.mkdir('load\POSWEB')
    os.mkdir('load\POSWEB\i')
    os.mkdir(os.path.join('load\POSWEB', 'f'))

    print('----pasta load criada----')
    print('----pasta load\POSWEB criada---')
    print('----pasta load\POSWEB\i criada---')
    print(f'----pasta load\POSWEB\{f} criada----')

#Função para coletar a extensão de cada arquivo
def pegar_extensao(nome):
    index = nome.rfind('.')
    return nome[index:]

#Função que renomeia o arquivo para uma nova extensão
def renomear(diretorio, arquivo, extensao_nova):

    print(f'Renomeando a extensão dos arquivos no diretorio {diretorio}')
    extensao_antiga = pegar_extensao(arquivo)
    arquivo_novo = arquivo.replace(extensao_antiga, extensao_nova)
    os.rename(os.path.join(diretorio, arquivo), os.path.join(diretorio, arquivo_novo))
    print(f'----renomeei a extensão do {arquivo} para {extensao_nova}---')

#Compila os arquivos WMLS para WMLSC
def compilar_WMLSC(diretorio):
    print(f'compilando os arquivos WMLSC do diretorio {diretorio}...')

    compiler_path = os.path.abspath('WMLSComp.exe')
    arquivosWMLS = os.listdir(os.path.join(os.path.abspath('.'), diretorio))

    for arquivo in arquivosWMLS:
        extensao = pegar_extensao(arquivo)

        if extensao == '.wmls':
            print(f'----compilei o arquivo {arquivo}----')
            archive_path = os.path.abspath(os.path.join(diretorio, arquivo))
            os.system(f"{compiler_path} {archive_path}")
    print('\n')

def main():
    criar_pastas()

    #diretorios
    srcPOSWEB = os.path.join(diretorioMAIN, 'src\POSWEB')
    loadPOSWEB = os.path.join(diretorioMAIN, 'load\POSWEB')
    loadPOSWEBf = os.path.join(diretorioMAIN, (os.path.join('load\POSWEB', 'f')))
    loadPOSWEBi = os.path.join(diretorioMAIN, 'load\POSWEB\i')
    srcPOSWEBdb = os.path.join(diretorioMAIN, 'src\POSWEB\db')
    srcPOSWEBimages = os.path.join(diretorioMAIN, 'src\POSWEB\images')
    scr_font = os.path.join(diretorioMAIN, 'src\_font')
    src = os.path.join(diretorioMAIN, 'src')
    scr_theme = os.path.join(src, '_theme')
    scr_minimal = os.path.join(src, '_minimal')

    compilar_WMLSC('src\POSWEB')
    arquivos_srcPOSWEB = os.listdir(srcPOSWEB)

    #Renomeia todos os arquivos .wmlsc para .wsc; ✅
    for arquivo in arquivos_srcPOSWEB:
        extensao = pegar_extensao(arquivo)
        if extensao == '.wmlsc':
            renomear(srcPOSWEB, arquivo, '.wsc')

    #Atualização da lista arquivosPOSWEB
    arquivos_srcPOSWEB = os.listdir(srcPOSWEB)

    #Movimentação de arquivos de acordo com a extensão 
    for arquivo in arquivos_srcPOSWEB:
        extensao = pegar_extensao(arquivo)
    
        # * Move arquivos .wsc para o diretório load\POSWEB\f\ ✅
        if extensao == '.wsc':
            shutil.move(os.path.join(srcPOSWEB, arquivo), loadPOSWEBf)
            print(f'movi o arquivo {arquivo} para o diretório {loadPOSWEBf}')
        # * Copia arquivos .wml para o diretório load\POSWEB\f\ ✅
        elif extensao == '.wml':
            shutil.copy(os.path.join(srcPOSWEB, arquivo), loadPOSWEBf)
            print(f'copiei o arquivo {arquivo} para {loadPOSWEBf}')
        # *Copia arquivo config.ini para o diretório load\POSWEB\i\; ✅
        elif extensao == '.ini':
            shutil.copy(os.path.join(srcPOSWEB, arquivo), loadPOSWEBi)
            print(f'copiei o arquivo {arquivo} para o direrório {loadPOSWEBi}')

    arquivos_srcPOSWEBdb = os.listdir(srcPOSWEBdb)
    # * Copia arquivos em src\POSWEB\db\ para load\POSWEB\i\ ✅ 
    for arquivo in arquivos_srcPOSWEBdb:
        endereçoAntigo = os.path.join(srcPOSWEBdb, arquivo)
        endereçoFinal = os.path.join(diretorioMAIN, 'load/POSWEB/i')
        shutil.copy(endereçoAntigo, endereçoFinal)
        print(f'copiei o arquivo {arquivo} para o direrório {loadPOSWEBi}')


    # * Copia arquivos em src\POSWEB\images\ para load\POSWEB\f\ ✅
    arquivos_srcPOSWEBimages = os.listdir(srcPOSWEBimages)
    for arquivo in arquivos_srcPOSWEBimages:
        endereçoAntigo = os.path.join(srcPOSWEBimages, arquivo)
        endereçoFinal = os.path.join(diretorioMAIN, os.path.join('load\POSWEB', 'f'))
        shutil.copy(endereçoAntigo, endereçoFinal)
        print(f'copiei o arquivo {arquivo} para o direrório {loadPOSWEBf}')

    # * A partir do diretório src\_font, copiar APENAS arquivos com extensão .pwf para load\POSWEB\f\; ✅
    arquivos_src_font = os.listdir(scr_font)
    for arquivo in arquivos_src_font:
        extensao = pegar_extensao(arquivo)

        #Verifica se a extensão do arquivo satisfaz o requisito de cópia
        if extensao == '.pwf':
            endereçoAntigo = os.path.join(scr_font, arquivo)
            endereçoFinal = os.path.join(diretorioMAIN, os.path.join('load\POSWEB', 'f'))
            shutil.copy(endereçoAntigo, endereçoFinal)
            print(f'copiei o arquivo {arquivo} para o direrório {loadPOSWEBi}')


    #Copia arquivos de src\_theme\ para load\POSWEB\f\; ✅
    arquivos_scr_theme = os.listdir(scr_theme)
    for arquivo in arquivos_scr_theme:
        endereçoAntigo = os.path.join(scr_theme, arquivo)
        endereçoFinal = os.path.join(diretorioMAIN, os.path.join('load\POSWEB', 'f'))
        shutil.copy(endereçoAntigo, endereçoFinal)
        print(f'copiei o arquivo {arquivo} para o diretório {endereçoFinal}')
    print('\n')

    #Copiar arquivos de src\_minimal\ para load\POSWEB\i\;✅
    arquivos_scr_minimal = os.listdir(scr_minimal)
    for arquivo in arquivos_scr_minimal:
        endereçoAntigo = os.path.join(scr_minimal, arquivo)
        endereçoFinal = os.path.join(diretorioMAIN, 'load\POSWEB\i')
        shutil.copy(endereçoAntigo, endereçoFinal)
        print(f'copiei o arquivo {arquivo} para o diretório {endereçoFinal}')
    print('\n')

    #Cria arquivo flist.web e preenche com o nome de todos os itens do diretório load\POSWEB\f\ ✅
    os.chdir(loadPOSWEB)
    filistWEB = open('flist.web', 'w')
    for arquivo in os.listdir(loadPOSWEBf):
        filistWEB.write(f'{arquivo} \n')
    filistWEB.close()

    #Cria arquivo ilist.web e preenche com o nome de todos os itens do diretório load\POSWEB\i\ ✅
    ilistWEB = open('ilist.web','w')
    for arquivo in os.listdir(loadPOSWEBi):
        ilistWEB.write(f'{arquivo} \n')
    ilistWEB.close()

if __name__ == '__main__':
    main()