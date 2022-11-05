from asyncio import sleep

from pyrogram import Client

# API keys you can find at https://my.telegram.org/apps
API_ID = " your api id"
API_HASH = "your api hash"
CLIENT_NAME = "my_account"

FROM_CHAT = "79999999999"
TO_CHAT = "79888888888"

app = Client(CLIENT_NAME, api_id=API_ID, api_hash=API_HASH)


async def main():
    print(
        "This app will forward all messages from "
        "one chat to another (or to the same) one"
    )
    async with app:
        count = await app.get_chat_history_count(FROM_CHAT)
        print(f"Total count is: {count} messages")

        messages_ids_for_resend = [
            message.id async for message in app.get_chat_history(FROM_CHAT)
        ]
        messages_ids_for_resend = messages_ids_for_resend[::-1]

        offset = 0
        limit = 100

        while True:
            part_of_messages = messages_ids_for_resend[offset: offset + limit]

            if not part_of_messages:
                break

            await app.forward_messages(TO_CHAT, FROM_CHAT, part_of_messages)

            offset += limit

            print(f"Forwarded {offset} messages")
            await sleep(60)  # to avoid API timeout

        print("Success")


app.run(main())
