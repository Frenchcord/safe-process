'''
ALL RIGHTS ARE RESERVED TO NAME AND FRENCHCORD
'''
import frenchcord, re
bot = frenchcord.Robot('Token goes here')
@bot.event('message')
def msg_process(message):
  bot.process_commands(message)

@bot.command
def execute(ctx):
  msgs: list = ctx.message.content.split('\n')
  for i in range(len(msgs):
    if i != 0:
      content += msgs[i]
  content = re.sub(r"(^`{1,3}(py(thon)?)?|`{1,3}$)", "", content)
  process = frenchcord.safe_process(content)
  process.execute()
  ctx.send(embeds=[frenchcord.Embed(titre=f'Code de {message.auteur.nom}', description="```py\n{content}\n```\n**Console**\n```console\n{process.console}```", couleur=frenchcord.color_random())])
bot.connexion(['?'])
