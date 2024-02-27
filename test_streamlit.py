import streamlit as st

placeholder = st.empty()

# Hiển thị đoạn văn bản định dạng Markdown
markdown_text = """
# Tiêu đề lớn
## Tiêu đề nhỏ
- Mục đầu tiên
- Mục thứ hai
- Mục thứ ba
"""

placeholder.markdown(markdown_text)

# Hiển thị liên kết định dạng Markdown
markdown_link = "[Google](https://www.google.com)"
placeholder.markdown(markdown_link)

# Hiển thị danh sách định dạng Markdown
markdown_list = """
- Mục 1
- Mục 2
- Mục 3
"""
placeholder.markdown(markdown_list)