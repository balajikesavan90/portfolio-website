import streamlit as st
st.set_page_config(
  page_title='Balaji Kesavan', 
  page_icon='🛠️', 
  layout='centered', 
  initial_sidebar_state='auto'
)

st.header(':blue[Balaji Kesavan]')

personal_projects, skills, corporate_work_experience, about_me = st.tabs(['Personal Projects', 'Skills', 'Corporate Work Experience', 'About Me'])

with personal_projects:
   
    st.subheader(':green[Cover Letter Craft]')
    st.write('Write a [cover letter](https://coverlettercraft.com/) that stands out from the crowd. This tool will help you craft a cover letter that is unique to you and the job you are applying for.')

    st.divider()
    st.subheader(':grey[Arctic Analytics]')
    st.write('[Arctic Analytics](https://arctic-analytics.streamlit.app/) can answer questions about your data, build charts and graphs from your data, and help document and debug your codebase. Arctic Analytics does not get access to your dataset.')

    st.divider()    
    st.subheader(':violet[Supah Search]')
    st.write('[Supah Search](https://supahsearch.com/) searches the internet and summarizes the results while giving you the sources and respecting robots.txt restrictions. The user can also perform semantic searches on their search history.')

    st.divider()
    st.subheader(':orange[PDF Merger]')
    st.write('[PDF Merger](https://pdf-merger.streamlit.app/) merges multiple PDF files into a single PDF file.')

with skills:

    st.subheader(':green[Technical Skills]')
    with st.expander(':black[AI Application Development]'):
        st.write('Leveraged technology from OpenAI, Streamlit, Supabase, Replicate, Snowflake, Azure, Bing Search, and more to build multiple AI applications')

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        with st.expander(':black[Programming Languages]'):
            st.write('Python, R, SQL')
    with row1_col2:
        with st.expander(':black[Machine Learning & Predictive Modeling]'):
            st.write('Skilled in developing and implementing machine learning algorithms for predictive analytics')

    st.subheader(':violet[Soft Skills]')
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        with st.expander(':black[Team Leadership & Collaboration:]'):
            st.write('Experienced in mentoring teams and fostering collaborative environments to achieve business objectives')
        with st.expander(':black[Stakeholder Management]'):
            st.write('Effective in engaging with stakeholders to translate technical details into actionable business insights')
    with row2_col2:
        with st.expander(':black[Strategic Planning & Execution]'):
            st.write('Adept at strategic planning and execution with a focus on delivering results')
        with st.expander(':black[Problem Solving & Innovation]'):
            st.write('Strong problem-solving skills with a track record of innovative solutions in complex scenarios')


with corporate_work_experience:

    st.caption(':blue[11+ years of experience in Data Science and Analytics]')
    with st.expander(':green[Data Science at Nike]\n\nJune 2017 - Present'):
        st.markdown('''* Engaged with stakeholders to provide thought leadership and foster adoption of advanced analytics
* Built a tool leveraging Machine Learning to simulate the orderpools of Nike’s centralized Distribution Centers 
* This tool aids planning teams in simulating the impact of changes to staffing levels, prioritization rules, and network allocation
* Developed a forecasting engine (ARIMA & ETS) for demand prediction of Nike products across various hierarchies and timeframes
* Mentored a team of five offshore individual contributors, focusing on methodologies and priority management
* Technologies: Python, SQL, SageMaker
''')
    
    with st.expander(':grey[Campaign Analytics Consultant at Microsoft]\n\nOctober 2015 - June 2017'):
        st.markdown('''* Designed AB testing experiments targeting end users with email and in-app marketing campaigns to evaluate their effectiveness
* Developed a campaign sizing tool enabling precise segmentation and analysis of end-user data for optimized audience targeting
* Technologies: R, SQL, PowerBI
''')
    
    with st.expander(':violet[Data Science at Humana]\n\nJanuary 2015 - October 2015'):
        st.markdown('''* Created an integrated referral framework, which refers Humana members to programs based on the output of multiple predictive models
* Built a predictive model identifying Humana members at high risk of suicide, utilizing data from medical claims, prescription claims, lab results, and program participation
* Technologies: SAS, SQL
''')
        
    with st.expander(':orange[Data Science at Mu Sigma]\n\nJuly 2011 - June 2013'):
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

    with right_col:
        st.image('balaji.jpg')