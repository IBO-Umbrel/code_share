import asyncio


colors = {
    "green": "\x1b[1m\x1b[32m",
    "white": "\x1b[1m\x1b[37m",
    "blue": "\x1b[1m\x1b[34m",
    "orange": "\x1b[33m",
    "red": "\x1b[1m\x1b[31m",
    "yellow": "\x1b[1m\x1b[33m",
};


def reader(filename: str):
    with open(filename) as file:
        return file.readlines()
    

ramadan_txt = reader("C:\\work_space\\Projects\\code_share\\ibrohimjon_toshtemirov\\ramadan_mubarak\\ramadan.txt")
mubarak_txt = reader("C:\\work_space\\Projects\\code_share\\ibrohimjon_toshtemirov\\ramadan_mubarak\\mubarak.txt")


async def run():
    print(colors["green"])
    for line in ramadan_txt:
        await asyncio.sleep(0.1)
        print(line, end="")
    
    print(colors["blue"])
    for line in mubarak_txt:
        await asyncio.sleep(0.1)
        print(line, end="")


asyncio.run(run())