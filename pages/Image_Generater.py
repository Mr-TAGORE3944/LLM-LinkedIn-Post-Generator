from huggingface_hub import InferenceClient
import streamlit as st

client = InferenceClient("Jovie/Midjourney", token="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")

def main():
    st.subheader("Image Generation with Mid Journey! AI")
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    prompt = st.text_input(label="Enter your prompt here...")
    options = ["realistic", "anime", "toon", "dark", "funny"]
    option = st.selectbox(label="Select your preferences...", options=options)
    image_placeholder = st.empty()
    
    # Generate button
    if st.button("Generate"):
        final_prompt = f"""
        Hey! create an image with prompt: '{prompt}'. Add some taste with {option}.
        """
        # Display the loader
        with image_placeholder:
            st.image("pages/loader.gif", caption="Generating image...")


        try:
            # Generate the image
            image = client.text_to_image(final_prompt)
            if image:
                image_placeholder.image(image, caption="Generated Image")
            else:
                st.error("Something went wrong!")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
