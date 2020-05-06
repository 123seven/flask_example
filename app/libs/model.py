# @Time    : 2020-04-30 11:03
# @Author  : Seven
# @File    : model.py
# @Desc    : BaseModel
from contextlib import contextmanager
from datetime import datetime

import orjson
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import inspect, Column, Integer, orm


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


db = SQLAlchemy(session_options={'autocommit': True})


class BaseModel(db.Model):
    __abstract__ = True
    create_time = Column(Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def insert(self):
        self._before_insert()
        self.try_to_add_ip()
        self.try_to_add_device_info()
        db.session.add(self)
        db.session.flush()
        self._after_insert()
        return self

    def update(self):
        self._before_update()
        db.session.merge(self)
        db.session.flush()
        self._after_update()
        return self

    def delete(self):
        self._before_delete()
        db.session.delete(self)
        db.session.flush()
        self._after_delete()

    def _before_insert(self):
        pass

    def _after_insert(self):
        pass

    def _before_update(self):
        pass

    def _after_update(self):
        pass

    def _before_delete(self):
        pass

    def _after_delete(self):
        pass

    @classmethod
    def load_all_data_field(cls):
        """
        获取类自身所有数据表映射字段名
        :return:
        """
        if hasattr(cls, '__table__'):
            return [c.name for c in cls.__table__.columns]

    def update_from_json(self, json_str):
        """
        接受json_str更新原本信息
        """
        json_obj = orjson.loads(json_str)
        self.__dict__.update(**json_obj)

    def __repr__(self):
        return self.to_json

    @property
    def to_json(self):
        return orjson.dumps(self)

    def save(self):
        if self.id:
            self.update()
        else:
            self.insert()


class MixinJSONSerializer:

    def __init__(self):
        self.__exclude = []
        self.__fields = []

    @orm.reconstructor
    def init_on_load(self):
        self.__prune_fields()

    def __prune_fields(self):
        columns = inspect(self.__class__).columns
        if not self._fields:
            all_columns = set(columns.keys())
            self._fields = list(all_columns - set(self.__exclude))

    def hide(self, *args):
        for key in args:
            self._fields.remove(key)
        return self

    def keys(self):
        return self.__fields

    def __getitem__(self, key):
        return getattr(self, key)
