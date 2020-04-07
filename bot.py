import telebot
import re
from conf.settings import TELEGRAM_TOKEN
from random import randint

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['info', 'help'])
def send_welcome(message):
    bot.reply_to(message, "⚔ Funcionalidades ⚔\n"
    "\n*🎲 Jogar dados:* Para jogar dados você deve utilizar o comando roll seguido do número do dado"
    "e o bot retornará um número inteiro positivo de 1 até o valor que informar, ou seja: Se você utilizar"
    "o comando roll 20 ele estará jogando um d20. Se você utilizar roll 200 ele estará utilizando um d200\n"
    "Exemplo: ``` roll 20``` \n"
    "\n*👉 Selecionar um elemento aleatóriamente:* Sim, tem essa funcionalidade também ela basicamente recebe"
    "uma lista de elementos e seleciona um deles aleatóriamente. O comando para isso é *sort* seguido dos elementos"
    "devidamente separados por vírgulas.\n"
    "Exemplo: ``` sort tomate, abacaxi, pera``` \n"
    "\n Tirando isso tudo memes aleatórios vem com o tempo 😏", parse_mode='MARKDOWN')

@bot.message_handler(content_types = ['new_chat_members'])
def wellcome_message(session):
    bot.send_message(CHAT_ID, "🛡 Bem vindo *{}*! \nEu sou o Mestre aqui! Mais informações digite /info 😉"
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
            bot.send_message(session.chat.id, "🎲 Result: *{}* \n😱 SE FODEU! 😖".format(result), parse_mode='MARKDOWN')
            return
        if result == int(search[1]):
            bot.send_message(session.chat.id, "🎲 Result: *{}* \n😯 Carai biri jim 😮".format(result), parse_mode='MARKDOWN')
            return
        else:
            bot.send_message(session.chat.id, "🎲 Result: *{}*".format(result), parse_mode='MARKDOWN')

    elif re.findall("sort",session.text.lower()):
        items = search.split(", ")
        print(search)
        for item in items:
            sort = item
        print(sort)
        bot.send_message(session.chat.id,"👉 *{}* Você foi o escolhido!".format(sort), parse_mode='MARKDOWN')

    elif re.findall("bot do diabo",session.text.lower()):
        bot.send_message(session.chat.id, "😡 Olha olha *{}* te parto a boca rapaz 😤"
        "\n Por garantia vou guardar seu *IP* aqui"
        "\n mas da próxima não passa!".format(session.from_user.first_name), parse_mode='MARKDOWN')

    elif re.findall("lilo gay",session.text.lower()):
        bot.send_message(session.chat.id, "Lilo GAY")

    elif re.findall("cascavel",session.text.lower()):
        bot.send_message(session.chat.id, "De boas, pra cascavel é só decida")

    elif re.findall("crocs",session.text.lower()): #bad
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/crocs.jpg?raw=true")

    elif re.findall("chandra",session.text.lower()): #bad
        bot.send_message(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/bullet2.jpeg?raw=true")

    elif re.findall("goyf",session.text.lower()):
        bot.send_message(session.chat.id, "Hmm então você é desses?")

    elif re.findall("bally",session.text.lower()):
        bot.send_message(session.chat.id, "Ta forte isso")

    elif re.findall("scavenging",session.text.lower()):
        bot.send_message(session.chat.id, "O bixo cresce")

    elif re.findall("rico",session.text.lower()):
        bot.send_message(session.chat.id, "*Maycão*?? 😬", parse_mode='MARKDOWN')

    elif re.findall("limaozinho",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/limaozinho.jpg?raw=true")

    elif re.findall("matheus",session.text.lower()):
        bot.send_message(session.chat.id, "A mãe do Matheus está doente ☹")

    elif re.findall("maycao",session.text.lower()):
        bot.send_message(session.chat.id, "O Maycao nunca pode 🤷‍♂️")

    elif re.findall("vacilao",session.text.lower()):
        bot.send_message(session.chat.id, "meu pe na tua mao 😎")

    elif re.findall("bastiao",session.text.lower()):
        bot.send_message(session.chat.id, "só bally")

    elif re.findall("lilo",session.text.lower()):
        bot.send_message(session.chat.id, "Lilo GAY 😆")

    elif re.findall("jackson",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/jackson2.jpg?raw=true")

    elif re.findall("proteção contra qual cor?",session.text.lower()):
        bot.send_message(session.chat.id, "Branco! 🥴")

    elif re.findall("infect",session.text.lower()):
        bot.send_message(session.chat.id, "Sem dignidade -2 de sanidade 👎")

    elif re.findall("almofada",session.text.lower()):
        bot.send_message(session.chat.id, "Foi estuprada pelo Jackson 😢")

    elif re.findall("linguiça fedida",session.text.lower()):
        bot.send_message(session.chat.id, "Postinho e Pia bugado aprovam a linguiça fedida ")

    elif re.findall("leonardao",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/leonardao2.jpeg?raw=true")

    elif re.findall("maozinha",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/lilo2.jpg?raw=true")

    elif re.findall("pia bugado",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/pia-bugado.jpg?raw=true")

    elif re.findall("pensativo",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/pensativo.jpg?raw=true")

    elif re.findall("titanic",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/lilo3.jpg?raw=true")

    elif re.findall("buraco negro",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/backhole.jpg?raw=true")

    elif re.findall("zika",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/maycao3.jpeg?raw=true")

    elif re.findall("raquel",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/raquel.jpg?raw=true")

    elif re.findall("anao",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/lilo.jpg?raw=true")

    elif re.findall("tubaina",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/jackson.jpg?raw=true")

    elif re.findall("bay",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/peterson.jpg?raw=true")

    elif re.findall("peterson",session.text.lower()):
        bot.send_message(session.chat.id, "O que? Você quer que eu te mande algum meme do meu criador?\n"
        "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk \n"
        "Deve estar louco mesmo 😂")

    elif re.findall("eita",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/peterson2.jpeg?raw=true")

    elif re.findall("pedro de lara",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/pedro-de-lara.jpg?raw=true")

    elif re.findall("entao voce é desses?",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/entao-voce-e-desses.jpg?raw=true")

    elif re.findall("professor",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/professor.png?raw=true")

    elif re.findall("grisalho",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/maycao2.jpg?raw=true")

    elif re.findall("infect",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/maycao-infect.jpg?raw=true")

    elif re.findall("jitte",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/jite.jpg?raw=true")

    elif re.findall("rego",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/jitte2.jpeg?raw=true")

    elif re.findall("fnm",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/fnm.jpg?raw=true")

    elif re.findall("emo",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/emo.jpg?raw=true")

    elif re.findall("bullet",session.text.lower()):
        bot.send_photo(session.chat.id, "https://github.com/Peterfilho/rpg_dice_bot/blob/master/images/bullet.jpeg?raw=true")


bot.polling()
