import streamlit as st
st.set_page_config(
  page_title='Balaji Kesavan', 
  page_icon='🤝', 
  layout='centered', 
  initial_sidebar_state='auto'
)

st.header(':blue[Balaji Kesavan]')

personal_projects, skills, corporate_work_experience, about_me = st.tabs(['🕰️Personal Projects', '🧩Skills', '💼 Work Experience', '📂About Me'])

with personal_projects:
   
    st.subheader('📝:green[Cover Letter Craft]')
    st.write('Write a [cover letter](https://coverlettercraft.com/) that stands out from the crowd. This tool will help you craft a cover letter that is unique to you and the job you are applying for.')

    st.divider()
    st.subheader('❄️:violet[Arctic Analytics]')
    st.caption('Runs on a free server, it might take a few seconds to load')
    st.write('[Arctic Analytics](https://arctic-analytics.streamlit.app/) is a powerful AI-driven data analysis tool that can autonomously run code to analyze data and generate actionable insights. The agent can execute Python expressions for quick data queries, run complex multi-line functions for sophisticated data manipulations, and generate well-formatted visualizations using matplotlib, all while providing detailed reasoning about its analytical approach. This intelligent system can identify patterns, calculate KPIs, filter and aggregate data, and create comprehensive reports and charts to help users understand their data through automated analysis and interactive exploration.')

    st.divider()
    st.subheader('🗒️:blue[Prep My Visit]')
    st.caption('Runs on a free server, it might take a few seconds to load')
    st.write('[prep-my-visit](https://prep-my-visit.streamlit.app/) is an AI-powered tool that helps patients prep for their doctor’s visit by capturing the key details of their symptom story. Through a few rounds of smart follow-up questions, it generates a clean summary and a structured clinical note focused on the “S” and “O” of SOAP—what the patient is experiencing and what’s observable—so the doctor can focus on what they do best: assessment and planning. Patients feel more prepared. Clinicians start with the signal, not the noise. It also outputs a FHIR R4–compliant JSON bundle that can be integrated with health care systems.')

    st.divider()
    st.subheader('🛠️:grey[Tool calling is all you need]')
    st.caption('Runs on a free server, it might take a few seconds to load')
    st.write('[Tool calling is all you need](https://esports-manager-challenge-tool-calling-is-all-you-need.streamlit.app/) is an implementation of a multi-agent framework using the AWS Bedrock converse API, prompt engineering & tool calling to build Valorant teams and answer questions about Valorant players.')

    st.divider()    
    st.subheader('🔍:orange[Supah Search]')
    st.caption('Runs on a free server, it might take a few seconds to load')
    st.write('[Supah Search](https://supahsearch.com/) is a comprehensive AI-powered assistant that acts as an intelligent "force multiplier" for users. It goes far beyond traditional web searching to include web research, integration with MCP (Model Context Protocol) servers for specialized data access, on-demand image generation, and location-based queries. The tool handles complex multi-faceted queries while delivering personalized, markdown-formatted responses with relevant media content and contextual follow-up questions for deeper exploration.')

    st.divider()
    st.subheader('📝:blue[The AI Pencil]')
    st.caption('Runs on a free server, it might take a few seconds to load')
    st.write("[The AI Pencil](https://theaipencil.com/) provides you with substantial content foundations that you can customize and complete with your personal touch. Rather than starting from scratch, you'll get well-developed content with clear indicators showing where to add your specific examples, insights, and expertise. This tool enhances and accelerates your writing process rather than replacing your creativity. It doesn't have internet access and works best when you add your unique perspective to the foundation it provides. Use The AI Pencil to get a strong head start on your writing projects.")

    st.divider()
    st.subheader('📄PDF Merger')
    st.caption('Runs on a free server, it might take a few seconds to load')
    st.write('[PDF Merger](https://pdf-merger.streamlit.app/) merges multiple PDF files into a single PDF file.')

with skills:

    st.subheader('🛠️:green[Technical Skills]')
    with st.expander(':blue[AI Application Development]', expanded=True):
        st.write('Leveraged technology from OpenAI, Meta, Anthropic, Streamlit, Render, Supabase, Replicate, Snowflake, Azure, AWS, Bing Search, and more to build multiple AI applications')

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        with st.expander(':blue[Programming Languages]', expanded=True):
            st.write('Python, R, SQL')
    with row1_col2:
        with st.expander(':blue[Machine Learning & Predictive Modeling]', expanded=True):
            st.write('Skilled in developing and implementing machine learning algorithms for predictive analytics')

    st.subheader('✨:violet[Soft Skills]')
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        with st.expander(':blue[Team Leadership & Collaboration:]', expanded=True):
            st.write('Experienced in mentoring teams and fostering collaborative environments to achieve business objectives')
        with st.expander(':blue[Stakeholder Management]', expanded=True):
            st.write('Effective in engaging with stakeholders to translate technical details into actionable business insights')
    with row2_col2:
        with st.expander(':blue[Strategic Planning & Execution]', expanded=True):
            st.write('Adept at strategic planning and execution with a focus on delivering results')
        with st.expander(':blue[Problem Solving & Innovation]', expanded=True):
            st.write('Strong problem-solving skills with a track record of innovative solutions in complex scenarios')


with corporate_work_experience:

    st.caption(':blue[12+ years of experience in Data Science and Analytics]')
    with st.expander(':green[Data Science at Nike]\n\nJune 2017 - Present', expanded=True):
        st.markdown('''* Engaged with stakeholders to provide thought leadership and foster adoption of advanced analytics and AI
* Led end-to-end delivery of advanced analytics and AI solutions, from problem definition to deployment and monitoring
* Built a tool leveraging Machine Learning to simulate the orderpools of Nike’s centralized Distribution Centers 
* This tool aids planning teams in simulating the impact of changes to staffing levels, prioritization rules, and network allocation
* Developed a forecasting engine (ARIMA & ETS) for demand prediction of Nike products across various hierarchies and timeframes
* Mentored a team of five offshore individual contributors, focusing on methodologies and priority management
* Technologies: Python, SQL, SageMaker
''')

    with st.expander(':grey[Campaign Analytics Consultant at Microsoft]\n\nOctober 2015 - June 2017', expanded=True):
        st.markdown('''* Designed AB testing experiments targeting end users with email and in-app marketing campaigns to evaluate their effectiveness
* Developed a campaign sizing tool enabling precise segmentation and analysis of end-user data for optimized audience targeting
* Technologies: R, SQL, PowerBI
''')

    with st.expander(':violet[Data Science at Humana]\n\nJanuary 2015 - October 2015', expanded=True):
        st.markdown('''* Created an integrated referral framework, which refers Humana members to programs based on the output of multiple predictive models
* Built a predictive model identifying Humana members at high risk of suicide, utilizing data from medical claims, prescription claims, lab results, and program participation
* Technologies: SAS, SQL
''')

    with st.expander(':orange[Data Science at Mu Sigma]\n\nJuly 2011 - June 2013', expanded=True):
        st.markdown('''* Built an optimization to segment sales force of the large pharmaceutical client
* Built logistic regression models to identify B2B leads across multiple product lines, business units and regions for the business
* Technologies: SAS, SQL
''')

with about_me:
    
    st.subheader(':blue[About Me]')

    left_col, right_col = st.columns([3,1])
    with left_col:
        st.write('''Hello and welcome to my website. My name is Balaji Kesavan, a tenacious and forward-thinking data science and analytics professional. My career trajectory has been enriched by significant roles across industry-leading organizations. The best place to get in touch with me is on [LinkedIn](https://www.linkedin.com/in/balaji-kesavan/)''')
        st.write('''Over the last few years I am excited to see the advancements in Machine Learning and Artificial Intelligence. I am passionate about leveraging these technologies to solve complex problems. I am always looking for opportunities to collaborate on projects that are challenging and impactful.''')
        st.write('''Check out my [GitHub](https://github.com/balajikesavan90)''')
        st.write('''Check out my [ORCID Profile](https://orcid.org/0009-0002-7714-518X)''')

    with right_col:
        st.image('balaji.jpg')