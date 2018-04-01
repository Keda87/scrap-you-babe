from collections import OrderedDict
from typing import AnyStr, List

from requests_html import HTMLSession

from utils import cleanup_text

session = HTMLSession()


def do_scrap_askfm(username: AnyStr) -> List[OrderedDict]:

    def scrap_list_qna(content):
        item_page = content.find('div.item-page', first=True)
        for item in item_page.find('article.item.streamItem.streamItem-answer')[:5]:
            question = item.find('header > h2', first=True).text
            answer = item.find('div.streamItem_content', first=True).text
            answer = cleanup_text(answer)
            info = item.find('div.streamItem_details', first=True).text
            yield OrderedDict(question=question, answer=answer, time_info=info)

    url = f'https://ask.fm/{username}'
    response = session.get(url=url)
    container = response.html.find('div.item-pager', first=True)
    yield from scrap_list_qna(content=container)

def do_scrap_twitter(username: AnyStr) -> dict:
    return {}