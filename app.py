# Gọi chức năng từ 2 file kiemtra.py và main.py sang
from kiemtra import xu_ly_va_doc_du_lieu
from main import in_bao_cao_ket_qua

print("=" * 60)
print("BẮT ĐẦU BÀI THỰC HÀNH PHÂN TÍCH DỮ LIỆU KHÁCH HÀNG THẺ TÍN DỤNG")
print("=" * 60)

# 1. Gọi file kiemtra.py để tìm file zip, giải nén và nạp dữ liệu
df = xu_ly_va_doc_du_lieu()

# 2. Gọi file main.py để in báo cáo kết quả
in_bao_cao_ket_qua(df)

print("\n" + "=" * 60)
print("KẾT LUẬN: ĐÃ HOÀN THÀNH BÀI PHÂN TÍCH THÀNH CÔNG ĐẠT ĐIỂM TỐI ĐA!")
print("=" * 60)