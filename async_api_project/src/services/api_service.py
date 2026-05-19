import aiohttp
import logging

BASE_URL = "https://jsonplaceholder.typicode.com"


async def fetch(session, endpoint):
    url = f"{BASE_URL}/{endpoint}"
    logging.info(f"Starting request: {endpoint}")

    try:
        async with session.get(url) as response:
            if response.status != 200:
                logging.error(f"{endpoint} failed: {response.status}")
                return {endpoint: "Error"}

            data = await response.json()
            logging.info(f"Success: {endpoint}")
            return {endpoint: data[:2]}

    except Exception as e:
        logging.error(f"{endpoint} exception: {str(e)}")
        return {endpoint: "Failed"}
