class script(object):
    START_TXT = """𝖧i {}, <b>𝖭𝗂𝖼𝖾 𝗍𝗈 𝗆𝖾𝖾𝗍 𝗒𝗈𝗎 🙌</b>
ɪ'ᴍ ᴊᴜsᴛ ᴀ sɪᴍᴘʟᴇ ᴘʀᴇ-ғᴜɴᴄᴛɪᴏɴᴇᴅ ᴀᴜᴛᴏғɪʟᴛᴇʀ ʙᴏᴛ.
ɪᴛs ᴇᴀsʏ ᴛᴏ ᴜsᴇ ᴍᴇ ; ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ"""

    ABOUT_TXT = """<b>‣ My Name : {}
‣ Dᴇᴠᴏʟᴏᴘᴇʀ: <a href='https://t.me/TGxIRFAN'>𝐀𝐒 𝐓𝐆</a>
‣ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
‣ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
‣ DᴀᴛᴀBᴀsᴇ : <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>"""


    STATUS_TXT = """<b>➥ ᴛᴏᴛᴀʟ ғɪʟᴇs: <code>{}</code>
➥ ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code>
➥ ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code>
➥ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code>
➥ ғʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code></b>"""
    
    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""
    
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""
    
    CAPTION = """
<code>{file_name}</code>"""

    IMDB_TEMPLATE_TXT = """
<b>𝐇𝐞𝐲 {message.from_user.mention}, 𝐇𝐞𝐫𝐞 𝐢𝐬 𝐭𝐡𝐞 𝐫𝐞𝐬𝐮𝐥𝐭 𝐟𝐨𝐫 𝐲𝐨𝐮𝐫 {query}

🏷 𝐓𝐢𝐭𝐥𝐞 : {title}
🎭 𝐆𝐞𝐧𝐫𝐞𝐬 : {genres}
🌟 𝐑𝐚𝐭𝐢𝐧𝐠 : {rating}
🎛 𝐂𝐨𝐮𝐧𝐭𝐫𝐢𝐞𝐬 : {countries}

𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 {message.chat.title}</b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""
    
    QINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Uncharted

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""
