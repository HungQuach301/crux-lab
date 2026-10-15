# M5 nhớ lại + chỗ muốn tua (m5)

- **Nhớ lại (chỉ báo):** 3/3 người kể ≥ 2/3 khoảnh khắc · câu hỏi đúng 3/3
- **Chỗ muốn tua (ngưỡng: không cảnh nào ≥ 2/3):** {'S25': 3, 'S03': 3, 'S24': 3, 'S22': 1, 'S23': 2} → **TRƯỢT**

- recall R1: {'moments': ['K1', 'K2', 'K3'], 'question_ok': True, 'why': "Recalls the 307-house street going from mostly lit with cash to about half with stocks (K1), and '152 of 307 lit, about half' (K3). Also recalls the Jan 1991 flip to '$485,063 behind' (K2a), but not the $54,310 drawdown (K2b). The question is correct: Nina rents and invests the difference, does she end up ahead of owning."}
- recall R2: {'moments': ['K1', 'K2', 'K3'], 'question_ok': True, 'why': "Recalls the Jan 1991 flip to '$485,063 behind' (K2a, no K2b), '152 of 307 lit' with the half in stretches (K3), and the 'stocks outgrew homes ~9 in 10, yet buyer ahead in half' contrast (K1). The question is correct."}
- recall R3: {'moments': ['K1', 'K2', 'K3'], 'question_ok': True, 'why': "Recalls '152 of the 307, about half' on the street (K3) and the Jan 1991 flip to '$485,063 behind' (K2a, no K2b). The K1 paradox shows only as 'stocks usually outgrow homes' plus cash vs stocks, so it is weaker. The question is correct."}
- skip R1: {'skip': ['S03', 'S24', 'S25'], 'engaged': ['S04', 'S19'], 'why': 'Skips the repeated hook at 0:22 (to the street at 0:46), the limits card at 8:00 and the recap at 8:11; engaged at 1:19 (first house) and 6:27 (the $400k vs $92k explanation).'}
- skip R2: {'skip': ['S03', 'S22', 'S23', 'S24', 'S25'], 'engaged': ['S04', 'S12'], 'why': 'Skips the restated question at 0:31, the dense limits text from 7:48 to 8:11 and the short recap at 8:13; engaged at 1:30 (cash vs stocks flip) and 3:42 to 3:57 (dark street).'}
- skip R3: {'skip': ['S03', 'S23', 'S24', 'S25'], 'engaged': ['S04', 'S14'], 'why': "Would jump from 0:31 to 0:46, and skip the limits card from 7:49 and the recap from 8:11; engaged at 1:30 (the $485,063 behind reveal) and 4:21 (the renter's pile sinks)."}
