import discord
from discord.ext import commands
import urllib.parse, urllib.request, re
import datetime
import os
import random
import traceback
import asyncio

access_token = os.environ["BOT_TOKEN"]

rainbow_serverid = 663273290982490113
rainbowrolename = "Rainbow"
rainbow_delay = 2

client = discord.Client()
colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]

async def rainbowrole(role):
    for role in client.get_guild(rainbow_serverid).roles:
        if str(role) == str(rainbowrolename):
            print("무지개 역할 발견")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("역할을 편집할 수 없습니다. 봇 역할이 무지개 역할 보다 위에 있는지 확인하세요.")
                    pass
                await asyncio.sleep(rainbow_delay)
    print('"' + rainbowrolename +'" 이 이름을 가진 역할을 찾을 수 없습니다.')
    print("역할을 생성합니다...")
    try:
        await client.get_guild(rainbow_serverid).create_role(reason="생성된 무지개 역할", name=rainbowrolename)
        print("역할이 생성되었습니다!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("역할을 생성할 수 없습니다.")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))

@client.event
async def on_ready():
    print("Bot is ready.")
    print(client.user)
    print(client.user.id)
    print("--------------------")

    # 무지개 역할
    # client.loop.create_task(rainbowrole(rainbowrolename))
    # 봇 상태
    await client.change_presence(status=discord.Status.idle)
    # 봇 활동 (type: 0=하는중, 1=트위치 생방송중, 2=듣는중)
    await client.change_presence(activity=discord.Activity(name='Overwatch II', type=1))


@client.event
async def on_message(message):
    # print("{0} | {1} | {2} | {3}".format(message.author, message.guild.name, message.channel.name, message.content))
    badword_list = ['섹스', '느금마', '애미', '애비', '장애인', '느금', '보지', '자지', '니애미']
    badwords = []
    if any(x in message.content for x in badword_list) and message.guild == client.get_guild(677424338877546506):
        for badword in badword_list:
            if badword in message.content:
                badwords.append(badword)

        print(badwords)
        from datetime import datetime
        embed = discord.Embed(
            description="{0}, {1} **채널에서 욕설 사용**".format(message.author.mention, message.channel.mention),
            # description='저를 부를 땐 앞에 "도비야"를 붙여주세요!',
            timestamp=datetime.utcnow(),
            colour=discord.Colour.red()
        )
        embed.set_author(name=message.author,
                         icon_url=message.author.avatar_url)
        embed.add_field(name="제거된 메시지", value=message.content)
        embed.add_field(name="감지된 욕설 ({0})".format(len(badwords)), value=", ".join(str(i) for i in badwords), inline=False)
        embed.set_footer(text="ID: {0}".format(message.author.id))
        await message.delete()
        await client.get_channel(678834899947618326).send(embed=embed)

    # 개인 메시지
    if isinstance(message.channel, discord.DMChannel):
        # 받은 DM을 포스팅할 채널
        channels = [678549751771430932]
        # 받음=빨강, 보냄=파랑
        embed = discord.Embed(description=message.author.mention + " -> " + client.user.mention,
                              colour=discord.Colour.red())
        if message.author == client.user:
            embed = discord.Embed(description=message.author.mention + " -> " + message.channel.recipient.mention,
                                  colour=discord.Colour.blue())

        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        from datetime import datetime
        now = datetime.now()
        now = now.strftime("%Y/%m/%d %I:%M:%S %p")
        embed.add_field(name=now, value=message.content, inline=True)
        embed.set_footer(text="ID: {0}".format(str(message.author.id), now))
        for x in channels:
            await client.get_channel(x).send(embed=embed)

    # 봇 명령어 (관리자 전용)
    admins = [524980170554212363, 252302363052867587, 276689714592088064, 533859758583840779]

    regionals = {'a': '\N{REGIONAL INDICATOR SYMBOL LETTER A}', 'b': '\N{REGIONAL INDICATOR SYMBOL LETTER B}',
                 'c': '\N{REGIONAL INDICATOR SYMBOL LETTER C}',
                 'd': '\N{REGIONAL INDICATOR SYMBOL LETTER D}', 'e': '\N{REGIONAL INDICATOR SYMBOL LETTER E}',
                 'f': '\N{REGIONAL INDICATOR SYMBOL LETTER F}',
                 'g': '\N{REGIONAL INDICATOR SYMBOL LETTER G}', 'h': '\N{REGIONAL INDICATOR SYMBOL LETTER H}',
                 'i': '\N{REGIONAL INDICATOR SYMBOL LETTER I}',
                 'j': '\N{REGIONAL INDICATOR SYMBOL LETTER J}', 'k': '\N{REGIONAL INDICATOR SYMBOL LETTER K}',
                 'l': '\N{REGIONAL INDICATOR SYMBOL LETTER L}',
                 'm': '\N{REGIONAL INDICATOR SYMBOL LETTER M}', 'n': '\N{REGIONAL INDICATOR SYMBOL LETTER N}',
                 'o': '\N{REGIONAL INDICATOR SYMBOL LETTER O}',
                 'p': '\N{REGIONAL INDICATOR SYMBOL LETTER P}', 'q': '\N{REGIONAL INDICATOR SYMBOL LETTER Q}',
                 'r': '\N{REGIONAL INDICATOR SYMBOL LETTER R}',
                 's': '\N{REGIONAL INDICATOR SYMBOL LETTER S}', 't': '\N{REGIONAL INDICATOR SYMBOL LETTER T}',
                 'u': '\N{REGIONAL INDICATOR SYMBOL LETTER U}',
                 'v': '\N{REGIONAL INDICATOR SYMBOL LETTER V}', 'w': '\N{REGIONAL INDICATOR SYMBOL LETTER W}',
                 'x': '\N{REGIONAL INDICATOR SYMBOL LETTER X}',
                 'y': '\N{REGIONAL INDICATOR SYMBOL LETTER Y}', 'z': '\N{REGIONAL INDICATOR SYMBOL LETTER Z}',
                 '0': '0⃣', '1': '1⃣', '2': '2⃣', '3': '3⃣',
                 '4': '4⃣', '5': '5⃣', '6': '6⃣', '7': '7⃣', '8': '8⃣', '9': '9⃣', '!': '\u2757',
                 '?': '\u2753', ' ': ' '}

    if message.author.id in admins and message.author != client.user:

        if message.content.startswith(">>") and message.author != client.user:
            result = ''
            for x in range(2, len(message.content)):
                letter = message.content[x:x + 1].lower()
                if letter in regionals:
                    result = result + regionals[letter] + " "
                    print(result)
            if result != '':
                await message.channel.send(result)

        if message.content.startswith('도비야 말해 '):
            msg = message.content[7:]
            await message.delete()
            await message.channel.send(msg)

        if message.content.startswith('도비야 읽어 '):
            msg = message.content[7:]
            await message.delete()
            await message.channel.send(msg, tts=True)

        if message.content.startswith('-diff'):
            msg = message.content[6:]
            await message.channel.send("```diff\n{0}\n```".format(msg))

    # 봇 명령어 (자유)
    if message.content.startswith("도비야 도와줘"):
        from datetime import datetime
        embed = discord.Embed(
            title='저를 부를 땐 앞에 "도비야"를 붙여주세요!',
            # description='저를 부를 땐 앞에 "도비야"를 붙여주세요!',
            timestamp=datetime.utcnow(),
            colour=discord.Colour.green()
        )
        embed.set_author(name='DoVi Bot Commands', icon_url="https://cdn.discordapp.com/avatars/276689714592088064/0f36e200633c84e1bc137e8f582d238a.png?size=1024")
        # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/276689714592088064/0f36e200633c84e1bc137e8f582d238a.png?size=1024")
        embed.add_field(name="관리자", value="`말해`, `읽어`, `디비전`", inline=False)
        embed.add_field(name="기본", value="`도와줘`, `안녕`, `누구야`, `멤버수`, `관리자`, `영웅추천`, `노래틀어줘`, `고마워`, `로스터`", inline=False)
        embed.add_field(name="검색", value="`유튜브`, `배틀태그`", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("도비야 안녕"):
        await message.channel.send("안녕하세요, {.mention}님 !".format(message.author))

    if message.content.startswith("도비야 누구야 "):
        author = message.author
        if len(message.content[8:]) > 0:
            author = message.mentions[0]
        import datetime
        date = datetime.datetime.utcfromtimestamp(((int(author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(
            description=author.mention,
            colour=discord.Colour.green()
        )
        embed.add_field(name="이름", value=author, inline=True)
        embed.add_field(name="서버닉네임", value=author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",
                        inline=True)
        embed.add_field(name="아이디", value=author.id, inline=True)
        embed.set_thumbnail(url=author.avatar_url)
        await message.channel.send("", embed=embed)

    if message.content.startswith("도비야 노래틀어줘"):
        from datetime import datetime
        date = datetime.now()
        await message.channel.send(";;p 멜론차트 {0}월 {1}일".format(str(date.month), str(date.day)))
        await asyncio.sleep(1)
        # await message.channel.send("인식이 안댕..")
        await message.channel.send("{0} 죄송해요 저는 아직 노래를 틀을수 없어요!!!".format(message.author.mention))

    if message.content.startswith("도비야 고마워"):
        thankmsg = ["헤헿", "^^", " (っ˘ڡ˘ς) ", "{0} 저도 고마워요!".format(message.author.mention), "응"]
        await message.channel.send(random.choice(thankmsg))

    if message.content.startswith("도비야 멤버수"):
        await message.channel.send("현재 `BIZ` 서버에는 `{0}`명이 있어요!".format(message.guild.member_count))

    if message.content.startswith("도비야 관리자"):
        admins_str = ""
        for x in admins:
            admins_str += message.guild.get_member(x).mention + ", "
        await message.channel.send(admins_str + "총 " + str(len(admins)) + "명")

    if message.content.startswith("도비야 영웅추천"):
        all_heroes = ["D.va", "겐지", "둠피스트", "라인하르트", "레킹볼", "로드호그",
                  "루시우", "리퍼", "맥크리", "메르시", "메이", "모이라", "바스티온", "바티스트", "브리기테",
                  "솔저: 76", "솜브라", "시그마", "시메트라", "아나", "애쉬", "오리사", "위도우메이커", "윈스턴",
                  "자리야", "정크랫", "젠야타", "토르비욘", "트레이서", "파라", "한조"]
        tank = ["D.va", "라인하르트", "레킹볼", "로드호그", "시그마", "오리사", "윈스턴", "자리야"]
        damage = ["겐지", "둠피스트", "리퍼", "맥크리", "메이", "바스티온", "솔저: 76", "솜브라", "시메트라", "애쉬", "위도우메이커", "정크랫", "토르비욘", "트레이서", "파라", "한조"]
        support = ["루시우", "메르시", "모이라", "바티스트", "브리기테", "아나", "젠야타"]

        if message.content[9:10] == "탱":
            result = random.choice(tank)
        elif message.content[9:10] == "딜":
            result = random.choice(damage)
        elif message.content[9:10] == "힐":
            result = random.choice(support)
        else:
            result = random.choice(all_heroes)

        await message.channel.send("{0.mention} `{1}` 이 영웅은 어때요?".format(message.author, result))

    if message.content.startswith("도비야 유튜브 "):
        search = message.content[8:]
        query_string = urllib.parse.urlencode({
            'search_query': search
        })
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string
        )
        search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
        randomNum = random.randrange(0, len(search_results))
        print("총 {0}개 검색, {1}번 출력".format(len(search_results), randomNum))
        await message.channel.send('{0}중 {1}\n'.format(len(search_results), randomNum) + 'http://www.youtube.com/watch?v=' + search_results[randomNum])

    if message.content.startswith("도비야 로스터"):
        biz_icon_url = "https://cdn.discordapp.com/icons/677424338877546506/81fbea82cf25ab6a53b12d077ca57b55.webp?size=1024"
        embed = discord.Embed(
            title="[BIZ 오버워치 프로지향팀]",
            # description="자세한건 `Unknown` 채널에서",
            colour=discord.Colour.blue()
        )
        embed.set_footer(text="Updating...", icon_url=biz_icon_url)
        embed.add_field(name="공격 (DPS)", value="```diff\n"
                                                "Update"
                                                "\n```", inline=True)
        embed.add_field(name="돌격 (Tank)", value="```diff\n"
                                                "Update"
                                                "\n```", inline=True)
        embed.add_field(name="지원 (Support)", value="```diff\n"
                                                "Update"
                                                "\n```", inline=True)
        embed.set_thumbnail(url=biz_icon_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("도비야 배틀태그 "):
        tag = message.content[9:]
        battletag = tag.replace("#", "-")
        print(tag + " to " + battletag)
        url = 'https://playoverwatch.com/ko-kr/career/pc/' + battletag
        url = urllib.parse.urlsplit(url)
        url = list(url)
        url[2] = urllib.parse.quote(url[2])
        profile_url = urllib.parse.urlunsplit(url)
        print(profile_url)
        htm_content = urllib.request.urlopen(profile_url).read()
        htm_content = str(htm_content)
        profile_img = re.findall(r'<img class="player-portrait" src="(https://.*?png)"', htm_content)
        if len(profile_img) < 1:
            await message.channel.send("유저를 찾을 수 없습니다. (소대문자를 확인해주세요!)")
            return
        print(htm_content)
        print(profile_url)
        print(profile_img)
        dealtier_img = re.findall(r'<img class="competitive-rank-tier-icon" src="(https://.*?png)"', htm_content)
        dealscore = re.findall(r'<div class="competitive-rank-level">(.*?)</div>', htm_content)
        print(dealscore)
        from datetime import datetime
        embed = discord.Embed(
            description="Searched by {.mention}".format(message.author),
            timestamp=datetime.utcnow(),
            colour=discord.Colour.green()
        )
        embed.set_author(name=tag, icon_url=profile_img[0], url=profile_url)
        if len(dealtier_img) > 1:
            embed.add_field(name="공격", value=dealscore[0])
            embed.set_thumbnail(url=dealtier_img[0])
        else:
            embed.set_thumbnail(url=profile_img[0])
        await message.channel.send("", embed=embed)

    if message.content.startswith("도비야 입장테스트"):
        welcomechannel = client.get_channel(677424338877546509)
        infochannel = client.get_channel(677527130653065248)
        await message.channel.send("{0} 채널에 보내질 메시지입니다.".format(welcomechannel.mention))
        await message.channel.send("🎊 {0}님, 오버워치 프로지향팀 **{1}** 서버에 오신것을 진심으로 환영합니다! 🎊\n공지사항 {2} 꼭 확인해주세요!".format(message.author.mention, message.guild.name, infochannel.mention))

@client.event
async def on_member_join(member):
    welcomechannel = client.get_channel(677424338877546509)
    infochannel = client.get_channel(677527130653065248)
    msg = "🎊 {0}님, 오버워치 프로지향팀 **{1}** 서버에 오신것을 진심으로 환영합니다! 🎊\n공지사항 {2} 꼭 확인해주세요!".format(member.mention, member.guild.name, infochannel.mention)
    await welcomechannel.send(msg)

@client.event
async def on_member_remove(member):
    byechannel = client.get_channel(677424338877546509)
    msg = "👋 잘가요 {0}님, 나중에 또봐요! `ಥ_ಥ`".format(member.mention)
    await byechannel.send(msg)


client.run(access_token)
