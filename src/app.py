from flask import Flask, request
from spell_suggestor import SpellingSuggestor

app = Flask(__name__)


@app.route('/spellCorrect')
def spell_correct():
    content = request.json
    return SpellingSuggestor(content['query']).spell_checker_result()


if __name__ == '__main__':
    app.run()
