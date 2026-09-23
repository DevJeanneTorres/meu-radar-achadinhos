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
        print("Achadinho real enviado com sucesso para o Telegram!")
    else:
        print(f"Erro ao enviar para o Telegram: {resposta.text}")

def processar_achadinhos_automaticos():
    # Lista atualizada apenas com produtos reais e ASINs válidos na Amazon Brasil
    catalogo_real = [
        {
            "titulo": "Kindle 11ª Geração com Tela de 300 ppp e Iluminação Embutida",
            "loja": "Amazon",
            "preco_antigo": 499.00,
            "preco_novo": 422.00,
            "asin": "B09SWW78VL"
        },
        {
            "titulo": "Fire TV Stick Com Alexa e Controles por Voz",
            "loja": "Amazon",
            "preco_antigo": 379.00,
            "preco_novo": 289.00,
            "asin": "B091G3VZ95"
        }
    ]
    
    # Seleciona um produto real do catálogo
    produto = random.choice(catalogo_real)
    
    preco_antigo = produto["preco_antigo"]
    preco_novo = produto["preco_novo"]
    
    # Cálculo automático do desconto
    desconto = int(((preco_antigo - preco_novo) / preco_antigo) * 100)
    
    # Monta o link de afiliado oficial com a tua tag correta
    link_afiliado = f"https://www.amazon.com.br/dp/{produto['asin']}?tag={AMAZON_TAG}"
    
    mensagem = (
        f"🔥 *ACHADINHO AUTOMÁTICO (Amazon)* 🔥\n\n"
        f"📦 *Produto:* {produto['titulo']}\n"
        f"❌ De: R$ {preco_antigo:.2f}\n"
        f"✅ Por: R$ {preco_novo:.2f} *(Oferta Ativa!)*\n\n"
        f"🔗 [Garantir com Desconto de Afiliado]({link_afiliado})"
    )
    
    print(f"A enviar oferta real do produto: {produto['titulo']}...")
    enviar_mensagem_telegram(mensagem)

if __name__ == "__main__":
    processar_achadinhos_automaticos()
