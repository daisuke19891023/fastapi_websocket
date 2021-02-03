# mixins.py

from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)
dotenv_path = os.path.join(os.path.abspath(__file__), '.env')
load_dotenv(dotenv_path)
MODE = os.environ.get('MODE')


class TimestampMixin(object):
    created_at = Column(Timestamp, nullable=False,
                        server_default=text('current_timestamp'))
    # os.environ["IS_TEST"] = "hoge"
    mysql_logic = 'current_timestamp on update current_timestamp' if MODE != "TEST" else 'current_timestamp'
    updated_at = Column(Timestamp, nullable=False,
                        server_default=text(mysql_logic))
