"""Embed topics-r1/blind/cards.json (no origin labels) into the grading page -> topics-r1/blind/grade.html."""
import hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
raw = open(os.path.join(HERE, 'cards.json'), 'rb').read()
cards = json.loads(raw)
page = open(os.path.join(HERE, 'page.template.html')).read()
page = page.replace('/*CARDS_JSON*/null', json.dumps(cards, ensure_ascii=False).replace('</', '<\\/'))
page = page.replace("/*CARDS_SHA*/''", repr(hashlib.sha256(raw).hexdigest()))
open(os.path.join(HERE, 'grade.html'), 'w').write(page)
print('grade.html', len(page), 'bytes; cards sha256', hashlib.sha256(raw).hexdigest())
