import telebot
import re
from conf.settings import TELEGRAM_TOKEN
from random import randint

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['info', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Olá, bem-vindo ao bot!")

@bot.message_handler(content_types = ['new_chat_members'])
def wellcome_message(session):
    bot.send_message(CHAT_ID, "Bem vindo *{}*! \nEu sou o Mestre aqui! Mais informações digite /info 😉"
    .format(session.new_chat_member.first_name), parse_mode='MARKDOWN')
    sleep(10)

@bot.message_handler(func=lambda m: True)
def reply(session):
    search = session.text
    if re.findall("roll",session.text.lower()):
        search = search.split(" ")
        print(search)
        result = randint(1,int(search[1]))
        print(result)
        if result == 1:
            bot.send_message(session.chat.id, "Result: *{}* \n😱 SE FODEU! 😖".format(result), parse_mode='MARKDOWN')
            return
        if result == int(search[1]):
            bot.send_message(session.chat.id, "Result: *{}* \n😯 Carai biri jim 😮".format(result), parse_mode='MARKDOWN')
            return
        else:
            bot.send_message(session.chat.id, "Result: *{}*".format(result), parse_mode='MARKDOWN')

    elif re.findall("sort",session.text.lower()):
        items = search.split(", ")
        print(search)
        for item in items:
            sort = item
        print(sort)
        bot.send_message(session.chat.id,"*{}* Você foi o escolhido!".format(sort), parse_mode='MARKDOWN')

    elif re.findall("bot do diabo",session.text.lower()):
        bot.send_message(session.chat.id, "😡 Olha olha *{}* te parto a boca rapaz 😤"
        "\n Por garantia vou guardar seu IP aqui"
        "\n mas da próxima não passa!".format(session.from_user.first_name), parse_mode='MARKDOWN')

    elif re.findall("lilo gay",session.text.lower()):
        bot.send_message(session.chat.id, "Lilo GAY")

    elif re.findall("cascavel",session.text.lower()):
        bot.send_message(session.chat.id, "De boas, pra cascavel é só decida")

    elif re.findall("crocs",session.text.lower()): #bad
        bot.send_message(session.chat.id, "encurtador.com.br/juxY7")

    elif re.findall("chandra",session.text.lower()): #bad
        bot.send_message(session.chat.id, "encurtador.com.br/aMNY8")

    elif re.findall("goyf",session.text.lower()):
        bot.send_message(session.chat.id, "Hmm então você é desses?")

    elif re.findall("bally",session.text.lower()):
        bot.send_message(session.chat.id, "Ta forte isso")

    elif re.findall("scavenging",session.text.lower()):
        bot.send_message(session.chat.id, "o bixo cresce")

    elif re.findall("rico",session.text.lower()):
        bot.send_message(session.chat.id, "*Maycão*??", parse_mode='MARKDOWN')

    elif re.findall("limaozinho",session.text.lower()):
        bot.send_photo(session.chat.id, "images/limaozinho.jpg")

    elif re.findall("Matheus",session.text.lower()):
        bot.send_message(session.chat.id, "A mãe do Matheus está doente")

    elif re.findall("Maycao",session.text.lower()):
        bot.send_message(session.chat.id, "Maycao nunca pode")

    elif re.findall("vacilao",session.text.lower()):
        bot.send_message(session.chat.id, "meu pe na tua mao")

    elif re.findall("Bastiao",session.text.lower()):
        bot.send_message(session.chat.id, "só bally")

    elif re.findall("lilo",session.text.lower()):
        bot.send_message(session.chat.id, "Lilo GAY")

    elif re.findall("linguiça fedida",session.text.lower()):
        bot.send_message(session.chat.id, "Postinho e Pia bugado aprovam a linguiça fedida kkkkk")

    elif re.findall("jackson",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/grEKT")

    elif re.findall("proteção contra qual cor?",session.text.lower()):
        bot.send_message(session.chat.id, "Branco!")

    elif re.findall("infect",session.text.lower()):
        bot.send_message(session.chat.id, "Sem dignidade -2 de sanidade")

    elif re.findall("almofada",session.text.lower()):
        bot.send_message(session.chat.id, "Foi estuprada pelo Jackson")

    elif re.findall("linguiça fedida",session.text.lower()):
        bot.send_message(session.chat.id, "Postinho e Pia bugado aprovam a linguiça fedida kkkkk")

    elif re.findall("leonardao",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/bEOVY")

    elif re.findall("lilo2",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/hACFL")

    elif re.findall("pia bugado",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/epIJ9")

    elif re.findall("lilo3",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/jrIKL")

    elif re.findall("buraco negro",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/epsK2")

    elif re.findall("maycao2",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/EIU23")

    elif re.findall("raquel",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/csR56")

    elif re.findall("lilo4",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/egiT7")

    elif re.findall("jackson2",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/gFKRY")

    elif re.findall("peterson2",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/imAMT")

    elif re.findall("peterson",session.text.lower()):
        bot.send_message(session.chat.id, "O que? Você quer que eu te mande algum meme do meu criador? Deve estar louco mesmo kkkk")

    elif re.findall("peterson3",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/gjuzT")

    elif re.findall("pedro de lara",session.text.lower()):
        bot.send_message(session.chat.id, "encurtador.com.br/ktwD9")

    elif re.findall("entao voce é desses?",session.text.lower()):
        bot.send_photo(session.chat.id, "https://scontent.fgpb3-1.fna.fbcdn.net/v/t1.0-9/1507909_664772920239918_1244974174_n.jpg?_nc_cat=109&_nc_sid=ca434c&_nc_eui2=AeH6AS2D_pE0m_2lhEDt90y_fbjOSoycHXt9uM5KjJwde5b-kvseOfoFhPxiyAym9wXz_GywynW0YVkmf2O3AvUN&_nc_ohc=5UWqjDiuYTIAX-fUq20&_nc_ht=scontent.fgpb3-1.fna&oh=e3bfdb09c5aaba6bcc2934eb6ec407b5&oe=5EB156BE")

bot.polling()
