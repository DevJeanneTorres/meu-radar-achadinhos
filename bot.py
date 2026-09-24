import os
import requests
import random

TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "@jeanne_achadinhos_70"

AMAZON_TAG = os.getenv("AMAZON_TAG", "jeanneachados-20")

def enviar_mensagem_telegram(mensagem):
    """Envia o achadinho via mensagem de texto estruturada em HTML."""
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
    # Lista de produtos reais com preços corretos e links limpos da Amazon
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
        },
        {
            "titulo": "Mouse Gamer Redragon Cobra M711 Chroma",
            "asin": "B079JAI63W",
            "preco_antigo": 149.90,
            "preco_novo": 99.99,
            "cupom": "COBRA10"
        }
    ]
    
    # Escolhe um produto de forma aleatória a cada execução
    produto = random.choice(produtos_reais)
    
    # Gera o link oficial de afiliado com a sua tag correta
    link_afiliado = f"https://www.amazon.com.br/dp/{produto['asin']}?tag={AMAZON_TAG}"
    
    # Mensagem otimizada: direta ao ponto, preço certo e link limpo
    mensagem = (
        f"🔥 <b>ACHADINHO IMPERDÍVEL</b> 🔥\n\n"
        f"📦 <b>{produto['titulo']}</b>\n\n"
        f"❌ De: <s>R$ {produto['preco_antigo']:.2f}</s>\n"
        f"⚡ <b>Por: R$ {produto['preco_novo']:.2f}</b>\n"
        f"🎯 Cupom: <code>{produto['cupom']}</code>\n\n"
        f"🛒 <a href='{link_afiliado}'>Garantir Oferta na Amazon</a>"
    )
    
    print(f"A enviar oferta do produto: {produto['titulo']}...")
    enviar_mensagem_telegram(mensagem)

if __name__ == "__main__":
    processar_achadinhos_automaticos()
