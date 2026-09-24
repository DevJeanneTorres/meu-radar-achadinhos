import os
import requests
import random
import json

TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "@jeanne_achadinhos_70"
HISTORICO_FILE = "ultimo.json"

def enviar_mensagem_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    
    resposta = requests.post(url, json=payload)
    if resposta.status_code == 200:
        print("Achadinho enviado com sucesso para el Telegram!")
    else:
        print(f"Erro ao enviar para o Telegram: {resposta.text}")

def carregar_ultimo_produto():
    if os.path.exists(HISTORICO_FILE):
        try:
            with open(HISTORICO_FILE, "r") as f:
                return json.load(f).get("titulo")
        except:
            return None
    return None

def salvar_ultimo_produto(titulo):
    with open(HISTORICO_FILE, "w") as f:
        json.dump({"titulo": titulo}, f)

def processar_achadinhos_automaticos():
    # Cada produto é um bloco único e fechado: o link pertence EXCLUSIVAMENTE a ele
    catalogo_produtos = [
        {
            "titulo": "Samsung Galaxy Buds3 Pro, Fone de Ouvido sem Fio",
            "preco_antigo": 1899.00,
            "preco_novo": 1749.00,
            "cupom": "BUDS10",
            "link": "https://amzn.to/4rtKQEx"
        },
        {
            "titulo": "Condicionador Tio Nacho Antiqueda Antienvelhecimento",
            "preco_antigo": 49.90,
            "preco_novo": 36.90,
            "cupom": "TIONACHO",
            "link": "https://amzn.to/3Ti06b6"
        },
        {
            "titulo": "Simplo - Balde Dobrável de Plástico 10 Litros",
            "preco_antigo": 89.90,
            "preco_novo": 69.90,
            "cupom": "BALDE10",
            "link": "https://amzn.to/4ydmQrV"
        },
        {
            "titulo": "Filtro de Linha CLAMPER Energia 5 Tomadas",
            "preco_antigo": 79.90,
            "preco_novo": 64.95,
            "cupom": "CLAMPER5",
            "link": "https://amzn.to/4hqu3xE"
        },
        {
            "titulo": "Blocos de Montar Educativos - Conjunto de Engenharia",
            "preco_antigo": 199.90,
            "preco_novo": 175.75,
            "cupom": "BLOCOS15",
            "link": "https://amzn.to/4hmDldV"
        }
    ]
    
    ultimo_enviado = carregar_ultimo_produto()
    
    # Filtra para nunca repetir o mesmo produto da última execução
    produtos_disponiveis = [p for p in catalogo_produtos if p["titulo"] != ultimo_enviado]
    
    if not produtos_disponiveis:
        produtos_disponiveis = catalogo_produtos
        
    produto = random.choice(produtos_disponiveis)
    
    # Salva para o histórico antirrepetição
    salvar_ultimo_produto(produto["titulo"])
    
    # Mensagem estruturada garantindo que o link e o texto combinem 100%
    mensagem = (
        f"🔥 <b>ACHADINHO IMPERDÍVEL</b> 🔥\n\n"
        f"📦 <b>{produto['titulo']}</b>\n\n"
        f"❌ De: <s>R$ {produto['preco_antigo']:.2f}</s>\n"
        f"⚡ <b>Por: R$ {produto['preco_novo']:.2f}</b>\n"
        f"🎯 Cupom: <code>{produto['cupom']}</code>\n\n"
        f"🛒 <a href='{produto['link']}'>Garantir Oferta na Amazon</a>"
    )
    
    print(f"A enviar oferta do produto: {produto['titulo']}...")
    enviar_mensagem_telegram(mensagem)

if __name__ == "__main__":
    processar_achadinhos_automaticos()
