import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop


lamp_status = 'Off'  # Inisialisasi status awal lampu

# Fungsi untuk menangani pesan yang berisi perintah /start
def handle_start(msg):
    chat_id = msg['chat']['id']
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text=f'Lampu : {lamp_status}', callback_data='toggle_lamp')],
                   [InlineKeyboardButton(text='Cek Jarak', callback_data='cek_jarak')]
               ])
    bot.sendMessage(chat_id, 'Halo selamat datang di Bot, silahkan pilih opsi dibawah:', reply_markup=keyboard)

# Fungsi untuk menangani pesan callback dari inline button
def on_callback_query(msg):
    global lamp_status  # Gunakan variabel lamp_status yang ada di luar fungsi
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    
    #Jika yang dipilih adalah lampu
    if query_data == 'toggle_lamp':
        # Toggle status lampu
        if lamp_status == 'On':
            bot.answerCallbackQuery(query_id, text='Mematikan lampu...')
            lamp_status = 'Off'
        else:
            bot.answerCallbackQuery(query_id, text='Menghidupkan lampu...')
            lamp_status = 'On'
        
        # Perbarui teks tombol inline
        new_button_text = f'Lampu : {lamp_status}'
        
        # Perbarui keyboard inline
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                       [InlineKeyboardButton(text=new_button_text, callback_data='toggle_lamp')],
                       [InlineKeyboardButton(text='Cek Jarak', callback_data='cek_jarak')]
                   ])
        
        # Edit pesan yang dikirim sebelumnya dengan keyboard inline yang diperbarui
        bot.editMessageReplyMarkup((from_id, msg['message']['message_id']), reply_markup=keyboard)
    
    # Jika yang dipilih adalah cek_jarak
    elif query_data == 'cek_jarak':
        # Respon dengan pesan "Mengecek jarak..."
        bot.answerCallbackQuery(query_id, text='Mengecek jarak...')
        bot.sendMessage(from_id, 'Jarak terdeteksi : .... cm')


# Token bot Anda dari BotFather
TOKEN = '6803335035:AAEsIx4P874EfbjP0OP0w9XpUVPB_0tOuoo'

# Inisialisasi bot
bot = telepot.Bot(TOKEN)

# Mendaftarkan handler untuk perintah /start
MessageLoop(bot, {'chat': handle_start,
                  'callback_query': on_callback_query}).run_as_thread()

print('Bot sedang berjalan...')

# Jangan biarkan program berhenti
while True:
    pass

# Jangan biarkan program berhenti
while True:
    pass
