from src.core.database import SessionLocal
from src.models.token_log import TokenLog

db = SessionLocal()

logs = db.query(TokenLog).all()

for log in logs:
    print(
        log.id,
        log.user_id,
        log.input_tokens,
        log.output_tokens,
        log.total_tokens,
        log.cost
    )

db.close()