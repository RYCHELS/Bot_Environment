import discord
import random
from discord.ext import commands

# Membaca token dari file token.txt
with open("Tooken.txt", "r") as f:
    token = f.read().strip()
with open("Id.txt", "r") as f:
    channel_id = f.read().strip()

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

reduce_tips = [
    "Bawa tas belanja sendiri untuk mengurangi penggunaan kantong plastik.",
    "Belilah produk dengan kemasan yang dapat didaur ulang atau tanpa kemasan.",
    "Gunakan botol minum yang dapat diisi ulang daripada botol sekali pakai."
]

reuse_tips = [
    "Gunakan kembali wadah kaca untuk menyimpan makanan atau barang-barang kecil.",
    "Gunakan kain lap atau handuk daripada tisu sekali pakai.",
    "Donasikan pakaian yang tidak terpakai daripada membuangnya."
]

recycle_tips = [
    "Pastikan memisahkan sampah daur ulang dari sampah organik.",
    "Cari tahu lokasi pusat daur ulang terdekat di daerah Anda.",
    "Daur ulang kertas, plastik, kaca, dan logam yang sudah tidak terpakai."
]

eco_friendly_products = [
    "Gunakan sikat gigi bambu sebagai pengganti sikat gigi plastik.",
    "Gunakan sedotan stainless steel atau bambu daripada sedotan plastik.",
    "Coba menstrual cup atau pembalut kain daripada pembalut sekali pakai."
]

def get_tip():
    tips = reduce_tips + reuse_tips + recycle_tips
    return random.choice(tips)

def get_product_recommendation():
    return random.choice(eco_friendly_products)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    send_tips.start()

@tasks.loop(hours=24)
async def send_tips():
    channel = bot.get_channel(channel_id)  # Gunakan ID saluran yang telah dibaca sebagai integer
    tip = get_tip()
    await channel.send(f"🌍 Tips Harian: {tip}")


bot.run(token)
