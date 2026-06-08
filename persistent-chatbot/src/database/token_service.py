from src.database.db import SessionLocal
from src.database.models import TokenLog

def save_token_usage(input_tokens, output_tokens, total_tokens, cost):

    db = SessionLocal()

    token_log = TokenLog(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        cost=cost
    )

    db.add(token_log)
    db.commit()
    db.close()