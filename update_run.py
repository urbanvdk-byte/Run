from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

if '<td>04.08.2026</td>' in s:
    raise SystemExit(0)


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise RuntimeError(f'Marker not found: {old[:140]}')
    return text.replace(old, new, 1)

# Main season table
last_row = "<tr class='type-aerobic'><td>30.07.2026</td><td>Аэробная мощность (рельеф)</td><td>10.01</td><td>1:02:23</td><td>6:14</td><td>157/171</td><td>168</td><td>118</td><td>—</td><td>3.8/3.2</td></tr>"
new_row = "<tr class='type-easy'><td>04.08.2026</td><td>Лёгкий бег (рельеф)</td><td>4.31</td><td>26:14</td><td>6:06</td><td>155/171</td><td>166</td><td>65</td><td>—</td><td>2.6/2.0</td></tr>"
s = replace_once(s, last_row + "</tbody></table>", last_row + new_row + "</tbody></table>")

# Coach note
progress_marker = "</div></div></div></div><div class='section-title'>Прогресс ключевых показателей</div>"
new_note = (
    "<div class='note-card'><div class='note-header' style='background:#d4edda'>"
    "<strong>04.08.2026 — Лёгкий бег (рельеф)</strong>"
    "<span class='meta'>Маршрут: Владивосток, рельеф &nbsp;|&nbsp; Борг: —</span></div>"
    "<div class='note-body'><div class='text'>"
    "Короткий аэробный бег между силовыми тренировками А (03.08) и Б (05.08). "
    "По сравнению с похожей пробежкой 02.07 темп улучшился с 6:34 до 6:06 мин/км при почти том же среднем пульсе (154 → 155), "
    "несмотря на больший набор высоты (43 → 65 м). Это хороший признак улучшения аэробной экономичности. "
    "Каденс немного снизился с 168 до 166, но остаётся стабильным; среднее время контакта с землёй — 264 мс. "
    "ТЭ 2.6/2.0 указывает на умеренную нагрузку: это не восстановительная прогулка, поэтому следующую пробежку проводить легко, без одновременного увеличения дистанции и скорости."
    "</div><div class='stats'>"
    "Дист: <span>4.31 км</span> &nbsp;|&nbsp; Время: <span>26:14</span> &nbsp;|&nbsp; Темп: <span>6:06</span><br>"
    "Пульс: <span>155/171</span> &nbsp;|&nbsp; Каденс: <span>166</span> &nbsp;|&nbsp; Набор: <span>65 м</span><br>"
    "ТЭ: <span>2.6 / 2.0</span> &nbsp;|&nbsp; Лучший темп: <span>5:46</span> &nbsp;|&nbsp; Приведённый темп: <span>5:54</span> &nbsp;|&nbsp; Длина шага: <span>99 см</span> &nbsp;|&nbsp; Время на земле: <span>264 мс</span>"
    "</div></div></div>"
)
s = replace_once(
    s,
    progress_marker,
    "</div></div></div>" + new_note + "</div><div class='section-title'>Прогресс ключевых показателей</div>",
)

# Progress table
s = replace_once(s, "<th>28.06</th><th>02.07</th><th>30.07</th><th>Динамика</th>", "<th>28.06</th><th>02.07</th><th>30.07</th><th>04.08</th><th>Динамика</th>")
s = replace_once(s, "<td><strong>168</strong></td><td class='indicator'>Стабильно 168 ✓</td>", "<td><strong>168</strong></td><td>166</td><td class='indicator'>Стабильно 166–168 ✓</td>")
s = replace_once(s, "<td>157</td><td class='indicator'>Рабочая интенсивность</td>", "<td>157</td><td>155</td><td class='indicator'>Темп быстрее при том же пульсе ✓</td>")
s = replace_once(s, "<td>10.01</td><td class='indicator'>10 км на рельефе ✓</td>", "<td>10.01</td><td>4.31</td><td class='indicator'>Короткая аэробная работа</td>")
s = replace_once(s, "<td><strong>3.8</strong></td><td class='indicator'>Развивающий стимул ✓</td>", "<td><strong>3.8</strong></td><td>2.6</td><td class='indicator'>Умеренный стимул</td>")
s = replace_once(s, "<td><strong>6:14</strong></td><td class='indicator'>Быстрее 18.06 на 16 сек/км ✓</td>", "<td><strong>6:14</strong></td><td><strong>6:06</strong></td><td class='indicator'>02.07 быстрее на 28 сек/км при том же пульсе ✓</td>")
s = replace_once(s, "<td>5:29</td><td class='indicator'>Стабильно на рельефе</td>", "<td>5:29</td><td>5:46</td><td class='indicator'>Контролируемо без рывков</td>")
s = replace_once(s, "<td><strong>261</strong></td><td class='indicator'>Экономичность улучшилась ✓</td>", "<td><strong>261</strong></td><td>264</td><td class='indicator'>Стабильно 261–264 мс</td>")
s = replace_once(s, "<td>118</td><td class='indicator'>Высокий рельеф ✓</td>", "<td>118</td><td>65</td><td class='indicator'>Рельефная работа ✓</td>")

p.write_text(s, encoding='utf-8')
