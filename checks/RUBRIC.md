# checks/RUBRIC.md — phiếu chấm tay (H1–H8)

Phiếu này chấm các yêu cầu `[NGƯỜI]` của `genre-spec/data-explainer.md`. Máy không thay được các câu này.

H1–H7 giữ nguyên câu hỏi và mốc điểm của phiếu bài D (`crux-spike-opus55`, `checks/RUBRIC.md` @ `76613cf`) để điểm các vòng so được với nhau. Chỉ đổi hai thứ:
- mã tham chiếu trỏ sang spec thể loại (`DX-…`);
- cột "Phần máy" trỏ sang luật của bộ luật này.

H8 là câu mới, tách "âm thanh theo dữ liệu" ra khỏi H7 (sổ gu G-001). Từ nay H7 chỉ chấm nhạc.

K2 (2026-09-28) bổ sung tiêu chí, không đổi câu hỏi gốc, nên điểm vẫn so được với vòng trước:
- **H1** thêm tiêu chí của sổ gu G-007: cold open cho người xem thấy chủ đề **liên quan đến chính mình**, qua **một người** và **một khoảnh khắc cụ thể**.
- **H4** thêm tiêu chí của sổ gu G-008: số liệu gắn với **hoàn cảnh của người xem**: một nhân vật, một kịch bản, một hệ quả. Phần máy tạm: S16.
- **H8** bỏ "kể cả khi đang có lời" theo sổ gu G-006 (lời là ưu tiên số một); thêm "không lấn lời". Phần máy: T1 (định nghĩa lại), L1 (mới).
- **H3** thêm tiêu chí của sổ gu G-009: kịch bản là một câu chuyện (bối cảnh → nhân vật → vấn đề → hành trình → đáp án), câu chữ liền mạch, có chuyển ý, không cụt lủn. Phần máy tạm: S13 (định nghĩa lại: không có chuỗi câu vụn).

Nguồn câu chữ (đọc 2026-09-28): `taste-ledger.md` trên `main` mới có G-001…G-004. G-005…G-008 nằm trên nhánh `ep001` (commit `bbc28fb`); G-007 và G-008 ở đây lấy nguyên văn từ đó. G-009 chưa có ở nhánh nào; câu chữ lấy từ chỉ dẫn của chủ dự án cho phiên K2.

## Cách chấm

1. Xem bản đầy đủ một lần liền mạch, ở cỡ thật, có tiếng, rồi mới chấm. Sau đó xem lại từng đoạn.
2. H7 và H8 nghe thêm một lần trên loa điện thoại. Đây là cách người xem nghe nhiều nhất, và gói duyệt cũng xem trên điện thoại (CHARTER §4, khâu 4).
3. Mỗi câu chấm 1–5. Mức 2 và 4 là mức giữa hai mô tả kề nhau.
4. Mỗi điểm kèm **mốc thời gian** làm bằng chứng. Điểm 1–2 phải chỉ mốc cụ thể của lỗi.
5. Nếu câu có phần máy đo (cột phải) thì điểm người không được mâu thuẫn với kết quả máy mà không giải thích.
6. Mức đạt (CHARTER §5): trung bình ≥ 4, không câu nào dưới 3. Với phiếu 8 câu, trung bình tính trên cả 8 câu.

## Các câu

| # | Mục spec | Câu hỏi | 1 | 3 | 5 | Phần máy |
|---|---|---|---|---|---|---|
| H1 | DX-S1, DX-S3 cold open (sổ gu G-007) | Trong ≤ 15 s đầu, hình có đi trước lời không? Có đặt ra một câu hỏi mở (open loop) cụ thể, được trả lời rõ ở hồi 3 không? **Người xem có thấy chủ đề liên quan đến chính mình không, qua một người và một khoảnh khắc cụ thể?** (G-007: "Cold open phải cho người xem thấy chủ đề liên quan đến chính mình — bằng một người và một khoảnh khắc cụ thể.") | Lời vào trước hoặc cùng lúc với hình. Không có câu hỏi, hoặc câu hỏi không bao giờ được trả lời. Chủ đề nói chung chung, không có ai trong đó ("lãi suất đang giảm") | Hình đi trước lời. Có câu hỏi nhưng chung chung ("chuyện gì đã xảy ra?"), hoặc hồi 3 trả lời ngầm, người xem phải tự nối. Có một người, nhưng là số trung bình không có khoảnh khắc ("người vay trung vị"), hoặc có khoảnh khắc mà người xem không thấy mình trong đó | Hình tự kể trước khi có lời. Câu hỏi cụ thể, khiến muốn xem tiếp. Hồi 3 trả lời đúng câu đó, gọi lại bằng cùng hình hoặc cùng chữ. **Một người cụ thể, ở một khoảnh khắc cụ thể** (ví dụ: tờ báo giá phí đóng hồ sơ $5,124 trên bàn, lãi vừa giảm nửa điểm), và người xem nhận ra "đây là quyết định của mình" | S15 (thời lượng) |
| H2 | DX-S4 câu móc lại | Ở 0:30–0:45 có câu hứa rõ điều người xem sẽ biết hoặc hiểu khi xem hết không? | Không có, hoặc nằm ngoài 0:30–0:45 | Có lời hứa nhưng mơ hồ ("chúng ta sẽ tìm hiểu…") | Một câu, cụ thể, đo được ("đến cuối, bạn sẽ thấy năm nào quyết định…"), và video giữ lời hứa | — |
| H3 | DX-S2 cấu trúc hồi (sổ gu G-009) | Mỗi hồi (1, 2, 3) có câu hỏi riêng, một bước ngoặt và một payoff trả lời câu hỏi đó không? **Kịch bản có là một câu chuyện không: bối cảnh → nhân vật → vấn đề → hành trình → đáp án; câu chữ liền mạch, có chuyển ý giữa các đoạn, không cụt lủn?** | Hồi không có câu hỏi riêng. Thông tin nối tiếp nhau, không có ngoặt. Đọc như danh sách số liệu; câu vụn nối câu vụn | Có câu hỏi và payoff, nhưng bước ngoặt yếu hoặc thiếu ở một hồi. Có nhân vật và vấn đề, nhưng vài đoạn nhảy ý không chuyển tiếp, hoặc có chuỗi câu cụt | Cả ba hồi: câu hỏi nêu rõ, bước ngoặt làm đổi cách hiểu, payoff khép câu hỏi và mở hồi sau. Nghe như một câu chuyện có người trong đó, đi từ bối cảnh tới đáp án; mỗi đoạn dẫn sang đoạn sau; câu ngắn chỉ dùng để nhấn | R01 (đỉnh, thung lũng), R05 (hồi 2 tăng tốc), S13 (không chuỗi câu vụn) |
| H4 | DX-S5 cái giá cụ thể (sổ gu G-008) | Cái giá có được nói bằng năm và số dư (ghi thực hay danh nghĩa), thay vì bằng khái niệm trừu tượng không? **Số liệu có gắn với hoàn cảnh của người xem không: một nhân vật, một kịch bản, một hệ quả?** (G-008: "Mọi số liệu phải gắn với hoàn cảnh của người xem (nhân vật, kịch bản, hệ quả), không diễn giải số đơn thuần.") | Chỉ nói khái niệm ("rủi ro thứ tự", "biến động"). Số đứng một mình, không thuộc về ai, không dẫn tới điều gì | Có số dư và năm nhưng ít, hoặc lẫn với cách nói trừu tượng ở chỗ quyết định. Số gắn với nhân vật hoặc kịch bản ở vài chỗ, nhưng con số quyết định thì không, hoặc không nói hệ quả | Mọi điểm quyết định đều gọi tên năm và số dư cụ thể (ví dụ "đến 1982, còn $X thực"). Người xem hình dung được hậu quả. **Mỗi con số quyết định thuộc về một nhân vật hoặc một kịch bản của hợp đồng tập, và nói hệ quả cho người đó** (ví dụ: "khoản vay $375,000 của người đó, giữ nhà 3 năm: cần cắt 0,56 điểm, nếu không thì mất $X") | S07, S09 (số có nguồn, ghi thực hay danh nghĩa), S16 (tạm: tỷ lệ câu có số quyết định gắn nhân vật hoặc kịch bản) |
| H5 | DX-V1 bố cục | Mỗi khung có thứ bậc ba mức rõ không (một thứ nhìn đầu tiên, vài thứ đọc sau, phần còn lại lùi)? Có đường dẫn mắt, khoảng trống phía trước theo hướng chuyển động, và khoảng âm có chủ ý không? | Nhiều thứ tranh nhau. Mắt không biết nhìn đâu. Khung chật | Thứ bậc rõ ở phần lớn khung. Vài khung chật, hoặc khoảng âm ngẫu nhiên | Mọi khung đọc được trong 1 giây. Khoảng âm dùng có chủ ý. Chuyển động luôn có chỗ để đi | V02 (vị trí mức 1), C10, V03, V11, V12 (chữ sắc khi máy chuyển) |
| H6 | DX-V7 hoạt hình | Có áp dụng lấy đà, theo đà, chồng lớp chuyển động, cung chuyển động, dàn cảnh không? Chữ có động theo nhịp lời không? | Chuyển động tuyến tính, mọi thứ động cùng lúc, chữ không theo lời | Có easing và vài lớp chồng. Một số chuyển động vẫn máy móc hoặc lệch nhịp lời | Mọi chuyển động có lấy đà và theo đà, lớp chồng tự nhiên, quỹ đạo cong. Chữ vào đúng nhịp lời. Dàn cảnh dẫn mắt tới điều cần thấy | V05 (máy quay 2.5D), C13 (số–lời) |
| H7 | DX-A2 nhạc không lộ vòng lặp | Nghe liền mạch, có nhận ra đoạn nhạc lặp lại y hệt (vòng lặp) không? Leitmotif có biến tấu theo số phận không? | Nghe rõ vòng lặp ngắn. Nhạc nền đơn điệu | Có lặp nhưng che được phần lớn. Leitmotif có nhưng ít biến tấu | Không nhận ra vòng lặp nào. Leitmotif của mỗi nhân vật nhận ra được và biến đổi theo diễn biến | T2 (tự tương đồng), A12 (accent–cắt), A08 (ducking) |
| H8 | DX-A1 âm thanh theo dữ liệu (sổ gu G-001, G-005, G-006) | Mỗi lần phần tử biểu đồ biến động (cột mọc, đường vẽ, điểm hiện) có nghe thấy tiếng riêng của nó không, ở khe nghỉ của lời và ở chỗ không có lời, mà không lấn lời? Tiếng có nói gì về dữ liệu không (cao độ theo giá trị, âm theo độ dốc, vị trí theo trục)? | Không nghe ra tiếng nào theo dữ liệu, hoặc chỉ nghe được khi đã biết trước chỗ để nghe | Nghe ra ở phần lớn các lần biến động, nhưng có đoạn mất (bị lời hay nhạc che), hoặc mọi phần tử cùng một tiếng, không theo giá trị | Mọi lần biến động đều nghe rõ, vào đúng khung. Cao độ, âm lượng và vị trí theo giá trị, nên nhắm mắt vẫn đoán được đường đi lên hay xuống. Không át lời, không mệt tai | T1 (nghe thấy ở khe nghỉ, dải tần của tập), L1 (không lấn lời), T3 (khoảng lặng) |

## Ghi phiếu chấm

Mỗi dòng ghi: `H# | điểm | mốc thời gian bằng chứng | một câu lý do`.

- Ghi rõ người chấm, ngày, và SHA-256 của master được chấm.
- Không chấm lại sau khi đã xem kết quả chấm của người khác.
- Với H8, ghi thêm nghe bằng gì (loa điện thoại, tai nghe, loa ngoài).
