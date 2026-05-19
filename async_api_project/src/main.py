import asyncio
import aiohttp
import time
import json
import logging

from services.api_service import fetch
from utils.logger import setup_logger


async def main():
    setup_logger()

    start_time = time.time()
    logging.info("Program started")

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch(session, "users"),
            fetch(session, "posts"),
            fetch(session, "comments"),
            fetch(session, "todos"),
            fetch(session, "albums"),
        ]

        results = await asyncio.gather(*tasks)

    # merge results
    final_data = {}
    for result in results:
        final_data.update(result)

    # save JSON
    with open("../data/output.json", "w") as file:
        json.dump(final_data, file, indent=4)

    end_time = time.time()
    logging.info(f"Execution time: {end_time - start_time:.2f} seconds")
    logging.info("Program finished")

    print("Done. Check data/output.json and logs/app.log")


# run
asyncio.run(main())