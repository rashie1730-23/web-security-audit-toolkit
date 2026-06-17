import streamlit as st
import tempfile

from steganography.encode import encode_message
from steganography.decode import decode_message


def render_steganography():

    st.markdown("""
    # 🖼️ Steganography Studio

    Hide secret messages inside images using LSB steganography.
    """)

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    message = st.text_area(
        "Secret Message",
        placeholder="Enter your secret message here..."
    )

    if uploaded_file is not None:

        col1, col2 = st.columns(2)

        with col1:

            st.image(
                uploaded_file,
                caption="Original Image",
                use_container_width=True
            )

        if st.button(
            "🔐 Encode Message",
            use_container_width=True
        ):

            try:

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".png"
                ) as temp_input:

                    temp_input.write(
                        uploaded_file.getbuffer()
                    )

                    input_path = temp_input.name

                output_path = (
                    input_path.replace(
                        ".png",
                        "_encoded.png"
                    )
                )

                encode_message(
                    input_path,
                    message,
                    output_path
                )

                st.success(
                    "✅ Message Hidden Successfully"
                )

                with open(
                    output_path,
                    "rb"
                ) as file:

                    st.download_button(
                        label="📥 Download Encoded Image",
                        data=file,
                        file_name="encoded_image.png",
                        mime="image/png"
                    )

                decoded_message = decode_message(
                    output_path
                )

                st.info(
                    f"🔍 Verification: {decoded_message}"
                )

            except Exception as e:

                st.error(
                    f"Encoding Error: {str(e)}"
                )

    else:

        st.info(
            "Upload an image to begin."
        )