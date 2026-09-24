import os
import requests
import random

TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "@jeanne_achadinhos_70"

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
    # Lista atualizada com os seus produtos reais e os links curtos oficiais
    produtos_reais = [
        {
            "titulo": "Samsung Galaxy Buds3 Pro, Fone de Ouvido sem Fio",
            "preco_antigo": 1899.00,
            "preco_novo": 1749.00,
            "cupom": "BUDS10",
            "link": "https://amzn.to/4rtKQEx"
        },
        {
            "titulo": "Condicionador Tio Nacho Antiqueda Antienvelhecimento",
            "preco_antigo": 49.90,
            "preco_novo": 36.90,
            "cupom": "TIONACHO",
            "link": "https://amzn.to/3Ti06b6"
        },
        {
            "titulo": "Simplo - Balde Dobrável de Plástico 10 Litros",
            "preco_antigo": 89.90,
            "preco_novo": 69.90,
            "cupom": "BALDE10",
            "link": "https://amzn.to/4ydmQrV"
        },
        {
            "titulo": "Filtro de Linha CLAMPER Energia 5 Tomadas",
            "preco_antigo": 79.90,
            "preco_novo": 64.95,
            "cupom": "CLAMPER5",
            "link": "https://amzn.to/4hqu3xE"
        },
        {
            "titulo": "Blocos de Montar Educativos - Conjunto de Engenharia",
            "preco_antigo": 199.90,
            "preco_novo": 175.75,
            "cupom": "BLOCOS15",
            "link": "https://amzn.to/4hmDldV"
        }
    ]
    
    # Escolhe um produto aleatório a cada execução do GitHub Actions
    produto = random.choice(produtos_reais)
    
    # Mensagem limpa, direta e com o link curto igualzinho ao seu exemplo
    mensagem = (
        f"🔥 <b>ACHADINHO IMPERDÍVEL</b> 🔥\n\n"
        f"📦 <b>{produto['titulo']}</b>\n\n"
        f"❌ De: <s>R$ {produto['preco_antigo']:.2f}</s>\n"
        f"⚡ <b>Por: R$ {produto['preco_novo']:.2f}</b>\n"
        f"🎯 Cupom: <code>{produto['cupom']}</code>\n\n"
        f"🛒 <a href='{produto['link']}'>{produto['link']}</a>"
    )
    
    print(f"A enviar oferta do produto: {produto['titulo']}...")
    enviar_mensagem_telegram(mensagem)

if __name__ == "__main__":
    processar_achadinhos_automaticos()
