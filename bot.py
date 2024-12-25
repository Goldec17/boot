import discord
import pytz
import sqlite3
from datetime import datetime
from discord.ext import commands
from random import randint

permissoes_bot = discord.Intents.all()
permissoes_bot.message_content = True
permissoes_bot.members = True
bot = commands.Bot(command_prefix="%", intents=permissoes_bot)

# Banco de dados
connect = sqlite3.connect('usuarios.db')
cursor = connect.cursor()
# Criação da tabela Usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID único para cada usuário
    nome TEXT NOT NULL,                    -- Nome do usuário
    mkoins INTEGER DEFAULT 1000               -- Quantidade inicial de mkoins
)
''')

# Confirma as alterações
connect.commit()

'''
@bot.commands()
async def mkoins(ctx):
'''

@bot.command()  # Inicio de comandos do bot
@commands.has_permissions(manage_roles=True)  # Requer permissão para gerenciar cargos
async def setcargo(ctx, member: discord.Member, *roles: discord.Role):
    if not roles:
        await ctx.reply("Você precisa mencionar pelo menos um cargo!")
        return

    added_roles = []
    for role in roles:
        if role not in member.roles:
            try:
                await member.add_roles(role)
                added_roles.append(role.name)
            except discord.Forbidden:
                await ctx.send(f"Não tenho permissão para adicionar o cargo {role.name}.")
        else:
            await ctx.send(f"{member.mention} já possui o cargo {role.name}.")

    if added_roles:
        added_roles_str = ", ".join(added_roles)
        await ctx.send(f"Cargos {added_roles_str} adicionados ao {member.mention} com sucesso!")


@bot.command()
async def saudacaosimples(ctx: commands.Context):
    user_mention = ctx.author.mention
    await ctx.reply(f"Opa, {user_mention}, tudo joia?")

    # Obter o horário atual no fuso horário local
    timezone = pytz.timezone("America/Sao_Paulo")
    local_time = datetime.now(timezone)
    time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")

    # ID do canal de log
    log_channel_id = 1320407543042015252  # Substitua pelo ID correto
    log_channel = bot.get_channel(log_channel_id)

    # Monta a mensagem de log
    log_message = f"{time_send}: O comando `medirBeleza` foi usado por {user_mention}."

    # Envia a mensagem para o canal de log
    if log_channel:
        try:
            await log_channel.send(log_message)
        except discord.Forbidden:
            print("Não foi possível enviar a mensagem para o canal de log. Verifique as permissões.")
    else:
        print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.command()
async def saudacao(ctx: commands.Context, *, frase):
    user_mention = ctx.author.mention
    await ctx.reply(f"Opa, {user_mention}, infelizmente não sei ler, culpe o <@1259893215465705553>.")

    # Obter o horário atual no fuso horário local
    timezone = pytz.timezone("America/Sao_Paulo")
    local_time = datetime.now(timezone)
    time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")

    # ID do canal de log
    log_channel_id = 1320407543042015252  # Substitua pelo ID correto
    log_channel = bot.get_channel(log_channel_id)

    # Monta a mensagem de log
    log_message = f"{time_send}: O comando `medirBeleza` foi usado por {user_mention}."

    # Envia a mensagem para o canal de log
    if log_channel:
        try:
            await log_channel.send(log_message)
        except discord.Forbidden:
            print("Não foi possível enviar a mensagem para o canal de log. Verifique as permissões.")
    else:
        print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.command()
async def saudacaopara(ctx: commands.Context, *, frase: str):
    user_mention = ctx.author.mention
    # Formata a menção do autor
    if ctx.message.mentions:  # Verifica se há menções
        mentioned_user = ctx.message.mentions[0]  # Pega o primeiro membro mencionado

        # Remove a menção do membro da frase
        frase_limpa = frase.replace(f"{mentioned_user.mention}", "").strip()

        await ctx.reply(f"{mentioned_user}, {user_mention} quer te dizer: {frase_limpa}")
    else:
        await ctx.reply("Por favor, mencione alguém na mensagem.")

        # Obter o horário atual no fuso horário local
        timezone = pytz.timezone("America/Sao_Paulo")
        local_time = datetime.now(timezone)
        time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")

        # ID do canal de log
        log_channel_id = 1320407543042015252  # Substitua pelo ID correto
        log_channel = bot.get_channel(log_channel_id)

        # Monta a mensagem de log
        log_message = f"{time_send}: O comando `medirBeleza` foi usado por {user_mention}."

        # Envia a mensagem para o canal de log
        if log_channel:
            try:
                await log_channel.send(log_message)
            except discord.Forbidden:
                print("Não foi possível enviar a mensagem para o canal de log. Verifique as permissões.")
        else:
            print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.command()
async def medirbeleza(ctx: commands.Context):
    blz = randint(0, 100)
    if blz < 10:
        print("Segunda chance")
        blz = randint(0, 100)
    user_mention = ctx.author.mention
    fmt_mtn_txt = f"{user_mention}, você tem: %{blz} de beleza!"
    await ctx.reply(fmt_mtn_txt)

    # Obter o horário atual no fuso horário local
    timezone = pytz.timezone("America/Sao_Paulo")
    local_time = datetime.now(timezone)
    time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")

    # ID do canal de log
    log_channel_id = 1320407543042015252  # Substitua pelo ID correto
    log_channel = bot.get_channel(log_channel_id)

    # Monta a mensagem de log
    log_message = f"{time_send}: O comando `medirBeleza` foi usado por {user_mention}."

    # Envia a mensagem para o canal de log
    if log_channel:
        try:
            await log_channel.send(log_message)
        except discord.Forbidden:
            print("Não foi possível enviar a mensagem para o canal de log. Verifique as permissões.")
    else:
        print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.command()
async def compararbeleza(ctx: commands.Context, *, frase: str):
    user_mention = ctx.author.mention
    if ctx.message.mentions:  # Verifica se há menções
        mentioned_user = ctx.message.mentions[0]  # Primeiro membro mencionado
        mentioned_mention = mentioned_user.mention

        # Calcula valores de beleza
        blz_user_mention = randint(0, 100)
        blz_user_mentioned = randint(0, 100)

        # Determina o vencedor
        if blz_user_mention > blz_user_mentioned:
            calc = blz_user_mention - blz_user_mentioned
            res = f"{user_mention} você tem %{calc} a mais de beleza que {mentioned_mention}!"
        elif blz_user_mention < blz_user_mentioned:
            calc = blz_user_mentioned - blz_user_mention
            res = f"{mentioned_mention} tem %{calc} a mais de beleza que você, {user_mention}!"
        else:
            res = f"{user_mention} e {mentioned_mention}, vocês têm exatamente a mesma beleza (%{blz_user_mention})!"

        txt = f'''{res}\n\n
        {user_mention}: %{blz_user_mention}\n
        {mentioned_mention}: %{blz_user_mentioned}\nLembrem-se que isso é apenas um jogo, ok?"'''
        # Envia a resposta
        await ctx.reply(txt)

    else:
        await ctx.reply("Por favor, mencione alguém para comparar a beleza.")

    # Obter o horário atual no fuso horário local
    timezone = pytz.timezone("America/Sao_Paulo")
    local_time = datetime.now(timezone)
    time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")

    # ID do canal de log
    log_channel_id = 1320407543042015252  # Substitua pelo ID correto
    log_channel = bot.get_channel(log_channel_id)

    # Monta a mensagem de log
    log_message = f"{time_send}: O comando `compararBeleza` foi usado por {user_mention}."

    # Envia a mensagem para o canal de log
    if log_channel:
        try:
            await log_channel.send(log_message)
        except discord.Forbidden:
            print("Não foi possível enviar a mensagem para o canal de log. Verifique as permissões.")
    else:
        print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.command()
async def enviar_embed(ctx:commands.Context):
    user_mention = ctx.author.mention
    meu_embed = discord.Embed(title="Olá, Mundo!", description="Meu primeiro embed!")

    # Para usar imagens
    meu_embed.set_image(url="https://www.google.com/imgres?q=imagens&imgurl=https%3A%2F%2Fichef.bbci.co.uk%2Face%2Fws%2F640%2Fcpsprodpb%2F8893%2Flive%2Fac7e5c10-c12f-11ee-896d-39d9bd3cadbb.jpg.webp&imgrefurl=https%3A%2F%2Fwww.bbc.com%2Fportuguese%2Farticles%2Fc1v1eevqgwko&docid=KYQ9A5hjav_nGM&tbnid=4z5SZSYXvYMrzM&vet=12ahUKEwii0u2vlcGKAxUBqZUCHU_JDgwQM3oECBcQAA..i&w=640&h=426&hcb=2&ved=2ahUKEwii0u2vlcGKAxUBqZUCHU_JDgwQM3oECBcQAA")

    await ctx.send(embed=meu_embed)

    # Obter o horário atual no fuso horário local
    timezone = pytz.timezone("America/Sao_Paulo")
    local_time = datetime.now(timezone)
    time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")

    # ID do canal de log
    log_channel_id = 1320407543042015252  # Substitua pelo ID correto
    log_channel = bot.get_channel(log_channel_id)

    # Monta a mensagem de log
    log_message = f"{time_send}: O comando `enviar_embed` foi usado por {user_mention}."

    # Envia a mensagem para o canal de log
    if log_channel:
        try:
            await log_channel.send(log_message)
        except discord.Forbidden:
            print("Não foi possível enviar a mensagem para o canal de log. Verifique as permissões.")
    else:
        print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.event   #Inicio de eventos do bot
async def on_ready():
    print("O bot foi iniciado!")


@bot.event
async def on_command_error(ctx, error):
    user_mention = ctx.author.mention
    timezone = pytz.timezone("America/Sao_Paulo")
    local_time = datetime.now(timezone)
    time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")

    # ID do canal de log
    log_channel_id = 1320407543042015252  # Substitua pelo ID correto
    log_channel = bot.get_channel(log_channel_id)

    if isinstance(error, commands.CommandNotFound):
        txt = f"❌ | O comando `{ctx.invoked_with}` não existe. Verifique a lista de comandos disponíveis com `%help`."
        await ctx.reply(txt)
        log_message = f"{time_send}: {user_mention} tentou usar um comando inexistente: `{ctx.invoked_with}`."
    elif isinstance(error, commands.MissingRequiredArgument):
        txt = f"⚠️ | O comando `{ctx.command}` está faltando argumentos obrigatórios. Use `%help {ctx.command}` para mais informações."
        await ctx.reply(txt)
        log_message = f"{time_send}: {user_mention} tentou usar o comando `{ctx.command}` com argumentos incompletos."
    else:
        print(f"Erro não tratado: {error}")
        log_message = f"{time_send}: Erro inesperado ao processar um comando de {user_mention}: {error}"

    # Envia a mensagem de log
    if log_channel:
        try:
            await log_channel.send(log_message)
        except discord.Forbidden:
            print("Não foi possível enviar a mensagem para o canal de log. Verifique as permissões.")
    else:
        print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.event
async def on_guild_channel_create(canal: discord.abc.GuildChannel):
    # Verifica se o canal é um canal de texto
    if isinstance(canal, discord.TextChannel):
        # Obter o horário de criação do canal
        utc_time = canal.created_at  # Horário UTC de criação do canal
        timezone = pytz.timezone("America/Sao_Paulo")  # Fuso horário
        local_time = utc_time.astimezone(timezone)  # Converte para o fuso horário local
        time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")  # Formata a data e hora

        # ID do canal de log
        log_channel_id = 1320091579725381652
        log_channel = bot.get_channel(log_channel_id)

        # Tenta identificar o criador do canal
        creator = None
        async for audit_log in canal.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create):
            creator = audit_log.user
            break  # Saia do loop após encontrar o criador

        if creator:
            log_message = f"{time_send}: O canal {canal.mention} foi criado por {creator.mention}."
        else:
            log_message = f"{time_send}: O canal {canal.mention} foi criado, mas não foi possível determinar o criador."

        # Envia a mensagem para o canal de log
        if log_channel:
            try:
                await log_channel.send(log_message)
            except discord.Forbidden:
                print(f"Não foi possível enviar a mensagem para o canal de log. Verifique as permissões.")
        else:
            print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.event
async def on_guild_channel_delete(canal: discord.abc.GuildChannel):
    if isinstance(canal, discord.TextChannel):
        # Obter o horário atual no momento da exclusão do canal
        utc_time = canal.created_at  # Horário UTC de criação do canal
        timezone = pytz.timezone("America/Sao_Paulo")  # Fuso horário
        local_time = utc_time.astimezone(timezone)  # Converte para o fuso horário local
        time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")  # Formata a data e hora

        # ID do canal de log
        log_channel_id = 1320091579725381652
        log_channel = bot.get_channel(log_channel_id)

        # Tenta identificar o destruidor do canal
        destrutc = None
        async for audit_log in canal.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete):
            destrutc = audit_log.user
            break  # Saia do loop após encontrar o destrutor

        if destrutc:
            log_message = f"{time_send}: O canal {canal.name} foi deletado por {destrutc.mention}."
        else:
            log_message = f"{time_send}: O canal {canal.name} foi deletado, mas não é possível determinar quem deletou."

        # Envia a mensagem para o canal de log
        if log_channel:
            try:
                await log_channel.send(log_message)
            except discord.Forbidden:
                print(f"Não foi possível enviar a mensagem para o canal de log. Verifique as permissões.")
        else:
            print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.event
async def on_member_join(member: discord.Member):
    user_mention = member.mention

    # Obter o horário de envio da mensagem com o fuso horário correto
    utc_time = member.created_at  # Horário UTC de criação da mensagem
    timezone = pytz.timezone("America/Sao_Paulo")  # Fuso horário
    local_time = utc_time.astimezone(timezone)  # Converte para o fuso horário local
    time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")  # Formata a data e hora

    # ID do canal de log
    log_channel_id = 1320064801279574136
    log_channel = bot.get_channel(log_channel_id)

    # Monta a mensagem de log
    log_message = f"{time_send}: {user_mention} entrou no servidor."

    # Envia a log para o canal de log, se disponível
    if log_channel:
        try:
            await log_channel.send(log_message)
        except discord.Forbidden:
            print(f"Não tenho permissão para enviar mensagens no canal de log: {log_channel_id}.")
    else:
        print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.event
async def on_member_remove(member: discord.Member):
    user_mention = member.name

    # Obter o horário de envio da mensagem com o fuso horário correto
    utc_time = member.created_at  # Horário UTC de criação da mensagem
    timezone = pytz.timezone("America/Sao_Paulo")  # Fuso horário
    local_time = utc_time.astimezone(timezone)  # Converte para o fuso horário local
    time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")  # Formata a data e hora

    # ID do canal de log
    log_channel_id = 1320064835035201576
    log_channel = bot.get_channel(log_channel_id)

    # Monta a mensagem de log
    log_message = f"{time_send}: {user_mention} foi embora do servidor."

    # Envia a mensagem para o canal de log
    if log_channel:
        try:
            await log_channel.send(log_message)
        except discord.Forbidden:
            print(f"Não tenho permissão para enviar mensagens no canal de log: {log_channel_id}.")
    else:
        print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.event
async def on_member_update(before, after):
    # ID do canal de log
    log_channel_id = 1320064919600762890  # Substitua pelo ID do seu canal de log
    log_channel = bot.get_channel(log_channel_id)

    changes = []

    # Verifica se o apelido mudou
    if before.nick != after.nick:
        changes.append(f"**Apelido alterado de:** {before.nick} para {after.nick}")

    # Verifica os cargos adicionados e removidos
    added_roles = [role for role in after.roles if role not in before.roles]
    removed_roles = [role for role in before.roles if role not in after.roles]

    if added_roles:
        changes.append(f"**Cargos adicionados:** {', '.join(role.name for role in added_roles)}")

    if removed_roles:
        changes.append(f"**Cargos removidos:** {', '.join(role.name for role in removed_roles)}")

    # Se houve mudanças, monta a mensagem de log
    if changes:
        log_message = f"As informações de {after.mention} foram modificadas:\n" + "\n".join(changes)

        # Envia a mensagem para o canal de log
        if log_channel:
            try:
                await log_channel.send(log_message)
            except discord.Forbidden:
                print(f"Não foi possível enviar a mensagem para o canal de log. Verifique as permissões.")
    else:
        print(f"Nenhuma alteração relevante foi detectada para {after.mention}.")


@bot.event
async def on_message(msg: discord.Message):
    usuario = msg.author

    # Ignorar mensagens enviadas por bots
    if usuario.bot:
        return

    # Obter o horário de envio da mensagem com o fuso horário correto
    utc_time = msg.created_at  # Horário UTC de criação da mensagem
    timezone = pytz.timezone("America/Sao_Paulo")  # Fuso horário
    local_time = utc_time.astimezone(timezone)  # Converte para o fuso horário local
    time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")  # Formata a data e hora

    # Nome do canal
    canal = msg.channel.name

    # ID do canal de log
    log_channel_id = 1320065044976762950
    log_channel = bot.get_channel(log_channel_id)

    # Monta a mensagem de log
    log_message = f"{time_send}: {usuario.mention} enviou: '{msg.content}' no canal: {canal}."

    # Enviar a mensagem de log para o canal
    if log_channel:
        try:
            await log_channel.send(log_message)
        except discord.Forbidden:
            print(f"Não tenho permissão para enviar mensagens no canal de log: {log_channel_id}.")
    else:
        print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")

    # Para processar outros comandos do bot
    await bot.process_commands(msg)


@bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    # Obter o horário da edição da mensagem
    utc_time = after.edited_at  # Horário UTC da edição
    timezone = pytz.timezone("America/Sao_Paulo")  # Fuso horário
    local_time = utc_time.astimezone(timezone)  # Converte para o fuso horário local
    time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")  # Formata a data e hora

    # ID do canal de log
    log_channel_id = 1320064968221003776  # Substitua pelo ID correto
    log_channel = bot.get_channel(log_channel_id)

    # Monta a mensagem de log
    log_message = (
        f"{time_send}: Mensagem editada no canal {before.channel.mention}.\n"
        f"**Antes:** {before.content}\n"
        f"**Depois:** {after.content}\n"
        f"**Autor:** {before.author.mention}"
    )

    # Enviar a mensagem de log para o canal
    if log_channel:
        try:
            await log_channel.send(log_message)
        except discord.Forbidden:
            print(f"Não tenho permissão para enviar mensagens no canal de log: {log_channel_id}.")
    else:
        print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


@bot.event
async def on_message_delete(message):
    # Obter o horário da exclusão da mensagem
    utc_time = message.created_at  # Horário UTC da criação da mensagem
    timezone = pytz.timezone("America/Sao_Paulo")  # Fuso horário
    local_time = utc_time.astimezone(timezone)  # Converte para o fuso horário local
    time_send = local_time.strftime("%d/%m/%Y %H:%M:%S")  # Formata a data e hora

    # ID do canal de log
    log_channel_id = 1320253816230121472
    log_channel = bot.get_channel(log_channel_id)

    # Monta a mensagem de log
    log_message = f"{time_send}: A mensagem de {message.author.mention} foi deletada.\n" \
                  f"**Conteúdo:** {message.content}"

    # Envia a mensagem para o canal de log
    if log_channel:
        try:
            await log_channel.send(log_message)
        except discord.Forbidden:
            print(f"Não foi possível enviar a mensagem para o canal de log. Verifique as permissões.")
    else:
        print(f"Não foi possível encontrar o canal de log. Verifique o ID: {log_channel_id}.")


bot.run("")
