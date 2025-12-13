import time

from sqlalchemy import text
from data_store.connection import engine

with engine.connect() as conn:
    start = time.time()
    result = conn.execute(text("SELECT * FROM bronze.countries"))
    print(result.all())
    print((time.time() - start) * 1e3, "ms")

# with engine.connect() as connection:
#     stmt = insert(CountryBronze).values(
#         name="Testland",
#         iso_alpha_2="TL",
#         iso_alpha_3="TST",
#         iso_num="999",
#         source_name="manual-entry",
#     )
#     connection.execute(stmt)
#     connection.commit()
