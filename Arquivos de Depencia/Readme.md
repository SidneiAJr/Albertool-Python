# 📦 Arquivos de Dependência
*"Um requirements certo vale mais que horas de debug."*

> Requirements prontos por especialidade.  
> Instala, roda, e parte pra lógica.

---

## 📋 O que tem aqui

| Arquivo | Especialidade | Principais libs |
|---------|--------------|-----------------|
| `requirements-basico.txt` | Projetos simples | requests, dotenv, pydantic, mysql |
| `requirements-pygame.txt` | Jogos 2D | pygame, numpy, pymunk, Pillow |
| `requirements-flask.txt` | API com Flask | flask, JWT, SQLAlchemy, bcrypt |
| `requirements-fastapi.txt` | API com FastAPI | fastapi, uvicorn, JWT, pydantic |
| `requirements-django.txt` | Web completo | django, DRF, celery, redis |
| `requirements-data.txt` | Data Science | pandas, matplotlib, scikit-learn, jupyter |
| `requirements-exe.txt` | Gerar executável | pyinstaller |

---

## 🚀 Como usar

```bash
# Instalar as dependências
pip install -r requirements-<especialidade>.txt

# Exemplos
pip install -r requirements-basico.txt
pip install -r requirements-flask.txt
pip install -r requirements-data.txt
```

---

## 🗃️ Estrutura

```
Arquivos de Depencia/
├── requirements-basico.txt
├── requirements-pygame.txt
├── requirements-flask.txt
├── requirements-fastapi.txt
├── requirements-django.txt
├── requirements-data.txt
└── requirements-exe.txt
```

---

## 💡 Dica

Recomendado usar um ambiente virtual antes de instalar:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements-<especialidade>.txt
```

---

**Criado no Brasil 🇧🇷 — Open source. Gratuito. Para sempre.**
