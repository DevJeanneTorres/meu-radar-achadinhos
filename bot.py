import os
import requests
import random

TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "@achadinhosdasjeh"  # Substitua pelo username exato do seu canal público

AMAZON_TAG = os.getenv("AMAZON_TAG", "jeanneachados-20")

def enviar_mensagem_telegram(mensagem, foto_url=None):
    """Envia a mensagem para o Telegram. Se houver foto, usa sendPhoto, senão sendMessage."""
    if foto_url:
        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        payload = {
            "chat_id": CHAT_ID,
            "photo": foto_url,
            "caption": mensagem,
            "parse_mode": "Markdown"
        }
    else:
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
    # Base ampliada com produtos reais da Amazon e imagens ilustrativas de alta qualidade
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
        },
        {
            "titulo": "Headset Gamer HyperX Cloud Stinger 2",
            "asin": "B0B4H27VSX",
            "preco_antigo": 329.90,
            "preco_novo": 239.99,
            "cupom": "HYPERX20",
            "imagem": "https://m.media-amazon.com/images/I/61unprF89FL._AC_SL1000_.jpg"
        },
        {
            "titulo": "Lâmpada Inteligente Positivo Wi-Fi RGB",
            "asin": "B07W5JK75H",
            "preco_antigo": 89.90,
            "preco_novo": 59.90,
            "cupom": "POSITIVO15",
            "imagem": "https://m.media-amazon.com/images/I/51wXh2vM1UL._AC_SL1000_.jpg"
        }
    ]
    
    # Define aleatoriamente quantos produtos serão enviados nesta execução (ex: entre 1 e 2 produtos)
    quantidade_a_enviar = random.randint(1, 2)
    
    # Seleciona produtos únicos de forma aleatória para não repetir na mesma rodada
    produtos_escolhidos = random.sample(produtos_reais, min(quantidade_a_enviar, len(produtos_reais)))
    
    for produto in produtos_escolhidos:
        link_afiliado = f"https://www.amazon.com.br/dp/{produto['asin']}?tag={AMAZON_TAG}"
        
        # Formato profissional ajustado para conversão
        mensagem = (
            f"🔥 *ACHADINHO IMPERDÍVEL* 🔥\n\n"
            f"📦 *{produto['titulo']}*\n\n"
            f"❌ De: ~~R$ {produto['preco_antigo']:.2f}~~\n"
            f"⚡ *Por: R$ {produto['preco_novo']:.2f}* via Pix/Aplica\n"
            f"🎯 *Cupom:* `{produto['cupom']}`\n\n"
            f"🛒 [Garantir Oferta na Amazon]({link_afiliado})"
        )
        
        print(f"A enviar oferta do produto: {produto['titulo']}...")
        enviar_mensagem_telegram(mensagem, foto_url=produto['imagem'])

if __name__ == "__main__":
    processar_achadinhos_automaticos()
