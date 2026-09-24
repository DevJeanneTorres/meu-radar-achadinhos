import os
import requests
import random

TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "@achadinhosdasjeh"

AMAZON_TAG = os.getenv("AMAZON_TAG", "jeanneachados-20")

def enviar_mensagem_telegram(mensagem, foto_url=None):
    """Envia a mensagem para o Telegram usando HTML para evitar erros de formatação."""
    if foto_url:
        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        payload = {
            "chat_id": CHAT_ID,
            "photo": foto_url,
            "caption": mensagem,
            "parse_mode": "HTML"
        }
    else:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": mensagem,
            "parse_mode": "HTML",
            "disable_web_page_preview": False
        }
    
    resposta = requests.post(url, json=payload)
    if resposta.status_code == 200:
        print("Achadinho enviado com sucesso para o Telegram!")
    else:
        print(f"Erro ao enviar para o Telegram: {resposta.text}")

def processar_achadinhos_automaticos():
    produtos_reais = [
        {
            "titulo": "Echo Dot 5ª Geração com Alexa",
            "asin": "B09B8V1LZ3",
            "preco_antigo": 429.00,
            "preco_novo": 359.00,
            "cupom": "ALEXA10",
            "imagem": "https://m.media-amazon.com/images/I/714RqwdBSLL._AC_SL1000_.jpg"
        },
        {
            "titulo": "Kindle 11ª Geração Tela 300 ppp",
            "asin": "B09SWW78VL",
            "preco_antigo": 499.00,
            "preco_novo": 422.00,
            "cupom": "KINDLEOFF",
            "imagem": "https://m.media-amazon.com/images/I/61AZvB20yGL._AC_SL1000_.jpg"
        },
        {
            "titulo": "Fire TV Stick com Controles por Voz",
            "asin": "B091G3VZ95",
            "preco_antigo": 379.00,
            "preco_novo": 289.00,
            "cupom": "FIRETV50",
            "imagem": "https://m.media-amazon.com/images/I/51Cg9I4nv-L._AC_SL1000_.jpg"
        },
        {
            "titulo": "Mouse Gamer Redragon Cobra M711 Chroma",
            "asin": "B079JAI63W",
            "preco_antigo": 149.90,
            "preco_novo": 99.99,
            "cupom": "COBRA10",
            "imagem": "https://m.media-amazon.com/images/I/618a3Be67YL._AC_SL1000_.jpg"
        }
    ]
    
    # Envia 1 produto por execução para testar com segurança
    produto = random.choice(produtos_reais)
    link_afiliado = f"https://www.amazon.com.br/dp/{produto['asin']}?tag={AMAZON_TAG}"
    
    # Mensagem estruturada em HTML (Tags <b>, <i>, <s>, <a>)
    mensagem = (
        f"🔥 <b>ACHADINHO IMPERDÍVEL</b> 🔥\n\n"
        f"📦 <b>{produto['titulo']}</b>\n\n"
        f"❌ De: <s>R$ {produto['preco_antigo']:.2f}</s>\n"
        f"⚡ <b>Por: R$ {produto['preco_novo']:.2f}</b> via Pix\n"
        f"🎯 Cupom: <code>{produto['cupom']}</code>\n\n"
        f"🛒 <a href='{link_afiliado}'>Garantir Oferta na Amazon</a>"
    )
    
    print(f"A enviar oferta do produto: {produto['titulo']}...")
    enviar_mensagem_telegram(mensagem, foto_url=produto['imagem'])

if __name__ == "__main__":
    processar_achadinhos_automaticos()
