import asyncio
import random
import string

from api.v1.database import QuestionCrud

personality = ['open', 'conscientious', 'extraverted', 'agreeable', 'neurotic']

async def rand():
    for _ in range(100):
        await QuestionCrud.create({
            'content': "".join(random.choices(string.ascii_letters, k=10)),
            'personality': random.choice(personality)
        })

asyncio.run(rand())
