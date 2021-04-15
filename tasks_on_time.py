import asyncio
from utils import select_row_in_db
from keyboards.inline.dynamic_keyboards import get_dynamic_keyboard
from loader import bot


async def send_message_from_db():
    event_success_id = await select_row_in_db()
    for ev, suc, ids in event_success_id:
        await bot.send_message(chat_id=433411432, text=f"ты продолжаешь событие - <u>{ev}</u>?",
                               reply_markup=get_dynamic_keyboard(ids))
        await asyncio.sleep(0.5)


loop = asyncio.get_event_loop()
loop.run_until_complete(send_message_from_db())
