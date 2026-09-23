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
        print("Oferta enviada com sucesso para o canal!")
    else:
        print("Erro ao enviar para o Telegram:", resposta.text)

def processar_achadinhos():
    produtos = [
        {
            "titulo": "Smartphone de Última Geração (Queima de Estoque)",
            "loja": "Amazon",
            "preco_antigo": 2500.00,
            "preco_novo": 699.00, 
            "link": "https://www.amazon.com.br/b?node=19875390011" # Página oficial de Ofertas da Amazon
        },
        {
            "titulo": "Kit Ferramentas Profissional Completo",
            "loja": "Shopee",
            "preco_antigo": 350.00,
            "preco_novo": 89.90,
            "link": "https://shopee.com.br/daily_discover" # Página de Achados Relâmpago da Shopee
        },
        {
            "titulo": "Fone Bluetooth Esportivo à Prova D'água",
            "loja": "Mercado Livre",
            "preco_antigo": 180.00,
            "preco_novo": 120.00, 
            "link": "https://www.mercadolivre.com.br/ofertas" # Página de Ofertas do Mercado Livre
        }
    ]

    print("Inspecionando ofertas das lojas...")

    for p in produtos:
        preco_antigo = p["preco_antigo"]
        preco_novo = p["preco_novo"]
        
        desconto = int(((preco_antigo - preco_novo) / preco_antigo) * 100)
        
        if desconto >= 70:
            mensagem = (
                f"🔥 *ACHADINHO IMPERDÍVEL ({p['loja']})!* 🔥\n\n"
                f"📦 *Produto:* {p['titulo']}\n"
                f"❌ De: R$ {preco_antigo:.2f}\n"
                f"✅ Por: R$ {preco_novo:.2f} *({desconto}% OFF!)*\n\n"
                f"🔗 [Clique aqui para garantir na {p['loja']}]({p['link']})"
            )
            
            print(f"Produto aprovado! Desconto de {desconto}% encontrado. Disparando...")
            enviar_mensagem_telegram(mensagem)
        else:
            print(f"Produto ignorado ({p['titulo']}): Desconto de {desconto}% (abaixo de 70%).")

if __name__ == "__main__":
    processar_achadinhos()
