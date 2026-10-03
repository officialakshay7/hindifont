/*! HindiFont.co.in — Kruti Dev 010 / DevLys 010 <-> Unicode converter (v1)
 * Handles: glyph mapping (longest match), pre-base ि (f) reordering,
 * reph र् (Z) repositioning, half-form + stem (k) joins, nukta (+).
 */
(function (root) {
  'use strict';
  var CONS = '\u0915-\u0939\u0958-\u095F';
  var MATRA = '\u093E-\u094C\u0901-\u0903\u0962\u0963';
  var REPH = '\u0001', SUBR = '\u0002';

  // Kruti Dev 010 glyph -> Unicode. Order does not matter (longest match is used).
  var KD = {
    // independent vowels
    'v\u201A': 'ऑ', 'vks': 'ओ', 'vkS': 'औ', 'vk': 'आ', 'v': 'अ',
    'bZ': 'ई', 'Ã': 'ई', 'b': 'इ', 'm': 'उ', 'Å': 'ऊ', ',s': 'ऐ', ',': 'ए', '_': 'ऋ',
    // matras & signs
    '\u201A': 'ॉ', 'ks': 'ो', 'kS': 'ौ', 'k': 'ा', 'h': 'ी', 'q': 'ु', 'w': 'ू', '`': 'ृ',
    'f': 'ि', 's': 'े', 'S': 'ै', 'a': 'ं', '¡': 'ँ', '%': 'ः', 'W': 'ॅ', '~': '्', '+': '़', '·': 'ऽ',
    // consonants: full / half
    'd': 'क', 'D': 'क्', 'Dk': 'क', '[k': 'ख', '[': 'ख्', 'x': 'ग', 'X': 'ग्', 'Xk': 'ग',
    '?k': 'घ', '?': 'घ्', '³': 'ङ', 'p': 'च', 'P': 'च्', 'Pk': 'च', 'N': 'छ',
    't': 'ज', 'T': 'ज्', 'Tk': 'ज', '>': 'झ', '÷': 'झ्', '¥': 'ञ',
    'V': 'ट', 'B': 'ठ', 'M': 'ड', '<': 'ढ', '.k': 'ण', '.': 'ण्',
    'r': 'त', 'R': 'त्', 'Rk': 'त', 'Fk': 'थ', 'F': 'थ्', 'n': 'द', '/k': 'ध', '/': 'ध्',
    'u': 'न', 'U': 'न्', 'Uk': 'न', 'i': 'प', 'I': 'प्', 'Ik': 'प', 'Q': 'फ', '¶': 'फ्',
    'c': 'ब', 'C': 'ब्', 'Ck': 'ब', 'Hk': 'भ', 'H': 'भ्', 'e': 'म', 'E': 'म्', 'Ek': 'म',
    ';': 'य', '¸': 'य्', 'j': 'र', 'y': 'ल', 'Y': 'ल्', 'Yk': 'ल', 'G': 'ळ',
    'o': 'व', 'O': 'व्', 'Ok': 'व', "'k": 'श', "'": 'श्', '"k': 'ष', '"': 'ष्',
    'l': 'स', 'L': 'स्', 'Lk': 'स', 'g': 'ह',
    // conjuncts & ligatures
    '{k': 'क्ष', '{': 'क्ष्', '=': 'त्र', '«': 'त्र्', 'K': 'ज्ञ', 'J': 'श्र', 'Ø': 'क्र',
    'Ùk': 'त्त', 'Ù': 'त्त्', 'ä': 'क्त', '–': 'दृ', '—': 'कृ', 'é': 'न्न', 'í': 'द्द',
    '|': 'द्य', '}': 'द्व', ')': 'द्ध', 'æ': 'द्र', 'ç': 'प्र', '#': 'रु', ':': 'रू',
    'ê': 'ट्ट', 'ë': 'ट्ठ', 'ì': 'ड्ड', 'ï': 'ड्ढ',
    'à': 'ह्न', 'á': 'ह्य', 'â': 'हृ', 'ã': 'ह्म', 'º': 'ह्', 'z': SUBR, 'ª': SUBR,
    'Z': REPH,
    // punctuation & digits
    'A': '।', '-': '.', '&': '-', ']': ',', '¼': '(', '½': ')', '\\': '?', '@': '/', 'ñ': '॰',
    'å': '०', 'ƒ': '१', '„': '२', '…': '३', '†': '४', '‡': '५', 'ˆ': '६', '‰': '७', 'Š': '८', '‹': '९'
  };

  // Unicode -> Kruti Dev (preferred typing forms)
  var UK = {
    'ऑ': 'v\u201A', 'ओ': 'vks', 'औ': 'vkS', 'आ': 'vk', 'अ': 'v', 'ई': 'bZ', 'इ': 'b', 'उ': 'm',
    'ऊ': 'Å', 'ऐ': ',s', 'ए': ',', 'ऋ': '_',
    'ॉ': '\u201A', 'ो': 'ks', 'ौ': 'kS', 'ा': 'k', 'ि': 'f', 'ी': 'h', 'ु': 'q', 'ू': 'w', 'ृ': '`',
    'े': 's', 'ै': 'S', 'ं': 'a', 'ँ': '¡', 'ः': '%', 'ॅ': 'W', '्': '~', '़': '+', 'ऽ': '·',
    'क': 'd', 'क्': 'D', 'ख': '[k', 'ख्': '[', 'ग': 'x', 'ग्': 'X', 'घ': '?k', 'घ्': '?', 'ङ': '³',
    'च': 'p', 'च्': 'P', 'छ': 'N', 'ज': 't', 'ज्': 'T', 'झ': '>', 'झ्': '÷', 'ञ': '¥',
    'ट': 'V', 'ठ': 'B', 'ड': 'M', 'ढ': '<', 'ण': '.k', 'ण्': '.',
    'त': 'r', 'त्': 'R', 'थ': 'Fk', 'थ्': 'F', 'द': 'n', 'ध': '/k', 'ध्': '/', 'न': 'u', 'न्': 'U',
    'प': 'i', 'प्': 'I', 'फ': 'Q', 'फ्': '¶', 'ब': 'c', 'ब्': 'C', 'भ': 'Hk', 'भ्': 'H', 'म': 'e', 'म्': 'E',
    'य': ';', 'य्': '¸', 'र': 'j', 'ल': 'y', 'ल्': 'Y', 'ळ': 'G', 'व': 'o', 'व्': 'O',
    'श': "'k", 'श्': "'", 'ष': '"k', 'ष्': '"', 'स': 'l', 'स्': 'L', 'ह': 'g',
    'क़': 'd+', 'ख़': '[k+', 'ग़': 'x+', 'ज़': 't+', 'ड़': 'M+', 'ढ़': '<+', 'फ़': 'Q+', 'य़': ';+',
    'क्ष': '{k', 'क्ष्': '{', 'त्र': '=', 'त्र्': '«', 'ज्ञ': 'K', 'श्र': 'J',
    'त्त': 'Ùk', 'त्त्': 'Ù', 'क्त': 'ä', 'दृ': '–', 'कृ': '—', 'न्न': 'é', 'द्द': 'í',
    'द्य': '|', 'द्व': '}', 'द्ध': ')', 'रु': '#', 'रू': ':',
    'ट्ट': 'ê', 'ट्ठ': 'ë', 'ड्ड': 'ì', 'ड्ढ': 'ï', 'ह्न': 'à', 'ह्य': 'á', 'हृ': 'â', 'ह्म': 'ã',
    // subscript र (placeholder SUBR = '्र')
    'द\u0002': 'æ', 'ट\u0002': 'Vª', 'ठ\u0002': 'Bª', 'ड\u0002': 'Mª', 'ढ\u0002': '<ª', 'छ\u0002': 'Nª',
    'ह\u0002': 'ºz', 'त\u0002': '=', 'त\u0002्': '«', 'श\u0002': 'J', '\u0002': 'z',
    '।': 'A', '॥': 'AA', '.': '-', ',': ']', '-': '&', '(': '¼', ')': '½', '?': '\\', '/': '@', '॰': 'ñ',
    '०': 'å', '१': 'ƒ', '२': '„', '३': '…', '४': '†', '५': '‡', '६': 'ˆ', '७': '‰', '८': 'Š', '९': '‹'
  };

  function compile(map) {
    var keys = Object.keys(map), max = 0;
    for (var i = 0; i < keys.length; i++) if (keys[i].length > max) max = keys[i].length;
    return { map: map, max: max };
  }
  var KDC = compile(KD), UKC = compile(UK);

  function scan(text, c) {
    var out = '', i = 0, n = text.length;
    while (i < n) {
      var hit = false;
      for (var len = Math.min(c.max, n - i); len > 0; len--) {
        var chunk = text.substr(i, len);
        if (Object.prototype.hasOwnProperty.call(c.map, chunk)) { out += c.map[chunk]; i += len; hit = true; break; }
      }
      if (!hit) { out += text.charAt(i); i++; }
    }
    return out;
  }

  var reCluster = '(?:[' + CONS + ']\u093C?\u094D)*[' + CONS + ']\u093C?';

  function toUnicode(text) {
    if (!text) return '';
    // normalise smart quotes (Word autocorrect breaks श/ष in DevLys/Kruti text)
    text = text.replace(/[\u2018\u2019]/g, "'").replace(/[\u201C\u201D]/g, '"');
    var s = scan(text, KDC);
    s = s.replace(/\u094D\u093E/g, '');                       // half form + stem = full consonant
    s = s.replace(new RegExp('\u0002', 'g'), '\u094D\u0930'); // subscript र
    s = s.replace(new RegExp('\u093F(' + reCluster + ')', 'g'), '$1\u093F');           // pre-base ि
    s = s.replace(new RegExp('(' + reCluster + ')([' + MATRA + ']*)\u0001', 'g'), '\u0930\u094D$1$2'); // reph
    s = s.replace(/\u0001/g, '\u0930\u094D');                  // stray reph
    s = s.replace(/\u093E\u0947/g, '\u094B').replace(/\u093E\u0948/g, '\u094C'); // ा+े=ो, ा+ै=ौ
    s = s.replace(/\u0905\u093E/g, '\u0906');                  // अ+ा = आ
    return s.normalize ? s.normalize('NFC') : s;
  }

  function fromUnicode(text) {
    if (!text) return '';
    var s = text.normalize ? text.normalize('NFC') : text;
    // decompose precomposed nukta letters so the table matches consistently
    s = s.replace(/\u0958/g, 'क़').replace(/\u0959/g, 'ख़').replace(/\u095A/g, 'ग़')
         .replace(/\u095B/g, 'ज़').replace(/\u095C/g, 'ड़').replace(/\u095D/g, 'ढ़')
         .replace(/\u095E/g, 'फ़').replace(/\u095F/g, 'य़');
    // reph: र् + cluster + matras  ->  cluster + matras + Z
    s = s.replace(new RegExp('\u0930\u094D(' + reCluster + ')([' + MATRA + ']*)', 'g'), '$1$2\u0001');
    // subscript र (्र) -> placeholder
    s = s.replace(/\u094D\u0930/g, '\u0002');
    // pre-base ि moves before its cluster
    s = s.replace(new RegExp('(' + reCluster + '\u0002?)\u093F', 'g'), '\u093F$1');
    var out = scan(s, UKC);
    return out.replace(/\u0001/g, 'Z');
  }

  root.HFLegacy = { toUnicode: toUnicode, fromUnicode: fromUnicode };
  if (typeof module !== 'undefined' && module.exports) module.exports = root.HFLegacy;
})(typeof window !== 'undefined' ? window : globalThis);
