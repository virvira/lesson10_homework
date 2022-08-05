import os
from utils import load_candidates, get_candidates, get_by_pk, get_by_skill
from flask import Flask

candidates_file = os.path.join('data', 'candidates.json')

app = Flask(__name__)

candidates_list = load_candidates(candidates_file)


@app.route("/")
def show_main():
    res = '<pre>'
    res += get_candidates(candidates_list)
    res += '</pre'
    return res


@app.route("/candidate/<int:x>")
def show_candidate(x):
    candidate = get_by_pk(x, candidates_list)
    candidates = []
    if candidate is not None:
        candidates.append(candidate)
        res = f'<img src="{candidate["picture"]}">'
        res += get_candidates(candidates)
        return res
    return f'Кандидат с pk = {x} не найден'


@app.route("/skills/<skill>")
def show_candidates_with_skill(skill):
    candidates = get_by_skill(skill, candidates_list)
    if candidates:
        res = get_candidates(candidates)
        return res
    return f'Кандидатов с навыком {skill} не найдено'


# get_all(candidates_list)
# print(candidates_list)
# print(get_by_pk(2, candidates_list))
# print(get_by_skill('python', candidates_list))

app.run()
