import os
import requests

TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "-1004394023772"

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
        print("Achadinho automático enviado com sucesso!")
    else:
        print("Erro ao enviar para o Telegram:", resposta.text)

def buscar_ofertas_automaticas():
    print("A varrer fontes de ofertas em busca de descontos > 70%...")
    
    # Aqui o robô pode consultar feeds públicos de promoções ou APIs de monitoramento.
    # Para o teste dinâmico automático, simulamos uma varredura de um produto que acabou de entrar em promoção relâmpago:
    
    ofertas_encontradas = [
        {
            "titulo": "Smart TV 4K LED 50 Polegadas (Erro de Preço Relâmpago)",
            "loja": "Amazon",
            "preco_antigo": 2800.00,
            "preco_novo": 750.00, # Desconto de 73%
            "link": "https://www.amazon.com.br"
        }
    ]

    for p in ofertas_encontradas:
        preco_antigo = p["preco_antigo"]
        preco_novo = p["preco_novo"]
        
        # Calcula o desconto de forma automática
        desconto = int(((preco_antigo - preco_novo) / preco_antigo) * 100)
        
        # Só envia se atingir a sua regra de ouro (> 70% OFF)
        if desconto >= 70:
            mensagem = (
                f"🚨 *ACHADINHO CAPTURADO AUTOMATICAMENTE ({p['loja']})!* 🚨\n\n"
                f"📦 *Produto:* {p['titulo']}\n"
                f"❌ De: R$ {preco_antigo:.2f}\n"
                f"✅ Por: R$ {preco_novo:.2f} *({desconto}% OFF!)*\n\n"
                f"🔗 [Aproveitar a Oferta na {p['loja']}]({p['link']})"
            )
            
            print(f"Oportunidade encontrada! {desconto}% de desconto. A disparar...")
            enviar_mensagem_telegram(mensagem)
        else:
            print(f"Oferta ignorada: Apenas {desconto}% de desconto.")

if __name__ == "__main__":
    buscar_ofertas_automaticas()
