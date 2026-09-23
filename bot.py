import requests

TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "-1004394023772"

def enviar_achadinho():
    mensagem = (
        "🔥 *RADAR DE ACHADINHOS (RODANDO NA NUVEM)* 🔥\n\n"
        "📦 *Status:* O robô rodou com sucesso de 5 em 5 minutos!\n"
        "❌ De: R$ 500,00\n"
        "✅ Por: R$ 99,90 *(Mais de 80% de desconto!)*\n\n"
        "🔗 [Acessar a Oferta](https://www.amazon.com.br)"
    )
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem,
        "parse_mode": "Markdown"
    }
    
    resposta = requests.post(url, json=payload)
    if resposta.status_code == 200:
        print("Mensagem automática enviada com sucesso!")
    else:
        print("Erro ao enviar:", resposta.text)

if __name__ == "__main__":
    enviar_achadinho()
