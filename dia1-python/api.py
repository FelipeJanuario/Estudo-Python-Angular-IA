from fastapi import FastAPI

app = FastAPI()

@app.get("/ola/{nome}")
def saudar(nome: str):
    return {"mensagem": f"Olá, {nome}! Bem-vindo à API!"}

# Para rodar a API, use o comando: 
# uvicorn api:app --reload
# Depois, acesse http://localhost:8000/ola/SeuNome para ver a mensagem de saudação.
