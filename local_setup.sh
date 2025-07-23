cd python-play-ground
python3.10 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install pipenv
pipenv install

pipenv run pip-audit -r <(pipenv requirements) --aliases

python3.10 -m pip wheel urllib3==1.25.3 --index-url https://pypi.org/simple


