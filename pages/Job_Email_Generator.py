import streamlit as st
from llm_helper import llm

class Skills:
    def __init__(self):
        self.skills = dict()
        self.profile = dict()

    def getSkills(self):
        return self.skills
    
    def getProfile(self):
        return self.profile

s = Skills()

class Projects:
    def __init__(self):
        self.projects = dict()

    def getProjects(self):
        return self.projects
    
p = Projects()


def Generate():
    # Fetch skills data from the Skills instance
    skills_data = s.getSkills()
    profile = s.getProfile()
    projects = p.getProjects()

    # Prepare the prompt
    prompt = f"""
    Hey! Generate an email message based on the following:
    Profile : {profile}
    Skills : {skills_data}
    Mention all skills in a paragraph with **bold text** and don't give the subject for the email.
    Here are the projects with their skills and descriptions. Overwhelm my projects by adding sugar-coating:
    Projects: {projects}
    Write a professional email based on this data with NO PREAMBLE.
    """
    
    # Invoke the LLM with the prompt
    res = llm.invoke(prompt)
    
    # Display the result with Markdown effects
    st.subheader("Generated Email")
    st.markdown(res.content)  # Display as Markdown
    st.success("Email generated! Use the 'Copy' button to save it to your clipboard.")

    # Optionally display the raw text with "Copy to Clipboard" functionality
    st.code(res.content, language="")

    
def main():
    st.subheader("Email and LinkedIn Post Generator using Llama3.2")
    st.text("This is for educational purposes. Please use with caution.")

    # Collect user details
    name = st.text_input(label="Enter your Name:")
    email = st.text_input(label="Enter your Email:")
    mob = st.text_input(label="Enter your Mobile Number:")

    s.profile["name"] = name or "Ram"
    s.profile["email"] = email or "enter_your_email@gmail.com"
    s.profile["mobile_number"] = mob or "+91 XXXXXXXXXX"

    # Experience Level
    options = ["Entry level", "1 year Experience", "2 years Experience", "3+ years Experience"]
    opt = st.selectbox(label="Select your Experience Level:", options=options)
    s.profile["Experience"] = opt

    st.markdown("---")
    st.subheader("Skills")

    # Frontend Technologies
    frontend_technologies = st.multiselect(
        "Select Frontend Technologies",
        ["ReactJs", "AngularJs", "VueJs", "HTML", "CSS", "JavaScript", "TypeScript", "SASS", "Tailwind CSS", "Bootstrap"]
    )
    s.skills["frontend"] = frontend_technologies or None

    # Backend Technologies
    backend_technologies = st.multiselect(
        "Select Backend Technologies",
        ["Node.js", "Django", "Flask", "Spring Boot", "Ruby on Rails", "Express.js", "ASP.NET", "FastAPI", "GraphQL", "PHP", "Go"]
    )
    s.skills["backend"] = backend_technologies or None

    # Additional Skills
    additional_skills = st.text_input(label="Enter additional skills not in the above list:")
    s.skills["additional"] = additional_skills or None

    st.markdown("---")
    st.subheader("Projects")

    # Project 1
    pro1 = st.text_input(label="Enter your Project-1 Name:")
    pro1Des = st.text_area(label="Description About Project-1:")
    pro1Skills = st.text_input(label="Technologies Used in Project-1:")
    p.projects["Project_one_name"] = pro1
    p.projects["Project_one_description"] = pro1Des
    p.projects["Skills_used_in_project_one"] = pro1Skills

    # Project 2
    pro2 = st.text_input(label="Enter your Project-2 Name:")
    pro2Des = st.text_area(label="Description About Project-2:")
    pro2Skills = st.text_input(label="Technologies Used in Project-2:")
    p.projects["Project_two_name"] = pro2
    p.projects["Project_two_description"] = pro2Des
    p.projects["Skills_used_in_project_two"] = pro2Skills

    # Button to trigger Generate
    if st.button("Generate"):
        Generate()


if __name__ == "__main__":
    main()
