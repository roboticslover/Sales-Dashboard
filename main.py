import streamlit as st


def main():
    st.title("Sales Dashboard Website")
    st.write("This project includes a dashboard for visualizing sales data.")

    st.image("first.png", caption="Sales Dashboard", use_column_width=True)

    st.header("Download Sales Dashboard")
    st.write("Download the sales dashboard file 'first.pbix' below:")
    with open('first.pbix', 'rb') as f:
        st.download_button(label='Download first.pbix', data=f,
                           file_name='first.pbix', mime='application/octet-stream')


if __name__ == "__main__":
    main()
