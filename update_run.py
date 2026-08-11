from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

if '<td>11.08.2026</td>' in s:
    raise SystemExit(0)


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise RuntimeError(f'Marker not found: {old[:180]}')
    return text.replace(old, new, 1)

# Main season table
last_row = "<tr class='type-aerobic'><td>06.08.2026</td><td>Аэробная работа (ровно)</td><td>5.01</td><td>27:43</td><td>5:32</td><td>158/179</td><td>175</td><td>14</td><td>—</td><td>2.6/2.5</td></tr>"
new_row = "<tr class='type-aerobic'><td>11.08.2026</td><td>Аэробная работа (рельеф)</td><td>4.73</td><td>26:44</td><td>5:39</td><td>155/172</td><td>171</td><td>72</td><td>—</td><td>2.5/2.3</td></tr>"
s = replace_once(s, last_row + "</tbody></table>", last_row + new_row + "</tbody></table>")

# Coach note
progress_marker = "</div></div></div></div><div class='section-title'>Прогресс ключевых показателей</div>"
new_note = (
    "<div class='note-card'><div class='note-header' style='background:#cce5ff'>"
    "<strong>11.08.2026 — Аэробная работа (рельеф)</strong>"
    "<span class='meta'>Маршрут: Приморский край, рельеф &nbsp;|&nbsp; Борг: —</span></div>"
    "<div class='note-body'><div class='text'>"
    "Короткая рельефная аэробная работа на следующий день после силовой Б. "
    "По сравнению с 04.08 на похожем рельефе темп улучшился с 6:06 до 5:39 мин/км при том же среднем пульсе 155 и близком наборе (65 → 72 м); каденс вырос с 166 до 171. "
    "По сравнению с более ровной 06.08 темп всего на 7 сек/км медленнее, но средний пульс ниже на 3 уд/мин; приведённый темп 5:34 почти совпадает с фактическим темпом 06.08 5:32. "
    "Это сильный признак улучшения аэробной экономичности на рельефе. Средняя мощность около 282 Вт, время контакта с землёй 251 мс, длина шага около 102 см, коэффициент шага около 8.5%, высота шага около 8.9 см. "
    "ТЭ 2.5/2.3 означает умеренную развивающую нагрузку, а не восстановительный бег. После вчерашних выпадов следующая пробежка должна быть лёгкой или после дня отдыха; интервалы подряд не ставить."
    "</div><div class='stats'>"
    "Дист: <span>4.73 км</span> &nbsp;|&nbsp; Время: <span>26:44</span> &nbsp;|&nbsp; Темп: <span>5:39</span><br>"
    "Пульс: <span>155/172</span> &nbsp;|&nbsp; Каденс: <span>171</span> &nbsp;|&nbsp; Набор: <span>72 м</span><br>"
    "ТЭ: <span>2.5 / 2.3</span> &nbsp;|&nbsp; Лучший темп: <span>5:06</span> &nbsp;|&nbsp; Приведённый темп: <span>5:34</span><br>"
    "Калории: <span>373</span> &nbsp;|&nbsp; Длина шага: <span>102 см</span> &nbsp;|&nbsp; Мощность: <span>282 Вт ср. / 372 Вт макс.</span> &nbsp;|&nbsp; Контакт с землёй: <span>251 мс</span>"
    "</div></div></div>"
)
s = replace_once(
    s,
    progress_marker,
    "</div></div></div>" + new_note + "</div><div class='section-title'>Прогресс ключевых показателей</div>",
)

# Progress table
s = replace_once(s, "<th>28.06</th><th>02.07</th><th>30.07</th><th>04.08</th><th>06.08</th><th>Динамика</th>", "<th>28.06</th><th>02.07</th><th>30.07</th><th>04.08</th><th>06.08</th><th>11.08</th><th>Динамика</th>")
s = replace_once(s, "<td><strong>175</strong></td><td class='indicator'>Каденс вырос до 175 ✓</td>", "<td><strong>175</strong></td><td>171</td><td class='indicator'>171 на рельефе, выше 04.08 на 5 ✓</td>")
s = replace_once(s, "<td>158</td><td class='indicator'>5:32 при умеренном росте ЧСС ✓</td>", "<td>158</td><td>155</td><td class='indicator'>5:39 при ЧСС 155 и наборе 72 м ✓</td>")
s = replace_once(s, "<td>5.01</td><td class='indicator'>Короткая аэробная работа</td>", "<td>5.01</td><td>4.73</td><td class='indicator'>Короткая аэробная работа</td>")
s = replace_once(s, "<td>2.6</td><td class='indicator'>Умеренный аэробный стимул</td>", "<td>2.6</td><td>2.5</td><td class='indicator'>Умеренный аэробный стимул</td>")
s = replace_once(s, "<td><strong>5:32</strong></td><td class='indicator'>04.08 быстрее на 34 сек/км при +3 уд/мин ✓</td>", "<td><strong>5:32</strong></td><td><strong>5:39</strong></td><td class='indicator'>04.08 быстрее на 27 сек/км при той же ЧСС ✓</td>")
s = replace_once(s, "<td>4:56</td><td class='indicator'>Скоростной запас вырос ✓</td>", "<td>4:56</td><td>5:06</td><td class='indicator'>Контролируемый быстрый темп на рельефе</td>")
s = replace_once(s, "<td><strong>246</strong></td><td class='indicator'>Контакт сократился до 246 мс ✓</td>", "<td><strong>246</strong></td><td>251</td><td class='indicator'>251 мс на рельефе — стабильно</td>")
s = replace_once(s, "<td>14</td><td class='indicator'>Почти ровный маршрут</td>", "<td>14</td><td>72</td><td class='indicator'>Рельефная работа ✓</td>")

p.write_text(s, encoding='utf-8')
