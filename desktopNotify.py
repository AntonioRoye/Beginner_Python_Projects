import asyncio
from desktop_notifier import DesktopNotifier
import time

notify = DesktopNotifier()

async def main():
    n = await notify.send(title="Hello World!", 
    message="This is my first Python notification. It will be cleared in 5 seconds.")
    time.sleep(5)
    notify.clear(n)
    

asyncio.run(main())

