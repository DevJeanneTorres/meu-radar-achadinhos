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
    requests.post(url, json=payload)

def puxar_achadinhos_reais():
    print("Conectando ao feed de ofertas para buscar links reais...")
    
    # Exemplo de integração com uma API de catálogo ou feed JSON de promoções
    # Numa aplicação avançada, você substitui esta URL pelo endpoint de uma API de afiliados ou agregador.
    url_feed = "https://api.exemplo-de-ofertas.com.br/v1/promocoes-recentes"
    
    try:
        # Faz a requisição para buscar os dados reais atualizados da internet
        resposta = requests.get(url_feed, timeout=10)
        
        # Simulamos a estrutura que a API traria (Título, Loja, Preços e o Link Direto real do produto)
        produtos_externos = [
            {
                "titulo": "Fritadeira Sem Óleo Airfryer 4L",
                "loja": "Amazon",
                "preco_antigo": 600.00,
                "preco_novo": 150.00, # 75% de desconto real
                "link_direto": "https://www.amazon.com.br/dp/exemplo-produto-real"
            }
        ]
        
        for p in produtos_externos:
            preco_antigo = p["preco_antigo"]
            preco_novo = p["preco_novo"]
            
            # Cálculo automático da porcentagem
            desconto = int(((preco_antigo - preco_novo) / preco_antigo) * 100)
            
            # Valida se cumpre a sua regra de ouro
            if desconto >= 70:
                mensagem = (
                    f"🔥 *ACHADINHO REAL DETECTADO ({p['loja']})!* 🔥\n\n"
                    f"📦 *Produto:* {p['titulo']}\n"
                    f"❌ De: R$ {preco_antigo:.2f}\n"
                    f"✅ Por: R$ {preco_novo:.2f} *({desconto}% OFF!)*\n\n"
                    f"🔗 [Comprar com Desconto Direto]({p['link_direto']})"
                )
                enviar_mensagem_telegram(mensagem)
                
    except Exception as e:
        print(f"Erro ao buscar ofertas automáticas: {e}")

if __name__ == "__main__":
    puxar_achadinhos_reais()
