from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

if '<td>06.08.2026</td>' in s:
    raise SystemExit(0)


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise RuntimeError(f'Marker not found: {old[:160]}')
    return text.replace(old, new, 1)

# Main season table
last_row = "<tr class='type-easy'><td>04.08.2026</td><td>Лёгкий бег (рельеф)</td><td>4.31</td><td>26:14</td><td>6:06</td><td>155/171</td><td>166</td><td>65</td><td>—</td><td>2.6/2.0</td></tr>"
new_row = "<tr class='type-aerobic'><td>06.08.2026</td><td>Аэробная работа (ровно)</td><td>5.01</td><td>27:43</td><td>5:32</td><td>158/179</td><td>175</td><td>14</td><td>—</td><td>2.6/2.5</td></tr>"
s = replace_once(s, last_row + "</tbody></table>", last_row + new_row + "</tbody></table>")

# Coach note
progress_marker = "</div></div></div></div><div class='section-title'>Прогресс ключевых показателей</div>"
new_note = (
    "<div class='note-card'><div class='note-header' style='background:#cce5ff'>"
    "<strong>06.08.2026 — Аэробная работа (ровно)</strong>"
    "<span class='meta'>Маршрут: Приморский край &nbsp;|&nbsp; Борг: —</span></div>"
    "<div class='note-body'><div class='text'>"
    "Короткая, но уже не восстановительная пробежка на следующий день после силовой Б. "
    "Относительно 04.08 средний темп ускорился с 6:06 до 5:32 мин/км (+34 сек/км), при росте среднего пульса только с 155 до 158. "
    "Каденс вырос с 166 до 175, а время контакта с землёй снизилось примерно с 264 до 246 мс — хороший признак экономичности на более высокой скорости. "
    "При этом максимальный пульс 179 и анаэробный ТЭ 2.5 показывают, что лёгкой эту работу считать нельзя. "
    "После силовой нагрузки на ноги такой темп не стоит превращать в привычный восстановительный бег; следующая пробежка — разговорная, без ускорения дистанции и скорости одновременно."
    "</div><div class='stats'>"
    "Дист: <span>5.01 км</span> &nbsp;|&nbsp; Время: <span>27:43</span> &nbsp;|&nbsp; Темп: <span>5:32</span><br>"
    "Пульс: <span>158/179</span> &nbsp;|&nbsp; Каденс: <span>175</span> &nbsp;|&nbsp; Набор: <span>14 м</span><br>"
    "ТЭ: <span>2.6 / 2.5</span> &nbsp;|&nbsp; Лучший темп: <span>4:56</span> &nbsp;|&nbsp; Приведённый темп: <span>5:31</span> &nbsp;|&nbsp; Длина шага: <span>104 см</span> &nbsp;|&nbsp; Время на земле: <span>246 мс</span>"
    "</div></div></div>"
)
s = replace_once(
    s,
    progress_marker,
    "</div></div></div>" + new_note + "</div><div class='section-title'>Прогресс ключевых показателей</div>",
)

# Progress table
s = replace_once(s, "<th>28.06</th><th>02.07</th><th>30.07</th><th>04.08</th><th>Динамика</th>", "<th>28.06</th><th>02.07</th><th>30.07</th><th>04.08</th><th>06.08</th><th>Динамика</th>")
s = replace_once(s, "<td>166</td><td class='indicator'>Стабильно 166–168 ✓</td>", "<td>166</td><td><strong>175</strong></td><td class='indicator'>Каденс вырос до 175 ✓</td>")
s = replace_once(s, "<td>155</td><td class='indicator'>Темп быстрее при том же пульсе ✓</td>", "<td>155</td><td>158</td><td class='indicator'>5:32 при умеренном росте ЧСС ✓</td>")
s = replace_once(s, "<td>4.31</td><td class='indicator'>Короткая аэробная работа</td>", "<td>4.31</td><td>5.01</td><td class='indicator'>Короткая аэробная работа</td>")
s = replace_once(s, "<td>2.6</td><td class='indicator'>Умеренный стимул</td>", "<td>2.6</td><td>2.6</td><td class='indicator'>Умеренный аэробный стимул</td>")
s = replace_once(s, "<td><strong>6:06</strong></td><td class='indicator'>02.07 быстрее на 28 сек/км при том же пульсе ✓</td>", "<td><strong>6:06</strong></td><td><strong>5:32</strong></td><td class='indicator'>04.08 быстрее на 34 сек/км при +3 уд/мин ✓</td>")
s = replace_once(s, "<td>5:46</td><td class='indicator'>Контролируемо без рывков</td>", "<td>5:46</td><td>4:56</td><td class='indicator'>Скоростной запас вырос ✓</td>")
s = replace_once(s, "<td>264</td><td class='indicator'>Стабильно 261–264 мс</td>", "<td>264</td><td><strong>246</strong></td><td class='indicator'>Контакт сократился до 246 мс ✓</td>")
s = replace_once(s, "<td>65</td><td class='indicator'>Рельефная работа ✓</td>", "<td>65</td><td>14</td><td class='indicator'>Почти ровный маршрут</td>")

p.write_text(s, encoding='utf-8')
