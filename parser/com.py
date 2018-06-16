from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u"\n".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen('https://kaktus.media/doc/375842_vpechatleniia_kaktus.media_ot_poezdki_na_shattl_base_iz_bishkeka_v_aeroport_manas_video.html').read()
print(text_from_html(html))
