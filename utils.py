from collections import OrderedDict
from typing import AnyStr, List


def render_error_response(
    message: AnyStr,
    status_code: int = 400,
) -> OrderedDict:
    return OrderedDict(status_code=status_code, success=False, message=message)


def render_success_response(
    result: List[OrderedDict],
    status_code: int = 200,
) -> OrderedDict:
    return OrderedDict(status_code=status_code, success=True, result=result)


def cleanup_text(text: AnyStr):
    return text.replace('\nView more', '')