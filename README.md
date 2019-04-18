# python-spellchecker
Flash Application in python to return list of correct word for a word

* Install pipenv
* `pip install -r requirement.txt`
* `python src/app.py`

## Sample queries
* `curl -X GET localhost:5000/spellCorrect  -d '{ "query":"hello:)world"}'| jq`
