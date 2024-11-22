import streamlit as st
from streamlit_ace import st_ace
import io
import contextlib

def run_text_editor() -> None:
    """Function to run the text editor with Dracula theme."""
    
    # Default code
    default_code = "# Write your Python code here...\n\nprint('Hello, World!')"
    
    # Display the Ace editor with Dracula theme
    text = st_ace(
        value=default_code,
        language="python",
        theme="dracula",  # Dracula theme
        height=300,
        key="ace_editor",
    )
    
    # Run button
    if st.button("Run"):
        try:
            # Capture the stdout and stderr output
            output_buffer = io.StringIO()
            with contextlib.redirect_stdout(output_buffer):
                with contextlib.redirect_stderr(output_buffer):
                    exec(text, {})  # Execute the code in an isolated namespace

            # Display the output
            output = output_buffer.getvalue()
            st.write("**Output:**")
            st.text(output if output.strip() else "Code executed successfully without output.")
        
        except Exception as e:
            # Display errors in execution
            st.write("**Error:**")
            st.text(str(e))

def main() -> None:
    """Main function to run the app."""
    
    st.subheader("Python Code Editor & Runner with Dracula Theme")
    st.write("Write your Python code in the Dracula-themed editor below and hit 'Run' to execute.")
    
    # Run the text editor
    run_text_editor()

    # Add the footer
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 10%;
            width: 100%;
            color: green;
            text-align: center;
            
        }
        </style>
        <div class="footer">
            Made with ❤️ in India - Tagore
        </div>
        """,
        unsafe_allow_html=True,
    )

# Run the app if __name__ == "__main__":
if __name__ == "__main__":
    main()
