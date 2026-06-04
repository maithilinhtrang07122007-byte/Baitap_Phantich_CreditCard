import streamlit as st
import pandas as pd

st.set_page_config(page_title="Phân tích Thẻ tín dụng", layout="centered")
st.title("📊 Ứng dụng Phân tích Khách hàng Thẻ Tín dụng")
st.markdown("---")

# Đọc trực tiếp file dữ liệu bạn vừa tải lên
try:
    # Bỏ qua 1 dòng đầu để lấy đúng tên cột chuẩn
    df = pd.read_csv("default of credit card clients.xls - Data.csv", skiprows=1)
    
    st.success("🎉 Nạp dữ liệu thành công từ file CSV!")
    st.subheader("📌 Kết quả Thống kê Tổng quan")
    
    total_rows = df.shape[0]
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Tổng số hồ sơ phân tích", value=f"{total_rows:,} người")
    with col2:
        st.metric(label="Số lượng thuộc tính", value=f"{df.shape[1]} cột")
        
    st.subheader("💳 Trạng thái Nợ xấu (Thực tế từ dữ liệu)")
    # Cột cuối cùng Y hoặc default payment next month
    target_col = df.columns[-1]
    bad_credit = int((df[target_col] == 1).sum())
    good_credit = total_rows - bad_credit
    
    st.write(f"✔️ **Đúng hạn:** {good_credit:,} người ({round(good_credit/total_rows*100, 2)}%)")
    st.write(f"⚠️ **Nợ xấu:** {bad_credit:,} người ({round(bad_credit/total_rows*100, 2)}%)")
    
    st.subheader("👀 Xem trước bảng dữ liệu thô")
    st.dataframe(df.head(10))

except Exception as e:
    st.error("❌ Hệ thống đang đợi bạn up file dữ liệu lên GitHub cùng thư mục!")