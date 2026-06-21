from fastapi import FastAPI

app = FastAPI()

async def listar():
    pass

async def buscar_id(id: int):
    pass

async def cadastrar():
    pass

async def atualizar(id: int):
    pass

async def deletar(id: int):
    pass

# ===== ROTAS =====
app.add_api_route("/", listar, methods=["GET"])
app.add_api_route("/{id}", buscar_id, methods=["GET"])
app.add_api_route("/", cadastrar, methods=["POST"])
app.add_api_route("/{id}", atualizar, methods=["PUT"])
app.add_api_route("/{id}", deletar, methods=["DELETE"])
