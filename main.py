import openai_secret_manager

# Dapatkan kunci API
rahasia = openai_secret_manager.get_secret("openai")
api_key = rahasia["api_key"]

# Import library OpenAI
import openai

# Gunakan kunci API
openai.api_key = api_key

# Definisikan fungsi untuk menghasilkan tanggapan dari chatbot
def tanggapan_chatbot(saran):
    selesai = openai.Completion.create(
        engine="text-davinci-002",
        prompt=saran,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    pesan = selesai.pilihan[0].teks
    return pesan.strip()

while True:
    masukan_pengguna = input("Anda: ")
    if masukan_pengguna.lower() == "keluar":
        break
    else:
        tanggapan_bot = tanggapan_chatbot(masukan_pengguna)
        print("Chatbot: " + tanggapan_bot)
