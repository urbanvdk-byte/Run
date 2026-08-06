from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

if '<td>30.07.2026</td>' in s:
    raise SystemExit(0)


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise RuntimeError(f'Marker not found: {old[:120]}')
    return text.replace(old, new, 1)

# Main season table
last_row = "<tr class='type-base'><td>02.07.2026</td><td>База (набережная)</td><td>4.89</td><td>32:08</td><td>6:34</td><td>154/170</td><td>168</td><td>43</td><td>—</td><td>2.7/1.1</td></tr>"
new_row = "<tr class='type-aerobic'><td>30.07.2026</td><td>Аэробная мощность (рельеф)</td><td>10.01</td><td>1:02:23</td><td>6:14</td><td>157/171</td><td>168</td><td>118</td><td>—</td><td>3.8/3.2</td></tr>"
s = replace_once(s, last_row + "</tbody></table>", last_row + new_row + "</tbody></table>")

# Coach note
progress_marker = "</div></div></div></div><div class='section-title'>Прогресс ключевых показателей</div>"
new_note = (
    "<div class='note-card'><div class='note-header' style='background:#cce5ff'>"
    "<strong>30.07.2026 — Аэробная мощность (рельеф)</strong>"
    "<span class='meta'>Маршрут: Владивосток, рельеф &nbsp;|&nbsp; Борг: —</span></div>"
    "<div class='note-body'><div class='text'>"
    "10 км по выраженному рельефу: набор 118 м, средний темп 6:14 при пульсе 157. "
    "По сравнению с похожей тренировкой 18.06 темп улучшился на 16 сек/км при чуть большем наборе (+11 м), "
    "но средний пульс вырос на 6 уд/мин и анаэробный ТЭ — до 3.2. Каденс 168 и время на земле 261 мс — техника стабильна. "
    "ТН 230 (высокая). Пробежка выполнена на следующий день после силовой Б с выпадами и икрами, поэтому такое сочетание не повторять перед ключевым бегом. "
    "Следующая похожая работа: те же 10 км без ускорения дистанции, удерживать пульс примерно до 155–158 и оценить ровность второй половины."
    "</div><div class='stats'>"
    "Дист: <span>10.01 км</span> &nbsp;|&nbsp; Время: <span>1:02:23</span> &nbsp;|&nbsp; Темп: <span>6:14</span><br>"
    "Пульс: <span>157/171</span> &nbsp;|&nbsp; Каденс: <span>168</span> &nbsp;|&nbsp; Набор: <span>118 м</span><br>"
    "ТЭ: <span>3.8 / 3.2</span> &nbsp;|&nbsp; Лучший темп: <span>5:29</span> &nbsp;|&nbsp; Мощность: <span>230 Вт</span> &nbsp;|&nbsp; Время на земле: <span>261 мс</span> &nbsp;|&nbsp; ТН: <span>230</span>"
    "</div></div></div>"
)
s = replace_once(
    s,
    progress_marker,
    "</div></div></div>" + new_note + "</div><div class='section-title'>Прогресс ключевых показателей</div>",
)

# Progress table
s = replace_once(s, "<th>28.06</th><th>02.07</th><th>Динамика</th>", "<th>28.06</th><th>02.07</th><th>30.07</th><th>Динамика</th>")
s = replace_once(s, "<td class='indicator'>Рост до 168 ✓</td>", "<td><strong>168</strong></td><td class='indicator'>Стабильно 168 ✓</td>")
s = replace_once(s, "<td class='indicator'>Стабильно ✓</td>", "<td>157</td><td class='indicator'>Рабочая интенсивность</td>")
s = replace_once(s, "<td class='indicator'>Рекорд 18.00 км ✓</td>", "<td>10.01</td><td class='indicator'>10 км на рельефе ✓</td>")
s = replace_once(s, "<td class='indicator'>Поддерживающий ✓</td>", "<td><strong>3.8</strong></td><td class='indicator'>Развивающий стимул ✓</td>")
s = replace_once(s, "<td class='indicator'>Лёгкая база ✓</td>", "<td><strong>6:14</strong></td><td class='indicator'>Быстрее 18.06 на 16 сек/км ✓</td>")
s = replace_once(s, "<td class='indicator'>Рекорд 4:24 ✓</td>", "<td>5:29</td><td class='indicator'>Стабильно на рельефе</td>")
s = replace_once(s, "<td class='indicator'>266 мс легко ✓</td>", "<td><strong>261</strong></td><td class='indicator'>Экономичность улучшилась ✓</td>")
s = replace_once(s, "<td class='indicator'>Рекорд 183 м ✓</td>", "<td>118</td><td class='indicator'>Высокий рельеф ✓</td>")

p.write_text(s, encoding='utf-8')
