import os
import json

#result = {"my_project/settings/": ["__init__.py", "dev.py", "prod.py"], "my_project/mainapp/": ["__init__.py", "models.py", "views.py"],"my_project/mainapp/templates/mainapp/": ["base.html", "index.html"], "my_project/authapp/": ["__init__.py", "models.py", "views.py"],"my_project/authapp/templates/authapp/": ["base.html", "index.html"]}

#with open('config.json', 'w', encoding='utf-8') as f:
 #   json.dump(result, f, ensure_ascii=False)
with open('config.json', 'r', encoding='utf-8') as f:
    res = json.load(f)

ROOT = os.path.dirname(__file__)

for path in res:
    test_path = os.path.join(ROOT, path)
    os.makedirs(test_path)
    for file_name in res[path]:
        with open(os.path.join(test_path, file_name), 'x', encoding='utf-8'):
            pass
