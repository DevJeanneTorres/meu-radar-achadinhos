import os
import requests
import random

# Versão do Bot: 4.0 (Mensagens visuais com Foto + Legenda)
TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "-1004394023772"

AMAZON_TAG = os.getenv("AMAZON_TAG", "jeanneachados-20")

def enviar_foto_telegram(foto_url, legenda):
    # Usamos o endpoint sendPhoto para enviar a imagem com a legenda formatada em baixo
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHAT_ID,
        "photo": foto_url,
        "caption": legenda,
        "parse_mode": "Markdown"
    }
    
    resposta = requests.post(url, json=payload)
    if resposta.status_code == 200:
        print("Achadinho visual enviado com sucesso para o Telegram!")
    else:
        print(f"Erro ao enviar foto para o Telegram: {resposta.text}")

def processar_achadinhos_automaticos():
    # Catálogo de produtos reais com imagens oficiais diretas e links limpos da Amazon
    produtos_reais = [
        {
            "titulo": "Echo Dot 5ª Geração com Alexa",
            "asin": "B09B8V1LZ3",
            "preco_novo": 359.00,
            "foto": "https://images-na.ssl-images-amazon.com/images/I/714RqScv7sL._AC_SL1000_.jpg",
            "cupom": "ALEXA10"
        },
        {
            "titulo": "Kindle 11ª Geração Tela 300 ppp",
            "asin": "B09SWW78VL",
            "preco_novo": 422.00,
            "foto": "https://images-na.ssl-images-amazon.com/images/I/61HQt3K07LL._AC_SL1000_.jpg",
            "cupom": "KINDLEOFF"
        },
        {
            "titulo": "Fire TV Stick com Controles por Voz",
            "asin": "B091G3VZ95",
            "preco_novo": 289.00,
            "foto": "https://images-na.ssl-images-amazon.com/images/I/51C0804-aSL._AC_SL1000_.jpg",
            "cupom": "FIRETV50"
        }
    ]
    
    produto = random.choice(produtos_reais)
    
    # Link oficial direto da Amazon com a tua tag de associada
    link_afiliado = f"https://www.amazon.com.br/dp/{produto['asin']}?tag={AMAZON_TAG}"
    
    # Mensagem estruturada exatamente no estilo de canal profissional
    legenda = (
        f"❄️ *Achado Imperdível (Amazon)*\n\n"
        f"📦 *{produto['titulo']}*\n\n"
        f"🔥 *Por: R$ {produto['preco_novo']:.2f}* (à vista / parcelado)\n"
        f"🎯 *Usem o cupom:* `{produto['cupom']}`\n\n"
        f"🛒 [Garantir Oferta na Amazon]({link_afiliado})"
    )
    
    print(f"A enviar oferta visual do produto: {produto['titulo']}...")
    enviar_foto_telegram(produto['foto'], legenda)

if __name__ == "__main__":
    processar_achadinhos_automaticos()
