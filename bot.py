import os
import requests

# Suas credenciais fixas do Telegram
TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "-1004394023772"

# Puxa a sua tag de associada com segurança direto do cofre do GitHub
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
        print("Achadinho automático enviado com sucesso para o Telegram!")
    else:
        print(f"Erro ao enviar para o Telegram: {resposta.text}")

def processar_achadinhos_automaticos():
    # Exemplo de produto capturado pelo sistema de monitoramento
    produto = {
        "titulo": "Smart TV 4K LED 50 Polegadas (Oferta Relâmpago)",
        "loja": "Amazon",
        "preco_antigo": 2800.00,
        "preco_novo": 750.00,
        "asin": "B09B8V1LZ3" # Código único do produto na Amazon
    }
    
    preco_antigo = produto["preco_antigo"]
    preco_novo = produto["preco_novo"]
    
    # Cálculo automático do desconto
    desconto = int(((preco_antigo - preco_novo) / preco_antigo) * 100)
    
    if desconto >= 70:
        # Monta o link de afiliado oficial automaticamente usando a sua Tag guardada
        link_afiliado = f"https://www.amazon.com.br/dp/{produto['asin']}?tag={AMAZON_TAG}"
        
        mensagem = (
            f"🔥 *ACHADINHO AUTOMÁTICO COM DESCONTO REAL ({produto['loja']})!* 🔥\n\n"
            f"📦 *Produto:* {produto['titulo']}\n"
            f"❌ De: R$ {preco_antigo:.2f}\n"
            f"✅ Por: R$ {preco_novo:.2f} *({desconto}% OFF!)*\n\n"
            f"🔗 [Garantir com Desconto de Afiliado]({link_afiliado})"
        )
        
        print(f"Desconto de {desconto}% detetado! A enviar link de afiliado...")
        enviar_mensagem_telegram(mensagem)
    else:
        print(f"Oferta ignorada: Apenas {desconto}% de desconto.")

if __name__ == "__main__":
    processar_achadinhos_automaticos()
