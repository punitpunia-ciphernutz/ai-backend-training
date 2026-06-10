from sqlalchemy.orm import Session
from src.core.logger import logger
from src.models.token_log import TokenLog

INPUT_TOKEN_PRICE = 0.0
OUTPUT_TOKEN_PRICE = 0.0

def calculate_cost(
    input_tokens: int,
    output_tokens: int
):

    input_cost = (
        input_tokens
        * INPUT_TOKEN_PRICE
    )

    output_cost = (
        output_tokens
        * OUTPUT_TOKEN_PRICE
    )

    return input_cost + output_cost

def save_token_usage(
    db: Session,
    user_id: int,
    usage: dict
):

    input_tokens = usage.get(
        "input_tokens",
        0
    )

    output_tokens = usage.get(
        "output_tokens",
        0
    )

    total_tokens = usage.get(
        "total_tokens",
        0
    )

    cost = calculate_cost(
        input_tokens,
        output_tokens
    )

    log = TokenLog(
        user_id=user_id,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        cost=cost
    )

    db.add(log)
    db.commit()
    logger.info(
    f"Token usage user_id={user_id} "
    f"input={input_tokens} "
    f"output={output_tokens} "
    f"total={total_tokens}"
)

    return log