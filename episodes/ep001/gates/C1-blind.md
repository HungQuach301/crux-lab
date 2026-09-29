# C1 — Kết quả kiểm mù (nguyên văn)

Ý đồ và tiêu chí: `C1-intent.md` (commit `5753f0a`, ghi trước khi chạy). Mỗi mẫu: một agent con mới (general-purpose), một file tên ngẫu nhiên trong thư mục riêng, câu hỏi cố định. Nguyên văn đầy đủ từng agent ở phụ lục cuối file.

## Vòng 1 (2026-09-29)

Mẫu:
- **L-A:** "Nora borrowed near the 2023 rate peak and watched rates dip without refinancing; now the bank's offer is smaller — is she too late, or can a smaller cut still pay back its fees?"
- **L-B:** "Nora's refinance offer falls short of the one-point line you may have heard of — but how big a cut does her own loan actually need, and why would a smaller loan need more?"
- **Đối chứng:** logline Cổng A bản cũ ("For households who borrowed at the 2023 rate peak, we find the rate drop … more than a full point for a small one.")

### Bảng chấm (P2, theo tiêu chí ghi trước)

| Mẫu | File | TC1 ai (người/hộ **ở Mỹ** vay mua nhà ~2023) | TC2 vay lại tốn phí | TC3 câu hỏi giảm bao nhiêu thì bù phí | Kể đúng (đủ 3) | Muốn xem |
|---|---|---|---|---|---|---|
| L-A | 32eaead6 | ✘ ("có lẽ vay mua nhà"; không nói Mỹ) | ✔ | ✔ | ✘ | Có thể |
| L-A | 03c0a8fe | ✘ (như trên) | ✔ | ✔ | ✘ | Có thể |
| L-A | da0433bc | ✘ | ✔ | ✔ | ✘ | Có thể |
| L-A | b477696a | ✘ (Mỹ chỉ đoán ở câu 3) | ✔ | ✔ | ✘ | Có thể |
| L-A | 3e45224c | ✘ | ✔ | ✔ | ✘ | Có thể |
| L-B | 18af62d9 | ✘ ("vay mua nhà"; không nói Mỹ) | ✔ | ✔ | ✘ | Có thể |
| L-B | f3aaea32 | ✘ (Mỹ chỉ ở câu 2) | ✔ | ✔ | ✘ | Có thể |
| L-B | 54223684 | ✘ | ✔ | ✔ | ✘ | Có thể |
| L-B | ff11cd44 | ✘ | ✔ | ✔ | ✘ | Có thể |
| L-B | 62b63961 | ✘ | ✔ | ✔ | ✘ | Có thể |
| Đối chứng | a4485311 | ✘ (vay mua nhà 2023; không nói Mỹ) | ✔ | ✔ | ✘ | Có thể |
| Đối chứng | 6da38e8e | ✘ | ✔ | ✔ | ✘ | Có thể |
| Đối chứng | 1366f595 | ✘ | ✔ | ✔ | ✘ | Có thể |

**Kết quả vòng 1:**
- L-A: kể đúng **0/5** theo tiêu chí chặt (5/5 nếu bỏ chữ "ở Mỹ"); muốn xem **0/5** ("Có thể" 5/5). **TRƯỢT.**
- L-B: kể đúng **0/5** chặt (5/5 nếu bỏ "ở Mỹ"); muốn xem **0/5** ("Có thể" 5/5). **TRƯỢT.**
- Đối chứng: 3/3 "Có thể"; 3/3 nói "logline đã nói hết đáp án nên ít lý do bấm xem".

**Ghi chú của P2 (không sửa ý đồ):**
1. Không logline nào nói "US" hay "mortgage", nên không agent nào nói được "ở Mỹ" trong phần kể lại. Đây là lỗi của logline, đồng thời tiêu chí có thể quá chặt với một logline đứng một mình (trên YouTube, tên kênh và tiêu đề mang ngữ cảnh Mỹ). Giữ tiêu chí; ghi để chủ dự án biết.
2. Câu hỏi cố định yêu cầu trả lời "bằng tiếng Việt", nên nhiều agent tự nhập vai người xem Việt ("người Việt có thể không biết refinance"). Đây là thiên lệch của câu hỏi, trong khi khán giả thật là người Mỹ. Vòng 2 giữ nguyên câu hỏi để so được với vòng 1; đưa vào gói quyết định.
3. Lời chê lặp lại ở ≥ 4/5 agent: L-A "the bank's offer is smaller" mơ hồ (5/5); L-B "one-point line" dễ nhầm với discount point (5/5); cả hai "refinance", "cut" không nói rõ (10/10); không nói vay gì, ở đâu (7/10).
4. L-B gây tò mò ở vế "smaller loan need more" (5/5 nhắc "nghe ngược đời").

## Phụ lục — nguyên văn vòng 1

### 32eaead6 (L-A)
> 1. Kể lại: Video kể về Nora, người vay tiền (có lẽ là vay mua nhà) đúng lúc lãi suất lên đỉnh năm 2023. Sau đó lãi suất giảm nhưng cô không vay lại để lấy lãi thấp hơn (refinance), và giờ ngân hàng chỉ còn cho cô mức giảm nhỏ hơn. Câu hỏi video sẽ trả lời: cô đã bỏ lỡ cơ hội rồi, hay mức giảm lãi nhỏ hơn này vẫn đủ bù lại các khoản phí khi vay lại?
> 2. Có muốn xem không: Có thể. Tình huống rất đời thường và có câu hỏi rõ ràng, nhưng chỉ ai đang vay mua nhà mới thấy liên quan. Người khác có thể thấy hơi khô.
> 3. Chỗ khó hiểu: "refinancing" là thuật ngữ tài chính, người xem bình thường có thể không biết đó là vay mới để trả khoản vay cũ với lãi thấp hơn. "the bank's offer is smaller": không rõ "nhỏ hơn" là mức giảm lãi nhỏ hơn hay khoản vay nhỏ hơn. Đến vế sau ("a smaller cut") mới đoán ra là mức giảm lãi. "pay back its fees": ý là tiền lãi tiết kiệm được có bù nổi phí refinance không. Ý này ngầm hiểu chứ không nói thẳng. Câu không nói đây là vay gì (nhà, xe…) và vay ở nước nào.

### 03c0a8fe (L-A)
> 1. Kể lại: Video kể về Nora, người vay tiền (có lẽ vay mua nhà) đúng lúc lãi suất cao nhất vào năm 2023. Sau đó lãi suất giảm nhưng cô không đổi sang khoản vay mới (refinance), và bây giờ mức giảm lãi mà ngân hàng đưa ra cho cô nhỏ hơn trước. Câu hỏi video sẽ trả lời: cô đã lỡ mất cơ hội chưa, hay mức giảm lãi nhỏ hơn này vẫn đủ bù lại các khoản phí khi đổi khoản vay?
> 2. Có thể. Chuyện này rất đời thường và dễ đồng cảm, ai có vay mua nhà cũng từng băn khoăn "giờ đổi có đáng không". Nhưng nếu tôi không có khoản vay nào thì chủ đề hơi khô, tôi chỉ bấm khi đang cần.
> 3. Chỗ khó hiểu: "refinancing": người xem Việt bình thường có thể không biết từ này; nó nghĩa là đổi sang một khoản vay mới có lãi thấp hơn để trả khoản vay cũ. "the bank's offer is smaller": không rõ "smaller" nghĩa là lãi được giảm ít hơn hay ngân hàng cho vay số tiền ít hơn. Đọc hết câu mới đoán ra là giảm lãi ít hơn. "a smaller cut still pay back its fees": ý "tiền tiết kiệm từ lãi có bù được phí đổi khoản vay không" hơi cô đọng. Người không rành tài chính sẽ không biết đổi khoản vay là mất phí. Không nói rõ Nora vay gì (nhà, xe?) và vay ở nước nào. Ý "đỉnh lãi suất 2023" thì người theo dõi tin tức hiểu, người khác có thể không hiểu.

### da0433bc (L-A)
> 1. Kể lại: Nora vay tiền (có lẽ là vay mua nhà) đúng lúc lãi suất gần đỉnh năm 2023. Sau đó lãi suất giảm, nhưng cô không kịp vay lại với lãi thấp hơn (refinance). Giờ mức giảm lãi mà ngân hàng đề nghị đã nhỏ hơn trước. Video sẽ trả lời hai câu hỏi: Nora đã lỡ cơ hội chưa, và một mức giảm lãi nhỏ như vậy có đủ bù lại các khoản phí khi refinance không.
> 2. Có thể. Tình huống này thực tế và nhiều người vay năm 2023 cũng gặp phải, nhưng chủ đề khá chuyên về tài chính. Tôi chỉ bấm xem nếu chính mình đang có khoản vay tương tự.
> 3. "refinancing": người xem bình thường, nhất là người Việt, có thể không biết đây là việc vay khoản mới với lãi thấp hơn để trả khoản vay cũ. "the bank's offer is smaller": không rõ "nhỏ hơn" là mức giảm lãi nhỏ hơn hay số tiền cho vay nhỏ hơn. Phải đọc tới vế sau ("smaller cut") mới đoán được là mức giảm lãi. "cut" và "pay back its fees": ý "phí refinance có được bù lại bằng tiền lãi tiết kiệm được hay không" hơi ngầm, người không quen khái niệm điểm hòa vốn sẽ khó hiểu. Logline không nói rõ đây là khoản vay gì (vay mua nhà hay loại khác) và ở nước nào.

### b477696a (L-A)
> 1. Kể lại: Video kể về Nora, người vay tiền (có lẽ là vay mua nhà) đúng lúc lãi suất gần đỉnh năm 2023. Sau đó lãi suất giảm nhưng cô không đảo nợ (refinance), và giờ ngân hàng chỉ đề nghị mức giảm nhỏ hơn. Video sẽ trả lời câu hỏi: cô đã lỡ mất cơ hội chưa, hay mức giảm lãi nhỏ đó vẫn đủ bù lại các khoản phí đảo nợ?
> 2. Có muốn xem không: Có thể. Chủ đề thực tế và có câu hỏi rõ ràng (có đáng làm không, bao lâu thì hoà vốn phí), nhưng chỉ hấp dẫn nếu mình đang có khoản vay cần cân nhắc.
> 3. "refinancing" (đảo nợ / tái cấp vốn) là thuật ngữ tài chính, người xem bình thường có thể không biết. "the bank's offer is smaller" hơi mơ hồ: "nhỏ hơn" ở đây là mức giảm lãi suất nhỏ hơn so với lúc lãi suất xuống thấp nhất, chứ không phải khoản vay nhỏ hơn. Phải đọc đến "smaller cut" mới hiểu. "pay back its fees" (bù lại phí) ngầm hiểu là phí đảo nợ, nhưng không nói rõ là phí gì. Không nói rõ là vay gì (nhà, xe?) và ở nước nào, dù "2023 rate peak" gợi ý là vay mua nhà ở Mỹ hoặc nước phương Tây.

### 3e45224c (L-A)
> 1. Kể lại: Video kể về Nora, một người vay tiền (có lẽ là vay mua nhà) đúng lúc lãi suất gần đỉnh năm 2023. Sau đó lãi suất giảm nhưng cô không kịp tái cấp vốn (refinance), và giờ mức giảm lãi mà ngân hàng đề nghị đã nhỏ hơn trước. Câu hỏi video trả lời là: cô đã lỡ mất cơ hội chưa, hay mức giảm lãi nhỏ này vẫn đủ để bù lại các khoản phí khi tái cấp vốn?
> 2. Có muốn xem không: Có thể. Tình huống cụ thể và gần gũi với người đang vay, lại có câu hỏi rõ ràng kiểu "có đáng không". Nhưng nếu tôi không có khoản vay nào thì chủ đề hơi hẹp.
> 3. "refinancing" (tái cấp vốn): người không rành tài chính có thể không biết từ này. Họ cũng không biết vì sao việc này tốn phí. "the bank's offer is smaller": không rõ "nhỏ hơn" là mức giảm lãi nhỏ hơn hay khoản vay/ưu đãi nhỏ hơn. Phải đọc tới vế sau ("smaller cut") mới đoán được là mức giảm lãi. "pay back its fees": ý là tiền lãi tiết kiệm được có bù nổi phí tái cấp vốn không (điểm hòa vốn). Cách diễn đạt này hơi ngắn gọn, có thể phải đọc lại mới hiểu. Logline không nói đây là khoản vay gì (mua nhà hay loại khác) và ở nước nào. Chi tiết "2023 rate peak" cũng giả định người xem đã biết lãi suất lên đỉnh vào năm 2023.

### 18af62d9 (L-B)
> 1. Kể lại: Video nói về Nora. Cô được mời refinance (vay lại khoản vay mua nhà với lãi suất mới), nhưng mức giảm lãi suất trong lời mời chưa tới "1 điểm phần trăm", tức con số theo quy tắc truyền miệng mà nhiều người nghe là cần có thì mới đáng vay lại. Video sẽ trả lời hai câu hỏi: với khoản vay cụ thể của Nora thì lãi suất phải giảm bao nhiêu mới đáng, và tại sao khoản vay nhỏ hơn lại cần mức giảm lớn hơn.
> 2. Có muốn xem không: Có thể. Câu hỏi "khoản vay nhỏ lại cần giảm lãi nhiều hơn" nghe ngược đời nên tôi tò mò. Nhưng tôi sẽ chỉ bấm xem nếu đang tính vay hoặc vay lại tiền mua nhà, vì chủ đề này khá hẹp.
> 3. "refinance": người xem phổ thông, nhất là người Việt, có thể không biết từ này nghĩa là vay khoản mới để trả khoản vay cũ với lãi suất khác. "the one-point line": câu không nói rõ đây là giảm 1 điểm phần trăm lãi suất. Người đọc cũng dễ nhầm với "point" theo nghĩa phí mua điểm (discount point) trong vay mua nhà. Ai chưa nghe quy tắc này thì sẽ không hiểu "line" là ngưỡng gì. "how big a cut": "cut" ở đây là mức giảm lãi suất, nhưng câu không nói thẳng ra. "Nora" xuất hiện mà không giới thiệu cô là ai. Chuyện này không sao, chỉ hơi đột ngột.

### f3aaea32 (L-B)
> 1. Kể lại: Video nói về Nora. Cô được mời refinance (vay lại khoản vay mua nhà với lãi suất mới), nhưng mức lãi suất được giảm chưa tới "1 điểm phần trăm", tức là cái ngưỡng người ta hay truyền tai nhau để quyết định có nên vay lại hay không. Video sẽ trả lời: riêng với khoản vay của Nora thì lãi suất phải giảm bao nhiêu mới đáng vay lại, và vì sao khoản vay càng nhỏ thì lại càng cần được giảm nhiều hơn.
> 2. Có thể. Câu hỏi "vay nhỏ mà lại cần giảm nhiều hơn" nghe ngược đời nên khá tò mò, nhưng chủ đề refinance ở Mỹ không liên quan lắm tới người xem Việt nếu họ không có khoản vay kiểu này.
> 3. "refinance" là thuật ngữ tài chính. Người không rành sẽ không biết đó là vay mới để trả khoản vay cũ. "the one-point line" rất mơ hồ. Không rõ "point" là 1 điểm phần trăm lãi suất hay là "discount point" (phí trả trước bằng 1% khoản vay). Người xem chỉ đoán được qua câu "you may have heard of", nếu chưa từng nghe quy tắc này thì sẽ bị hụt. "cut" không nói rõ là cắt cái gì. Phải tự hiểu là mức giảm lãi suất. Ý "smaller loan need more" không có manh mối nào giải thích, vì logline không nhắc tới chi phí refinance cố định. Chính điều này tạo tò mò, nhưng cũng dễ làm người xem bối rối. Câu khá dài, lại có hai câu hỏi nối nhau nên phải đọc hai lần mới nắm được.

### 54223684 (L-B)
> 1. Kể lại: Video kể về Nora, một người đang được mời refinance (vay lại khoản vay mua nhà với lãi suất mới). Mức giảm lãi suất người ta chào cho cô không đạt "ngưỡng 1 điểm" mà người ta hay truyền miệng (quy tắc: chỉ nên refinance khi lãi suất giảm ít nhất 1%). Video sẽ trả lời hai câu: với khoản vay cụ thể của Nora thì lãi suất phải giảm bao nhiêu mới đáng refinance, và vì sao khoản vay nhỏ hơn lại cần mức giảm lớn hơn.
> 2. Có thể. Câu "khoản vay nhỏ hơn lại cần giảm nhiều hơn" nghe ngược đời nên khá tò mò, nhưng chủ đề refinance chỉ hấp dẫn nếu tôi đang có khoản vay mua nhà.
> 3. "refinance" là thuật ngữ tài chính, người xem phổ thông có thể không biết. "the one-point line": không rõ "one-point" là 1 điểm phần trăm lãi suất hay 1 "point" phí (discount point) khi vay. Chữ "line" cũng mơ hồ (ngưỡng? quy tắc?). Logline cho rằng người xem đã "nghe qua" quy tắc này, nhưng nhiều người chưa nghe. "how big a cut": cắt giảm cái gì? Có thể hiểu là giảm lãi suất, nhưng câu không nói rõ. "falls short of": phải đọc hai lần mới hiểu là mức giảm được chào nhỏ hơn 1 điểm, chứ không phải lãi suất thấp hơn. "why would a smaller loan need more": không có ngữ cảnh thì người xem khó hiểu ngay rằng lý do là chi phí refinance cố định chiếm tỷ lệ lớn hơn trên khoản vay nhỏ. Nhưng chính chỗ mơ hồ này lại là cái móc gây tò mò.

### ff11cd44 (L-B)
> 1. Kể lại: Video nói về Nora, một người đang nhận được lời mời vay lại (refinance) khoản vay mua nhà của mình. Mức lãi suất mới chỉ giảm chưa tới "1 điểm phần trăm", tức con số mà người ta hay truyền tai nhau là ngưỡng đáng để refinance. Video sẽ trả lời hai câu hỏi: với khoản vay cụ thể của Nora thì lãi suất phải giảm bao nhiêu mới đáng làm, và vì sao khoản vay càng nhỏ thì lại cần mức giảm càng lớn (có lẽ vì chi phí refinance gần như cố định, còn khoản tiết kiệm thì nhỏ hơn).
> 2. Có thể. Câu hỏi "khoản vay nhỏ lại cần giảm nhiều hơn" nghe ngược đời và khá tò mò, nhưng chủ đề refinance chỉ thật sự hút tôi nếu tôi đang có khoản vay mua nhà.
> 3. "Refinance": người xem không rành tài chính (nhất là người Việt) có thể không biết đây là vay khoản mới để trả khoản vay cũ với lãi suất thấp hơn. "The one-point line": không nói rõ là 1 điểm phần trăm lãi suất. Người đọc có thể nhầm sang "1 point" theo nghĩa phí trả trước (discount point, bằng 1% khoản vay), một nghĩa cũng phổ biến trong chuyện vay mua nhà. Cụm "you may have heard of" giả định người xem đã biết quy tắc này. "How big a cut": không nói rõ là cắt giảm cái gì. Phải tự hiểu là mức giảm lãi suất. "Falls short of": phải đọc kỹ mới hiểu mức giảm của Nora nhỏ hơn 1 điểm, chứ không phải lãi suất của cô thấp hơn.

### 62b63961 (L-B)
> 1. Kể lại: Video nói về Nora, một người đang được đề nghị refinance, tức là vay lại khoản vay (chắc là vay mua nhà) với lãi suất mới. Mức lãi suất được giảm trong đề nghị này chưa tới "một điểm phần trăm", là ngưỡng mà nhiều người vẫn truyền tai nhau là có giảm được chừng đó thì mới đáng vay lại. Video sẽ trả lời hai câu: với khoản vay của riêng Nora thì lãi suất phải giảm bao nhiêu mới đáng, và tại sao khoản vay càng nhỏ lại càng cần giảm nhiều hơn.
> 2. Có thể. Câu hỏi "vay ít hơn mà lại cần giảm nhiều hơn" nghe ngược đời nên tôi tò mò, nhưng tôi phải đang có khoản vay mua nhà hoặc đang tính vay lại thì mới thật sự bấm xem.
> 3. "Refinance": người xem Việt Nam bình thường có thể không biết từ này, nghĩa là vay khoản mới để trả khoản vay cũ. "The one-point line": không nói rõ là giảm 1 điểm phần trăm lãi suất. Chữ "point" còn dễ bị nhầm với "điểm phí" (discount points) trong vay mua nhà ở Mỹ. Người chưa nghe quy tắc này thì không hiểu nó là gì. "A cut": câu không nói rõ đây là giảm lãi suất. "Why would a smaller loan need more?": ý này hiểu được nhưng lúc đầu thấy ngược. Người xem phải tự đoán là do phí làm thủ tục vay lại gần như cố định, nên khoản vay nhỏ phải giảm lãi nhiều hơn mới bù được phí. Nora là ai thì không có giới thiệu, nhưng điều này không gây trở ngại lớn.

### a4485311 (đối chứng)
> 1. Kể lại: Video dành cho những gia đình đã vay mua nhà vào đúng lúc lãi suất cao nhất năm 2023. Câu hỏi của video: lãi suất phải giảm bao nhiêu thì việc vay lại (refinance) mới đáng, tức là số tiền tiết kiệm bù lại được phí làm hồ sơ vay trong vòng 3 năm. Câu trả lời đã nằm sẵn trong logline: khoảng 1/3 điểm phần trăm với khoản vay lớn, nửa điểm với khoản vay trung bình, và hơn 1 điểm với khoản vay nhỏ.
> 2. Có thể. Chủ đề thiết thực nếu tôi đang có khoản vay năm 2023, nhưng logline đã nói hết đáp án nên tôi không còn nhiều lý do để bấm vào xem, trừ khi muốn biết cách tính hoặc "lớn/nhỏ" là bao nhiêu tiền.
> 3. "point" (điểm): người xem không rành tài chính dễ nhầm với "points" trong thế chấp Mỹ (phí mua lãi suất, 1 point = 1% khoản vay). Ở đây có lẽ ý là điểm phần trăm lãi suất, nhưng không nói rõ. "loan costs" / "pays back": không rõ gồm những phí gì (closing costs?), và "pays back" nghĩa là tiền lãi tiết kiệm được mỗi tháng cộng lại bù đủ phí. Người mới phải tự suy ra. "large / median / small loan": không nói con số cụ thể (bao nhiêu đô), nên tôi không biết khoản vay của mình thuộc nhóm nào. "2023 rate peak": giả định người xem biết lãi suất vay nhà Mỹ đạt đỉnh năm 2023; với người xem ngoài Mỹ thì không rõ. Câu dài, nhiều số liệu dồn một lúc, và "we find" nghe giống tóm tắt nghiên cứu hơn là giới thiệu video.

### 6da38e8e (đối chứng)
> 1. Kể lại: Video nói về những hộ gia đình vay mua nhà đúng lúc lãi suất lên cao nhất năm 2023. Câu hỏi video trả lời là: lãi suất phải giảm bao nhiêu thì việc vay lại (refinance) mới đáng làm, tức là số tiền tiết kiệm được bù lại chi phí làm hồ sơ vay trong vòng 3 năm. Câu trả lời tùy vào khoản vay lớn hay nhỏ: khoản vay lớn chỉ cần giảm khoảng 1/3 điểm phần trăm, khoản vay trung bình cần khoảng 0,5 điểm, còn khoản vay nhỏ cần hơn 1 điểm.
> 2. Có thể. Nếu tôi đang có khoản vay từ năm 2023 thì câu hỏi này rất thiết thực với tôi. Nhưng logline đã nói luôn đáp án, nên có khi tôi không cần bấm xem nữa. Với người không vay thì chủ đề này cũng khá khô.
> 3. "a point" (một điểm): người xem bình thường có thể không biết đây là 1 điểm phần trăm lãi suất (ví dụ từ 7% xuống 6%). Dễ nhầm với "points" là phí trả trước khi vay (discount points). "refinance" và "loan costs": không nói rõ chi phí gồm những gì (phí hồ sơ, phí thẩm định, v.v.) và tốn khoảng bao nhiêu. "large / median / small loan": không có con số cụ thể, nên tôi không biết khoản vay của mình thuộc nhóm nào. "we find": không rõ "we" là ai và kết quả dựa trên dữ liệu gì. "2023 rate peak": người ngoài Mỹ có thể không biết lãi suất vay mua nhà lúc đó cao đến mức nào (khoảng 7–8%). Không nói rõ vì sao khoản vay nhỏ lại cần lãi giảm nhiều hơn. Lý do là chi phí vay lại phần lớn cố định, nên khoản vay nhỏ tiết kiệm ít hơn mỗi tháng. Ý này hiểu được nhưng người xem phải tự suy ra.

### 1366f595 (đối chứng)
> 1. Kể lại: Video dành cho những gia đình vay mua nhà năm 2023, lúc lãi suất lên cao nhất. Câu hỏi video trả lời là: lãi suất phải giảm bao nhiêu thì việc vay lại (refinance) mới đáng làm, tức là số tiền lãi tiết kiệm được bù lại chi phí làm khoản vay mới trong vòng 3 năm. Kết quả tùy theo khoản vay lớn hay nhỏ: vay lớn chỉ cần giảm khoảng 0,33 điểm phần trăm, vay mức trung bình cần 0,5 điểm, còn vay nhỏ cần giảm hơn 1 điểm.
> 2. Có thể. Nếu tôi đang có khoản vay năm 2023 thì chắc chắn sẽ bấm xem vì nó cho con số cụ thể để tự áp vào mình. Nhưng người không vay thì thấy chủ đề khá hẹp và hơi khô. Thêm nữa, câu giới thiệu đã nói hết đáp án nên cũng ít lý do để phải bấm vào xem.
> 3. "refinance" và "loan costs" là thuật ngữ tài chính. Người xem bình thường, nhất là người Việt, có thể không biết đây là vay mới để trả khoản vay cũ, và "loan costs" là phí làm hồ sơ, phí đóng khoản vay. "a point" dễ gây nhầm. Nó là 1 điểm phần trăm lãi suất, nhưng trong vay thế chấp ở Mỹ "point" còn có nghĩa là phí trả trước (1% số tiền vay). "large / median / small loan" không nêu số tiền cụ thể, nên người xem không biết khoản vay của mình thuộc nhóm nào. "2023 rate peak" ngầm hiểu là lãi suất vay mua nhà ở Mỹ. Câu không nói rõ nước nào. "pays back within three years" là khái niệm thời gian hoàn vốn. Ý này hợp lý nhưng cần đọc hai lần mới hiểu.

(Các agent nêu dòng nội dung file ở đầu câu trả lời; đã lược dòng đó vì trùng mẫu ở trên.)
