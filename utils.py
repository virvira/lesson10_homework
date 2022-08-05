import json


def load_candidates(file_):
    '''Загружает данные из файла, возвращает список кандидатов'''
    with open(file_, 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def get_candidates(candidates_list):
    '''Показывает всех кандидатов'''
    res = '<pre>'
    for candidate in candidates_list:
        res += f'Имя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки через ' \
               f'запятую - {str(candidate["skills"]).lower()}\n\n'
    res += '</pre>'
    return res


def get_by_pk(pk, candidates_list):
    '''Возвращает кандидата по pk'''
    for candidate in candidates_list:
        if candidate["pk"] == pk:
            return candidate
    return None


def get_by_skill(skill_name, candidates_list):
    '''Возвращает кандидатов по навыку'''
    candidates_with_skill = []
    for candidate in candidates_list:
        if skill_name.lower() in candidate["skills"].lower().split(', '):
            candidates_with_skill.append(candidate)
    return candidates_with_skill
