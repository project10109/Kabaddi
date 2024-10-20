import streamlit as st
import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings('ignore')
# from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import gspread

def get_df_new():
    
    dataframe1 = pd.read_csv('Kabaddi 2024_Google.csv')
    return dataframe1

df = get_df_new()

df['Team'] = df['Team'].fillna(' ')


# Get unique team names
team1_choices = df['Team'].drop_duplicates().unique()
team2_choices = df['Team'].drop_duplicates().unique()

# Select Team 1 and Team 2
team1_choice = st.sidebar.selectbox('Select Team1:', team1_choices,index=1)
team2_choice = st.sidebar.selectbox('Select Team2:', team2_choices,index=3)

st.sidebar.title('Developed by :')
st.sidebar.markdown('[![Rohit Nair]'
                    '(https://img.shields.io/badge/Author-Rohit%20Nair-brightgreen)]'
                    '(https://www.linkedin.com/in/rohitn220/)')


# Create datafarame for team 1 and team 2

team1 = df[df['Team']==team1_choice].reset_index(drop=True)
team2 = df[df['Team']==team2_choice].reset_index(drop=True)

# Header for Right Raiders
st.header('Right Raiders')

# Sub header for team 1
st.subheader('Player Battle for' +'  ' +('{}'.format(team1_choice)))


#col1, col2 = st.columns([2, 1])

# Right Raider for Team 1
right_raider_team1  = team1[team1['Type']=='Right Raider'].reset_index(drop=True)
try:
    def_cover_team2=team2[team2['Type'].isin( ['Left Corner','Right Cover'])]
except:
    def_cover_team2=team2[team2['Type'].isin( ['Right Cover'])]

def_cover_team2.set_index('Team')
right_raider_names=pd.DataFrame(list(right_raider_team1['Name'].values))
def_cover_team2_names=pd.DataFrame(list(def_cover_team2['Name'].values))
def_cover_team2_names.columns=['Defender']
right_raider_names.columns=['Raider']
final=pd.concat([right_raider_names,def_cover_team2_names])
final=final.fillna('')
#final.columns=['Raider','Defender']
 
#st.text('{}'.format(list(right_raider_team1['Name'])) +' VS ' +('{}'.format(list(def_cover_team2['Name']))))
#AgGrid(final)
data_container = st.container()
with data_container:
    table, plot = st.columns(2)
    with table:
        st.table(right_raider_names)
    with plot:
        st.table(def_cover_team2_names)

# Right Raider for Team 2
st.subheader('Player Battle for' +'  ' +('{}'.format(team2_choice)))
right_raider_team2  = team2[team2['Type']=='Right Raider'].reset_index(drop=True)

try:
    def_cover_team1=team1[team1['Type'].isin( ['Left Corner','Right Cover'])]
except:
    def_cover_team1=team1[team1['Type'].isin( ['Right Cover'])]

def_cover_team1.set_index('Team')
right_raider_names2=pd.DataFrame(list(right_raider_team2['Name'].values))
def_cover_team1_names=pd.DataFrame(list(def_cover_team1['Name'].values))
#print('def_cover_team1_names',def_cover_team1_names)
def_cover_team1_names.columns=['Defender']
right_raider_names2.columns=['Raider']
final=pd.concat([right_raider_names2,def_cover_team1_names])
final=final.fillna('')
#final.columns=['Raider','Defender']
 
#st.text('{}'.format(list(right_raider_team1['Name'])) +' VS ' +('{}'.format(list(def_cover_team2['Name']))))
#AgGrid(final)
data_container = st.container()
with data_container:
    table, plot = st.columns(2)
    with table:
        st.table(right_raider_names2)
    with plot:
        st.table(def_cover_team1_names)

#st.text('{}'.format(list(right_raider_team2['Name'])) +' VS ' +('{}'.format(list(def_cover_team1['Name']))))


# Header for Left Raiders
st.header('Left Raiders')

# Right Raider for Team 1
st.subheader('Player Battle for' +'  ' +('{}'.format(team1_choice)))


# Left Raider for team 1
try:
    left_raider_team1  = team1[team1['Type']=='Left Raider'].reset_index(drop=True)

    try:
        def_leftcover_team2=team2[team2['Type'].isin(["Right Corner", "Left Cover"])] 
    except:
        def_leftcover_team2=team2[team2['Type'].isin(["Left Cover"])] 



    #try:
        #print(('{}'.format(list(left_raider_team1['Name']))) +' VS ' +('{}'.format(list(def_cover_team2['Name']))))
       #st.text('{}'.format(list(left_raider_team1['Name'])) +' VS ' +('{}'.format(list(def_cover_team2['Name']))))

    #except Exception as e:
     #   print(e)
except:
    pass
        #print(('{}'.format(' [ ]')) +' VS ' +('{}'.format(list(def_cover_team2['Name']))))
        #st.text('{}'.format(list('{}'.format(list(def_cover_team2['Name'])))))

# Header for Left Raider for Team 2

#def_leftcover_team2.set_index('Team')
print(def_leftcover_team2)
left_raider_team1=pd.DataFrame(list(left_raider_team1['Name'].values))
def_leftcover_team2_names=pd.DataFrame(list(def_leftcover_team2['Name'].values))
def_leftcover_team2_names.columns=['Defender']
left_raider_team1.columns=['Raider']
final=pd.concat([left_raider_team1,def_leftcover_team2_names])
final=final.fillna('')
#final.columns=['Raider','Defender']
 
#st.text('{}'.format(list(right_raider_team1['Name'])) +' VS ' +('{}'.format(list(def_cover_team2['Name']))))
#AgGrid(final)
data_container = st.container()
with data_container:
    table, plot = st.columns(2)
    with table:
        st.table(left_raider_team1)
    with plot:
        st.table(def_leftcover_team2_names)

st.subheader('Player Battle for' +'  ' +('{}'.format(team2_choice)))

# Left Raider for team 2
try:
#     team2=team2.reset_index()
    left_raider_team2  = team2[team2['Type']=='Left Raider'].reset_index(drop=True)
    #left_raider_team2

    try:
        def_cover_team1=team1[team1['Type'].isin(["Right Corner", "Left Cover"])] 
    except:
        def_cover_team1=team1[team1['Type'].isin(["Left Cover"])] 


    
    #print(('{}'.format(list(left_raider_team2['Name']))) +' VS ' +('{}'.format(list(def_cover_team1['Name']))))
    #st.text('{}'.format(list(left_raider_team2['Name'])) +' VS ' +('{}'.format(list(def_cover_team1['Name']))))

except Exception as e:
        print(e)
        #print(('{}'.format(' [ ]')) +' VS ' +('{}'.format(list(def_cover_team1['Name']))))
        #st.text('{}'.format(('{}'.format(list(def_cover_team1['Name'])))))

#def_leftcover_team2.set_index('Team')
print(def_leftcover_team2)
left_raider_team2=pd.DataFrame(list(left_raider_team2['Name'].values))
def_leftcover_team1_names=pd.DataFrame(list(def_cover_team1['Name'].values))
def_leftcover_team1_names.columns=['Defender']
left_raider_team2.columns=['Raider']
final=pd.concat([left_raider_team2,def_leftcover_team1_names])
final=final.fillna('')
#final.columns=['Raider','Defender']
 
#st.text('{}'.format(list(right_raider_team1['Name'])) +' VS ' +('{}'.format(list(def_cover_team2['Name']))))
#AgGrid(final)
data_container = st.container()
with data_container:
    table, plot = st.columns(2)
    with table:
        st.table(left_raider_team2)
    with plot:
        st.table(def_leftcover_team1_names)