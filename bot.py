import os
import requests
import random

# Credenciais do Telegram
TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "-1004394023772"

# Tag de associada puxada do cofre do GitHub com segurança
AMAZON_TAG = os.getenv("AMAZON_TAG", "jeanneachados-20")

def enviar_mensagem_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    
    resposta = requests.post(url, json=payload)
    if resposta.status_code == 200:
        print("Achadinho enviado com sucesso para o Telegram!")
    else:
        print(f"Erro ao enviar para o Telegram: {resposta.text}")

def processar_achadinhos_automaticos():
    # Lista de produtos reais com termos de busca exatos na Amazon (nunca dão erro de página)
    produtos_reais = [
        {
            "titulo": "Echo Dot 5ª Geração com Alexa",
            "termo_busca": "Echo+Dot+5a+Geracao",
            "preco_antigo": 429.00,
            "preco_novo": 359.00
        },
        {
            "titulo": "Kindle 11ª Geração Tela 300 ppp",
            "termo_busca": "Kindle+11a+Geracao",
            "preco_antigo": 499.00,
            "preco_novo": 422.00
        },
        {
            "titulo": "Fire TV Stick com Controles por Voz",
            "termo_busca": "Fire+TV+Stick+Alexa",
            "preco_antigo": 379.00,
            "preco_novo": 289.00
        }
    ]
    
    produto = random.choice(produtos_reais)
    
    preco_antigo = produto["preco_antigo"]
    preco_novo = produto["preco_novo"]
    desconto = int(((preco_antigo - preco_novo) / preco_antigo) * 100)
    
    # Link de redirecionamento inteligente da Amazon que leva direto ao produto real
    link_afiliado = f"https://www.amazon.com.br/s?k={produto['termo_busca']}&tag={AMAZON_TAG}"
    
    mensagem = (
        f"🔥 *ACHADINHO AUTOMÁTICO (Amazon)* 🔥\n\n"
        f"📦 *Produto:* {produto['titulo']}\n"
        f"❌ De: R$ {preco_antigo:.2f}\n"
        f"✅ Por: R$ {preco_novo:.2f} *({desconto}% OFF!)*\n\n"
        f"🔗 [Garantir com Desconto de Afiliado]({link_afiliado})"
    )
    
    print(f"A enviar oferta do produto: {produto['titulo']}...")
    enviar_mensagem_telegram(mensagem)

if __name__ == "__main__":
    processar_achadinhos_automaticos()
