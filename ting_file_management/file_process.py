from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    for f in instance._data:
        if f["nome_do_arquivo"] == path_file:
            return None
    response = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    instance.enqueue(response)
    print(response)


def remove(instance):
    if len(instance._data) == 0:
        print("Não há elementos")
        return None
    remove = instance.dequeue()
    path_file = remove["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(instance._data[position])
    except IndexError:
        return sys.stderr.write("Posição inválida")
