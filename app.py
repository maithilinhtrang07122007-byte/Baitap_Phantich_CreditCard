import streamlit as st
import pandas as pd
import plotly.express as px

# Cấu hình giao diện rộng, chuyên nghiệp
st.set_page_config(page_title="Phân tích Thẻ tín dụng", layout="wide")
st.title("📊 Hệ Thống Phân Tích Dữ Liệu Khách Hàng & Nợ Xấu")
st.markdown("---")

# Tên file dữ liệu trong thư mục
file_path = "default of credit card clients.xls"

try:
    # Đọc dữ liệu (bỏ qua dòng text giải thích đầu tiên)
    df = pd.read_excel(file_path, skiprows=1)
    
    # Chuẩn hóa nhãn dữ liệu
    df['GIỚI TÍNH'] = df['SEX'].map({1: 'Nam', 2: 'Nữ'})
    df['HỌC VẤN'] = df['EDUCATION'].map({1: 'Cao học', 2: 'Đại học', 3: 'Bản xứ/CĐ', 4: 'Khác'})
    df['HỌC VẤN'] = df['HỌC VẤN'].fillna('Khác')
    df['TRẠNG THÁI'] = df['default payment next month'].map({0: 'Đúng hạn', 1: 'Nợ xấu'})

    # ---- THANH BỘ LỌC SIDEBAR ----
    st.sidebar.header("⚙️ Bộ Lọc Phân Tích")
    gen_list = df['GIỚI TÍNH'].unique().tolist()
    selected_gen = st.sidebar.multiselect("Chọn Giới Tính:", gen_list, default=gen_list)
    
    # Lọc dữ liệu
    df_filtered = df[df['GIỚI TÍNH'].isin(selected_gen)]

    # ---- HIỂN THỊ KPI ----
    total = len(df_filtered)
    bad = int((df_filtered['default payment next month'] == 1).sum())
    rate = round((bad/total)*100, 2) if total > 0 else 0

    c1, c2, c3 = st.columns(3)
    c1.metric("👥 Tổng khách hàng", f"{total:,}")
    c2.metric("⚠️ Số ca nợ xấu", f"{bad:,}")
    c3.metric("🚨 Tỷ lệ nợ xấu", f"{rate}%")

    st.markdown("---")

    # ---- BIỂU ĐỒ ----
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.subheader("📈 Tỷ lệ trạng thái thanh toán")
        fig_pie = px.pie(df_filtered, names='TRẠNG THÁI', color='TRẠNG THÁI', 
                         color_discrete_map={'Đúng hạn':'#2ecc71','Nợ xấu':'#e74c3c'})
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col_chart2:
        st.subheader("📊 Phân bố nợ xấu theo học vấn")
        fig_bar = px.bar(df_filtered, x='HỌC VẤN', color='TRẠNG THÁI', barmode='group')
        st.plotly_chart(fig_bar, use_container_width=True)

    st.subheader("🔍 Danh sách dữ liệu chi tiết")
    st.dataframe(df_filtered.head(50))

except Exception as e:
    st.error(f"Đang đợi file dữ liệu... Lỗi: {e}")