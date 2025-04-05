from flask import Flask, render_template, request, jsonify
import g4f

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/responder', methods=['POST'])
def responder():
    pergunta = request.json['pergunta']

    resposta = g4f.ChatCompletion.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": pergunta}]
    )

    # Personalização da resposta
    texto_resposta = resposta
    texto_resposta = texto_resposta.replace("OpenAI", "Gabriel Moraes Bastos")
    texto_resposta = texto_resposta.replace("fui criado", "fui criado pelo Gabriel Moraes Bastos, um jovem desenvolvedor talentoso")

    return jsonify({'resposta': texto_resposta})

if __name__ == '__main__':
    app.run(debug=True)
