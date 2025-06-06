uni2latex = {
0x0022: "''",                                    # character "
0x0023: r'\#',                                   # character #
0x0024: r'\$',                                   # character $
0x0025: r'\%',                                   # character %
0x0026: r'\&',                                   # character &
0x003C: r'\ensuremath{<}',                       # <
0x003E: r'\ensuremath{>}',                       # >
0x005C: r'\textbackslash',                       # the \ character itself
0x005E: r'\textasciicircum',                     # character ^
0x005F: r'\_',                                   # character _
0x007B: r'\{',                                   # character {
0x007D: r'\}',                                   # character }
0x007E: r'\textasciitilde',                      # character ~
0x00A0: r'~',                                    # character NO-BREAK SPACE
0x00A1: r'\textexclamdown',                      # character ¡
0x00A2: r'\textcent',                            # character ¢
0x00A3: r'\textsterling',                        # character £
0x00A4: r'\textcurrency',                        # character ¤
0x00A5: r'\textyen',                             # character ¥
0x00A6: r'\textbrokenbar',                       # character ¦
0x00A7: r'\textsection',                         # character §
0x00A8: r'\textasciidieresis',                   # character ¨
0x00A9: r'\textcopyright',                       # character ©
0x00AA: r'\textordfeminine',                     # character ª
0x00AB: r'\guillemotleft',                       # character «
0x00AC: r'\textlnot',                            # character ¬
0x00AD: r'\-',                                   # SOFT HYPHEN [­]
0x00AE: r'\textregistered',                      # character ®
0x00AF: r'\textasciimacron',                     # character ¯
0x00B0: r'\textdegree',                          # character °
0x00B1: r'\ensuremath{\pm}',                     # character ±
0x00B2: r'\texttwosuperior',                     # character ²
0x00B3: r'\textthreesuperior',                   # character ³
0x00B4: r'\textasciiacute',                      # character ´
0x00B5: r'\textmu',                              # character µ
0x00B6: r'\textparagraph',                       # character ¶
0x00B7: r'\textperiodcentered',                  # character ·
0x00B9: r'\textonesuperior',                     # character ¹
0x00BA: r'\textordmasculine',                    # character º
0x00BB: r'\guillemotright',                      # character »
0x00BC: r'\textonequarter',                      # character ¼
0x00BD: r'\textonehalf',                         # character ½
0x00BE: r'\textthreequarters',                   # character ¾
0x00BF: r'\textquestiondown',                    # character ¿
0x00C0: r'\`A',                                  # character À
0x00C1: "\\'A",                                  # character Á
0x00C2: r'\^A',                                  # character Â
0x00C3: r'\~A',                                  # character Ã
0x00C4: r'\"A',                                  # character Ä
0x00C5: r'\r{A}',                                # character Å
0x00C6: r'\AE',                                  # character Æ
0x00C7: r'\c{C}',                                # character Ç
0x00C8: r'\`E',                                  # character È
0x00C9: "\\'E",                                  # character É
0x00CA: r'\^E',                                  # character Ê
0x00CB: r'\"E',                                  # character Ë
0x00CC: r'\`I',                                  # character Ì
0x00CD: "\\'I",                                  # character Í
0x00CE: r'\^I',                                  # character Î
0x00CF: r'\"I',                                  # character Ï
0x00D0: r'\DH',                                  # character Ð
0x00D1: r'\~N',                                  # character Ñ
0x00D2: r'\`O',                                  # character Ò
0x00D3: "\\'O",                                  # character Ó
0x00D4: r'\^O',                                  # character Ô
0x00D5: r'\~O',                                  # character Õ
0x00D6: r'\"O',                                  # character Ö
0x00D7: r'\texttimes',                           # character ×
0x00D8: r'\O',                                   # character Ø
0x00D9: r'\`U',                                  # character Ù
0x00DA: "\\'U",                                  # character Ú
0x00DB: r'\^U',                                  # character Û
0x00DC: r'\"U',                                  # character Ü
0x00DD: "\\'Y",                                  # character Ý
0x00DE: r'\TH',                                  # character Þ
0x00DF: r'\ss',                                  # character ß
0x00E0: r'\`a',                                  # character à
0x00E1: "\\'a",                                  # character á
0x00E2: r'\^a',                                  # character â
0x00E3: r'\~a',                                  # character ã
0x00E4: r'\"a',                                  # character ä
0x00E5: r'\r{a}',                                # character å
0x00E6: r'\ae',                                  # character æ
0x00E7: r'\c{c}',                                # character ç
0x00E8: r'\`e',                                  # character è
0x00E9: "\\'e",                                  # character é
0x00EA: r'\^e',                                  # character ê
0x00EB: r'\"e',                                  # character ë
0x00EC: r'\`\i',                                 # character ì
0x00ED: "\\'\\i",                                # character í
0x00EE: r'\^\i',                                 # character î
0x00EF: r'\"\i',                                 # character ï
0x00F0: r'\dh',                                  # character ð
0x00F1: r'\~n',                                  # character ñ
0x00F2: r'\`o',                                  # character ò
0x00F3: "\\'o",                                  # character ó
0x00F4: r'\^o',                                  # character ô
0x00F5: r'\~o',                                  # character õ
0x00F6: r'\"o',                                  # character ö
0x00F7: r'\textdiv',                             # character ÷
0x00F8: r'\o',                                   # character ø
0x00F9: r'\`u',                                  # character ù
0x00FA: "\\'u",                                  # character ú
0x00FB: r'\^u',                                  # character û
0x00FC: r'\"u',                                  # character ü
0x00FD: "\\'y",                                  # character ý
0x00FE: r'\th',                                  # character þ
0x00FF: r'\"y',                                  # character ÿ
0x0100: r'\={A}',
0x0101: r'\={a}',
0x0102: r'\u{A}',
0x0103: r'\u{a}',
0x0104: r'\k{A}',
0x0105: r'\k{a}',
0x0106: "\\'C",
0x0107: "\\'c",
0x0108: r'\^{C}',
0x0109: r'\^{c}',
0x010A: r'\.{C}',
0x010B: r'\.{c}',
0x010C: r'\v{C}',
0x010D: r'\v{c}',
0x010E: r'\v{D}',
0x010F: r'\v{d}',
0x0110: r'\DJ',
0x0111: r'\dj',
0x0112: r'\={E}',
0x0113: r'\={e}',
0x0114: r'\u{E}',
0x0115: r'\u{e}',
0x0116: r'\.{E}',
0x0117: r'\.{e}',
0x0118: r'\k{E}',
0x0119: r'\k{e}',
0x011A: r'\v{E}',
0x011B: r'\v{e}',
0x011C: r'\^{G}',
0x011D: r'\^{g}',
0x011E: r'\u{G}',
0x011F: r'\u{g}',
0x0120: r'\.{G}',
0x0121: r'\.{g}',
0x0122: r'\c{G}',
0x0123: r'\c{g}',
0x0124: r'\^{H}',
0x0125: r'\^{h}',
0x0126: r'\={H}',
0x0127: r'\={h}',
0x0128: r'\~{I}',
0x0129: r'\~{i}',
0x012A: r'\={I}',
0x012B: r'\={i}',
0x012C: r'\u{I}',
0x012D: r'\u{i}',
0x012E: r'\k{I}',
0x012F: r'\k{i}',
0x0130: r'\.I',
0x0131: r'\i',
0x0132: r'\IJ',
0x0133: r'\ij',
0x0134: r'\^{J}',
0x0135: r'\^{j}',
0x0136: r'\c{K}',
0x0137: r'\c{k}',
0x0138: r'\textsc{k}',
0x0139: "\\'L",
0x013A: "\\'l",
0x013B: r'\c{L}',
0x013C: r'\c{l}',
0x013D: r'\v{L}',
0x013E: r'\v{l}',
0x013F: r'\.{L}',
0x0140: r'\.{l}',
0x0141: r'\L',
0x0142: r'\l',
0x0143: "\\'N",
0x0144: "\\'n",
0x0145: r'\c{N}',
0x0146: r'\c{n}',
0x0147: r'\v{N}',
0x0148: r'\v{n}',
0x0149: r'\nument{149}',
0x014A: r'\NG',
0x014B: r'\ng',
0x014C: r'\={O}',
0x014D: r'\={o}',
0x014E: r'\u{O}',
0x014F: r'\u{o}',
0x0150: r'\H{O}',
0x0151: r'\H{o}',
0x0152: r'\OE',
0x0153: r'\oe',
0x0154: "\\'R",
0x0155: "\\'r",
0x0156: r'\c{R}',
0x0157: r'\c{r}',
0x0158: r'\v{R}',
0x0159: r'\v{r}',
0x015A: "\\'S",
0x015B: "\\'s",
0x015C: r'\^{S}',
0x015D: r'\^{s}',
0x015E: r'\c{S}',
0x015F: r'\c{s}',
0x0160: r'\v{S}',
0x0161: r'\v{s}',
0x0162: r'\c{T}',
0x0163: r'\c{t}',
0x0164: r'\v{T}',
0x0165: r'\v{t}',
0x0166: r'\={T}',
0x0167: r'\={t}',
0x0168: r'\~{U}',
0x0169: r'\~{u}',
0x016A: r'\={U}',
0x016B: r'\={u}',
0x016C: r'\u{U}',
0x016D: r'\u{u}',
0x016E: r'\r{U}',
0x016F: r'\r{u}',
0x0170: "\\'{U}",
0x0171: "\\'{u}",
0x0172: r'\k{U}',
0x0173: r'\k{u}',
0x0174: r'\^{W}',
0x0175: r'\^{w}',
0x0176: r'\^{Y}',
0x0177: r'\^{y}',
0x0178: r'\"Y',
0x0179: "\\'Z",
0x017A: "\\'z",
0x017B: r'\.Z',
0x017C: r'\.z',
0x017D: r'\v{Z}',
0x017E: r'\v{z}',
0x0192: r'\textflorin',                          # 0x0192
0x0195: r'\texthvlig',                            # LATIN SMALL LETTER HV [ƕ]
0x019E: r'\textnrleg',                            # LATIN SMALL LETTER N WITH LONG RIGHT LEG [ƞ]
0x01F5: r"\'{g}",                                 # LATIN SMALL LETTER G WITH ACUTE [ǵ]


0x0228: r'\c{E}',
0x0229: r'\c{e}',

# chars in linguistics, thanks @roedoejet (https://github.com/roedoejet/pylatexenc)
0x0259: r'\textschwa',
0x025B: r'\varepsilon',                           # LATIN SMALL LETTER OPEN E [ɛ]
0x0278: r'\textphi',                              # LATIN SMALL LETTER PHI [ɸ]
0x0294: r'\textglotstop',
0x029E: r'\textturnk',                            # LATIN SMALL LETTER TURNED K [ʞ]
0x02B7: r'\textsuperscript{w}',

0x02C6: r'\textasciicircum',                     # 0x02C6
0x02C7: r'\textasciicaron',
0x02D8: r'\textasciibreve',
0x02D9: r'\textperiodcentered',                   # DOT ABOVE [˙]
0x02DA: r'\r{}',                                  # RING ABOVE [˚]
0x02DB: r'\k{}',                                  # OGONEK [˛]
0x02DC: r'\textasciitilde',
0x02DD: r'\textacutedbl',                        # 0x02DD


# ---------------------

0x02BC: "'",                                     # MODIFIER LETTER APOSTROPHE

# Combining Diacritical Marks (!!TODO!! smarter)
0x0307: r'\ensuremath{\dot{}}',
0x0308: r'\ensuremath{\ddot{}}',

0x0386: "\\'{}A",                                 # GREEK CAPITAL LETTER ALPHA WITH TONOS [Ά]
0x0388: "\\'{}E",                                 # GREEK CAPITAL LETTER EPSILON WITH TONOS [Έ]
0x0389: "\\'{}H",                                 # GREEK CAPITAL LETTER ETA WITH TONOS [Ή]
0x038A: "\\'{}I",                               # GREEK CAPITAL LETTER IOTA WITH TONOS [Ί]
0x038C: "\\'{}O",                                 # GREEK CAPITAL LETTER OMICRON WITH TONOS [Ό]
0x038E: "\\'{}Y",                                 # GREEK CAPITAL LETTER UPSILON WITH TONOS [Ύ]
0x038F: "\\'{}\\ensuremath{\\Omega}",             # GREEK CAPITAL LETTER OMEGA WITH TONOS [Ώ]
0x0390: r'\acute{\ddot{\iota}}',                  # GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS [ΐ]
0x0391: r'A',                                    # GREEK CAPITAL LETTER ALPHA
0x0392: r'B',                                    # GREEK CAPITAL LETTER BETA
0x0393: r'\ensuremath{\Gamma}',                  # GREEK CAPITAL LETTER GAMMA
0x0394: r'\ensuremath{\Delta}',                  # ...
0x0395: r'E',
0x0396: r'Z',
0x0397: r'H',
0x0398: r'\ensuremath{\Theta}',
0x0399: r'I',
0x039A: r'K',
0x039B: r'\ensuremath{\Lambda}',
0x039C: r'M',
0x039D: r'N',
0x039E: r'\ensuremath{\Xi}',
0x039F: r'O',
0x03A0: r'\ensuremath{\Pi}',
0x03A1: r'P',
0x03A3: r'\ensuremath{\Sigma}',
0x03A4: r'T',
0x03A5: r'\ensuremath{\Upsilon}',
0x03A6: r'\ensuremath{\Phi}',
0x03A7: r'X',
0x03A8: r'\ensuremath{\Psi}',
0x03A9: r'\ensuremath{\Omega}',
# tonos letters [ ... ]
0x03AA: r'\ensuremath{\ddot{I}}',                 # GREEK CAPITAL LETTER IOTA WITH DIALYTIKA [Ϊ]
0x03AB: r'\ensuremath{\ddot{Y}}',                 # GREEK CAPITAL LETTER UPSILON WITH DIALYTIKA [Ϋ]
0x03AC: r"\ensuremath{\acute\alpha}",             # GREEK SMALL LETTER ALPHA WITH TONOS [ά]
0x03AD: r"\ensuremath{\acute\epsilon}",           # GREEK SMALL LETTER EPSILON WITH TONOS [έ]
0x03AE: r"\ensuremath{\acute\eta}",               # GREEK SMALL LETTER ETA WITH TONOS [ή]
0x03AF: r"\ensuremath{\acute\iota}",              # GREEK SMALL LETTER IOTA WITH TONOS [ί]
0x03B0: r'\ensuremath{\acute{\ddot{\upsilon}}}',  # GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS [ΰ]
0x03CA: r'\ensuremath{\ddot\iota}',               # GREEK SMALL LETTER IOTA WITH DIALYTIKA [ϊ]
0x03CB: r'\ensuremath{\ddot{\upsilon}}',          # GREEK SMALL LETTER UPSILON WITH DIALYTIKA [ϋ]
0x03CC: r"\'{o}",                                 # GREEK SMALL LETTER OMICRON WITH TONOS [ό]
0x03CD: r"\ensuremath{\acute\upsilon}",           # GREEK SMALL LETTER UPSILON WITH TONOS [ύ]
0x03CE: r"\ensuremath{\acute\omega}",             # GREEK SMALL LETTER OMEGA WITH TONOS [ώ]

0x03B1: r'\ensuremath{\alpha}',                  # Greek Small Letter Alpha
0x03B2: r'\ensuremath{\beta}',
0x03B3: r'\ensuremath{\gamma}',
0x03B4: r'\ensuremath{\delta}',
0x03B5: r'\ensuremath{\varepsilon}',
0x03B6: r'\ensuremath{\zeta}',
0x03B7: r'\ensuremath{\eta}',
0x03B8: r'\ensuremath{\theta}',
0x03B9: r'\ensuremath{\iota}',
0x03BA: r'\ensuremath{\kappa}',
0x03BB: r'\ensuremath{\lambda}',
0x03BC: r'\ensuremath{\mu}',
0x03BD: r'\ensuremath{\nu}',
0x03BE: r'\ensuremath{\xi}',
0x03BF: r'o',
0x03C0: r'\ensuremath{\pi}',
0x03C1: r'\ensuremath{\rho}',
0x03C2: r'\ensuremath{\varsigma}',
0x03C3: r'\ensuremath{\sigma}',
0x03C4: r'\ensuremath{\tau}',
0x03C5: r'\ensuremath{\upsilon}',
0x03C6: r'\ensuremath{\varphi}',
0x03C7: r'\ensuremath{\chi}',
0x03C8: r'\ensuremath{\psi}',
0x03C9: r'\ensuremath{\omega}',

0x03D1: r'\ensuremath{\vartheta}',                # GREEK THETA SYMBOL [ϑ]
0x03D2: r'\Upsilon',                              # GREEK UPSILON WITH HOOK SYMBOL [ϒ]
0x03D5: r'\ensuremath{\phi}',                     # GREEK PHI SYMBOL [ϕ]
0x03D6: r'\ensuremath{\varpi}',                   # GREEK PI SYMBOL [ϖ]
0x03F0: r'\ensuremath{\varkappa}',                # GREEK KAPPA SYMBOL [ϰ]
0x03F1: r'\ensuremath{\varrho}',                  # GREEK RHO SYMBOL [ϱ]
0x03F5: r'\ensuremath{\epsilon}',                 # GREEK LUNATE EPSILON SYMBOL [ϵ]
0x03F6: r'\ensuremath{\backepsilon}',             # GREEK REVERSED LUNATE EPSILON SYMBOL [϶]


# 0x0400: r'\`\CYRE',                              # 0x0400
# 0x0401: r'\CYRYO',
# 0x0402: r'\CYRDJE',
# 0x0403: r'\`\CYRG',
# 0x0404: r'\CYRIE',
# 0x0405: r'\CYRDZE',
# 0x0406: r'\CYRII',
# 0x0407: r'\CYRYI',
# 0x0408: r'\CYRJE',
# 0x0409: r'\CYRLJE',
# 0x040A: r'\CYRNJE',
# 0x040B: r'\CYRTSHE',
# 0x040C: r'\`\CYRK',
# 0x040D: r'\`\CYRI',
# 0x040E: r'\CYRUSHRT',
# 0x040F: r'\CYRDZHE',
# 0x0410: r'\CYRA',
# 0x0411: r'\CYRB',
# 0x0412: r'\CYRV',
# 0x0413: r'\CYRG',
# 0x0414: r'\CYRD',
# 0x0415: r'\CYRE',
# 0x0416: r'\CYRZH',
# 0x0417: r'\CYRZ',
# 0x0418: r'\CYRI',
# 0x0419: r'\CYRISHRT',
# 0x041A: r'\CYRK',
# 0x041B: r'\CYRL',
# 0x041C: r'\CYRM',
# 0x041D: r'\CYRN',
# 0x041E: r'\CYRO',
# 0x041F: r'\CYRP',
# 0x0420: r'\CYRR',
# 0x0421: r'\CYRS',
# 0x0422: r'\CYRT',
# 0x0423: r'\CYRU',
# 0x0424: r'\CYRF',
# 0x0425: r'\CYRH',
# 0x0426: r'\CYRC',
# 0x0427: r'\CYRCH',
# 0x0428: r'\CYRSH',
# 0x0429: r'\CYRSHCH',
# 0x042A: r'\CYRHRDSN',
# 0x042B: r'\CYRERY',
# 0x042C: r'\CYRSFTSN',
# 0x042D: r'\CYREREV',
# 0x042E: r'\CYRYU',
# 0x042F: r'\CYRYA',
# 0x0430: r'\cyra',
# 0x0431: r'\cyrb',
# 0x0432: r'\cyrv',
# 0x0433: r'\cyrg',
# 0x0434: r'\cyrd',
# 0x0435: r'\cyre',
# 0x0436: r'\cyrzh',
# 0x0437: r'\cyrz',
# 0x0438: r'\cyri',
# 0x0439: r'\cyrishrt',
# 0x043A: r'\cyrk',
# 0x043B: r'\cyrl',
# 0x043C: r'\cyrm',
# 0x043D: r'\cyrn',
# 0x043E: r'\cyro',
# 0x043F: r'\cyrp',
# 0x0440: r'\cyrr',
# 0x0441: r'\cyrs',
# 0x0442: r'\cyrt',
# 0x0443: r'\cyru',
# 0x0444: r'\cyrf',
# 0x0445: r'\cyrh',
# 0x0446: r'\cyrc',
# 0x0447: r'\cyrch',
# 0x0448: r'\cyrsh',
# 0x0449: r'\cyrshch',
# 0x044A: r'\cyrhrdsn',
# 0x044B: r'\cyrery',
# 0x044C: r'\cyrsftsn',
# 0x044D: r'\cyrerev',
# 0x044E: r'\cyryu',
# 0x044F: r'\cyrya',
# 0x0450: r'\`\cyre',
# 0x0451: r'\cyryo',
# 0x0452: r'\cyrdje',
# 0x0453: r'\`\cyrg',
# 0x0454: r'\cyrie',
# 0x0455: r'\cyrdze',
# 0x0456: r'\cyrii',
# 0x0457: r'\cyryi',
# 0x0458: r'\cyrje',
# 0x0459: r'\cyrlje',
# 0x045A: r'\cyrnje',
# 0x045B: r'\cyrtshe',
# 0x045C: r'\`\cyrk',
# 0x045D: r'\`\cyri',
# 0x045E: r'\cyrushrt',
# 0x045F: r'\cyrdzhe',
# 0x0460: r'\cyrchar\CYROMEGA',                     # CYRILLIC CAPITAL LETTER OMEGA [Ѡ]
# 0x0461: r'\cyrchar\cyromega',                     # CYRILLIC SMALL LETTER OMEGA [ѡ]
# 0x0462: r'\CYRYAT',
# 0x0463: r'\cyryat',
# 0x0464: r'\cyrchar\CYRIOTE',                      # CYRILLIC CAPITAL LETTER IOTIFIED E [Ѥ]
# 0x0465: r'\cyrchar\cyriote',                      # CYRILLIC SMALL LETTER IOTIFIED E [ѥ]
# 0x0466: r'\cyrchar\CYRLYUS',                      # CYRILLIC CAPITAL LETTER LITTLE YUS [Ѧ]
# 0x0467: r'\cyrchar\cyrlyus',                      # CYRILLIC SMALL LETTER LITTLE YUS [ѧ]
# 0x0468: r'\cyrchar\CYRIOTLYUS',                   # CYRILLIC CAPITAL LETTER IOTIFIED LITTLE YUS [Ѩ]
# 0x0469: r'\cyrchar\cyriotlyus',                   # CYRILLIC SMALL LETTER IOTIFIED LITTLE YUS [ѩ]
# 0x046A: r'\CYRBYUS',
# 0x046B: r'\cyrbyus',
# 0x046C: r'\cyrchar\CYRIOTBYUS',                   # CYRILLIC CAPITAL LETTER IOTIFIED BIG YUS [Ѭ]
# 0x046D: r'\cyrchar\cyriotbyus',                   # CYRILLIC SMALL LETTER IOTIFIED BIG YUS [ѭ]
# 0x046E: r'\cyrchar\CYRKSI',                       # CYRILLIC CAPITAL LETTER KSI [Ѯ]
# 0x046F: r'\cyrchar\cyrksi',                       # CYRILLIC SMALL LETTER KSI [ѯ]
# 0x0470: r'\cyrchar\CYRPSI',                       # CYRILLIC CAPITAL LETTER PSI [Ѱ]
# 0x0471: r'\cyrchar\cyrpsi',                       # CYRILLIC SMALL LETTER PSI [ѱ]
# 0x0472: r'\CYRFITA',
# 0x0473: r'\cyrfita',
# 0x0474: r'\CYRIZH',
# 0x0475: r'\cyrizh',
# 0x0476: r'\C\CYRIZH',
# 0x0477: r'\C\cyrizh',
# 0x0478: r'\cyrchar\CYRUK',                        # CYRILLIC CAPITAL LETTER UK [Ѹ]
# 0x0479: r'\cyrchar\cyruk',                        # CYRILLIC SMALL LETTER UK [ѹ]
# 0x047A: r'\cyrchar\CYROMEGARND',                  # CYRILLIC CAPITAL LETTER ROUND OMEGA [Ѻ]
# 0x047B: r'\cyrchar\cyromegarnd',                  # CYRILLIC SMALL LETTER ROUND OMEGA [ѻ]
# 0x047C: r'\cyrchar\CYROMEGATITLO',                # CYRILLIC CAPITAL LETTER OMEGA WITH TITLO [Ѽ]
# 0x047D: r'\cyrchar\cyromegatitlo',                # CYRILLIC SMALL LETTER OMEGA WITH TITLO [ѽ]
# 0x047E: r'\cyrchar\CYROT',                        # CYRILLIC CAPITAL LETTER OT [Ѿ]
# 0x047F: r'\cyrchar\cyrot',                        # CYRILLIC SMALL LETTER OT [ѿ]
# 0x0480: r'\cyrchar\CYRKOPPA',                     # CYRILLIC CAPITAL LETTER KOPPA [Ҁ]
# 0x0481: r'\cyrchar\cyrkoppa',                     # CYRILLIC SMALL LETTER KOPPA [ҁ]
# 0x0482: r'\cyrchar\cyrthousands',                 # CYRILLIC THOUSANDS SIGN [҂]
# 0x0488: r'\cyrchar\cyrhundredthousands',          # COMBINING CYRILLIC HUNDRED THOUSANDS SIGN [҈]
# 0x0489: r'\cyrchar\cyrmillions',                  # COMBINING CYRILLIC MILLIONS SIGN [҉]
# 0x048C: r'\CYRSEMISFTSN',
# 0x048D: r'\cyrsemisftsn',
# 0x048E: r'\CYRRTICK',
# 0x048F: r'\cyrrtick',
# 0x0490: r'\CYRGUP',
# 0x0491: r'\cyrgup',
# 0x0492: r'\CYRGHCRS',
# 0x0493: r'\cyrghcrs',
# 0x0494: r'\CYRGHK',
# 0x0495: r'\cyrghk',
# 0x0496: r'\CYRZHDSC',
# 0x0497: r'\cyrzhdsc',
# 0x0498: r'\CYRZDSC',
# 0x0499: r'\cyrzdsc',
# 0x049A: r'\CYRKDSC',
# 0x049B: r'\cyrkdsc',
# 0x049C: r'\CYRKVCRS',
# 0x049D: r'\cyrkvcrs',
# 0x049E: r'\CYRKHCRS',
# 0x049F: r'\cyrkhcrs',
# 0x04A0: r'\CYRKBEAK',
# 0x04A1: r'\cyrkbeak',
# 0x04A2: r'\CYRNDSC',
# 0x04A3: r'\cyrndsc',
# 0x04A4: r'\CYRNG',
# 0x04A5: r'\cyrng',
# 0x04A6: r'\CYRPHK',
# 0x04A7: r'\cyrphk',
# 0x04A8: r'\CYRABHHA',
# 0x04A9: r'\cyrabhha',
# 0x04AA: r'\CYRSDSC',
# 0x04AB: r'\cyrsdsc',
# 0x04AC: r'\CYRTDSC',
# 0x04AD: r'\cyrtdsc',
# 0x04AE: r'\CYRY',
# 0x04AF: r'\cyry',
# 0x04B0: r'\CYRYHCRS',
# 0x04B1: r'\cyryhcrs',
# 0x04B2: r'\CYRHDSC',
# 0x04B3: r'\cyrhdsc',
# 0x04B4: r'\CYRTETSE',
# 0x04B5: r'\cyrtetse',
# 0x04B6: r'\CYRCHRDSC',
# 0x04B7: r'\cyrchrdsc',
# 0x04B8: r'\CYRCHVCRS',
# 0x04B9: r'\cyrchvcrs',
# 0x04BA: r'\CYRSHHA',
# 0x04BB: r'\cyrshha',
# 0x04BC: r'\CYRABHCH',
# 0x04BD: r'\cyrabhch',
# 0x04BE: r'\CYRABHCHDSC',
# 0x04BF: r'\cyrabhchdsc',
# 0x04C0: r'\CYRpalochka',
# 0x04C1: r'\U\CYRZH',
# 0x04C2: r'\U\cyrzh',
# 0x04C3: r'\CYRKHK',
# 0x04C4: r'\cyrkhk',
# 0x04C5: r'\CYRLDSC',
# 0x04C6: r'\cyrldsc',
# 0x04C7: r'\CYRNHK',
# 0x04C8: r'\cyrnhk',
# 0x04CB: r'\CYRCHLDSC',
# 0x04CC: r'\cyrchldsc',
# 0x04CD: r'\CYRMDSC',
# 0x04CE: r'\cyrmdsc',
# 0x04D0: r'\U\CYRA',
# 0x04D1: r'\U\cyra',
# 0x04D2: r'\"\CYRA',
# 0x04D3: r'\"\cyra',
# 0x04D4: r'\CYRAE',
# 0x04D5: r'\cyrae',
# 0x04D6: r'\U\CYRE',
# 0x04D7: r'\U\cyre',
# 0x04D8: r'\CYRSCHWA',
# 0x04D9: r'\cyrschwa',
# 0x04DA: r'\"\CYRSCHWA',
# 0x04DB: r'\"\cyrschwa',
# 0x04DC: r'\"\CYRZH',
# 0x04DD: r'\"\cyrzh',
# 0x04DE: r'\"\CYRZ',
# 0x04DF: r'\"\cyrz',
# 0x04E0: r'\CYRABHDZE',
# 0x04E1: r'\cyrabhdze',
# 0x04E2: r'\=\CYRI',
# 0x04E3: r'\=\cyri',
# 0x04E4: r'\"\CYRI',
# 0x04E5: r'\"\cyri',
# 0x04E6: r'\"\CYRO',
# 0x04E7: r'\"\cyro',
# 0x04E8: r'\CYROTLD',
# 0x04E9: r'\cyrotld',
# 0x04EC: r'\"\CYREREV',
# 0x04ED: r'\"\cyrerev',
# 0x04EE: r'\=\CYRU',
# 0x04EF: r'\=\cyru',
# 0x04F0: r'\"\CYRU',
# 0x04F1: r'\"\cyru',
# 0x04F2: r'\H\CYRU',
# 0x04F3: r'\H\cyru',
# 0x04F4: r'\"\CYRCH',
# 0x04F5: r'\"\cyrch',
# 0x04F6: r'\CYRGDSC',
# 0x04F7: r'\cyrgdsc',
# 0x04F8: r'\"\CYRERY',
# 0x04F9: r'\"\cyrery',
# 0x04FA: r'\CYRGDSCHCRS',
# 0x04FB: r'\cyrgdschcrs',
# 0x04FC: r'\CYRHHK',
# 0x04FD: r'\cyrhhk',
# 0x04FE: r'\CYRHHCRS',
# 0x04FF: r'\cyrhhcrs',                            # 0x04FF


0x0E3F: r'\textbaht',


# spaces
0x2000: r'\enskip',                              # EN QUAD (= EN SPACE U+2002)
0x2001: r'\quad',                                # EM QUAD (= EM SPACE U+2003)
0x2002: r'\enskip',                              # EN SPACE
0x2003: r'\quad',                                # EM SPACE
0x2004: r'\hspace{0.33em}',                      # THREE-PER-EM SPACE
0x2005: r'\hspace{0.25em}',                      # FOUR-PER-EM SPACE
0x2006: r'\hspace{0.167em}',                     # SIX-PER-EM SPACE
0x2007: r'~',                                    # FIGURE SPACE
0x2008: r'\;',                                   # PUNCTUATION SPACE
0x2009: r'\,',                                   # thin space
0x200A: r'\hspace{1pt}',                         # supposed to be thinnest typographical space available

0x200C: r'\textcompwordmark',                    # ZERO WIDTH NON-JOINER

0x2010: r'-',                                    # HYPHEN
0x2011: r'\nobreakdash-',                        # NON-BREAKING HYPHEN, https://tex.stackexchange.com/a/330437/32188
0x2012: r'-',                                    # FIGURE DASH
0x2013: r'\textendash',                          # 0x2013
0x2014: r'\textemdash',
0x2015: r'\textemdash',                          # HORIZONTAL BAR
0x2016: r'\ensuremath{\Vert}',
0x2018: r'\textquoteleft',
0x2019: r'\textquoteright',
0x201A: r'\quotesinglbase',                      # 0x201A
0x201C: r'\textquotedblleft',
0x201D: r'\textquotedblright',
0x201E: r'\quotedblbase',
0x2020: r'\textdagger',
0x2021: r'\textdaggerdbl',
0x2022: r'\textbullet',
0x2024: r'.',                                     # ONE DOT LEADER [․]
0x2025: r'..',                                    # TWO DOT LEADER [‥]
0x2026: r'\textellipsis',
0x2030: r'\textperthousand',
0x2031: r'\textpertenthousand',
0x2032: "'",                                      # PRIME [′]
0x2033: "''",                                     # DOUBLE PRIME [″]
0x2034: "'''",                                    # TRIPLE PRIME [‴]
0x2035: r'\ensuremath{\backprime}',               # REVERSED PRIME [‵]
0x2039: r'\guilsinglleft',
0x203A: r'\guilsinglright',
0x203B: r'\textreferencemark',
0x203D: r'\textinterrobang',
0x2044: r'\textfractionsolidus',
0x204E: r'\textasteriskcentered',
0x2052: r'\textdiscount',                        # 0x2052
0x2057: "''''",                                   # QUADRUPLE PRIME [⁗]

0x205F: r'\hspace{0.22em}',                             # MEDIUM MATHEMATICAL SPACE [ ]
0x2060: r'\nolinebreak',                          # WORD JOINER [⁠]
0x2061: r'',                                     # FUNCTION APPLICATION

0x20A1: r'\textcolonmonetary',                   # 0x20A1
0x20A4: r'\textlira',
0x20A6: r'\textnaira',
0x20A9: r'\textwon',
0x20AB: r'\textdong',
0x20AC: r'\texteuro',
0x20B1: r'\textpeso',                            # 0x20B1


# letter-like symbols
0x2102: r'\ensuremath{\mathbb{C}}',              # DOUBLE-STRUCK CAPITAL C
0x2103: r'\textcelsius',                         # DEGREE CELSIUS
0x2109: r'\ensuremath{^\circ}F',                 # DEGREE FARENHEIT
0x210A: r'\ensuremath{g}',                       # SCRIPT SMALL G
0x210B: r'\ensuremath{\mathscr{H}}',             # SCRIPT CAPITAL H
0x210C: r'\ensuremath{\mathfrak{H}}',            # BLACK-LETTER CAPITAL H
0x210D: r'\ensuremath{\mathbb{H}}',              # DOUBLE-STRUCK CAPITAL H
0x210E: r'\ensuremath{h}',                       # PLANCK CONSTANT
0x210F: r'\ensuremath{\hbar}',                   # h bar, PLANCK CONSTANT OVER TWO PI
0x2110: r'\ensuremath{\mathscr{I}}',             # SCRIPT CAPITAL I
0x2111: r'\ensuremath{\mathfrak{I}}',            # BLACK-LETTER CAPITAL I
0x2112: r'\ensuremath{\mathscr{L}}',             # SCRIPT CAPITAL L
0x2113: r'\ensuremath{\ell}',                    # SCRIPT SMALL L
0x2115: r'\ensuremath{\mathbb{N}}',              # DOUBLE-STRUCK CAPITAL N
0x2116: r'\textnumero',                          # NUMERO SIGN
0x2117: r'\textcircledP',                        # SOUND RECORDING COPYRIGHT
0x2118: r'\ensuremath{\wp}',                     # SCRIPT CAPITAL P [℘]
0x211E: r'\textrecipe',                          # PRESCRIPTION TAKE
0x2119: r'\ensuremath{\mathbb{P}}',              # DOUBLE-STRUCK CAPITAL P
0x211A: r'\ensuremath{\mathbb{Q}}',              # DOUBLE-STRUCK CAPITAL Q
0x211B: r'\ensuremath{\mathscr{R}}',             # SCRIPT CAPITAL R
0x211C: r'\ensuremath{\mathfrak{R}}',            # BLACK-LETTER CAPITAL R
0x211D: r'\ensuremath{\mathbb{R}}',              # DOUBLE-STRUCK CAPITAL R
0x2120: r'\textservicemark',                     # SERVICE MARK
0x2122: r'\texttrademark',                       # TRADE MARK SIGN
0x2124: r'\ensuremath{\mathbb{Z}}',              # DOUBLE-STRUCK CAPITAL Z
0x2126: r'\textohm',                             # OHM SIGN
0x2127: r'\textmho',                             # OHM SIGN
0x2128: r'\ensuremath{\mathfrak{Z}}',            # BLACK-LETTER CAPITAL Z
0x212A: r'K',                                    # KELVIN SIGN
0x212B: r'\r{A}',                                # ANGSTROM SIGN
0x212C: r'\ensuremath{\mathscr{B}}',             # SCRIPT CAPITAL B
0x212D: r'\ensuremath{\mathfrak{C}}',            # BLACK-LETTER CAPITAL C
0x212E: r'\textestimated',                       # ESTIMATED SYMBOL
0x212F: r'\ensuremath{e}',                       # SCRIPT SMALL E
0x2130: r'\ensuremath{\mathscr{E}}',             # SCRIPT CAPITAL E
0x2131: r'\ensuremath{\mathscr{F}}',             # SCRIPT CAPITAL F
0x2133: r'\ensuremath{\mathscr{M}}',             # SCRIPT CAPITAL M
0x2134: r'\ensuremath{o}',                       # SCRIPT SMALL O
0x2135: r'\ensuremath{\aleph}',                  # ALEF SYMBOL
0x2136: r'\ensuremath{\beth}',                    # BET SYMBOL [ℶ]
0x2137: r'\ensuremath{\gimel}',                   # GIMEL SYMBOL [ℷ]
0x2138: r'\ensuremath{\daleth}',                  # DALET SYMBOL [ℸ]

0x2153: r'\textfrac{1}{3}',                       # VULGAR FRACTION ONE THIRD [⅓]
0x2154: r'\textfrac{2}{3}',                       # VULGAR FRACTION TWO THIRDS [⅔]
0x2155: r'\textfrac{1}{5}',                       # VULGAR FRACTION ONE FIFTH [⅕]
0x2156: r'\textfrac{2}{5}',                       # VULGAR FRACTION TWO FIFTHS [⅖]
0x2157: r'\textfrac{3}{5}',                       # VULGAR FRACTION THREE FIFTHS [⅗]
0x2158: r'\textfrac{4}{5}',                       # VULGAR FRACTION FOUR FIFTHS [⅘]
0x2159: r'\textfrac{1}{6}',                       # VULGAR FRACTION ONE SIXTH [⅙]
0x215A: r'\textfrac{5}{6}',                       # VULGAR FRACTION FIVE SIXTHS [⅚]
0x215B: r'\textfrac{1}{8}',                       # VULGAR FRACTION ONE EIGHTH [⅛]
0x215C: r'\textfrac{3}{8}',                       # VULGAR FRACTION THREE EIGHTHS [⅜]
0x215D: r'\textfrac{5}{8}',                       # VULGAR FRACTION FIVE EIGHTHS [⅝]
0x215E: r'\textfrac{7}{8}',                       # VULGAR FRACTION SEVEN EIGHTHS [⅞]

0x2190: r'\textleftarrow',                       # 0x2190
0x2191: r'\textuparrow',
0x2192: r'\textrightarrow',
0x2193: r'\textdownarrow',                       # 0x2193
0x2194: r'\ensuremath{\leftrightarrow}',          # LEFT RIGHT ARROW [↔]
0x2195: r'\ensuremath{\updownarrow}',                         # UP DOWN ARROW [↕]
0x2196: r'\ensuremath{\nwarrow}',                             # NORTH WEST ARROW [↖]
0x2197: r'\ensuremath{\nearrow}',                             # NORTH EAST ARROW [↗]
0x2198: r'\ensuremath{\searrow}',                             # SOUTH EAST ARROW [↘]
0x2199: r'\ensuremath{\swarrow}',                             # SOUTH WEST ARROW [↙]
0x219A: r'\ensuremath{\nleftarrow}',                          # LEFTWARDS ARROW WITH STROKE [↚]
0x219B: r'\ensuremath{\nrightarrow}',                         # RIGHTWARDS ARROW WITH STROKE [↛]
0x219C: r'\ensuremath{\arrowwaveleft}',                       # LEFTWARDS WAVE ARROW [↜]
0x219D: r'\ensuremath{\arrowwaveright}',                      # RIGHTWARDS WAVE ARROW [↝]
0x219E: r'\ensuremath{\twoheadleftarrow}',                    # LEFTWARDS TWO HEADED ARROW [↞]
0x21A0: r'\ensuremath{\twoheadrightarrow}',                   # RIGHTWARDS TWO HEADED ARROW [↠]
0x21A2: r'\ensuremath{\leftarrowtail}',                       # LEFTWARDS ARROW WITH TAIL [↢]
0x21A3: r'\ensuremath{\rightarrowtail}',                      # RIGHTWARDS ARROW WITH TAIL [↣]
0x21A6: r'\ensuremath{\mapsto}',                              # RIGHTWARDS ARROW FROM BAR [↦]
0x21A9: r'\ensuremath{\hookleftarrow}',                       # LEFTWARDS ARROW WITH HOOK [↩]
0x21AA: r'\ensuremath{\hookrightarrow}',                      # RIGHTWARDS ARROW WITH HOOK [↪]
0x21AB: r'\ensuremath{\looparrowleft}',                       # LEFTWARDS ARROW WITH LOOP [↫]
0x21AC: r'\ensuremath{\looparrowright}',                      # RIGHTWARDS ARROW WITH LOOP [↬]
0x21AD: r'\ensuremath{\leftrightsquigarrow}',                 # LEFT RIGHT WAVE ARROW [↭]
0x21AE: r'\ensuremath{\nleftrightarrow}',                     # LEFT RIGHT ARROW WITH STROKE [↮]
0x21B0: r'\ensuremath{\Lsh}',                                 # UPWARDS ARROW WITH TIP LEFTWARDS [↰]
0x21B1: r'\ensuremath{\Rsh}',                                 # UPWARDS ARROW WITH TIP RIGHTWARDS [↱]
0x21B6: r'\ensuremath{\curvearrowleft}',                      # ANTICLOCKWISE TOP SEMICIRCLE ARROW [↶]
0x21B7: r'\ensuremath{\curvearrowright}',                     # CLOCKWISE TOP SEMICIRCLE ARROW [↷]
0x21BA: r'\ensuremath{\circlearrowleft}',                     # ANTICLOCKWISE OPEN CIRCLE ARROW [↺]
0x21BB: r'\ensuremath{\circlearrowright}',                    # CLOCKWISE OPEN CIRCLE ARROW [↻]
0x21BC: r'\ensuremath{\leftharpoonup}',                       # LEFTWARDS HARPOON WITH BARB UPWARDS [↼]
0x21BD: r'\ensuremath{\leftharpoondown}',                     # LEFTWARDS HARPOON WITH BARB DOWNWARDS [↽]
0x21BE: r'\ensuremath{\upharpoonright}',                      # UPWARDS HARPOON WITH BARB RIGHTWARDS [↾]
0x21BF: r'\ensuremath{\upharpoonleft}',                       # UPWARDS HARPOON WITH BARB LEFTWARDS [↿]
0x21C0: r'\ensuremath{\rightharpoonup}',                      # RIGHTWARDS HARPOON WITH BARB UPWARDS [⇀]
0x21C1: r'\ensuremath{\rightharpoondown}',                    # RIGHTWARDS HARPOON WITH BARB DOWNWARDS [⇁]
0x21C2: r'\ensuremath{\downharpoonright}',                    # DOWNWARDS HARPOON WITH BARB RIGHTWARDS [⇂]
0x21C3: r'\ensuremath{\downharpoonleft}',                     # DOWNWARDS HARPOON WITH BARB LEFTWARDS [⇃]
0x21C4: r'\ensuremath{\rightleftarrows}',                     # RIGHTWARDS ARROW OVER LEFTWARDS ARROW [⇄]
0x21C5: r'\ensuremath{\dblarrowupdown}',                      # UPWARDS ARROW LEFTWARDS OF DOWNWARDS ARROW [⇅]
0x21C6: r'\ensuremath{\leftrightarrows}',                     # LEFTWARDS ARROW OVER RIGHTWARDS ARROW [⇆]
0x21C7: r'\ensuremath{\leftleftarrows}',                      # LEFTWARDS PAIRED ARROWS [⇇]
0x21C8: r'\ensuremath{\upuparrows}',                          # UPWARDS PAIRED ARROWS [⇈]
0x21C9: r'\ensuremath{\rightrightarrows}',                    # RIGHTWARDS PAIRED ARROWS [⇉]
0x21CA: r'\ensuremath{\downdownarrows}',                      # DOWNWARDS PAIRED ARROWS [⇊]
0x21CB: r'\ensuremath{\leftrightharpoons}',                   # LEFTWARDS HARPOON OVER RIGHTWARDS HARPOON [⇋]
0x21CC: r'\ensuremath{\rightleftharpoons}',                   # RIGHTWARDS HARPOON OVER LEFTWARDS HARPOON [⇌]
0x21CD: r'\ensuremath{\nLeftarrow}',                          # LEFTWARDS DOUBLE ARROW WITH STROKE [⇍]
0x21CE: r'\ensuremath{\nLeftrightarrow}',                     # LEFT RIGHT DOUBLE ARROW WITH STROKE [⇎]
0x21CF: r'\ensuremath{\nRightarrow}',                         # RIGHTWARDS DOUBLE ARROW WITH STROKE [⇏]
0x21D0: r'\ensuremath{\Leftarrow}',                           # LEFTWARDS DOUBLE ARROW [⇐]
0x21D1: r'\ensuremath{\Uparrow}',                             # UPWARDS DOUBLE ARROW [⇑]
0x21D2: r'\ensuremath{\Rightarrow}',                          # RIGHTWARDS DOUBLE ARROW [⇒]
0x21D3: r'\ensuremath{\Downarrow}',                           # DOWNWARDS DOUBLE ARROW [⇓]
0x21D4: r'\ensuremath{\Leftrightarrow}',                      # LEFT RIGHT DOUBLE ARROW [⇔]
0x21D5: r'\ensuremath{\Updownarrow}',                         # UP DOWN DOUBLE ARROW [⇕]
0x21DA: r'\ensuremath{\Lleftarrow}',                          # LEFTWARDS TRIPLE ARROW [⇚]
0x21DB: r'\ensuremath{\Rrightarrow}',                         # RIGHTWARDS TRIPLE ARROW [⇛]
0x21DD: r'\ensuremath{\rightsquigarrow}',                     # RIGHTWARDS SQUIGGLE ARROW [⇝]
0x21F5: r'\ensuremath{\DownArrowUpArrow}',                    # DOWNWARDS ARROW LEFTWARDS OF UPWARDS ARROW [⇵]


# Math operators and symbols (U+22XX)
0x2200: r'\ensuremath{\forall}',
0x2201: r'\ensuremath{\complement}',
0x2202: r'\ensuremath{\partial}',
0x2203: r'\ensuremath{\exists}',
0x2204: r'\ensuremath{\nexists}',
0x2205: r'\ensuremath{\varnothing}',
0x2206: r'\ensuremath{\Delta}',
0x2207: r'\ensuremath{\nabla}',
0x2208: r'\ensuremath{\in}',
0x2209: r'\ensuremath{\notin}',
0x220A: r'\ensuremath{\in}',                     # alternative
0x220B: r'\ensuremath{\ni}',
0x220C: r'\ensuremath{\not\ni}',
0x220D: r'\ensuremath{\ni}',                     # alternative
0x220E: r'\ensuremath{\blacksquare}',
0x220F: r'\ensuremath{\prod}',
0x2210: r'\ensuremath{\coprod}',
0x2211: r'\ensuremath{\sum}',
0x2212: r'\ensuremath{-}',
0x2213: r'\ensuremath{\mp}',
0x2214: r'\ensuremath{\dotplus}',                             # DOT PLUS [∔]
0x2215: r'\ensuremath{/}',
0x2216: r'\ensuremath{\smallsetminus}',
0x2217: r'\ensuremath{*}',
0x2218: r'\ensuremath{\circ}',
0x2219: r'\ensuremath{\bullet}',
0x221A: r'\ensuremath{\sqrt{}}',
0x221B: r'\ensuremath{\sqrt[3]{}}',
0x221C: r'\ensuremath{\sqrt[4]{}}',
0x221D: r'\ensuremath{\propto}',
0x221E: r'\ensuremath{\infty}',
0x221F: r'\ensuremath{\rightangle}',                          # RIGHT ANGLE [∟]
0x2220: r'\ensuremath{\angle}',                               # ANGLE [∠]
0x2221: r'\ensuremath{\measuredangle}',                       # MEASURED ANGLE [∡]
0x2222: r'\ensuremath{\sphericalangle}',                      # SPHERICAL ANGLE [∢]
0x2223: r'\ensuremath{\mid}',
0x2224: r'\ensuremath{\nmid}',
0x2225: r'\ensuremath{\parallel}',
0x2226: r'\ensuremath{\nparallel}',
0x2227: r'\ensuremath{\wedge}',
0x2228: r'\ensuremath{\vee}',
0x2229: r'\ensuremath{\cap}',
0x222A: r'\ensuremath{\cup}',
0x222B: r'\ensuremath{\int}',
0x222C: r'\ensuremath{\iint}',
0x222D: r'\ensuremath{\iiint}',
0x222E: r'\ensuremath{\oint}',
0x222F: r'\ensuremath{\surfintegral}',                        # SURFACE INTEGRAL [∯]
0x2230: r'\ensuremath{\volintegral}',                         # VOLUME INTEGRAL [∰]
0x2231: r'\ensuremath{\clwintegral}',                         # CLOCKWISE INTEGRAL [∱]
#0x2232: CLOCKWISE CONTOUR INTEGRAL
#0x2233: ANTICLOCKWISE CONTOUR INTEGRAL
0x2234: r'\ensuremath{\therefore}',
0x2235: r'\ensuremath{\because}',
0x2236: r'\ensuremath{:}',
0x2237: r'\ensuremath{::}',
#0x2238: DOT MINUS
#...
0x223A: r'\ensuremath{\mathbin{{:}\!\!{-}\!\!{:}}}', # GEOMETRIC PROPORTION [∺]
0x223B: r'\ensuremath{\homothetic}',              # HOMOTHETIC [∻]
0x223C: r'\ensuremath{\sim}',
0x223D: r'\ensuremath{\backsim}',
0x223E: r'\ensuremath{\lazysinv}',                            # INVERTED LAZY S [∾]
#
0x2240: r'\ensuremath{\wr}',                                  # WREATH PRODUCT [≀]
0x2241: r'\ensuremath{\not\sim}',                             # NOT TILDE [≁]
0x2243: r'\ensuremath{\simeq}',                               # ASYMPTOTICALLY EQUAL TO [≃]
0x2244: r'\ensuremath{\not\simeq}',                           # NOT ASYMPTOTICALLY EQUAL TO [≄]
0x2245: r'\ensuremath{\cong}',                                # APPROXIMATELY EQUAL TO [≅]
0x2246: r'\ensuremath{\approxnotequal}',          # APPROXIMATELY BUT NOT ACTUALLY EQUAL TO [≆]
0x2247: r'\ensuremath{\not\cong}',                # NEITHER APPROXIMATELY NOR ACTUALLY EQUAL TO [≇]
0x2248: r'\ensuremath{\approx}',
0x2249: r'\ensuremath{\not\approx}',                          # NOT ALMOST EQUAL TO [≉]
0x224A: r'\ensuremath{\approxeq}',                            # ALMOST EQUAL OR EQUAL TO [≊]
0x224B: r'\ensuremath{\tildetrpl}',                           # TRIPLE TILDE [≋]
0x224C: r'\ensuremath{\allequal}',                            # ALL EQUAL TO [≌]
0x224D: r'\ensuremath{\asymp}',                               # EQUIVALENT TO [≍]
0x224E: r'\ensuremath{\Bumpeq}',                              # GEOMETRICALLY EQUIVALENT TO [≎]
0x224F: r'\ensuremath{\bumpeq}',                              # DIFFERENCE BETWEEN [≏]
0x2250: r'\ensuremath{\doteq}',                               # APPROACHES THE LIMIT [≐]
0x2251: r'\ensuremath{\doteqdot}',                            # GEOMETRICALLY EQUAL TO [≑]
0x2252: r'\ensuremath{\fallingdotseq}',                       # APPROXIMATELY EQUAL TO OR THE IMAGE OF [≒]
0x2253: r'\ensuremath{\risingdotseq}',                        # IMAGE OF OR APPROXIMATELY EQUAL TO [≓]
0x2254: r'\ensuremath{:=}',                                    # COLON EQUALS [≔]
0x2255: r'\ensuremath{=:}',                                    # EQUALS COLON [≕]
0x2256: r'\ensuremath{\eqcirc}',                              # RING IN EQUAL TO [≖]
0x2257: r'\ensuremath{\circeq}',                              # RING EQUAL TO [≗]
0x2259: r'\ensuremath{\estimates}',                           # ESTIMATES [≙]
0x225B: r'\ensuremath{\starequal}',                           # STAR EQUALS [≛]
0x225C: r'\ensuremath{\triangleq}',                           # DELTA EQUAL TO [≜]
#
0x2260: r'\ensuremath{\neq}',
0x2261: r'\ensuremath{\equiv}',
0x2262: r'\ensuremath{\not\equiv}',
#0x2263: STRICTLY EQUIVALENT TO
0x2264: r'\ensuremath{\leq}',
0x2265: r'\ensuremath{\geq}',
0x2266: r'\ensuremath{\leqq}',
0x2267: r'\ensuremath{\geqq}',
0x2268: r'\ensuremath{\lneqq}',
0x2269: r'\ensuremath{\gneqq}',
0x226A: r'\ensuremath{\ll}',
0x226B: r'\ensuremath{\gg}',
0x226C: r'\ensuremath{\between}',                             # BETWEEN [≬]
0x226D: r'\ensuremath{\not\kern-0.3em\times}',                # NOT EQUIVALENT TO [≭]
0x226E: r'\ensuremath{\nless}',
0x226F: r'\ensuremath{\ngtr}',
0x2270: r'\ensuremath{\nleq}',
0x2271: r'\ensuremath{\ngeq}',
0x2272: r'\ensuremath{\lesssim}',
0x2273: r'\ensuremath{\gtrsim}',
0x2274: r'\ensuremath{\not\lesssim}',
0x2275: r'\ensuremath{\not\gtrsim}',
0x2276: r'\ensuremath{\lessgtr}',
0x2277: r'\ensuremath{\gtrless}',
0x2278: r'\ensuremath{\notlessgreater}',                      # NEITHER LESS-THAN NOR GREATER-THAN [≸]
0x2279: r'\ensuremath{\notgreaterless}',                      # NEITHER GREATER-THAN NOR LESS-THAN [≹]
0x227A: r'\ensuremath{\prec}',
0x227B: r'\ensuremath{\succ}',
0x227C: r'\ensuremath{\preceq}',
0x227D: r'\ensuremath{\succeq}',
0x227E: r'\ensuremath{\precsim}',
0x227F: r'\ensuremath{\succsim}',
0x2280: r'\ensuremath{\nprec}',
0x2281: r'\ensuremath{\nsucc}',
0x2282: r'\ensuremath{\subset}',
0x2283: r'\ensuremath{\supset}',
0x2284: r'\ensuremath{\not\subset}',
0x2285: r'\ensuremath{\not\supset}',
0x2286: r'\ensuremath{\subseteq}',
0x2287: r'\ensuremath{\supseteq}',
0x2288: r'\ensuremath{\nsubseteq}',
0x2289: r'\ensuremath{\nsupseteq}',
0x228A: r'\ensuremath{\subsetneq}',
0x228B: r'\ensuremath{\supsetneq}',
0x228E: r'\ensuremath{\uplus}',                               # MULTISET UNION [⊎]
0x228F: r'\ensuremath{\sqsubset}',                            # SQUARE IMAGE OF [⊏]
0x2290: r'\ensuremath{\sqsupset}',                            # SQUARE ORIGINAL OF [⊐]
0x2291: r'\ensuremath{\sqsubseteq}',                          # SQUARE IMAGE OF OR EQUAL TO [⊑]
0x2292: r'\ensuremath{\sqsupseteq}',                          # SQUARE ORIGINAL OF OR EQUAL TO [⊒]
0x2293: r'\ensuremath{\sqcap}',
0x2294: r'\ensuremath{\sqcup}',
0x2295: r'\ensuremath{\oplus}',
0x2296: r'\ensuremath{\ominus}',
0x2297: r'\ensuremath{\otimes}',
0x2298: r'\ensuremath{\oslash}',
0x2299: r'\ensuremath{\odot}',
0x229A: r'\ensuremath{\circledcirc}',                         # CIRCLED RING OPERATOR [⊚]
0x229B: r'\ensuremath{\circledast}',                          # CIRCLED ASTERISK OPERATOR [⊛]
0x229D: r'\ensuremath{\circleddash}',                         # CIRCLED DASH [⊝]
0x229E: r'\ensuremath{\boxplus}',                             # SQUARED PLUS [⊞]
0x229F: r'\ensuremath{\boxminus}',                            # SQUARED MINUS [⊟]
0x22A0: r'\ensuremath{\boxtimes}',                            # SQUARED TIMES [⊠]
0x22A1: r'\ensuremath{\boxdot}',                              # SQUARED DOT OPERATOR [⊡]
0x22A2: r'\ensuremath{\vdash}',                               # RIGHT TACK [⊢]
0x22A3: r'\ensuremath{\dashv}',                               # LEFT TACK [⊣]
0x22A4: r'\ensuremath{\top}',                                 # DOWN TACK [⊤]
0x22A5: r'\ensuremath{\perp}',                                # UP TACK [⊥]
0x22A7: r'\ensuremath{\truestate}',                           # MODELS [⊧]
0x22A8: r'\ensuremath{\forcesextra}',                         # TRUE [⊨]
0x22A9: r'\ensuremath{\Vdash}',                               # FORCES [⊩]
0x22AA: r'\ensuremath{\Vvdash}',                              # TRIPLE VERTICAL BAR RIGHT TURNSTILE [⊪]
0x22AB: r'\ensuremath{\VDash}',                   # DOUBLE VERTICAL BAR DOUBLE RIGHT TURNSTILE [⊫]
0x22AC: r'\ensuremath{\nvdash}',                              # DOES NOT PROVE [⊬]
0x22AD: r'\ensuremath{\nvDash}',                              # NOT TRUE [⊭]
0x22AE: r'\ensuremath{\nVdash}',                              # DOES NOT FORCE [⊮]
0x22AF: r'\ensuremath{\nVDash}',                  # NEGATED DOUBLE VERTICAL BAR DOUBLE RIGHT TURNSTILE [⊯]
0x22B2: r'\ensuremath{\vartriangleleft}',                     # NORMAL SUBGROUP OF [⊲]
0x22B3: r'\ensuremath{\vartriangleright}',                    # CONTAINS AS NORMAL SUBGROUP [⊳]
0x22B4: r'\ensuremath{\trianglelefteq}',                      # NORMAL SUBGROUP OF OR EQUAL TO [⊴]
0x22B5: r'\ensuremath{\trianglerighteq}',                     # CONTAINS AS NORMAL SUBGROUP OR EQUAL TO [⊵]
0x22B6: r'\ensuremath{\original}',                            # ORIGINAL OF [⊶]
0x22B7: r'\ensuremath{\image}',                               # IMAGE OF [⊷]
0x22B8: r'\ensuremath{\multimap}',                            # MULTIMAP [⊸]
0x22B9: r'\ensuremath{\hermitconjmatrix}',                    # HERMITIAN CONJUGATE MATRIX [⊹]
0x22BA: r'\ensuremath{\intercal}',                            # INTERCALATE [⊺]
0x22BB: r'\ensuremath{\veebar}',                              # XOR [⊻]
0x22BE: r'\ensuremath{\rightanglearc}',                       # RIGHT ANGLE WITH ARC [⊾]
0x22C0: r'\ensuremath{\bigwedge}',
0x22C1: r'\ensuremath{\bigvee}',
0x22C2: r'\ensuremath{\bigcap}',
0x22C3: r'\ensuremath{\bigcup}',
0x22C4: r'\ensuremath{\diamond}',
0x22C5: r'\ensuremath{\cdot}',
0x22C6: r'\ensuremath{\star}',
0x22C7: r'\ensuremath{\divideontimes}',
0x22C8: r'\ensuremath{\bowtie}',
0x22C9: r'\ensuremath{\ltimes}',
0x22CA: r'\ensuremath{\rtimes}',
0x22CB: r'\ensuremath{\leftthreetimes}',
0x22CC: r'\ensuremath{\rightthreetimes}',
0x22CD: r'\ensuremath{\backsimeq}',                           # REVERSED TILDE EQUALS [⋍]
0x22CE: r'\ensuremath{\curlyvee}',                            # CURLY LOGICAL OR [⋎]
0x22CF: r'\ensuremath{\curlywedge}',                          # CURLY LOGICAL AND [⋏]
0x22D0: r'\ensuremath{\Subset}',                              # DOUBLE SUBSET [⋐]
0x22D1: r'\ensuremath{\Supset}',                              # DOUBLE SUPERSET [⋑]
0x22D2: r'\ensuremath{\Cap}',                                 # DOUBLE INTERSECTION [⋒]
0x22D3: r'\ensuremath{\Cup}',                                 # DOUBLE UNION [⋓]
0x22D4: r'\ensuremath{\pitchfork}',                           # PITCHFORK [⋔]
0x22D6: r'\ensuremath{\lessdot}',                             # LESS-THAN WITH DOT [⋖]
0x22D7: r'\ensuremath{\gtrdot}',                              # GREATER-THAN WITH DOT [⋗]
0x22D8: r'\ensuremath{\verymuchless}',                        # VERY MUCH LESS-THAN [⋘]
0x22D9: r'\ensuremath{\verymuchgreater}',                     # VERY MUCH GREATER-THAN [⋙]
0x22DA: r'\ensuremath{\lesseqgtr}',                           # LESS-THAN EQUAL TO OR GREATER-THAN [⋚]
0x22DB: r'\ensuremath{\gtreqless}',                           # GREATER-THAN EQUAL TO OR LESS-THAN [⋛]
0x22DE: r'\ensuremath{\curlyeqprec}',                         # EQUAL TO OR PRECEDES [⋞]
0x22DF: r'\ensuremath{\curlyeqsucc}',                         # EQUAL TO OR SUCCEEDS [⋟]
0x22E2: r'\ensuremath{\not\sqsubseteq}',                      # NOT SQUARE IMAGE OF OR EQUAL TO [⋢]
0x22E3: r'\ensuremath{\not\sqsupseteq}',                      # NOT SQUARE ORIGINAL OF OR EQUAL TO [⋣]
0x22E6: r'\ensuremath{\lnsim}',                               # LESS-THAN BUT NOT EQUIVALENT TO [⋦]
0x22E7: r'\ensuremath{\gnsim}',                               # GREATER-THAN BUT NOT EQUIVALENT TO [⋧]
0x22E8: r'\ensuremath{\precedesnotsimilar}',                  # PRECEDES BUT NOT EQUIVALENT TO [⋨]
0x22E9: r'\ensuremath{\succnsim}',                            # SUCCEEDS BUT NOT EQUIVALENT TO [⋩]
0x22EA: r'\ensuremath{\ntriangleleft}',                       # NOT NORMAL SUBGROUP OF [⋪]
0x22EB: r'\ensuremath{\ntriangleright}',                      # DOES NOT CONTAIN AS NORMAL SUBGROUP [⋫]
0x22EC: r'\ensuremath{\ntrianglelefteq}',                     # NOT NORMAL SUBGROUP OF OR EQUAL TO [⋬]
0x22ED: r'\ensuremath{\ntrianglerighteq}',        # DOES NOT CONTAIN AS NORMAL SUBGROUP OR EQUAL [⋭]
0x22EE: r'\ensuremath{\vdots}',
0x22EF: r'\ensuremath{\cdots}',
0x22F0: r'\ensuremath{\udots}',
0x22F1: r'\ensuremath{\ddots}',
# ...
0x2305: r'\ensuremath{\barwedge}',                            # PROJECTIVE [⌅]
0x2306: r'\ensuremath{\varperspcorrespond}',                  # PERSPECTIVE [⌆]
0x2308: r'\ensuremath{\lceil}',                               # LEFT CEILING [⌈]
0x2309: r'\ensuremath{\rceil}',                               # RIGHT CEILING [⌉]
0x230A: r'\ensuremath{\lfloor}',                              # LEFT FLOOR [⌊]
0x230B: r'\ensuremath{\rfloor}',                              # RIGHT FLOOR [⌋]
0x2315: r'\ensuremath{\recorder}',                            # TELEPHONE RECORDER [⌕]
0x2316: r'\ensuremath{\mathchar"2208}',                        # POSITION INDICATOR [⌖]
0x231C: r'\ensuremath{\ulcorner}',                            # TOP LEFT CORNER [⌜]
0x231D: r'\ensuremath{\urcorner}',                            # TOP RIGHT CORNER [⌝]
0x231E: r'\ensuremath{\llcorner}',                            # BOTTOM LEFT CORNER [⌞]
0x231F: r'\ensuremath{\lrcorner}',                            # BOTTOM RIGHT CORNER [⌟]
0x2322: r'\ensuremath{\frown}',                               # FROWN [⌢]
0x2323: r'\ensuremath{\smile}',                               # SMILE [⌣]

0x23B0: r'\ensuremath{\lmoustache}',              # UPPER LEFT OR LOWER RIGHT CURLY BRACKET SECTION [⎰]
0x23B1: r'\ensuremath{\rmoustache}',              # UPPER RIGHT OR LOWER LEFT CURLY BRACKET SECTION [⎱]

0x2329: r'\textlangle',                          # 0x2329
0x232A: r'\textrangle',
0x2422: r'\textblank',
0x2423: r'\textvisiblespace',
0x25A0: r'\ensuremath{\blacksquare}',             # BLACK SQUARE [■]
0x25A1: r'\ensuremath{\square}',                  # WHITE SQUARE [□]
0x25AA: r'{\small\ensuremath{\blacksquare}}',     # BLACK SMALL SQUARE [▪]
0x25AD: r'\fbox{~~}',                             # WHITE RECTANGLE [▭]
0x25B3: r'\ensuremath{\bigtriangleup}',                       # WHITE UP-POINTING TRIANGLE [△]
0x25B4: r'\ensuremath{\blacktriangle}',                       # BLACK UP-POINTING SMALL TRIANGLE [▴]
0x25B5: r'\ensuremath{\vartriangle}',                         # WHITE UP-POINTING SMALL TRIANGLE [▵]
0x25B8: r'\ensuremath{\blacktriangleright}',                  # BLACK RIGHT-POINTING SMALL TRIANGLE [▸]
0x25B9: r'\ensuremath{\triangleright}',                       # WHITE RIGHT-POINTING SMALL TRIANGLE [▹]
0x25BD: r'\ensuremath{\bigtriangledown}',                     # WHITE DOWN-POINTING TRIANGLE [▽]
0x25BE: r'\ensuremath{\blacktriangledown}',                   # BLACK DOWN-POINTING SMALL TRIANGLE [▾]
0x25BF: r'\ensuremath{\triangledown}',                        # WHITE DOWN-POINTING SMALL TRIANGLE [▿]
0x25C2: r'\ensuremath{\blacktriangleleft}',                   # BLACK LEFT-POINTING SMALL TRIANGLE [◂]
0x25C3: r'\ensuremath{\triangleleft}',                        # WHITE LEFT-POINTING SMALL TRIANGLE [◃]
0x25CA: r'\ensuremath{\lozenge}',                             # LOZENGE [◊]
0x25CB: r'\ensuremath{\bigcirc}',                             # WHITE CIRCLE [○]

0x25E6: r'\textopenbullet',
0x25EF: r'\textbigcircle',
0x2662: r'\ensuremath{\diamond}',                             # WHITE DIAMOND SUIT [♢]
0x266A: r'\textmusicalnote',                     # 0x266A
0x2669: r'\quarternote',                          # QUARTER NOTE [♩]
0x266D: r'\flat',                                 # MUSIC FLAT SIGN [♭]
0x266E: r'\natural',                              # MUSIC NATURAL SIGN [♮]
0x266F: r'\sharp',                                # MUSIC SHARP SIGN [♯]


0x27E8: r'\ensuremath{\langle}',                 # MATHEMATICAL LEFT ANGLE BRACKET
0x27E9: r'\ensuremath{\rangle}',                 # MATHEMATICAL RIGHT ANGLE BRACKET

0x27F5: r'\ensuremath{\longleftarrow}',                       # LONG LEFTWARDS ARROW [⟵]
0x27F6: r'\ensuremath{\longrightarrow}',                      # LONG RIGHTWARDS ARROW [⟶]
0x27F7: r'\ensuremath{\longleftrightarrow}',                  # LONG LEFT RIGHT ARROW [⟷]
0x27F8: r'\ensuremath{\Longleftarrow}',                       # LONG LEFTWARDS DOUBLE ARROW [⟸]
0x27F9: r'\ensuremath{\Longrightarrow}',                      # LONG RIGHTWARDS DOUBLE ARROW [⟹]
0x27FA: r'\ensuremath{\Longleftrightarrow}',                  # LONG LEFT RIGHT DOUBLE ARROW [⟺]
0x27FC: r'\ensuremath{\longmapsto}',                          # LONG RIGHTWARDS ARROW FROM BAR [⟼]
0x27FF: r'\ensuremath{\sim\joinrel\leadsto}',                 # LONG RIGHTWARDS SQUIGGLE ARROW [⟿]

0x2993: r'\ensuremath{<\kern-0.58em(}',                        # LEFT ARC LESS-THAN BRACKET [⦓]
0x29EB: r'\ensuremath{\blacklozenge}',                        # BLACK LOZENGE [⧫]
# Supplemental Mathematical Operators U+2AXX
0x2A0F: r'\ensuremath{\clockoint}',                           # INTEGRAL AVERAGE WITH SLASH [⨏]
0x2A16: r'\ensuremath{\sqrint}',                              # QUATERNION INTEGRAL OPERATOR [⨖]
0x2A3F: r'\ensuremath{\amalg}',                               # AMALGAMATION OR COPRODUCT [⨿]
0x2A6E: r'\ensuremath{\stackrel{*}{=}}',                       # EQUALS WITH ASTERISK [⩮]
0x2A75: r'==',                               # TWO CONSECUTIVE EQUALS SIGNS [⩵]
0x2A7D: r'\ensuremath{\leqslant}',
0x2A7E: r'\ensuremath{\geqslant}',
0x2A85: r'\ensuremath{\lessapprox}',                          # LESS-THAN OR APPROXIMATE [⪅]
0x2A86: r'\ensuremath{\gtrapprox}',                           # GREATER-THAN OR APPROXIMATE [⪆]
0x2A87: r'\ensuremath{\lneq}',                                # LESS-THAN AND SINGLE-LINE NOT EQUAL TO [⪇]
0x2A88: r'\ensuremath{\gneq}',                                # GREATER-THAN AND SINGLE-LINE NOT EQUAL TO [⪈]
0x2A89: r'\ensuremath{\lnapprox}',                            # LESS-THAN AND NOT APPROXIMATE [⪉]
0x2A8A: r'\ensuremath{\gnapprox}',                            # GREATER-THAN AND NOT APPROXIMATE [⪊]
0x2A8B: r'\ensuremath{\lesseqqgtr}',              # LESS-THAN ABOVE DOUBLE-LINE EQUAL ABOVE GREATER-THAN [⪋]
0x2A8C: r'\ensuremath{\gtreqqless}',              # GREATER-THAN ABOVE DOUBLE-LINE EQUAL ABOVE LESS-THAN [⪌]
0x2A95: r'\ensuremath{\eqslantless}',                         # SLANTED EQUAL TO OR LESS-THAN [⪕]
0x2A96: r'\ensuremath{\eqslantgtr}',                          # SLANTED EQUAL TO OR GREATER-THAN [⪖]
0x2AAF: r'\ensuremath{\preceq}',                              # PRECEDES ABOVE SINGLE-LINE EQUALS SIGN [⪯]
0x2AB0: r'\ensuremath{\succeq}',                              # SUCCEEDS ABOVE SINGLE-LINE EQUALS SIGN [⪰]
0x2AB5: r'\ensuremath{\precneqq}',                            # PRECEDES ABOVE NOT EQUAL TO [⪵]
0x2AB6: r'\ensuremath{\succneqq}',                            # SUCCEEDS ABOVE NOT EQUAL TO [⪶]
0x2AB7: r'\ensuremath{\precapprox}',                          # PRECEDES ABOVE ALMOST EQUAL TO [⪷]
0x2AB8: r'\ensuremath{\succapprox}',                          # SUCCEEDS ABOVE ALMOST EQUAL TO [⪸]
0x2AB9: r'\ensuremath{\precnapprox}',                         # PRECEDES ABOVE NOT ALMOST EQUAL TO [⪹]
0x2ABA: r'\ensuremath{\succnapprox}',                         # SUCCEEDS ABOVE NOT ALMOST EQUAL TO [⪺]
0x2AC5: r'\ensuremath{\subseteqq}',                           # SUBSET OF ABOVE EQUALS SIGN [⫅]
0x2AC6: r'\ensuremath{\supseteqq}',                           # SUPERSET OF ABOVE EQUALS SIGN [⫆]
0x2ACB: r'\ensuremath{\subsetneqq}',                          # SUBSET OF ABOVE NOT EQUAL TO [⫋]
0x2ACC: r'\ensuremath{\supsetneqq}',                          # SUPERSET OF ABOVE NOT EQUAL TO [⫌]
0x2AFD: r'\ensuremath{{{/}\!\!{/}}}',                          # DOUBLE SOLIDUS OPERATOR [⫽]

# CJK Symbols Punktuation (!) U+3000 : for \langle/\rangle
0x3008: r'\ensuremath{\langle}',
0x3009: r'\ensuremath{\rangle}',

# ligatures
0xFB00: r'ff',                                   # LATIN SMALL LIGATURE FF
0xFB01: r'fi',                                   # LATIN SMALL LIGATURE FI
0xFB02: r'fl',                                   # LATIN SMALL LIGATURE FL
0xFB03: r'ffi',                                  # LATIN SMALL LIGATURE FFI
0xFB04: r'ffl',                                  # LATIN SMALL LIGATURE FFL


# Mathematical Alphanumeric Symbols
0x1D400: r'\ensuremath{\mathbf{A}}',              # MATHEMATICAL BOLD CAPITAL A
0x1D401: r'\ensuremath{\mathbf{B}}',              # MATHEMATICAL BOLD CAPITAL B
0x1D402: r'\ensuremath{\mathbf{C}}',              # MATHEMATICAL BOLD CAPITAL C
0x1D403: r'\ensuremath{\mathbf{D}}',              # MATHEMATICAL BOLD CAPITAL D
0x1D404: r'\ensuremath{\mathbf{E}}',              # MATHEMATICAL BOLD CAPITAL E
0x1D405: r'\ensuremath{\mathbf{F}}',              # MATHEMATICAL BOLD CAPITAL F
0x1D406: r'\ensuremath{\mathbf{G}}',              # MATHEMATICAL BOLD CAPITAL G
0x1D407: r'\ensuremath{\mathbf{H}}',              # MATHEMATICAL BOLD CAPITAL H
0x1D408: r'\ensuremath{\mathbf{I}}',              # MATHEMATICAL BOLD CAPITAL I
0x1D409: r'\ensuremath{\mathbf{J}}',              # MATHEMATICAL BOLD CAPITAL J
0x1D40A: r'\ensuremath{\mathbf{K}}',              # MATHEMATICAL BOLD CAPITAL K
0x1D40B: r'\ensuremath{\mathbf{L}}',              # MATHEMATICAL BOLD CAPITAL L
0x1D40C: r'\ensuremath{\mathbf{M}}',              # MATHEMATICAL BOLD CAPITAL M
0x1D40D: r'\ensuremath{\mathbf{N}}',              # MATHEMATICAL BOLD CAPITAL N
0x1D40E: r'\ensuremath{\mathbf{O}}',              # MATHEMATICAL BOLD CAPITAL O
0x1D40F: r'\ensuremath{\mathbf{P}}',              # MATHEMATICAL BOLD CAPITAL P
0x1D410: r'\ensuremath{\mathbf{Q}}',              # MATHEMATICAL BOLD CAPITAL Q
0x1D411: r'\ensuremath{\mathbf{R}}',              # MATHEMATICAL BOLD CAPITAL R
0x1D412: r'\ensuremath{\mathbf{S}}',              # MATHEMATICAL BOLD CAPITAL S
0x1D413: r'\ensuremath{\mathbf{T}}',              # MATHEMATICAL BOLD CAPITAL T
0x1D414: r'\ensuremath{\mathbf{U}}',              # MATHEMATICAL BOLD CAPITAL U
0x1D415: r'\ensuremath{\mathbf{V}}',              # MATHEMATICAL BOLD CAPITAL V
0x1D416: r'\ensuremath{\mathbf{W}}',              # MATHEMATICAL BOLD CAPITAL W
0x1D417: r'\ensuremath{\mathbf{X}}',              # MATHEMATICAL BOLD CAPITAL X
0x1D418: r'\ensuremath{\mathbf{Y}}',              # MATHEMATICAL BOLD CAPITAL Y
0x1D419: r'\ensuremath{\mathbf{Z}}',              # MATHEMATICAL BOLD CAPITAL Z

0x1D41A: r'\ensuremath{\mathbf{a}}',              # MATHEMATICAL BOLD SMALL a
0x1D41B: r'\ensuremath{\mathbf{b}}',              # MATHEMATICAL BOLD SMALL b
0x1D41C: r'\ensuremath{\mathbf{c}}',              # MATHEMATICAL BOLD SMALL c
0x1D41D: r'\ensuremath{\mathbf{d}}',              # MATHEMATICAL BOLD SMALL d
0x1D41E: r'\ensuremath{\mathbf{e}}',              # MATHEMATICAL BOLD SMALL e
0x1D41F: r'\ensuremath{\mathbf{f}}',              # MATHEMATICAL BOLD SMALL f
0x1D420: r'\ensuremath{\mathbf{g}}',              # MATHEMATICAL BOLD SMALL g
0x1D421: r'\ensuremath{\mathbf{h}}',              # MATHEMATICAL BOLD SMALL h
0x1D422: r'\ensuremath{\mathbf{i}}',              # MATHEMATICAL BOLD SMALL i
0x1D423: r'\ensuremath{\mathbf{j}}',              # MATHEMATICAL BOLD SMALL j
0x1D424: r'\ensuremath{\mathbf{k}}',              # MATHEMATICAL BOLD SMALL k
0x1D425: r'\ensuremath{\mathbf{l}}',              # MATHEMATICAL BOLD SMALL l
0x1D426: r'\ensuremath{\mathbf{m}}',              # MATHEMATICAL BOLD SMALL m
0x1D427: r'\ensuremath{\mathbf{n}}',              # MATHEMATICAL BOLD SMALL n
0x1D428: r'\ensuremath{\mathbf{o}}',              # MATHEMATICAL BOLD SMALL o
0x1D429: r'\ensuremath{\mathbf{p}}',              # MATHEMATICAL BOLD SMALL p
0x1D42A: r'\ensuremath{\mathbf{q}}',              # MATHEMATICAL BOLD SMALL q
0x1D42B: r'\ensuremath{\mathbf{r}}',              # MATHEMATICAL BOLD SMALL r
0x1D42C: r'\ensuremath{\mathbf{s}}',              # MATHEMATICAL BOLD SMALL s
0x1D42D: r'\ensuremath{\mathbf{t}}',              # MATHEMATICAL BOLD SMALL t
0x1D42E: r'\ensuremath{\mathbf{u}}',              # MATHEMATICAL BOLD SMALL u
0x1D42F: r'\ensuremath{\mathbf{v}}',              # MATHEMATICAL BOLD SMALL v
0x1D430: r'\ensuremath{\mathbf{w}}',              # MATHEMATICAL BOLD SMALL w
0x1D431: r'\ensuremath{\mathbf{x}}',              # MATHEMATICAL BOLD SMALL x
0x1D432: r'\ensuremath{\mathbf{y}}',              # MATHEMATICAL BOLD SMALL y
0x1D433: r'\ensuremath{\mathbf{z}}',              # MATHEMATICAL BOLD SMALL z

0x1D434: r'\ensuremath{\mathit{A}}',              # MATHEMATICAL ITALIC CAPITAL A
0x1D435: r'\ensuremath{\mathit{B}}',              # MATHEMATICAL ITALIC CAPITAL B
0x1D436: r'\ensuremath{\mathit{C}}',              # MATHEMATICAL ITALIC CAPITAL C
0x1D437: r'\ensuremath{\mathit{D}}',              # MATHEMATICAL ITALIC CAPITAL D
0x1D438: r'\ensuremath{\mathit{E}}',              # MATHEMATICAL ITALIC CAPITAL E
0x1D439: r'\ensuremath{\mathit{F}}',              # MATHEMATICAL ITALIC CAPITAL F
0x1D43A: r'\ensuremath{\mathit{G}}',              # MATHEMATICAL ITALIC CAPITAL G
0x1D43B: r'\ensuremath{\mathit{H}}',              # MATHEMATICAL ITALIC CAPITAL H
0x1D43C: r'\ensuremath{\mathit{I}}',              # MATHEMATICAL ITALIC CAPITAL I
0x1D43D: r'\ensuremath{\mathit{J}}',              # MATHEMATICAL ITALIC CAPITAL J
0x1D43E: r'\ensuremath{\mathit{K}}',              # MATHEMATICAL ITALIC CAPITAL K
0x1D43F: r'\ensuremath{\mathit{L}}',              # MATHEMATICAL ITALIC CAPITAL L
0x1D440: r'\ensuremath{\mathit{M}}',              # MATHEMATICAL ITALIC CAPITAL M
0x1D441: r'\ensuremath{\mathit{N}}',              # MATHEMATICAL ITALIC CAPITAL N
0x1D442: r'\ensuremath{\mathit{O}}',              # MATHEMATICAL ITALIC CAPITAL O
0x1D443: r'\ensuremath{\mathit{P}}',              # MATHEMATICAL ITALIC CAPITAL P
0x1D444: r'\ensuremath{\mathit{Q}}',              # MATHEMATICAL ITALIC CAPITAL Q
0x1D445: r'\ensuremath{\mathit{R}}',              # MATHEMATICAL ITALIC CAPITAL R
0x1D446: r'\ensuremath{\mathit{S}}',              # MATHEMATICAL ITALIC CAPITAL S
0x1D447: r'\ensuremath{\mathit{T}}',              # MATHEMATICAL ITALIC CAPITAL T
0x1D448: r'\ensuremath{\mathit{U}}',              # MATHEMATICAL ITALIC CAPITAL U
0x1D449: r'\ensuremath{\mathit{V}}',              # MATHEMATICAL ITALIC CAPITAL V
0x1D44A: r'\ensuremath{\mathit{W}}',              # MATHEMATICAL ITALIC CAPITAL W
0x1D44B: r'\ensuremath{\mathit{X}}',              # MATHEMATICAL ITALIC CAPITAL X
0x1D44C: r'\ensuremath{\mathit{Y}}',              # MATHEMATICAL ITALIC CAPITAL Y
0x1D44D: r'\ensuremath{\mathit{Z}}',              # MATHEMATICAL ITALIC CAPITAL Z

0x1D44E: r'\ensuremath{\mathit{a}}',              # MATHEMATICAL ITALIC SMALL a
0x1D44F: r'\ensuremath{\mathit{b}}',              # MATHEMATICAL ITALIC SMALL b
0x1D450: r'\ensuremath{\mathit{c}}',              # MATHEMATICAL ITALIC SMALL c
0x1D451: r'\ensuremath{\mathit{d}}',              # MATHEMATICAL ITALIC SMALL d
0x1D452: r'\ensuremath{\mathit{e}}',              # MATHEMATICAL ITALIC SMALL e
0x1D453: r'\ensuremath{\mathit{f}}',              # MATHEMATICAL ITALIC SMALL f
0x1D454: r'\ensuremath{\mathit{g}}',              # MATHEMATICAL ITALIC SMALL g
0x1D455: r'\ensuremath{\mathit{h}}',              # MATHEMATICAL ITALIC SMALL h
0x1D456: r'\ensuremath{\mathit{i}}',              # MATHEMATICAL ITALIC SMALL i
0x1D457: r'\ensuremath{\mathit{j}}',              # MATHEMATICAL ITALIC SMALL j
0x1D458: r'\ensuremath{\mathit{k}}',              # MATHEMATICAL ITALIC SMALL k
0x1D459: r'\ensuremath{\mathit{l}}',              # MATHEMATICAL ITALIC SMALL l
0x1D45A: r'\ensuremath{\mathit{m}}',              # MATHEMATICAL ITALIC SMALL m
0x1D45B: r'\ensuremath{\mathit{n}}',              # MATHEMATICAL ITALIC SMALL n
0x1D45C: r'\ensuremath{\mathit{o}}',              # MATHEMATICAL ITALIC SMALL o
0x1D45D: r'\ensuremath{\mathit{p}}',              # MATHEMATICAL ITALIC SMALL p
0x1D45E: r'\ensuremath{\mathit{q}}',              # MATHEMATICAL ITALIC SMALL q
0x1D45F: r'\ensuremath{\mathit{r}}',              # MATHEMATICAL ITALIC SMALL r
0x1D460: r'\ensuremath{\mathit{s}}',              # MATHEMATICAL ITALIC SMALL s
0x1D461: r'\ensuremath{\mathit{t}}',              # MATHEMATICAL ITALIC SMALL t
0x1D462: r'\ensuremath{\mathit{u}}',              # MATHEMATICAL ITALIC SMALL u
0x1D463: r'\ensuremath{\mathit{v}}',              # MATHEMATICAL ITALIC SMALL v
0x1D464: r'\ensuremath{\mathit{w}}',              # MATHEMATICAL ITALIC SMALL w
0x1D465: r'\ensuremath{\mathit{x}}',              # MATHEMATICAL ITALIC SMALL x
0x1D466: r'\ensuremath{\mathit{y}}',              # MATHEMATICAL ITALIC SMALL y
0x1D467: r'\ensuremath{\mathit{z}}',              # MATHEMATICAL ITALIC SMALL z

0x1D468: r'\ensuremath{\boldsymbol{\mathit{A}}}', # MATHEMATICAL BOLD ITALIC CAPITAL A
0x1D469: r'\ensuremath{\boldsymbol{\mathit{B}}}', # MATHEMATICAL BOLD ITALIC CAPITAL B
0x1D46A: r'\ensuremath{\boldsymbol{\mathit{C}}}', # MATHEMATICAL BOLD ITALIC CAPITAL C
0x1D46B: r'\ensuremath{\boldsymbol{\mathit{D}}}', # MATHEMATICAL BOLD ITALIC CAPITAL D
0x1D46C: r'\ensuremath{\boldsymbol{\mathit{E}}}', # MATHEMATICAL BOLD ITALIC CAPITAL E
0x1D46D: r'\ensuremath{\boldsymbol{\mathit{F}}}', # MATHEMATICAL BOLD ITALIC CAPITAL F
0x1D46E: r'\ensuremath{\boldsymbol{\mathit{G}}}', # MATHEMATICAL BOLD ITALIC CAPITAL G
0x1D46F: r'\ensuremath{\boldsymbol{\mathit{H}}}', # MATHEMATICAL BOLD ITALIC CAPITAL H
0x1D470: r'\ensuremath{\boldsymbol{\mathit{I}}}', # MATHEMATICAL BOLD ITALIC CAPITAL I
0x1D471: r'\ensuremath{\boldsymbol{\mathit{J}}}', # MATHEMATICAL BOLD ITALIC CAPITAL J
0x1D472: r'\ensuremath{\boldsymbol{\mathit{K}}}', # MATHEMATICAL BOLD ITALIC CAPITAL K
0x1D473: r'\ensuremath{\boldsymbol{\mathit{L}}}', # MATHEMATICAL BOLD ITALIC CAPITAL L
0x1D474: r'\ensuremath{\boldsymbol{\mathit{M}}}', # MATHEMATICAL BOLD ITALIC CAPITAL M
0x1D475: r'\ensuremath{\boldsymbol{\mathit{N}}}', # MATHEMATICAL BOLD ITALIC CAPITAL N
0x1D476: r'\ensuremath{\boldsymbol{\mathit{O}}}', # MATHEMATICAL BOLD ITALIC CAPITAL O
0x1D477: r'\ensuremath{\boldsymbol{\mathit{P}}}', # MATHEMATICAL BOLD ITALIC CAPITAL P
0x1D478: r'\ensuremath{\boldsymbol{\mathit{Q}}}', # MATHEMATICAL BOLD ITALIC CAPITAL Q
0x1D479: r'\ensuremath{\boldsymbol{\mathit{R}}}', # MATHEMATICAL BOLD ITALIC CAPITAL R
0x1D47A: r'\ensuremath{\boldsymbol{\mathit{S}}}', # MATHEMATICAL BOLD ITALIC CAPITAL S
0x1D47B: r'\ensuremath{\boldsymbol{\mathit{T}}}', # MATHEMATICAL BOLD ITALIC CAPITAL T
0x1D47C: r'\ensuremath{\boldsymbol{\mathit{U}}}', # MATHEMATICAL BOLD ITALIC CAPITAL U
0x1D47D: r'\ensuremath{\boldsymbol{\mathit{V}}}', # MATHEMATICAL BOLD ITALIC CAPITAL V
0x1D47E: r'\ensuremath{\boldsymbol{\mathit{W}}}', # MATHEMATICAL BOLD ITALIC CAPITAL W
0x1D47F: r'\ensuremath{\boldsymbol{\mathit{X}}}', # MATHEMATICAL BOLD ITALIC CAPITAL X
0x1D480: r'\ensuremath{\boldsymbol{\mathit{Y}}}', # MATHEMATICAL BOLD ITALIC CAPITAL Y
0x1D481: r'\ensuremath{\boldsymbol{\mathit{Z}}}', # MATHEMATICAL BOLD ITALIC CAPITAL Z

0x1D482: r'\ensuremath{\boldsymbol{\mathit{a}}}', # MATHEMATICAL BOLD ITALIC SMALL a
0x1D483: r'\ensuremath{\boldsymbol{\mathit{b}}}', # MATHEMATICAL BOLD ITALIC SMALL b
0x1D484: r'\ensuremath{\boldsymbol{\mathit{c}}}', # MATHEMATICAL BOLD ITALIC SMALL c
0x1D485: r'\ensuremath{\boldsymbol{\mathit{d}}}', # MATHEMATICAL BOLD ITALIC SMALL d
0x1D486: r'\ensuremath{\boldsymbol{\mathit{e}}}', # MATHEMATICAL BOLD ITALIC SMALL e
0x1D487: r'\ensuremath{\boldsymbol{\mathit{f}}}', # MATHEMATICAL BOLD ITALIC SMALL f
0x1D488: r'\ensuremath{\boldsymbol{\mathit{g}}}', # MATHEMATICAL BOLD ITALIC SMALL g
0x1D489: r'\ensuremath{\boldsymbol{\mathit{h}}}', # MATHEMATICAL BOLD ITALIC SMALL h
0x1D48A: r'\ensuremath{\boldsymbol{\mathit{i}}}', # MATHEMATICAL BOLD ITALIC SMALL i
0x1D48B: r'\ensuremath{\boldsymbol{\mathit{j}}}', # MATHEMATICAL BOLD ITALIC SMALL j
0x1D48C: r'\ensuremath{\boldsymbol{\mathit{k}}}', # MATHEMATICAL BOLD ITALIC SMALL k
0x1D48D: r'\ensuremath{\boldsymbol{\mathit{l}}}', # MATHEMATICAL BOLD ITALIC SMALL l
0x1D48E: r'\ensuremath{\boldsymbol{\mathit{m}}}', # MATHEMATICAL BOLD ITALIC SMALL m
0x1D48F: r'\ensuremath{\boldsymbol{\mathit{n}}}', # MATHEMATICAL BOLD ITALIC SMALL n
0x1D490: r'\ensuremath{\boldsymbol{\mathit{o}}}', # MATHEMATICAL BOLD ITALIC SMALL o
0x1D491: r'\ensuremath{\boldsymbol{\mathit{p}}}', # MATHEMATICAL BOLD ITALIC SMALL p
0x1D492: r'\ensuremath{\boldsymbol{\mathit{q}}}', # MATHEMATICAL BOLD ITALIC SMALL q
0x1D493: r'\ensuremath{\boldsymbol{\mathit{r}}}', # MATHEMATICAL BOLD ITALIC SMALL r
0x1D494: r'\ensuremath{\boldsymbol{\mathit{s}}}', # MATHEMATICAL BOLD ITALIC SMALL s
0x1D495: r'\ensuremath{\boldsymbol{\mathit{t}}}', # MATHEMATICAL BOLD ITALIC SMALL t
0x1D496: r'\ensuremath{\boldsymbol{\mathit{u}}}', # MATHEMATICAL BOLD ITALIC SMALL u
0x1D497: r'\ensuremath{\boldsymbol{\mathit{v}}}', # MATHEMATICAL BOLD ITALIC SMALL v
0x1D498: r'\ensuremath{\boldsymbol{\mathit{w}}}', # MATHEMATICAL BOLD ITALIC SMALL w
0x1D499: r'\ensuremath{\boldsymbol{\mathit{x}}}', # MATHEMATICAL BOLD ITALIC SMALL x
0x1D49A: r'\ensuremath{\boldsymbol{\mathit{y}}}', # MATHEMATICAL BOLD ITALIC SMALL y
0x1D49B: r'\ensuremath{\boldsymbol{\mathit{z}}}', # MATHEMATICAL BOLD ITALIC SMALL z

0x1D49C: r'\ensuremath{\mathscr{A}}',             # MATHEMATICAL SCRIPT CAPITAL A
0x1D49D: r'\ensuremath{\mathscr{B}}',             # MATHEMATICAL SCRIPT CAPITAL B
0x1D49E: r'\ensuremath{\mathscr{C}}',             # MATHEMATICAL SCRIPT CAPITAL C
0x1D49F: r'\ensuremath{\mathscr{D}}',             # MATHEMATICAL SCRIPT CAPITAL D
0x1D4A0: r'\ensuremath{\mathscr{E}}',             # MATHEMATICAL SCRIPT CAPITAL E
0x1D4A1: r'\ensuremath{\mathscr{F}}',             # MATHEMATICAL SCRIPT CAPITAL F
0x1D4A2: r'\ensuremath{\mathscr{G}}',             # MATHEMATICAL SCRIPT CAPITAL G
0x1D4A3: r'\ensuremath{\mathscr{H}}',             # MATHEMATICAL SCRIPT CAPITAL H
0x1D4A4: r'\ensuremath{\mathscr{I}}',             # MATHEMATICAL SCRIPT CAPITAL I
0x1D4A5: r'\ensuremath{\mathscr{J}}',             # MATHEMATICAL SCRIPT CAPITAL J
0x1D4A6: r'\ensuremath{\mathscr{K}}',             # MATHEMATICAL SCRIPT CAPITAL K
0x1D4A7: r'\ensuremath{\mathscr{L}}',             # MATHEMATICAL SCRIPT CAPITAL L
0x1D4A8: r'\ensuremath{\mathscr{M}}',             # MATHEMATICAL SCRIPT CAPITAL M
0x1D4A9: r'\ensuremath{\mathscr{N}}',             # MATHEMATICAL SCRIPT CAPITAL N
0x1D4AA: r'\ensuremath{\mathscr{O}}',             # MATHEMATICAL SCRIPT CAPITAL O
0x1D4AB: r'\ensuremath{\mathscr{P}}',             # MATHEMATICAL SCRIPT CAPITAL P
0x1D4AC: r'\ensuremath{\mathscr{Q}}',             # MATHEMATICAL SCRIPT CAPITAL Q
0x1D4AD: r'\ensuremath{\mathscr{R}}',             # MATHEMATICAL SCRIPT CAPITAL R
0x1D4AE: r'\ensuremath{\mathscr{S}}',             # MATHEMATICAL SCRIPT CAPITAL S
0x1D4AF: r'\ensuremath{\mathscr{T}}',             # MATHEMATICAL SCRIPT CAPITAL T
0x1D4B0: r'\ensuremath{\mathscr{U}}',             # MATHEMATICAL SCRIPT CAPITAL U
0x1D4B1: r'\ensuremath{\mathscr{V}}',             # MATHEMATICAL SCRIPT CAPITAL V
0x1D4B2: r'\ensuremath{\mathscr{W}}',             # MATHEMATICAL SCRIPT CAPITAL W
0x1D4B3: r'\ensuremath{\mathscr{X}}',             # MATHEMATICAL SCRIPT CAPITAL X
0x1D4B4: r'\ensuremath{\mathscr{Y}}',             # MATHEMATICAL SCRIPT CAPITAL Y
0x1D4B5: r'\ensuremath{\mathscr{Z}}',             # MATHEMATICAL SCRIPT CAPITAL Z
0x1D4B6: r'\ensuremath{\mathscr{a}}',                          # MATHEMATICAL SCRIPT SMALL A [𝒶]
0x1D4B7: r'\ensuremath{\mathscr{b}}',                          # MATHEMATICAL SCRIPT SMALL B [𝒷]
0x1D4B8: r'\ensuremath{\mathscr{c}}',                          # MATHEMATICAL SCRIPT SMALL C [𝒸]
0x1D4B9: r'\ensuremath{\mathscr{d}}',                          # MATHEMATICAL SCRIPT SMALL D [𝒹]
0x1D4BB: r'\ensuremath{\mathscr{f}}',                          # MATHEMATICAL SCRIPT SMALL F [𝒻]
0x1D4BD: r'\ensuremath{\mathscr{h}}',                          # MATHEMATICAL SCRIPT SMALL H [𝒽]
0x1D4BE: r'\ensuremath{\mathscr{i}}',                          # MATHEMATICAL SCRIPT SMALL I [𝒾]
0x1D4BF: r'\ensuremath{\mathscr{j}}',                          # MATHEMATICAL SCRIPT SMALL J [𝒿]
0x1D4C0: r'\ensuremath{\mathscr{k}}',                          # MATHEMATICAL SCRIPT SMALL K [𝓀]
0x1D4C1: r'\ensuremath{\mathscr{l}}',                          # MATHEMATICAL SCRIPT SMALL L [𝓁]
0x1D4C2: r'\ensuremath{\mathscr{m}}',                          # MATHEMATICAL SCRIPT SMALL M [𝓂]
0x1D4C3: r'\ensuremath{\mathscr{n}}',                          # MATHEMATICAL SCRIPT SMALL N [𝓃]
0x1D4C5: r'\ensuremath{\mathscr{p}}',                          # MATHEMATICAL SCRIPT SMALL P [𝓅]
0x1D4C6: r'\ensuremath{\mathscr{q}}',                          # MATHEMATICAL SCRIPT SMALL Q [𝓆]
0x1D4C7: r'\ensuremath{\mathscr{r}}',                          # MATHEMATICAL SCRIPT SMALL R [𝓇]
0x1D4C8: r'\ensuremath{\mathscr{s}}',                          # MATHEMATICAL SCRIPT SMALL S [𝓈]
0x1D4C9: r'\ensuremath{\mathscr{t}}',                          # MATHEMATICAL SCRIPT SMALL T [𝓉]
0x1D4CA: r'\ensuremath{\mathscr{u}}',                          # MATHEMATICAL SCRIPT SMALL U [𝓊]
0x1D4CB: r'\ensuremath{\mathscr{v}}',                          # MATHEMATICAL SCRIPT SMALL V [𝓋]
0x1D4CC: r'\ensuremath{\mathscr{w}}',                          # MATHEMATICAL SCRIPT SMALL W [𝓌]
0x1D4CD: r'\ensuremath{\mathscr{x}}',                          # MATHEMATICAL SCRIPT SMALL X [𝓍]
0x1D4CE: r'\ensuremath{\mathscr{y}}',                          # MATHEMATICAL SCRIPT SMALL Y [𝓎]
0x1D4CF: r'\ensuremath{\mathscr{z}}',                          # MATHEMATICAL SCRIPT SMALL Z [𝓏]

0x1D504: r'\ensuremath{\mathfrak{A}}',            # MATHEMATICAL FRAKTUR CAPITAL A
0x1D505: r'\ensuremath{\mathfrak{B}}',            # MATHEMATICAL FRAKTUR CAPITAL B
0x1D506: r'\ensuremath{\mathfrak{C}}',            # MATHEMATICAL FRAKTUR CAPITAL C
0x1D507: r'\ensuremath{\mathfrak{D}}',            # MATHEMATICAL FRAKTUR CAPITAL D
0x1D508: r'\ensuremath{\mathfrak{E}}',            # MATHEMATICAL FRAKTUR CAPITAL E
0x1D509: r'\ensuremath{\mathfrak{F}}',            # MATHEMATICAL FRAKTUR CAPITAL F
0x1D50A: r'\ensuremath{\mathfrak{G}}',            # MATHEMATICAL FRAKTUR CAPITAL G
0x1D50B: r'\ensuremath{\mathfrak{H}}',            # MATHEMATICAL FRAKTUR CAPITAL H
0x1D50C: r'\ensuremath{\mathfrak{I}}',            # MATHEMATICAL FRAKTUR CAPITAL I
0x1D50D: r'\ensuremath{\mathfrak{J}}',            # MATHEMATICAL FRAKTUR CAPITAL J
0x1D50E: r'\ensuremath{\mathfrak{K}}',            # MATHEMATICAL FRAKTUR CAPITAL K
0x1D50F: r'\ensuremath{\mathfrak{L}}',            # MATHEMATICAL FRAKTUR CAPITAL L
0x1D510: r'\ensuremath{\mathfrak{M}}',            # MATHEMATICAL FRAKTUR CAPITAL M
0x1D511: r'\ensuremath{\mathfrak{N}}',            # MATHEMATICAL FRAKTUR CAPITAL N
0x1D512: r'\ensuremath{\mathfrak{O}}',            # MATHEMATICAL FRAKTUR CAPITAL O
0x1D513: r'\ensuremath{\mathfrak{P}}',            # MATHEMATICAL FRAKTUR CAPITAL P
0x1D514: r'\ensuremath{\mathfrak{Q}}',            # MATHEMATICAL FRAKTUR CAPITAL Q
0x1D515: r'\ensuremath{\mathfrak{R}}',            # MATHEMATICAL FRAKTUR CAPITAL R
0x1D516: r'\ensuremath{\mathfrak{S}}',            # MATHEMATICAL FRAKTUR CAPITAL S
0x1D517: r'\ensuremath{\mathfrak{T}}',            # MATHEMATICAL FRAKTUR CAPITAL T
0x1D518: r'\ensuremath{\mathfrak{U}}',            # MATHEMATICAL FRAKTUR CAPITAL U
0x1D519: r'\ensuremath{\mathfrak{V}}',            # MATHEMATICAL FRAKTUR CAPITAL V
0x1D51A: r'\ensuremath{\mathfrak{W}}',            # MATHEMATICAL FRAKTUR CAPITAL W
0x1D51B: r'\ensuremath{\mathfrak{X}}',            # MATHEMATICAL FRAKTUR CAPITAL X
0x1D51C: r'\ensuremath{\mathfrak{Y}}',            # MATHEMATICAL FRAKTUR CAPITAL Y
0x1D51D: r'\ensuremath{\mathfrak{Z}}',            # MATHEMATICAL FRAKTUR CAPITAL Z

0x1D51E: r'\ensuremath{\mathfrak{a}}',            # MATHEMATICAL FRAKTUR SMALL a
0x1D51F: r'\ensuremath{\mathfrak{b}}',            # MATHEMATICAL FRAKTUR SMALL b
0x1D520: r'\ensuremath{\mathfrak{c}}',            # MATHEMATICAL FRAKTUR SMALL c
0x1D521: r'\ensuremath{\mathfrak{d}}',            # MATHEMATICAL FRAKTUR SMALL d
0x1D522: r'\ensuremath{\mathfrak{e}}',            # MATHEMATICAL FRAKTUR SMALL e
0x1D523: r'\ensuremath{\mathfrak{f}}',            # MATHEMATICAL FRAKTUR SMALL f
0x1D524: r'\ensuremath{\mathfrak{g}}',            # MATHEMATICAL FRAKTUR SMALL g
0x1D525: r'\ensuremath{\mathfrak{h}}',            # MATHEMATICAL FRAKTUR SMALL h
0x1D526: r'\ensuremath{\mathfrak{i}}',            # MATHEMATICAL FRAKTUR SMALL i
0x1D527: r'\ensuremath{\mathfrak{j}}',            # MATHEMATICAL FRAKTUR SMALL j
0x1D528: r'\ensuremath{\mathfrak{k}}',            # MATHEMATICAL FRAKTUR SMALL k
0x1D529: r'\ensuremath{\mathfrak{l}}',            # MATHEMATICAL FRAKTUR SMALL l
0x1D52A: r'\ensuremath{\mathfrak{m}}',            # MATHEMATICAL FRAKTUR SMALL m
0x1D52B: r'\ensuremath{\mathfrak{n}}',            # MATHEMATICAL FRAKTUR SMALL n
0x1D52C: r'\ensuremath{\mathfrak{o}}',            # MATHEMATICAL FRAKTUR SMALL o
0x1D52D: r'\ensuremath{\mathfrak{p}}',            # MATHEMATICAL FRAKTUR SMALL p
0x1D52E: r'\ensuremath{\mathfrak{q}}',            # MATHEMATICAL FRAKTUR SMALL q
0x1D52F: r'\ensuremath{\mathfrak{r}}',            # MATHEMATICAL FRAKTUR SMALL r
0x1D530: r'\ensuremath{\mathfrak{s}}',            # MATHEMATICAL FRAKTUR SMALL s
0x1D531: r'\ensuremath{\mathfrak{t}}',            # MATHEMATICAL FRAKTUR SMALL t
0x1D532: r'\ensuremath{\mathfrak{u}}',            # MATHEMATICAL FRAKTUR SMALL u
0x1D533: r'\ensuremath{\mathfrak{v}}',            # MATHEMATICAL FRAKTUR SMALL v
0x1D534: r'\ensuremath{\mathfrak{w}}',            # MATHEMATICAL FRAKTUR SMALL w
0x1D535: r'\ensuremath{\mathfrak{x}}',            # MATHEMATICAL FRAKTUR SMALL x
0x1D536: r'\ensuremath{\mathfrak{y}}',            # MATHEMATICAL FRAKTUR SMALL y
0x1D537: r'\ensuremath{\mathfrak{z}}',            # MATHEMATICAL FRAKTUR SMALL z

0x1D538: r'\ensuremath{\mathbb{A}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL A
0x1D539: r'\ensuremath{\mathbb{B}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL B
0x1D53A: r'\ensuremath{\mathbb{C}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL C
0x1D53B: r'\ensuremath{\mathbb{D}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL D
0x1D53C: r'\ensuremath{\mathbb{E}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL E
0x1D53D: r'\ensuremath{\mathbb{F}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL F
0x1D53E: r'\ensuremath{\mathbb{G}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL G
0x1D53F: r'\ensuremath{\mathbb{H}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL H
0x1D540: r'\ensuremath{\mathbb{I}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL I
0x1D541: r'\ensuremath{\mathbb{J}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL J
0x1D542: r'\ensuremath{\mathbb{K}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL K
0x1D543: r'\ensuremath{\mathbb{L}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL L
0x1D544: r'\ensuremath{\mathbb{M}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL M
0x1D545: r'\ensuremath{\mathbb{N}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL N
0x1D546: r'\ensuremath{\mathbb{O}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL O
0x1D547: r'\ensuremath{\mathbb{P}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL P
0x1D548: r'\ensuremath{\mathbb{Q}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL Q
0x1D549: r'\ensuremath{\mathbb{R}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL R
0x1D54A: r'\ensuremath{\mathbb{S}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL S
0x1D54B: r'\ensuremath{\mathbb{T}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL T
0x1D54C: r'\ensuremath{\mathbb{U}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL U
0x1D54D: r'\ensuremath{\mathbb{V}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL V
0x1D54E: r'\ensuremath{\mathbb{W}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL W
0x1D54F: r'\ensuremath{\mathbb{X}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL X
0x1D550: r'\ensuremath{\mathbb{Y}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL Y
0x1D551: r'\ensuremath{\mathbb{Z}}',              # MATHEMATICAL DOUBLE-STRUCK CAPITAL Z
0x1D552: r'\ensuremath{\mathbb{a}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL A [𝕒]
0x1D553: r'\ensuremath{\mathbb{b}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL B [𝕓]
0x1D554: r'\ensuremath{\mathbb{c}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL C [𝕔]
0x1D555: r'\ensuremath{\mathbb{d}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL D [𝕕]
0x1D556: r'\ensuremath{\mathbb{e}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL E [𝕖]
0x1D557: r'\ensuremath{\mathbb{f}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL F [𝕗]
0x1D558: r'\ensuremath{\mathbb{g}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL G [𝕘]
0x1D559: r'\ensuremath{\mathbb{h}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL H [𝕙]
0x1D55A: r'\ensuremath{\mathbb{i}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL I [𝕚]
0x1D55B: r'\ensuremath{\mathbb{j}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL J [𝕛]
0x1D55C: r'\ensuremath{\mathbb{k}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL K [𝕜]
0x1D55D: r'\ensuremath{\mathbb{l}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL L [𝕝]
0x1D55E: r'\ensuremath{\mathbb{m}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL M [𝕞]
0x1D55F: r'\ensuremath{\mathbb{n}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL N [𝕟]
0x1D560: r'\ensuremath{\mathbb{o}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL O [𝕠]
0x1D561: r'\ensuremath{\mathbb{p}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL P [𝕡]
0x1D562: r'\ensuremath{\mathbb{q}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL Q [𝕢]
0x1D563: r'\ensuremath{\mathbb{r}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL R [𝕣]
0x1D564: r'\ensuremath{\mathbb{s}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL S [𝕤]
0x1D565: r'\ensuremath{\mathbb{t}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL T [𝕥]
0x1D566: r'\ensuremath{\mathbb{u}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL U [𝕦]
0x1D567: r'\ensuremath{\mathbb{v}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL V [𝕧]
0x1D568: r'\ensuremath{\mathbb{w}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL W [𝕨]
0x1D569: r'\ensuremath{\mathbb{x}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL X [𝕩]
0x1D56A: r'\ensuremath{\mathbb{y}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL Y [𝕪]
0x1D56B: r'\ensuremath{\mathbb{z}}',                           # MATHEMATICAL DOUBLE-STRUCK SMALL Z [𝕫]

0x1D5A0: r'\ensuremath{\mathsf{A}}',                           # MATHEMATICAL SANS-SERIF CAPITAL A [𝖠]
0x1D5A1: r'\ensuremath{\mathsf{B}}',                           # MATHEMATICAL SANS-SERIF CAPITAL B [𝖡]
0x1D5A2: r'\ensuremath{\mathsf{C}}',                           # MATHEMATICAL SANS-SERIF CAPITAL C [𝖢]
0x1D5A3: r'\ensuremath{\mathsf{D}}',                           # MATHEMATICAL SANS-SERIF CAPITAL D [𝖣]
0x1D5A4: r'\ensuremath{\mathsf{E}}',                           # MATHEMATICAL SANS-SERIF CAPITAL E [𝖤]
0x1D5A5: r'\ensuremath{\mathsf{F}}',                           # MATHEMATICAL SANS-SERIF CAPITAL F [𝖥]
0x1D5A6: r'\ensuremath{\mathsf{G}}',                           # MATHEMATICAL SANS-SERIF CAPITAL G [𝖦]
0x1D5A7: r'\ensuremath{\mathsf{H}}',                           # MATHEMATICAL SANS-SERIF CAPITAL H [𝖧]
0x1D5A8: r'\ensuremath{\mathsf{I}}',                           # MATHEMATICAL SANS-SERIF CAPITAL I [𝖨]
0x1D5A9: r'\ensuremath{\mathsf{J}}',                           # MATHEMATICAL SANS-SERIF CAPITAL J [𝖩]
0x1D5AA: r'\ensuremath{\mathsf{K}}',                           # MATHEMATICAL SANS-SERIF CAPITAL K [𝖪]
0x1D5AB: r'\ensuremath{\mathsf{L}}',                           # MATHEMATICAL SANS-SERIF CAPITAL L [𝖫]
0x1D5AC: r'\ensuremath{\mathsf{M}}',                           # MATHEMATICAL SANS-SERIF CAPITAL M [𝖬]
0x1D5AD: r'\ensuremath{\mathsf{N}}',                           # MATHEMATICAL SANS-SERIF CAPITAL N [𝖭]
0x1D5AE: r'\ensuremath{\mathsf{O}}',                           # MATHEMATICAL SANS-SERIF CAPITAL O [𝖮]
0x1D5AF: r'\ensuremath{\mathsf{P}}',                           # MATHEMATICAL SANS-SERIF CAPITAL P [𝖯]
0x1D5B0: r'\ensuremath{\mathsf{Q}}',                           # MATHEMATICAL SANS-SERIF CAPITAL Q [𝖰]
0x1D5B1: r'\ensuremath{\mathsf{R}}',                           # MATHEMATICAL SANS-SERIF CAPITAL R [𝖱]
0x1D5B2: r'\ensuremath{\mathsf{S}}',                           # MATHEMATICAL SANS-SERIF CAPITAL S [𝖲]
0x1D5B3: r'\ensuremath{\mathsf{T}}',                           # MATHEMATICAL SANS-SERIF CAPITAL T [𝖳]
0x1D5B4: r'\ensuremath{\mathsf{U}}',                           # MATHEMATICAL SANS-SERIF CAPITAL U [𝖴]
0x1D5B5: r'\ensuremath{\mathsf{V}}',                           # MATHEMATICAL SANS-SERIF CAPITAL V [𝖵]
0x1D5B6: r'\ensuremath{\mathsf{W}}',                           # MATHEMATICAL SANS-SERIF CAPITAL W [𝖶]
0x1D5B7: r'\ensuremath{\mathsf{X}}',                           # MATHEMATICAL SANS-SERIF CAPITAL X [𝖷]
0x1D5B8: r'\ensuremath{\mathsf{Y}}',                           # MATHEMATICAL SANS-SERIF CAPITAL Y [𝖸]
0x1D5B9: r'\ensuremath{\mathsf{Z}}',                           # MATHEMATICAL SANS-SERIF CAPITAL Z [𝖹]
0x1D5BA: r'\ensuremath{\mathsf{a}}',                           # MATHEMATICAL SANS-SERIF SMALL A [𝖺]
0x1D5BB: r'\ensuremath{\mathsf{b}}',                           # MATHEMATICAL SANS-SERIF SMALL B [𝖻]
0x1D5BC: r'\ensuremath{\mathsf{c}}',                           # MATHEMATICAL SANS-SERIF SMALL C [𝖼]
0x1D5BD: r'\ensuremath{\mathsf{d}}',                           # MATHEMATICAL SANS-SERIF SMALL D [𝖽]
0x1D5BE: r'\ensuremath{\mathsf{e}}',                           # MATHEMATICAL SANS-SERIF SMALL E [𝖾]
0x1D5BF: r'\ensuremath{\mathsf{f}}',                           # MATHEMATICAL SANS-SERIF SMALL F [𝖿]
0x1D5C0: r'\ensuremath{\mathsf{g}}',                           # MATHEMATICAL SANS-SERIF SMALL G [𝗀]
0x1D5C1: r'\ensuremath{\mathsf{h}}',                           # MATHEMATICAL SANS-SERIF SMALL H [𝗁]
0x1D5C2: r'\ensuremath{\mathsf{i}}',                           # MATHEMATICAL SANS-SERIF SMALL I [𝗂]
0x1D5C3: r'\ensuremath{\mathsf{j}}',                           # MATHEMATICAL SANS-SERIF SMALL J [𝗃]
0x1D5C4: r'\ensuremath{\mathsf{k}}',                           # MATHEMATICAL SANS-SERIF SMALL K [𝗄]
0x1D5C5: r'\ensuremath{\mathsf{l}}',                           # MATHEMATICAL SANS-SERIF SMALL L [𝗅]
0x1D5C6: r'\ensuremath{\mathsf{m}}',                           # MATHEMATICAL SANS-SERIF SMALL M [𝗆]
0x1D5C7: r'\ensuremath{\mathsf{n}}',                           # MATHEMATICAL SANS-SERIF SMALL N [𝗇]
0x1D5C8: r'\ensuremath{\mathsf{o}}',                           # MATHEMATICAL SANS-SERIF SMALL O [𝗈]
0x1D5C9: r'\ensuremath{\mathsf{p}}',                           # MATHEMATICAL SANS-SERIF SMALL P [𝗉]
0x1D5CA: r'\ensuremath{\mathsf{q}}',                           # MATHEMATICAL SANS-SERIF SMALL Q [𝗊]
0x1D5CB: r'\ensuremath{\mathsf{r}}',                           # MATHEMATICAL SANS-SERIF SMALL R [𝗋]
0x1D5CC: r'\ensuremath{\mathsf{s}}',                           # MATHEMATICAL SANS-SERIF SMALL S [𝗌]
0x1D5CD: r'\ensuremath{\mathsf{t}}',                           # MATHEMATICAL SANS-SERIF SMALL T [𝗍]
0x1D5CE: r'\ensuremath{\mathsf{u}}',                           # MATHEMATICAL SANS-SERIF SMALL U [𝗎]
0x1D5CF: r'\ensuremath{\mathsf{v}}',                           # MATHEMATICAL SANS-SERIF SMALL V [𝗏]
0x1D5D0: r'\ensuremath{\mathsf{w}}',                           # MATHEMATICAL SANS-SERIF SMALL W [𝗐]
0x1D5D1: r'\ensuremath{\mathsf{x}}',                           # MATHEMATICAL SANS-SERIF SMALL X [𝗑]
0x1D5D2: r'\ensuremath{\mathsf{y}}',                           # MATHEMATICAL SANS-SERIF SMALL Y [𝗒]
0x1D5D3: r'\ensuremath{\mathsf{z}}',                           # MATHEMATICAL SANS-SERIF SMALL Z [𝗓]

0x1D670: r'\ensuremath{\mathtt{A}}',                           # MATHEMATICAL MONOSPACE CAPITAL A [𝙰]
0x1D671: r'\ensuremath{\mathtt{B}}',                           # MATHEMATICAL MONOSPACE CAPITAL B [𝙱]
0x1D672: r'\ensuremath{\mathtt{C}}',                           # MATHEMATICAL MONOSPACE CAPITAL C [𝙲]
0x1D673: r'\ensuremath{\mathtt{D}}',                           # MATHEMATICAL MONOSPACE CAPITAL D [𝙳]
0x1D674: r'\ensuremath{\mathtt{E}}',                           # MATHEMATICAL MONOSPACE CAPITAL E [𝙴]
0x1D675: r'\ensuremath{\mathtt{F}}',                           # MATHEMATICAL MONOSPACE CAPITAL F [𝙵]
0x1D676: r'\ensuremath{\mathtt{G}}',                           # MATHEMATICAL MONOSPACE CAPITAL G [𝙶]
0x1D677: r'\ensuremath{\mathtt{H}}',                           # MATHEMATICAL MONOSPACE CAPITAL H [𝙷]
0x1D678: r'\ensuremath{\mathtt{I}}',                           # MATHEMATICAL MONOSPACE CAPITAL I [𝙸]
0x1D679: r'\ensuremath{\mathtt{J}}',                           # MATHEMATICAL MONOSPACE CAPITAL J [𝙹]
0x1D67A: r'\ensuremath{\mathtt{K}}',                           # MATHEMATICAL MONOSPACE CAPITAL K [𝙺]
0x1D67B: r'\ensuremath{\mathtt{L}}',                           # MATHEMATICAL MONOSPACE CAPITAL L [𝙻]
0x1D67C: r'\ensuremath{\mathtt{M}}',                           # MATHEMATICAL MONOSPACE CAPITAL M [𝙼]
0x1D67D: r'\ensuremath{\mathtt{N}}',                           # MATHEMATICAL MONOSPACE CAPITAL N [𝙽]
0x1D67E: r'\ensuremath{\mathtt{O}}',                           # MATHEMATICAL MONOSPACE CAPITAL O [𝙾]
0x1D67F: r'\ensuremath{\mathtt{P}}',                           # MATHEMATICAL MONOSPACE CAPITAL P [𝙿]
0x1D680: r'\ensuremath{\mathtt{Q}}',                           # MATHEMATICAL MONOSPACE CAPITAL Q [𝚀]
0x1D681: r'\ensuremath{\mathtt{R}}',                           # MATHEMATICAL MONOSPACE CAPITAL R [𝚁]
0x1D682: r'\ensuremath{\mathtt{S}}',                           # MATHEMATICAL MONOSPACE CAPITAL S [𝚂]
0x1D683: r'\ensuremath{\mathtt{T}}',                           # MATHEMATICAL MONOSPACE CAPITAL T [𝚃]
0x1D684: r'\ensuremath{\mathtt{U}}',                           # MATHEMATICAL MONOSPACE CAPITAL U [𝚄]
0x1D685: r'\ensuremath{\mathtt{V}}',                           # MATHEMATICAL MONOSPACE CAPITAL V [𝚅]
0x1D686: r'\ensuremath{\mathtt{W}}',                           # MATHEMATICAL MONOSPACE CAPITAL W [𝚆]
0x1D687: r'\ensuremath{\mathtt{X}}',                           # MATHEMATICAL MONOSPACE CAPITAL X [𝚇]
0x1D688: r'\ensuremath{\mathtt{Y}}',                           # MATHEMATICAL MONOSPACE CAPITAL Y [𝚈]
0x1D689: r'\ensuremath{\mathtt{Z}}',                           # MATHEMATICAL MONOSPACE CAPITAL Z [𝚉]
0x1D68A: r'\ensuremath{\mathtt{a}}',                           # MATHEMATICAL MONOSPACE SMALL A [𝚊]
0x1D68B: r'\ensuremath{\mathtt{b}}',                           # MATHEMATICAL MONOSPACE SMALL B [𝚋]
0x1D68C: r'\ensuremath{\mathtt{c}}',                           # MATHEMATICAL MONOSPACE SMALL C [𝚌]
0x1D68D: r'\ensuremath{\mathtt{d}}',                           # MATHEMATICAL MONOSPACE SMALL D [𝚍]
0x1D68E: r'\ensuremath{\mathtt{e}}',                           # MATHEMATICAL MONOSPACE SMALL E [𝚎]
0x1D68F: r'\ensuremath{\mathtt{f}}',                           # MATHEMATICAL MONOSPACE SMALL F [𝚏]
0x1D690: r'\ensuremath{\mathtt{g}}',                           # MATHEMATICAL MONOSPACE SMALL G [𝚐]
0x1D691: r'\ensuremath{\mathtt{h}}',                           # MATHEMATICAL MONOSPACE SMALL H [𝚑]
0x1D692: r'\ensuremath{\mathtt{i}}',                           # MATHEMATICAL MONOSPACE SMALL I [𝚒]
0x1D693: r'\ensuremath{\mathtt{j}}',                           # MATHEMATICAL MONOSPACE SMALL J [𝚓]
0x1D694: r'\ensuremath{\mathtt{k}}',                           # MATHEMATICAL MONOSPACE SMALL K [𝚔]
0x1D695: r'\ensuremath{\mathtt{l}}',                           # MATHEMATICAL MONOSPACE SMALL L [𝚕]
0x1D696: r'\ensuremath{\mathtt{m}}',                           # MATHEMATICAL MONOSPACE SMALL M [𝚖]
0x1D697: r'\ensuremath{\mathtt{n}}',                           # MATHEMATICAL MONOSPACE SMALL N [𝚗]
0x1D698: r'\ensuremath{\mathtt{o}}',                           # MATHEMATICAL MONOSPACE SMALL O [𝚘]
0x1D699: r'\ensuremath{\mathtt{p}}',                           # MATHEMATICAL MONOSPACE SMALL P [𝚙]
0x1D69A: r'\ensuremath{\mathtt{q}}',                           # MATHEMATICAL MONOSPACE SMALL Q [𝚚]
0x1D69B: r'\ensuremath{\mathtt{r}}',                           # MATHEMATICAL MONOSPACE SMALL R [𝚛]
0x1D69C: r'\ensuremath{\mathtt{s}}',                           # MATHEMATICAL MONOSPACE SMALL S [𝚜]
0x1D69D: r'\ensuremath{\mathtt{t}}',                           # MATHEMATICAL MONOSPACE SMALL T [𝚝]
0x1D69E: r'\ensuremath{\mathtt{u}}',                           # MATHEMATICAL MONOSPACE SMALL U [𝚞]
0x1D69F: r'\ensuremath{\mathtt{v}}',                           # MATHEMATICAL MONOSPACE SMALL V [𝚟]
0x1D6A0: r'\ensuremath{\mathtt{w}}',                           # MATHEMATICAL MONOSPACE SMALL W [𝚠]
0x1D6A1: r'\ensuremath{\mathtt{x}}',                           # MATHEMATICAL MONOSPACE SMALL X [𝚡]
0x1D6A2: r'\ensuremath{\mathtt{y}}',                           # MATHEMATICAL MONOSPACE SMALL Y [𝚢]
0x1D6A3: r'\ensuremath{\mathtt{z}}',                           # MATHEMATICAL MONOSPACE SMALL Z [𝚣]

0x1D7CE: r'\ensuremath{\mathbf{0}}',                           # MATHEMATICAL BOLD DIGIT ZERO [𝟎]
0x1D7CF: r'\ensuremath{\mathbf{1}}',                           # MATHEMATICAL BOLD DIGIT ONE [𝟏]
0x1D7D0: r'\ensuremath{\mathbf{2}}',                           # MATHEMATICAL BOLD DIGIT TWO [𝟐]
0x1D7D1: r'\ensuremath{\mathbf{3}}',                           # MATHEMATICAL BOLD DIGIT THREE [𝟑]
0x1D7D2: r'\ensuremath{\mathbf{4}}',                           # MATHEMATICAL BOLD DIGIT FOUR [𝟒]
0x1D7D3: r'\ensuremath{\mathbf{5}}',                           # MATHEMATICAL BOLD DIGIT FIVE [𝟓]
0x1D7D4: r'\ensuremath{\mathbf{6}}',                           # MATHEMATICAL BOLD DIGIT SIX [𝟔]
0x1D7D5: r'\ensuremath{\mathbf{7}}',                           # MATHEMATICAL BOLD DIGIT SEVEN [𝟕]
0x1D7D6: r'\ensuremath{\mathbf{8}}',                           # MATHEMATICAL BOLD DIGIT EIGHT [𝟖]
0x1D7D7: r'\ensuremath{\mathbf{9}}',                           # MATHEMATICAL BOLD DIGIT NINE [𝟗]
0x1D7D8: r'\ensuremath{\mathbb{0}}',                           # MATHEMATICAL DOUBLE-STRUCK DIGIT ZERO [𝟘]
0x1D7D9: r'\ensuremath{\mathbb{1}}',                           # MATHEMATICAL DOUBLE-STRUCK DIGIT ONE [𝟙]
0x1D7DA: r'\ensuremath{\mathbb{2}}',                           # MATHEMATICAL DOUBLE-STRUCK DIGIT TWO [𝟚]
0x1D7DB: r'\ensuremath{\mathbb{3}}',                           # MATHEMATICAL DOUBLE-STRUCK DIGIT THREE [𝟛]
0x1D7DC: r'\ensuremath{\mathbb{4}}',                           # MATHEMATICAL DOUBLE-STRUCK DIGIT FOUR [𝟜]
0x1D7DD: r'\ensuremath{\mathbb{5}}',                           # MATHEMATICAL DOUBLE-STRUCK DIGIT FIVE [𝟝]
0x1D7DE: r'\ensuremath{\mathbb{6}}',                           # MATHEMATICAL DOUBLE-STRUCK DIGIT SIX [𝟞]
0x1D7DF: r'\ensuremath{\mathbb{7}}',                           # MATHEMATICAL DOUBLE-STRUCK DIGIT SEVEN [𝟟]
0x1D7E0: r'\ensuremath{\mathbb{8}}',                           # MATHEMATICAL DOUBLE-STRUCK DIGIT EIGHT [𝟠]
0x1D7E1: r'\ensuremath{\mathbb{9}}',                           # MATHEMATICAL DOUBLE-STRUCK DIGIT NINE [𝟡]
0x1D7E2: r'\ensuremath{\mathsf{0}}',                           # MATHEMATICAL SANS-SERIF DIGIT ZERO [𝟢]
0x1D7E3: r'\ensuremath{\mathsf{1}}',                           # MATHEMATICAL SANS-SERIF DIGIT ONE [𝟣]
0x1D7E4: r'\ensuremath{\mathsf{2}}',                           # MATHEMATICAL SANS-SERIF DIGIT TWO [𝟤]
0x1D7E5: r'\ensuremath{\mathsf{3}}',                           # MATHEMATICAL SANS-SERIF DIGIT THREE [𝟥]
0x1D7E6: r'\ensuremath{\mathsf{4}}',                           # MATHEMATICAL SANS-SERIF DIGIT FOUR [𝟦]
0x1D7E7: r'\ensuremath{\mathsf{5}}',                           # MATHEMATICAL SANS-SERIF DIGIT FIVE [𝟧]
0x1D7E8: r'\ensuremath{\mathsf{6}}',                           # MATHEMATICAL SANS-SERIF DIGIT SIX [𝟨]
0x1D7E9: r'\ensuremath{\mathsf{7}}',                           # MATHEMATICAL SANS-SERIF DIGIT SEVEN [𝟩]
0x1D7EA: r'\ensuremath{\mathsf{8}}',                           # MATHEMATICAL SANS-SERIF DIGIT EIGHT [𝟪]
0x1D7EB: r'\ensuremath{\mathsf{9}}',                           # MATHEMATICAL SANS-SERIF DIGIT NINE [𝟫]

0x1D7F6: r'\ensuremath{\mathtt{0}}',                           # MATHEMATICAL MONOSPACE DIGIT ZERO [𝟶]
0x1D7F7: r'\ensuremath{\mathtt{1}}',                           # MATHEMATICAL MONOSPACE DIGIT ONE [𝟷]
0x1D7F8: r'\ensuremath{\mathtt{2}}',                           # MATHEMATICAL MONOSPACE DIGIT TWO [𝟸]
0x1D7F9: r'\ensuremath{\mathtt{3}}',                           # MATHEMATICAL MONOSPACE DIGIT THREE [𝟹]
0x1D7FA: r'\ensuremath{\mathtt{4}}',                           # MATHEMATICAL MONOSPACE DIGIT FOUR [𝟺]
0x1D7FB: r'\ensuremath{\mathtt{5}}',                           # MATHEMATICAL MONOSPACE DIGIT FIVE [𝟻]
0x1D7FC: r'\ensuremath{\mathtt{6}}',                           # MATHEMATICAL MONOSPACE DIGIT SIX [𝟼]
0x1D7FD: r'\ensuremath{\mathtt{7}}',                           # MATHEMATICAL MONOSPACE DIGIT SEVEN [𝟽]
0x1D7FE: r'\ensuremath{\mathtt{8}}',                           # MATHEMATICAL MONOSPACE DIGIT EIGHT [𝟾]
0x1D7FF: r'\ensuremath{\mathtt{9}}',                           # MATHEMATICAL MONOSPACE DIGIT NINE [𝟿]


}

