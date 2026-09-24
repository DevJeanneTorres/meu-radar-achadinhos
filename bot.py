import os
import requests
import random
import json

TOKEN = "8956945544:AAGQX1z5Vk4zRFDiCUPTpcgTU-KeVsyV19o"
CHAT_ID = "@jeanne_achadinhos_70"
HISTORICO_FILE = "ultimo.json"
PRODUTOS_FILE = "produtos.json"

def enviar_mensagem_telegram(mensagem):
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

def carregar_historico():
    if os.path.exists(HISTORICO_FILE):
        try:
            with open(HISTORICO_FILE, "r", encoding="utf-8") as f:
                return json.load(f).get("titulo")
        except:
            return None
    return None

def salvar_historico(titulo):
    with open(HISTORICO_FILE, "w", encoding="utf-8") as f:
        json.dump({"titulo": titulo}, f, ensure_ascii=False)

def carregar_produtos():
    if os.path.exists(PRODUTOS_FILE):
        try:
            with open(PRODUTOS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            print("Erro ao ler o ficheiro produtos.json")
            return []
    return []

def processar_achadinhos_automaticos():
    catalogo_produtos = carregar_produtos()
    
    if not catalogo_produtos:
        print("Nenhum produto encontrado no catálogo.")
        return

    ultimo_enviado = carregar_historico()
    
    # Filtra para nunca repetir o último produto enviado na rodada anterior
    produtos_disponiveis = [p for p in catalogo_produtos if p.get("titulo") != ultimo_enviado]
    
    if not produtos_disponiveis:
        produtos_disponiveis = catalogo_produtos
        
    produto = random.choice(produtos_disponiveis)
    
    # Salva no histórico para evitar repetição na próxima execução
    salvar_historico(produto["titulo"])
    
    # Mensagem 100% amarrada ao bloco do produto correto
    mensagem = (
        f"🔥 <b>ACHADINHO IMPERDÍVEL</b> 🔥\n\n"
        f"📦 <b>{produto['titulo']}</b>\n\n"
        f"❌ De: <s>R$ {produto['preco_antigo']:.2f}</s>\n"
        f"⚡ <b>Por: R$ {produto['preco_novo']:.2f}</b>\n"
        f"🎯 Cupom: <code>{produto['cupom']}</code>\n\n"
        f"🛒 <a href='{produto['link']}'>Garantir Oferta na Amazon</a>"
    )
    
    print(f"A enviar oferta do produto: {produto['titulo']}...")
    enviar_mensagem_telegram(mensagem)

if __name__ == "__main__":
    processar_achadinhos_automaticos()
