from sqlalchemy.orm import Session

from data_store.engine import engine
from data_store.schema import LocaleBronzeSchema


def seed_locales():
    with Session(engine) as session:
        # Check if already seeded
        if session.query(LocaleBronzeSchema).count() > 0:
            return

        # Seed with some common locales
        session.add_all(
            [
                LocaleBronzeSchema(
                    locale="en-US",
                    language="en",
                    region="US",
                    script="Latn",
                    source_name="seed",
                ),
                LocaleBronzeSchema(
                    locale="en-GB",
                    language="en",
                    region="GB",
                    script="Latn",
                    source_name="seed",
                ),
                LocaleBronzeSchema(
                    locale="fr-FR",
                    language="fr",
                    region="FR",
                    script="Latn",
                    source_name="seed",
                ),
                LocaleBronzeSchema(
                    locale="es-ES",
                    language="es",
                    region="ES",
                    script="Latn",
                    source_name="seed",
                ),
                LocaleBronzeSchema(
                    locale="el-GR",
                    language="el",
                    region="GR",
                    script="Cyrl",
                    source_name="seed",
                ),
                LocaleBronzeSchema(
                    locale="zh-CN",
                    language="zh",
                    region="CN",
                    script="Hans",
                    source_name="seed",
                ),
                LocaleBronzeSchema(
                    locale="ko-KR",
                    language="ko",
                    region="KR",
                    script="Hang",
                    source_name="seed",
                ),
            ]
        )
        session.commit()
