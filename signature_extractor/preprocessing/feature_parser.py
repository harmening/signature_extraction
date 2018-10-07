# -*- coding: UTF-8 -*-
import re
import nltk


def contains_email(text):
    o = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    return len(o) > 0


def has_only_quotes(text):
    o = re.findall(r'^[\s]*---*[\s]*$', text)
    return len(o) > 0


def contains_phone(text):
    o = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
    return len(o) > 0


def count_named_entities(text):
    entities_count = 0
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                entities_count += 1

    if entities_count > 0:
        return entities_count
    return False


def is_in_last_five_lines(text, line):
    try:
        lines = text.split('\n')
        lines = [l.strip() for l in lines if len(l) > 0]
        line_index = max([i for i, l in enumerate(lines) if line in l])
        output = True if len(lines) - 6 < line_index else False
    except:
        output = False
    return output


def is_in_second_part(text, line):
    all_num = len(text)
    _50per = (50 * all_num) // 100
    idx = text.rfind(line)

    if idx > -1 and all_num - _50per <= idx:
        return True
    return False


def contains_signature_word(text):
    o = re.findall(
        "Dept\.|University|Corp\.|Corporations?|College|Ave\.|Laboratory|[D|d]isclaimer| Division|"
        "Professor|Laboratories|Institutes?|Services|Engineering|Director|Doctor|President|Sciences?| Address|"
        "Manager|Street|St\.|Avenue",
        text)
    return len(o) > 0


def is_under_closing_phrase(text, line):
    regex_closing_phrase = """Best|Cordially yours|Fond regards|In appreciation|In sympathy|Kind regards|Kind thanks|Kind wishes|
    Many thanks|Regards|Respectfully|Respectfully yours|Sincerely|Sincerely yours|Thanks|Thank you|
    Thank you for your assistance in this matter|Thank you for your consideration|Thank you for your recommendation|
    Thank you for your time|Warm regards|Warm wishes|Warmly|With appreciation|With deepest sympathy|With gratitude|
    With sincere thanks|With sympathy|Your help is greatly
     appreciated|Yours cordially|Yours faithfully|Yours sincerely|Yours truly"""

    o = re.findall(regex_closing_phrase, text)
    found_phrases = [m.end(0) for m in re.finditer(regex_closing_phrase, text)]
    signature_closing_end_idx = max(found_phrases) if len(list(found_phrases)) > 0 else -1
    line_idx = text.find(line)
    return signature_closing_end_idx < line_idx


def has_url(text):
    url_regex = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop
    |info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|
    be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|
    do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|
    hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|
    me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|
    pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|
    tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|
    \([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?
    «»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|
    name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|
    bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|
    fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|
    ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|
    my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|
    si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|
    vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""
    o = re.findall(url_regex, text)
    return len(o) > 0
