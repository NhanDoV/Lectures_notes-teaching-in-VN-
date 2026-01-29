import re
from collections import defaultdict

# ===================== SENTIMENT DICTIONARY =====================
"""
Score-based sentiment dictionary
Score range:
    Positive:  (0, 1]
    Negative:  [-1, 0)
    Neutral:   ~0
"""

SENTIMENT_DICT = {
    'vi_positive': {
        'tốt': 0.6,
        'hay': 0.5,
        'đẹp': 0.5,
        'ngon': 0.5,
        'yêu': 0.8,
        'thích': 0.6,
        'tuyệt': 0.8,
        'hoàn hảo': 1.0,
        'xuất sắc': 0.9,
        'tuyệt vời': 1.0,
        'rất tốt': 0.9,
        'siêu phẩm': 0.8,
        'đỉnh cao': 0.85,
        'hài lòng': 0.6,
        'vui vẻ': 0.5
    },

    'vi_negative': {
        'ngu': -0.6,
        'xấu': -0.5,
        'dở': -0.5,
        'tệ': -0.6,
        'ghét': -0.8,
        'kinh': -0.6,
        'đáng ghét': -0.9,
        'tồi tệ': -0.9,
        'không thích': -0.7,
        'chán': -0.4,
        'buồn': -0.3,
        'thất vọng': -0.7,
        'cặc': -0.95,
        'kém chất lượng': -0.8,

        # profanity / intensity
        'vãi lồn': -1.0,
        'vãi lìn': -0.95,
        'vãi cặc': -1.0,
        'vãi chưởng': -0.8,
        'vãi linh hồn': -0.2,
        'như cặc': -0.99,
        'như con cặc': -0.999,
        'vãi cả cặc': -0.995,        
        'địt mẹ': -1.0
    },

    'vi_neutral': {
        'không': 0.0,
        'có': 0.0,
        'là': 0.0,
        'của': 0.0,
        'trong': 0.0,
        'với': 0.0,
        'được': 0.0
    },

    'en_positive': {
        'good': 0.6,
        'great': 0.8,
        'awesome': 0.9,
        'excellent': 1.0,
        'love': 0.9
    },

    'en_negative': {
        'bad': -0.6,
        'terrible': -0.9,
        'awful': -0.9,
        'hate': -0.8
    },

    'en_neutral': {
        'the': 0.0,
        'is': 0.0,
        'are': 0.0,
        'and': 0.0,
        'or': 0.0
    }
}

# ===================== LANGUAGE =====================

def detect_language(text: str) -> str:
    if re.search(r'[àáạảãâăđêôơư]', text.lower()):
        return 'vi'
    return 'en'

# ===================== KEYWORD EXTRACTION =====================

def extract_keywords(text, sentiment_dict):
    """
        Extract ONLY keywords that exist in sentiment dictionary
        Priority: compound words > unigram
    """
    text = text.lower()
    tokens = []

    # flatten all vocab
    all_vocab = set().union(*sentiment_dict.values())

    # compound words first
    for phrase in all_vocab:
        if ' ' in phrase and phrase in text:
            tokens.append(phrase)

    # remove compound text to avoid double count
    tmp_text = text
    for c in tokens:
        tmp_text = tmp_text.replace(c, '')

    # unigram
    words = re.findall(r'\b[a-zà-ỹ]{2,}\b', tmp_text)
    tokens.extend(words)

    return tokens

# ===================== SENTIMENT =====================

def calculate_sentiment_scores(text):
    lang = detect_language(text)

    dict_pos = SENTIMENT_DICT[f'{lang}_positive']
    dict_neg = SENTIMENT_DICT[f'{lang}_negative']
    dict_neu = SENTIMENT_DICT[f'{lang}_neutral']

    tokens = extract_keywords(
        text,
        {
            'pos': dict_pos,
            'neg': dict_neg,
            'neu': dict_neu
        }
    )

    scores = {'positive': 0.0, 'negative': 0.0, 'neutral': 0.0}
    keyword_hits = defaultdict(list)

    total_magnitude = 0.0

    for token in tokens:
        if token in dict_pos:
            s = dict_pos[token]
            scores['positive'] += s
            keyword_hits['positive'].append((token, s))
            total_magnitude += abs(s)

        elif token in dict_neg:
            s = dict_neg[token]
            scores['negative'] += abs(s)
            keyword_hits['negative'].append((token, s))
            total_magnitude += abs(s)

        elif token in dict_neu:
            s = dict_neu[token]
            scores['neutral'] += 0.01
            keyword_hits['neutral'].append((token, s))
            total_magnitude += 0.01

    # normalize to probability-like distribution
    if total_magnitude > 0:
        for k in scores:
            scores[k] /= total_magnitude
    else:
        scores = {'positive': 0.33, 'negative': 0.33, 'neutral': 0.34}

    return scores, keyword_hits, lang

# ===================== TOP KEYWORDS =====================

def get_top_keywords(keyword_hits, top_n=5):
    """
        Sort keywords by absolute sentiment score
    """
    result = {}
    for cat, kws in keyword_hits.items():
        result[cat] = sorted(
            kws,
            key = lambda x: abs(x[1]),
            reverse = True
        )[:top_n]
    return result

# ==================== COLOR UTILS =============================
def generate_shades(base_color, n):
    """
        Generate n shades from dark -> light of a base hex color
    """
    import matplotlib.colors as mcolors
    base = mcolors.to_rgb(base_color)
    shades = []
    for i in range(n):
        factor = 0.3 + 0.7 * (1 - i / max(1, n - 1))  # Đảo: đầu tối, cuối sáng
        shades.append(mcolors.to_hex([c * factor for c in base]))
    return shades
