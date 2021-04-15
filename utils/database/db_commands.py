import aiosqlite
import asyncio
import os

# path_db = r"D:\motivation_bot\utils\database\event_database.db"
path_db = os.path.join(os.path.dirname(__file__), 'event_database.db')


async def insert_row_to_db(text):
    db = await aiosqlite.connect(path_db)
    await db.execute('INSERT INTO events (event_name) VALUES (?)', (text,))
    await db.commit()
    await db.close()


async def select_row_in_db():
    db = await aiosqlite.connect(path_db)
    cursor = await db.execute('SELECT * FROM events')
    result = [[row[0], row[2], row[3]] for row in await cursor.fetchall()]
    await db.close()
    return result


async def update_row_in_db(person_id: int, flag=True):
    db = await aiosqlite.connect(path_db)
    if flag:
        await db.execute('UPDATE events SET success = success + 1 WHERE person_id = ?', (person_id,))
    else:
        await db.execute('UPDATE events SET success = 0 WHERE person_id = ?', (person_id,))
    await db.commit()
    await db.close()

# async def main():
#     await update_row_in_db(1)
#     return
#
#
# asyncio.run(main())
