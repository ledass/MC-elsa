from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages
import asyncio
from pyrogram.errors import FloodWait

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
# https://t.me/GetTGLink/4178
async def speed_verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Broadcasting your messages...'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    success = 0
    failed = 0
    async for user in users:
        try:
            await b_msg.copy(chat_id=int(user['id']))
            success += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await b_msg.copy(chat_id=int(user['id']))
        except Exception as e:
            failed += 1
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Completed\nTotal : {total_users}\nSuccess : {success}\nFailed : {failed}\nTime Taken : {time_taken}")
       
@Client.on_message(filters.command("ohibroadcast") & filters.user(ADMINS) & filters.reply)
async def users_broadcast(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Broadcasting your users messages...'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"Users broadcast in progress...\n\nTotal Users: <code>{total_users}</code>\nCompleted: <code>{done} / {total_users}</code>\nSuccess: <code>{success}</code>\nBlocked: <code>{blocked}</code>\nDeleted: <code>{deleted}</code>")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Users broadcast completed.\nCompleted in {time_taken} seconds.\n\nTotal Users: <code>{total_users}</code>\nCompleted: <code>{done} / {total_users}</code>\nSuccess: <code>{success}</code>\nBlocked: <code>{blocked}</code>\nDeleted: <code>{deleted}</code>")
