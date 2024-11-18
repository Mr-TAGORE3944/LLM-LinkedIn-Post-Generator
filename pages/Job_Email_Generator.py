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

    def p(self):
        print(self.skills)
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
    prompt = f"""
    Hey! Generate an email message based on the following :
    Profile : {profile}
    Skills : {skills_data}
    Hey! mention all skills in paragraph manner in bold text and don't give the subject for email.
    Here I give projects with their skills and description. Overwhlem my projects with adding sugarCoating 
    Projects: {projects}
    from the give data write an professtional Email with NO PREAMBLE
    """
    
    # Invoke the LLM with the prompt
    res = llm.invoke(prompt)
    # Display the result
    st.write(res.content)


def main():
    st.subheader("Email and LinkedIn Post Generator using Llama3.2")
    st.text("It is Educational Purpose. Please use with caution.")

    # Collect user details
    name = st.text_input(label="Enter your Name:")
    email = st.text_input(label="Enter your Email:")
    mob = st.text_input(label="Enter your Mobile Number:")
    s.profile["name"] = name or "Ram"
    s.profile["email"] = email or "enter_your_email@gmail.com"
    s.profile["mobile_number"] = mob or "+91 XXXXXXXXXX"


    options = ["Entry level", "1 year Experience", "2 years Experience", "3+ years Experience"]
    opt = st.selectbox(label="Select your Experience Level:", options=options)
    # st.write(opt)
    s.profile["Exprience"] = opt
    st.html("<hr/>")

    st.subheader("Skills")

    # st.write(s.profile)

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

    # Machine Learning
    machine_learning_technologies = st.multiselect(
        "Select Machine Learning Technologies",
        ["TensorFlow", "PyTorch", "Scikit-Learn", "Keras", "XGBoost", "OpenCV", "NLTK", "Pandas", "NumPy", "Hugging Face Transformers"]
    )
    s.skills["ML"] = machine_learning_technologies or None

    # Operating Systems
    operating_systems = st.multiselect(
        "Select Operating Systems",
        ["Linux", "Windows", "MacOS", "Unix", "Ubuntu", "CentOS", "Red Hat", "Debian", "Kali Linux", "Fedora"]
    )
    s.skills["OS"] = operating_systems or None

    # Cloud Platforms
    cloud_platforms = st.multiselect(
        "Select Cloud Platforms",
        ["AWS", "Google Cloud", "Microsoft Azure", "IBM Cloud", "Heroku", "DigitalOcean", "Oracle Cloud", "Cloudflare", "Alibaba Cloud"]
    )
    s.skills["cloud_platforms"] = cloud_platforms or None

    # DevOps Tools
    devops_tools = st.multiselect(
        "Select DevOps Tools",
        ["Docker", "Kubernetes", "Jenkins", "Git", "GitHub Actions", "GitLab CI/CD", "Terraform", "Ansible", "Puppet", "Chef"]
    )
    s.skills["devops_tools"] = devops_tools or None

    # Databases
    databases = st.multiselect(
        "Select Databases",
        ["MySQL", "PostgreSQL", "MongoDB", "SQLite", "Redis", "Cassandra", "MariaDB", "Oracle DB", "Firebase", "ElasticSearch"]
    )
    s.skills["databases"] = databases or None

    # Programming Languages
    programming_languages = st.multiselect(
        "Select Programming Languages",
        ["Python", "Java", "JavaScript", "C++", "C#", "Ruby", "Go", "Rust", "Swift", "PHP", "Kotlin", "R"]
    )
    s.skills["programming_languages"] = programming_languages or None

    # Testing Tools
    testing_tools = st.multiselect(
        "Select Testing Tools",
        ["Selenium", "Jest", "Mocha", "Cypress", "JUnit", "Postman", "SoapUI", "Robot Framework", "Appium", "Cucumber"]
    )
    s.skills["testing_tools"] = testing_tools or None

    # Mobile Development
    mobile_development_tools = st.multiselect(
        "Select Mobile Development Tools",
        ["React Native", "Flutter", "Swift", "Kotlin", "Ionic", "Cordova", "Xamarin", "Unity", "Objective-C", "Java for Android"]
    )
    s.skills["mobile_development_tools"] = mobile_development_tools or None

    # Analytics & Visualization
    analytics_visualization_tools = st.multiselect(
        "Select Analytics & Visualization Tools",
        ["Tableau", "Power BI", "Google Data Studio", "Matplotlib", "Seaborn", "Plotly", "D3.js", "Excel", "Looker", "QlikView"]
    )
    s.skills["analytics_visualization_tools"] = analytics_visualization_tools or None

    # Cybersecurity Tools
    cybersecurity_tools = st.multiselect(
        "Select Cybersecurity Tools",
        ["Wireshark", "Metasploit", "Nmap", "Burp Suite", "OWASP ZAP", "Kali Linux", "Splunk", "Snort", "Nessus", "Fortinet"]
    )
    s.skills["cybersecurity_tools"] = cybersecurity_tools or None

    # Message Queues
    message_queues = st.multiselect(
        "Select Message Queues",
        ["RabbitMQ", "Kafka", "ActiveMQ", "Amazon SQS", "Google Pub/Sub", "Redis Streams", "ZeroMQ", "Apache Pulsar"]
    )
    s.skills["message_queues"] = message_queues or None

    # Additional Skills
    additional_skills = st.text_input(label="Enter additional skills not in the above list:")
    s.skills["additional"] = additional_skills or None


    st.html("<hr/>")

    st.subheader("Projects")


    pro1 = st.text_input(label="Enter your Project-1 ")
    pro1Des = st.text_area(label="Description About your Project")
    pro1Skills = st.text_input(label="Technologies Used in Project-1 ")
    p.projects["Project_one_name"] = pro1
    p.projects["Project_one_description"] = pro1Des
    p.projects["Skills_used_in_project_one"] = pro1Skills
    st.html("<hr/>")
    pro2 = st.text_input(label="Enter your Project-2 ")
    pro2Des = st.text_area(label="Description About Project-2 ")
    pro2Skills = st.text_input(label="Technologies Used in Project-2 ")
    p.projects["Project_two_name"] = pro2
    p.projects["Project_two_description"] = pro2Des
    p.projects["Skills_used_in_project_two"] = pro2Skills


























    # Button to trigger Generate
    if st.button("Generate"):
        Generate()


if __name__ == "__main__":
    main()
