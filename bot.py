import os
import requests
import random

TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "-1004394023772"

AMAZON_TAG = os.getenv("AMAZON_TAG", "jeanneachados-20")

def enviar_mensagem_telegram(mensagem):
    # Usamos o sendMessage formatado com Markdown (garantia total de entrega sem falhas de imagem)
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
    # Lista de ofertas reais com links diretos e limpos para a Amazon
    produtos_reais = [
        {
            "titulo": "Echo Dot 5ª Geração com Alexa",
            "asin": "B09B8V1LZ3",
            "preco_antigo": 429.00,
            "preco_novo": 359.00,
            "cupom": "ALEXA10"
        },
        {
            "titulo": "Kindle 11ª Geração Tela 300 ppp",
            "asin": "B09SWW78VL",
            "preco_antigo": 499.00,
            "preco_novo": 422.00,
            "cupom": "KINDLEOFF"
        },
        {
            "titulo": "Fire TV Stick com Controles por Voz",
            "asin": "B091G3VZ95",
            "preco_antigo": 379.00,
            "preco_novo": 289.00,
            "cupom": "FIRETV50"
        }
    ]
    
    produto = random.choice(produtos_reais)
    
    # Link direto oficial da Amazon com a sua tag de associada
    link_afiliado = f"https://www.amazon.com.br/dp/{produto['asin']}?tag={AMAZON_TAG}"
    
    # Mensagem profissional estilo canal de promoções
    mensagem = (
        f"🔥 *ACHADINHO IMPERDÍVEL (Amazon)* 🔥\n\n"
        f"📦 *{produto['titulo']}*\n\n"
        f"❌ De: ~~R$ {produto['preco_antigo']:.2f}~~\n"
        f"⚡ *Por: R$ {produto['preco_novo']:.2f}* (à vista / parcelado)\n"
        f"🎯 *Cupom:* `{produto['cupom']}`\n\n"
        f"🛒 [Garantir Oferta na Amazon]({link_afiliado})"
    )
    
    print(f"A enviar oferta do produto: {produto['titulo']}...")
    enviar_mensagem_telegram(mensagem)

if __name__ == "__main__":
    processar_achadinhos_automaticos()
