import os

# local do arquivo
folder = (r'caminho da pasta')


def rename_files():
    for filename in os.listdir(folder):
        try:
            # split_file = o nome do arquivo é fatiado e transformado em uma lista dividia pelo "."
            split_file = f'{filename}'.split('.')
            # new = a primeira parte do nome
            new = str(split_file[0])
            # src = local do arquivo original
            src = f'{folder}/{filename}'
            # dst = o local do arquivo com a nova extenssão
            dst = f'{folder}/{new}.jpg'
            # os.rename = renomeia os arquivos
            os.rename(src, dst)

            # mostra o processo de alteração
            print(f'Anterior: {filename} --->  Novo: {dst}')
        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    rename_files()
