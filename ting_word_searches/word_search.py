def create_response(cases, response, word, name):
    if len(cases) > 0:
        response.append({
            'arquivo': name,
            'ocorrencias': cases,
            'palavra': word,
        })
    return response

def find__words(lines, word, word_exists):
    cases = []
    for index, line in enumerate(lines, 1):
        if line.lower().find(word.lower()) != -1:
            if word_exists:
                cases.append({'linha': index})
            else:
                cases.append({
                    'linha': index,
                    'conteudo': line,
                })
    return cases

def exists_word(word, instance):
    response = []
    word_exists = True
    for archive in instance._data:
        archive_lines = archive['linhas_do_arquivo']
        cases = find__words(archive_lines, word, word_exists)
        archive_name = archive['nome_do_arquivo']
        response = create_response(cases, response, word, archive_name)
    return response

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
