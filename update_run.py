from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

if '<td>18.08.2026</td>' in s:
    raise SystemExit(0)


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise RuntimeError(f'Marker not found: {old[:180]}')
    return text.replace(old, new, 1)

# Main season table
last_row = "<tr class='type-aerobic'><td>11.08.2026</td><td>Аэробная работа (рельеф)</td><td>4.73</td><td>26:44</td><td>5:39</td><td>155/172</td><td>171</td><td>72</td><td>—</td><td>2.5/2.3</td></tr>"
new_row = "<tr class='type-interval'><td>18.08.2026</td><td>Интервалы 800 м × 6 (стадион)</td><td>10.01</td><td>59:03</td><td>5:54</td><td>151/169</td><td>165</td><td>0</td><td>—</td><td>3.6/3.9</td></tr>"
s = replace_once(s, last_row + "</tbody></table>", last_row + new_row + "</tbody></table>")

# Coach note
progress_marker = "</div></div></div></div><div class='section-title'>Прогресс ключевых показателей</div>"
new_note = (
    "<div class='note-card'><div class='note-header' style='background:#fff3cd'>"
    "<strong>18.08.2026 — Интервалы 800 м × 6 (стадион)</strong>"
    "<span class='meta'>Маршрут: стадион, плоско &nbsp;|&nbsp; Борг: —</span></div>"
    "<div class='note-body'><div class='text'>"
    "Полноценная интервальная работа: по графику видно шесть выраженных быстрых блоков с активным восстановлением. Общий объём 10.01 км за 59:03. "
    "Средний пульс 151, максимум 169 — существенно контролируемее, чем на тяжёлых интервалах 14.06 (154/179, ТЭ 3.2/5.2) и 21.06 (157/175, ТЭ 3.5/5.1), при большем общем объёме. "
    "Аэробный/анаэробный ТЭ 3.6/3.9 даёт сильный, но не чрезмерный стимул. Каденс 165 в среднем и до 187 на быстрых участках; длина шага около 103 см. "
    "Средняя мощность около 288 Вт, максимум около 359 Вт; пики мощности и каденса повторяются ровно, без явного развала последних повторов. Контакт с землёй около 268 мс в среднем, на быстрых отрезках заметно сокращается. "
    "Восстановление между отрезками по графику не опускало пульс до 120–125: для такой работы это и не требуется. На следующих 800-метровых отрезках лучше ориентироваться на 1:45–2:15 лёгкого бега и стартовать следующий повтор примерно после падения ЧСС к 135–145, сохраняя ровный темп и технику."
    "</div><div class='stats'>"
    "Дист: <span>10.01 км</span> &nbsp;|&nbsp; Время: <span>59:03</span> &nbsp;|&nbsp; Темп общий: <span>5:54</span><br>"
    "Пульс: <span>151/169</span> &nbsp;|&nbsp; Каденс: <span>165 ср. / 187 макс.</span> &nbsp;|&nbsp; Набор: <span>0 м</span><br>"
    "ТЭ: <span>3.6 / 3.9</span> &nbsp;|&nbsp; Лучший темп: <span>5:10</span> &nbsp;|&nbsp; Калории: <span>812</span><br>"
    "Длина шага: <span>103 см</span> &nbsp;|&nbsp; Мощность: <span>~288 Вт ср. / ~359 Вт макс.</span> &nbsp;|&nbsp; Контакт с землёй: <span>~268 мс</span>"
    "</div></div></div>"
)
s = replace_once(
    s,
    progress_marker,
    "</div></div></div>" + new_note + "</div><div class='section-title'>Прогресс ключевых показателей</div>",
)

# Progress table
s = replace_once(s, "<th>28.06</th><th>02.07</th><th>30.07</th><th>04.08</th><th>06.08</th><th>11.08</th><th>Динамика</th>", "<th>28.06</th><th>02.07</th><th>30.07</th><th>04.08</th><th>06.08</th><th>11.08</th><th>18.08</th><th>Динамика</th>")
s = replace_once(s, "<td>171</td><td class='indicator'>171 на рельефе, выше 04.08 на 5 ✓</td>", "<td>171</td><td>165</td><td class='indicator'>Средний 165 при интервалах, максимум 187 ✓</td>")
s = replace_once(s, "<td>155</td><td class='indicator'>5:39 при ЧСС 155 и наборе 72 м ✓</td>", "<td>155</td><td>151</td><td class='indicator'>Интервальная работа при среднем пульсе 151 ✓</td>")
s = replace_once(s, "<td>4.73</td><td class='indicator'>Короткая аэробная работа</td>", "<td>4.73</td><td>10.01</td><td class='indicator'>10 км с 6 быстрыми блоками ✓</td>")
s = replace_once(s, "<td>2.5</td><td class='indicator'>Умеренный аэробный стимул</td>", "<td>2.5</td><td>3.6</td><td class='indicator'>Сильный аэробный стимул без перегруза</td>")
s = replace_once(s, "<td><strong>5:39</strong></td><td class='indicator'>04.08 быстрее на 27 сек/км при той же ЧСС ✓</td>", "<td><strong>5:39</strong></td><td>5:54</td><td class='indicator'>Общий темп включает активные восстановления</td>")
s = replace_once(s, "<td>5:06</td><td class='indicator'>Контролируемый быстрый темп на рельефе</td>", "<td>5:06</td><td>5:10</td><td class='indicator'>Быстрые блоки повторяются без явного развала</td>")
s = replace_once(s, "<td>251</td><td class='indicator'>251 мс на рельефе — стабильно</td>", "<td>251</td><td>268</td><td class='indicator'>Среднее выше из-за восстановлений; на быстрых блоках сокращается</td>")
s = replace_once(s, "<td>72</td><td class='indicator'>Рельефная работа ✓</td>", "<td>72</td><td>0</td><td class='indicator'>Стадион: чистая скоростная работа</td>")

p.write_text(s, encoding='utf-8')
