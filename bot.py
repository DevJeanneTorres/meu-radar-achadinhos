import os
import requests
import random

TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
# Mude provisoriamente para o ID numérico com -100 se tiver o ID, 
# ou mantenha o @ se tiver certeza absoluta que o canal aceita via username.
CHAT_ID = "@jeanne_achadinhos_70"

AMAZON_TAG = os.getenv("AMAZON_TAG", "jeanneachados-20")

def testar_envio():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    mensagem = (
        "🔥 <b>TESTE DE CONEXÃO DO ROBÔ</b> 🔥\n\n"
        "📦 Se esta mensagem apareceu aqui, a API do Telegram e o bot estão 100% conectados!"
    )
    
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem,
        "parse_mode": "HTML"
    }
    
    print(f"A tentar enviar para o chat: {CHAT_ID}...")
    resposta = requests.post(url, json=payload)
    
    # Imprime a resposta crua da API do Telegram nos logs do GitHub Actions
    print(f"Status Code da API: {resposta.status_code}")
    print(f"Resposta da API do Telegram: {resposta.text}")
    
    if resposta.status_code == 200:
        print("SUCESSO ABSOLUTO! Mensagem entregue no Telegram.")
    else:
        print("FALHA NA ENTREGA. Veja o erro detalhado acima.")

if __name__ == "__main__":
    testar_envio()
