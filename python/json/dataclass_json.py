# KEYS=[python json dataclasses]

from dacite import from_dict
import jsonpickle


def json_encode(v) -> str:
    return jsonpickle.encode(v, unpicklable=False)


class JSON:
    def json(self):
        return json_encode(self)

    @classmethod
    def from_json(cls, data):
        return cls.from_dict(jsonpickle.decode(data))

    @classmethod
    def from_dict(cls, data):
        return from_dict(data_class=cls, data=data)
