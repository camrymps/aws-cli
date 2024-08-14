import click
import json


class DictParamType(click.ParamType):
    name = "string"

    def convert(self, value, param, ctx):
        try:
            return json.loads(value)
        except TypeError:
            self.fail(
                "expected string for dict conversion, got "
                f"{value!r} of type {type(value).__name__}",
                param,
                ctx,
            )
        except ValueError:
            self.fail(f"{value!r} is not a valid dict", param, ctx)


DICT = DictParamType
