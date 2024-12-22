
import streamlit as st

# Hàm phân loại level và gán màu theo số lượng tab
def get_level_and_color(line):
    tab_count = len(line) - len(line.lstrip('\t'))  # Đếm số lượng tab ở đầu dòng
    
    if tab_count == 0:
        # Level 1: Không có tab, màu đỏ
        return f'<span style="color:red; white-space:pre-wrap;">{line}</span>'
    elif tab_count == 1:
        # Level 2: 1 tab, màu xanh dương
        return f'<span style="color:blue; white-space:pre-wrap;">{line}</span>'
    elif tab_count == 2:
        # Level 3: 2 tabs, màu đen
        return f'<span style="color:gray; white-space:pre-wrap;">{line}</span>'
    else:
        # Level 4: 3 tabs trở lên, màu xám
        return f'<span style="color:lightgray; white-space:pre-wrap;">{line}</span>'

# Tải lên tệp tin
uploaded_file = st.file_uploader("Chọn tệp .txt để tải lên", type="txt")

if uploaded_file is not None:
    # Đọc nội dung tệp
    lines = uploaded_file.readlines()
    # Chuyển đổi từ bytes sang string
    lines = [line.decode("utf-8") for line in lines]
    
    # Gán màu cho các dòng theo level
    colored_lines = [get_level_and_color(line) for line in lines]
    
    # Kết hợp các dòng đã phân loại và thêm thẻ <pre> để giữ nguyên định dạng tab và khoảng trắng
    output = "<pre>" + "".join(colored_lines) + "</pre>"
    
    # Hiển thị kết quả trong Streamlit
    st.markdown(output, unsafe_allow_html=True)
