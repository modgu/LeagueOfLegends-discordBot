import discord
import bot
import algo
import random


NApeople = []
EUWpeople = []
EUNEpeople = []
players = []
na_games = 0
euw_games = 0
eune_games = 0
game_nb = 0
solo_na = 0
solo_eune = 0
solo_euw = 0
gameover_counts = {}


class EUWView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_button_click(self, interaction: discord.Interaction, value: str):
        user = interaction.user.name
        EUWpeople.append((user, value))
        bot.EUWpeople = algo.clean(bot.EUWpeople)
        matching_roles = algo.getTeams(EUWpeople)
        await interaction.response.defer()
        if len(matching_roles) == 10:
            for x in matching_roles:
                EUWpeople.remove(x)
            team = algo.splitTeams(matching_roles)
            team1 = team[0:5]
            team2 = team[5:10]
            guild = interaction.guild
            game = guild.get_channel(1136054481583357973)

            player_team1 = [member for member in guild.members if
                            member.name in [player[0] for player in team1]]

            player_team2 = [member for member in guild.members if
                            member.name in [player[0] for player in team2]]
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }

            arbiters_role = discord.utils.get(guild.roles, name="Arbiter Mods")

            if arbiters_role:
                overwrites[arbiters_role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)


            for member in player_team1:
                overwrites[member] = discord.PermissionOverwrite(read_messages=True, send_messages=False)
            for member in player_team2:
                overwrites[member] = discord.PermissionOverwrite(read_messages=True, send_messages=False)

            channel = await guild.create_text_channel(category=game, name='euw-game' + str(bot.euw_games)
                                                      ,overwrites=overwrites)

            message = "Summoner's Drift 5v5"
            embed = discord.Embed(title=f'{message}', colour=discord.Colour.dark_red())
            team1_filed = algo.decoration(team1)
            team2_filed = algo.decoration(team2)
            embed.add_field(name='Team 1', value=team1_filed)
            embed.add_field(name=f'Team 2', value=team2_filed)


            embed.set_footer(text='【N o t e】: Each player must be on the team they are assigned to')

            bot.euw_games += 1
            members_mention = ""
            for i in player_team1:
                members_mention += i.mention + " "
            for i in player_team2:
                members_mention += i.mention + " "


            captain = random.choice(player_team1)
            captainEmbed = discord.Embed(title='Lobby Creator', colour=discord.Colour.dark_red())
            captainEmbed.add_field(name='', value=f'{captain.mention}')

            community_channel = guild.get_channel(1136025715779833876)
            communityEmbd = discord.Embed(title='EUW Game Started', colour=discord.Colour.dark_red())

            team_1_details = ''
            team_2_details = ''
            for i in team1:
                team_1_details += i[0] + "\n"

            for i in team2:
                team_2_details += i[0] + "\n"

            communityEmbd.add_field(name='Team 1', value=f'{team_1_details}')
            communityEmbd.add_field(name='Team 2', value=f'{team_2_details}')

            await channel.send(f'{members_mention}')
            await channel.send(embed=embed)
            await channel.send(embed=captainEmbed)
            await community_channel.send(embed=communityEmbd)
    async def remove_handler(self, interaction: discord.Interaction):
        user = interaction.user
        username = user.name
        await interaction.response.defer()
        for users in EUWpeople:
            if username == users[0]:
                EUWpeople.pop(EUWpeople.index(users))
            else:
                pass

    @discord.ui.button(label='Top',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|EUW'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Jungle',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit1(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|EUW'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Mid',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit2(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|EUW'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='ADC',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit3(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|EUW'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Support',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit4(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|EUW'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Leave Queue', style=discord.ButtonStyle.blurple, row=1)
    async def on_submit5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.remove_handler(interaction)


class NAView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_button_click(self, interaction: discord.Interaction, value: str):
        user = interaction.user.name
        NApeople.append((user, value))
        bot.NApeople = algo.clean(bot.NApeople)
        matching_roles = algo.getTeams(NApeople)
        await interaction.response.defer()
        if len(matching_roles) == 10:
            for x in matching_roles:
                NApeople.remove(x)
            team = algo.splitTeams(matching_roles)
            team1 = team[0:5]
            team2 = team[5:10]
            guild = interaction.guild
            game = guild.get_channel(1136054022932021358)

            player_team1 = [member for member in guild.members if
                            member.name in [player[0] for player in team1]]

            player_team2 = [member for member in guild.members if
                            member.name in [player[0] for player in team2]]
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }

            arbiters_role = discord.utils.get(guild.roles, name="Arbiter Mods")

            if arbiters_role:
                overwrites[arbiters_role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)


            for member in player_team1:
                overwrites[member] = discord.PermissionOverwrite(read_messages=True, send_messages=False)
            for member in player_team2:
                overwrites[member] = discord.PermissionOverwrite(read_messages=True, send_messages=False)

            channel = await guild.create_text_channel(category=game, name='na-game' + str(bot.na_games),
                                                      overwrites=overwrites)

            message = "Summoner's Drift 5v5"
            embed = discord.Embed(title=f'{message}', colour=discord.Colour.dark_red())
            team1_filed = algo.decoration(team1)
            team2_filed = algo.decoration(team2)
            embed.add_field(name='Team 1', value=team1_filed)
            embed.add_field(name=f'Team 2', value=team2_filed)

            embed.set_footer(text='【N o t e】: Each player must be on the team they are assigned to')


            bot.na_games += 1
            members_mention = ""
            for i in player_team1:
                members_mention += i.mention + " "
            for i in player_team2:
                members_mention += i.mention + " "

            captain = random.choice(player_team1)
            captainEmbed = discord.Embed(title='Lobby Creator',colour=discord.Colour.dark_red())
            captainEmbed.add_field(name='', value=f'{captain.mention}')

            community_channel = guild.get_channel(1136025715779833876)
            communityEmbd = discord.Embed(title='NA Game Started', colour=discord.Colour.dark_red())

            team_1_details = ''
            team_2_details = ''
            for i in team1:
                team_1_details += i[0] + "\n"

            for i in team2:
                team_2_details+=i[0] + "\n"

            communityEmbd.add_field(name='Team 1', value=f'{team_1_details}')
            communityEmbd.add_field(name='Team 2', value=f'{team_2_details}')

            await channel.send(f'{members_mention}')
            await channel.send(embed=embed)
            await channel.send(embed=captainEmbed)
            await community_channel.send(embed=communityEmbd)

    async def remove_handler(self, interaction: discord.Interaction):
        user = interaction.user
        username = user.name
        await interaction.response.defer()
        for users in NApeople:
            if username == users[0]:
                NApeople.pop(NApeople.index(users))
            else:
                pass

    @discord.ui.button(label='Top',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|NA'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Jungle',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit1(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|NA'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Mid',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit2(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|NA'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='ADC',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit3(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|NA'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Support',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit4(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|NA'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Leave Queue', style=discord.ButtonStyle.blurple, row=1)
    async def on_submit5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.remove_handler(interaction)


class EUNEView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_button_click(self, interaction: discord.Interaction, value: str):
        user = interaction.user.name
        EUNEpeople.append((user, value))
        bot.EUNEpeople = algo.clean(bot.EUNEpeople)
        matching_roles = algo.getTeams(EUNEpeople)
        await interaction.response.defer()
        if len(matching_roles) == 10:
            for x in matching_roles:
                EUNEpeople.remove(x)
            team = algo.splitTeams(matching_roles)
            team1 = team[0:5]
            team2 = team[5:10]
            guild = interaction.guild
            game = guild.get_channel(1136054803684925580)

            player_team1 = [member for member in guild.members if
                            member.name in [player[0] for player in team1]]

            player_team2 = [member for member in guild.members if
                            member.name in [player[0] for player in team2]]
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }

            arbiters_role = discord.utils.get(guild.roles, name="Arbiter Mods")

            if arbiters_role:
                overwrites[arbiters_role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)


            for member in player_team1:
                overwrites[member] = discord.PermissionOverwrite(read_messages=True, send_messages=False)
            for member in player_team2:
                overwrites[member] = discord.PermissionOverwrite(read_messages=True, send_messages=False)


            channel = await guild.create_text_channel(category=game, name='eune-game' + str(bot.eune_games)
                                                      ,overwrites=overwrites)
            message = "Summoner's Drift 5v5"
            embed = discord.Embed(title=f'{message}', colour=discord.Colour.dark_red())
            team1_filed = algo.decoration(team1)
            team2_filed = algo.decoration(team2)
            embed.add_field(name='Team 1', value=team1_filed)
            embed.add_field(name=f'Team 2', value=team2_filed)

            embed.set_footer(text='【N o t e】: Each player must be on the team they are assigned to')

            bot.eune_games += 1
            members_mention = ""
            for i in player_team1:
                members_mention += i.mention + " "
            for i in player_team2:
                members_mention += i.mention + " "

            playButton = discord.ui.Button(style=discord.ButtonStyle.success, label="Play",
                                           url=f"https://matches.arbiters.io/info/{channel.id}")


            captain = random.choice(player_team1)
            captainEmbed = discord.Embed(title='Lobby Creator', colour=discord.Colour.dark_red())
            captainEmbed.add_field(name='', value=f'{captain.mention}')

            community_channel = guild.get_channel(1136025715779833876)
            communityEmbd = discord.Embed(title='EUNE Game Started', colour=discord.Colour.dark_red())

            team_1_details = ''
            team_2_details = ''
            for i in team1:
                team_1_details += i[0] + "\n"

            for i in team2:
                team_2_details += i[0] + "\n"

            communityEmbd.add_field(name='Team 1', value=f'{team_1_details}')
            communityEmbd.add_field(name='Team 2', value=f'{team_2_details}')

            await channel.send(f'{members_mention}')
            await channel.send(embed=embed)
            await channel.send(embed=captainEmbed)
            await community_channel.send(embed=communityEmbd)

    async def remove_handler(self, interaction: discord.Interaction):
        user = interaction.user
        username = user.name
        await interaction.response.defer()
        for users in EUNEpeople:
            if username == users[0]:
                EUNEpeople.pop(EUNEpeople.index(users))
            else:
                pass

    @discord.ui.button(label='Top',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|EUNE'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Jungle',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit1(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|EUNE'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Mid',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit2(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|EUNE'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='ADC',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit3(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|EUNE'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Support',
                       style=discord.ButtonStyle.red, row=0)
    async def on_submit4(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        value += '|EUNE'
        await self.handle_button_click(interaction, value)

    @discord.ui.button(label='Leave Queue', style=discord.ButtonStyle.blurple, row=1)
    async def on_submit5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.remove_handler(interaction)


class SoloView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def select_handler(self, interaction: discord.Interaction, value: str):
        user = interaction.user
        username = user.name
        players.append((username, value))
        bot.players = algo.clean(bot.players)
        matching_roles = algo.getPlayer(players)
        await interaction.response.defer()
        if len(matching_roles) == 2:
            for x in matching_roles:
                players.remove(x)
            guild = interaction.guild
            player_members = [member for member in guild.members if
                              member.name in [player[0] for player in matching_roles]]
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            }


            arbiters_role = discord.utils.get(guild.roles, name="Arbiter Mods")

            if arbiters_role:
                overwrites[arbiters_role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)

            for member in player_members:
                overwrites[member] = discord.PermissionOverwrite(read_messages=True, send_messages=False)

            game_name = matching_roles[0][1]

            if(game_name == 'NA'):
                game = guild.get_channel(1136055392141594644)
                channel = await guild.create_text_channel(category=game, name=f'{game_name}-game' + str(bot.solo_na),
                                                          overwrites=overwrites)
                em = discord.Embed(title='Howling Abyss 1v1',colour=discord.Colour.dark_red())
                match = algo.solo_decoration(matching_roles)
                em.add_field(name="Match", value=f'{match}')
                em.set_footer(text='【N o t e】: Each player must be on the team they are assigned to')


                mention_message = ""
                for i in player_members:
                    mention_message += i.mention + " "

                captain = random.choice(player_members)

                captainEmbed = discord.Embed(title='Lobby Creator', colour=discord.Colour.dark_red())
                captainEmbed.add_field(name='', value=f'{captain.mention}')
                community_channel = guild.get_channel(1136058401835716778)
                communityEmbd = discord.Embed(title='NA Game Started',colour=discord.Colour.dark_red())

                info_details = ''
                for i in matching_roles:
                    info_details += i[0]+"\n"
                communityEmbd.add_field(name='',value=info_details)

                await channel.send(f'{mention_message}')
                await channel.send(embed=em)
                await channel.send(embed=captainEmbed)
                await community_channel.send(embed=communityEmbd)

            elif(game_name == 'EUW'):
                game = guild.get_channel(1136055438597701822)
                channel = await guild.create_text_channel(category=game, name=f'{game_name}-game' + str(bot.solo_euw),
                                                          overwrites=overwrites)
                em = discord.Embed(title='Howling Abyss 1v1', colour=discord.Colour.dark_red())
                match = algo.solo_decoration(matching_roles)
                em.add_field(name="Match", value=f'{match}')
                em.set_footer(text='【N o t e】: Each player must be on the team they are assigned to')

                cahnnelID = [("ChannelID", channel.id)]
                cahnelID_filed = algo.toJson(cahnnelID)
                game_response = algo.toJson(matching_roles)
                sentData = algo.combineJSON([cahnelID_filed, game_response])

                bot.solo_euw += 1

                mention_message = ""
                for i in player_members:
                    mention_message += i.mention + " "

                captain = random.choice(player_members)

                captainEmbed = discord.Embed(title='Lobby Creator', colour=discord.Colour.dark_red())
                captainEmbed.add_field(name='', value=f'{captain.mention}')

                community_channel = guild.get_channel(1136058401835716778)
                communityEmbd = discord.Embed(title='EUW Game Started', colour=discord.Colour.dark_red())
                info_details = ''
                for i in matching_roles:
                    info_details += i[0] + "\n"
                communityEmbd.add_field(name='', value=info_details)

                await channel.send(f'{mention_message}')
                await channel.send(embed=em)
                await channel.send(embed=captainEmbed)
                await community_channel.send(embed=communityEmbd)

            elif(game_name == 'EUNE'):
                game = guild.get_channel(1136055472550596779)
                channel = await guild.create_text_channel(category=game, name=f'{game_name}-game' + str(bot.solo_eune),
                                                          overwrites=overwrites)
                em = discord.Embed(title='Howling Abyss 1v1', colour=discord.Colour.dark_red())
                match = algo.solo_decoration(matching_roles)
                em.add_field(name="Match", value=f'{match}')
                em.set_footer(text='【N o t e】: Each player must be on the team they are assigned to')

                bot.solo_eune += 1
                mention_message = ""
                for i in player_members:
                    mention_message += i.mention + " "

                captain = random.choice(player_members)

                captainEmbed = discord.Embed(title='Lobby Creator', colour=discord.Colour.dark_red())

                captainEmbed.add_field(name='', value=f'{captain.mention}')
                community_channel = guild.get_channel(1136058401835716778)
                communityEmbd = discord.Embed(title='EUNE Game Started', colour=discord.Colour.dark_red())

                info_details = ''
                for i in matching_roles:
                    info_details += i[0] + "\n"
                communityEmbd.add_field(name='', value=info_details)

                await channel.send(f'{mention_message}')
                await channel.send(embed=em)
                await channel.send(embed=captainEmbed)
                await community_channel.send(embed=communityEmbd)

    async def remove_handle(self, interaction: discord.Interaction):
        user = interaction.user
        username = user.name
        await interaction.response.defer()
        for users in players:
            if username == users[0]:
                players.pop(players.index(users))
            else:
                pass

    @discord.ui.button(label='EUW', style=discord.ButtonStyle.red)
    async def on_submit(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        await self.select_handler(interaction, value)

    @discord.ui.button(label='NA', style=discord.ButtonStyle.red)
    async def on_submit1(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        await self.select_handler(interaction, value)

    @discord.ui.button(label='EUNE', style=discord.ButtonStyle.red)
    async def on_submit2(self, interaction: discord.Interaction, button: discord.ui.Button):
        value = button.label
        await self.select_handler(interaction, value)

    @discord.ui.button(label='Leave Queue', style=discord.ButtonStyle.blurple, row=1)
    async def on_submit3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.remove_handle(interaction)


def run():

    token = 'ADD_YOUR_TOKEN'
    intents = discord.Intents.all()
    intents.message_content = True
    intents.guilds = True
    intents.members = True
    permision = discord.Permissions()
    permision.manage_channels = True
    bot = discord.ext.commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

        guild = bot.guilds[0]
        server_channel = discord.utils.get(guild.channels, name='🟢・na-server')
        server_channel3 = discord.utils.get(guild.channels, name='🟢・euw-server')
        server_channel4 = discord.utils.get(guild.channels, name='🟢・eune-server')
        server_channel1 = discord.utils.get(guild.channels, name='🟢・1v1-lobby')

        if server_channel:
            message = 'Choose a role to be matched with a team \n' \
                      'You may change your role at any given time before a match has been found'
            squadEmbed = discord.Embed(title='NA Queue', colour=discord.Colour.red())
            squadEmbed.add_field(name="Summoner's Rift 5v5", value=message)
            view = NAView()
            await server_channel.send(embed=squadEmbed)
            await server_channel.send(view=view)

        if server_channel3:

            message = 'Choose a role to be matched with a team \n' \
                      'You may change your role at any given time before a match has been found'
            squadEmbed = discord.Embed(title='EUW Queue', colour=discord.Colour.red())
            squadEmbed.add_field(name="Summoner's Rift 5v5", value=message)
            view = EUWView()
            await server_channel3.send(embed=squadEmbed)
            await server_channel3.send(view=view)

        if server_channel4:
            message = 'Choose a role to be matched with a team \n' \
                      'You may change your role at any given time before a match has been found'
            squadEmbed = discord.Embed(title='EUNE Queue', colour=discord.Colour.red())
            squadEmbed.add_field(name="Summoner's Rift 5v5", value=message)
            view = EUNEView()
            await server_channel4.send(embed=squadEmbed)
            await server_channel4.send(view=view)

        if server_channel1:
            message = 'Choose a server to be matched with a team \n' \
                      'You may change your server at any given time before a match has been found'
            soloEmbed = discord.Embed(title='SOLO',colour=discord.Colour.red())
            soloEmbed.add_field(name='Howling Abyss 1v1', value=message)
            view = SoloView()
            await server_channel1.send(embed=soloEmbed)
            await server_channel1.send(view=view)

        await bot.tree.sync()

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, discord.ext.commands.CommandNotFound):
            return


    @bot.command(name='nalist')
    async def naList(ctx):
        channel = ctx.channel
        if channel.name != '🤖・commands':
            return
        else:
            embed = discord.Embed(colour=discord.Colour.dark_red())
            na_list = NApeople
            if len(na_list) == 0:
                embed.add_field(name='NA-Players',value='No Players')
                await ctx.send(embed=embed)
            else:
                embed.add_field(name='NA-Players',value=f'{na_list}')
                await ctx.send(embed=embed)

    @bot.command(name='euwlist')
    async def naList(ctx):
        channel = ctx.channel
        if channel.name != '🤖・commands':
            return
        else:
            embed = discord.Embed(colour=discord.Colour.dark_red())
            euw_list = EUWpeople
            if len(euw_list) == 0:
                embed.add_field(name='EUW-Players', value='No Players')
                await ctx.send(embed=embed)
            else:
                embed.add_field(name='EUW-Players', value=f'{euw_list}')
                await ctx.send(embed=embed)

    @bot.command(name='eunelist')
    async def naList(ctx):
        channel = ctx.channel
        if channel.name != '🤖・commands':
            return
        else:
            embed = discord.Embed(colour=discord.Colour.dark_red())
            eune_list = EUNEpeople
            if len(eune_list) == 0:
                embed.add_field(name='EUNE-Players', value='No Players')
                await ctx.send(embed=embed)
            else:
                embed.add_field(name='EUNE-Players', value=f'{eune_list}')
                await ctx.send(embed=embed)

    @bot.tree.command(name="na", description='check NA players')
    async def na(interaction: discord.Interaction):
        channel = interaction.channel
        channel_name = channel.name
        if channel_name == '👥・squad-community':
            embed = discord.Embed(colour=discord.Colour.dark_red())
            list = NApeople
            if len(list) == 0:
                embed.add_field(name='NA-Players', value='No players')
                await interaction.response.send_message(embed=embed)
            else:
                roles = []
                for i in list:
                    role = i[1]
                    roles.append(role)
                count_roles = algo.countNAPlayers(roles)
                message = ''
                for key,values in count_roles.items():
                    message+= f'{key} : {values} \n'
                embed.add_field(name='NA-Players',value=message)
                await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message('cant be invoked here',ephemeral=True)

    @bot.tree.command(name="euw", description='check EUW players')
    async def euw(interaction: discord.Interaction):
        channel = interaction.channel
        channel_name = channel.name
        if channel_name == '👥・squad-community':
            embed = discord.Embed(colour=discord.Colour.dark_red())
            list = EUWpeople
            if len(list) == 0:
                embed.add_field(name='EUW-Players', value='No players')
                await interaction.response.send_message(embed=embed)
            else:
                roles = []
                for i in list:
                    role = i[1]
                    roles.append(role)
                count_roles = algo.countEUWPlayers(roles)
                message = ''
                for key, values in count_roles.items():
                    message += f'{key} : {values} \n'
                embed.add_field(name='EUW-Players', value=message)
                await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message('cant be invoked here', ephemeral=True)

    @bot.tree.command(name="eune", description='check EUNE players')
    async def eune(interaction: discord.Interaction):
        channel = interaction.channel
        channel_name = channel.name
        if channel_name == '👥・squad-community':
            embed = discord.Embed(colour=discord.Colour.dark_red())
            list = EUNEpeople
            if len(list) == 0:
                embed.add_field(name='EUNE-Players', value='No players')
                await interaction.response.send_message(embed=embed)
            else:
                roles = []
                for i in list:
                    role = i[1]
                    roles.append(role)
                count_roles = algo.countEUNEPlayers(roles)
                message = ''
                for key, values in count_roles.items():
                    message += f'{key} : {values} \n'
                embed.add_field(name='EUNE-Players', value=message)
                await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message('cant be invoked here', ephemeral=True)

    bot.run(token)