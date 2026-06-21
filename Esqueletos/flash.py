from flask import Flask, request, jsonify

app = Flask(__name__)

def listar():
    pass

def buscar_id():
    pass

def cadastrar():
    pass

def atualizar():
    pass

def deletar():
    pass

# ===== ROTAS =====
app.add_url_rule("/", view_func=listar, methods=["GET"])
app.add_url_rule("/<int:id>", view_func=buscar_id, methods=["GET"])
app.add_url_rule("/", view_func=cadastrar, methods=["POST"])
app.add_url_rule("/<int:id>", view_func=atualizar, methods=["PUT"])
app.add_url_rule("/<int:id>", view_func=deletar, methods=["DELETE"])

if __name__ == "__main__":
    app.run(debug=True)
