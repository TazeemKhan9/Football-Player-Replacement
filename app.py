 Commented out IPython magic to ensure Python compatibility.
 import streamlit as st
 import pandas as pd
 import plotly.express as px
 import plotly.figure_factory as ff 
 url1='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/Goalkeeper/prepocessed_gk_basic.xlsx?raw=true'
 url2='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/Goalkeeper/preprocessed_gk_advance.xlsx?raw=true'
 url3='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/Right%20Back/right_back_basic.xlsx?raw=true'
 url4='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/Right%20Back/right_back_advance.xlsx?raw=true'
 url5='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/Left%20Back/left_back_basic.xlsx?raw=true'
 url6='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/Left%20Back/left_back_advance.xlsx?raw=true'
 url7='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/Centre%20Back/cb_passing_search.xlsx?raw=true'
 url8='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/Centre%20Back/cb_basic_cluster.xlsx?raw=true'
 url9='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/Input%20Data/Input%20Data.xlsx?raw=true'
 url10='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/CM/cm_basic.xlsx?raw=true'
 url11='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/CM/cm_advance.xlsx?raw=true'
 url12='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/CDM/cdm_basic_cluster.xlsx?raw=true'
 url13='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/CDM/cdm_advance_cluster.xlsx?raw=true'
 url14='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/AM/am_basic.xlsx?raw=true'
 url15='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/AM/am_advance.xlsx?raw=true'
 url16='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/LW/lw_basic.xlsx?raw=true'
 url17='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/LW/lw_advance.xlsx?raw=true'
 url18='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/RW/rw_basic.xlsx?raw=true'
 url19='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/RW/rw_advance.xlsx?raw=true'
 url20='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/CF/cf_basic.xlsx?raw=true'
 url21='https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/CF/cf_advance.xlsx?raw=true'
 
 
 
 
 
 
 PAGE_CONFIG = {"page_title":"StColab.io","page_icon":":smiley:","layout":"centered"}
 st.beta_set_page_config(**PAGE_CONFIG)
 
 def load_data(url,nrows):
     data = pd.read_excel(url, nrows=nrows)
 		
 
     lowercase = lambda x: str(x).lower()
     data.rename(lowercase, axis='columns', inplace=True)
     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
 
     return data
 
 def Replacement_cb(cb_search,Player, Age, Value):
 	Basic_Cluster_number=int(cb_search[cb_search['player']==Player]['basic_cluster'])
 	if Basic_Cluster_number==0:
 		search_df= cb_search.query('basic_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==1:
 		search_df= cb_search.query('basic_cluster == 1 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==2:
 		search_df= cb_search.query('basic_cluster == 2 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 
 
 
 def Replacement_cb_passing(cb_passing_search,Player, Age, Value):
 	Advance_Cluster_number=int(cb_passing_search[cb_passing_search['player']==Player]['advance_cluster'])
 	if Advance_Cluster_number==0:
 		search_df= cb_passing_search.query('advance_cluster == 0 or advance_cluster == 1 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==1:
 		search_df= cb_passing_search.query('advance_cluster == 1 or advance_cluster == 0  and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==2:
 		search_df= cb_passing_search.query('advance_cluster == 0 or advance_cluster == 1 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 
 
 
 
 def Replacement_rb(rb_search,Player, Age, Value):
 	Basic_Cluster_number=int(rb_search[rb_search['player']==Player]['basic_cluster'])
 	if Basic_Cluster_number==0:
 		search_df= rb_search.query('basic_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==1:
 		search_df= rb_search.query('basic_cluster == 1 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==2:
 		search_df= rb_search.query('basic_cluster == 2 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 
 def Replacement_rb_passing(rb_passing_search,Player, Age, Value):
 	Advance_Cluster_number=int(rb_passing_search[rb_passing_search['player']==Player]['advance_cluster'])
 	if Advance_Cluster_number==0:
 		search_df= rb_passing_search.query('advance_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==1:
 		search_df= rb_passing_search.query('advance_cluster == 1 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==2:
 		search_df= rb_passing_search.query('advance_cluster == 2 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 def Replacement_lb(lb_search,Player, Age,Value):
 	Basic_Cluster_number=int(lb_search[lb_search['player']==Player]['basic_cluster'])
 	if Basic_Cluster_number==0:
 		search_df= lb_search.query('basic_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==1:
 		search_df= lb_search.query('basic_cluster == 1 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==2:
 		search_df= lb_search.query('basic_cluster == 2 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==3:
 		search_df= lb_search.query('basic_cluster == 3 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 
 def Replacement_lb_passing(lb_passing_search,Player, Age, Value):
 	Advance_Cluster_number=int(lb_passing_search[lb_passing_search['player']==Player]['advance_cluster'])
 	if Advance_Cluster_number==0:
 		search_df= lb_passing_search.query('advance_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==1:
 		search_df= lb_passing_search.query('advance_cluster == 1 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==2:
 		search_df= lb_passing_search.query('advance_cluster == 2 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 def Replacement_cdm(cdm_defending_search,Player, Age, Value):
 	Basic_Cluster_number=int(cdm_defending_search[cdm_defending_search['player']==Player]['basic_cluster'])
 	if Basic_Cluster_number==0:
 		search_df= cdm_defending_search.query('basic_cluster == 0 and age <= Age and value_num <= Value' )
 	elif Basic_Cluster_number==1:
 		search_df= cdm_defending_search.query('basic_cluster == 1 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==2:
 		search_df= cdm_defending_search.query('basic_cluster == 2 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 def Replacement_cdm_passing(cdm_passing_search,Player, Age, Value):
 	Advance_Cluster_number=int(cdm_passing_search[cdm_passing_search['player']==Player]['advance_cluster'])
 	if Advance_Cluster_number==0:
 		search_df= cdm_passing_search.query('advance_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==1:
 		search_df= cdm_passing_search.query('advance_cluster == 1 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==2:
 		search_df= cdm_passing_search.query('advance_cluster == 2 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 
 def Replacement_cm_passing(cm_passing_search,Player, Age, Value):
 	Basic_Cluster_number=int(cm_passing_search[cm_passing_search['player']==Player]['basic_cluster'])
 	if Basic_Cluster_number==0:
 		search_df= cm_passing_search.query('basic_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==1:
 		search_df= cm_passing_search.query('basic_cluster == 3 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==2:
 		search_df= cm_passing_search.query('basic_cluster == 2 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==3:
 		search_df= cm_passing_search.query('basic_cluster == 3 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 def Replacement_cm_attacking(cm_attacking_search,Player, Age, Value):
 	Advance_Cluster_number=int(cm_attacking_search[cm_attacking_search['player']==Player]['advance_cluster'])
 	if Advance_Cluster_number==0:
 		search_df= cm_attacking_search.query('advance_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==1:
 		search_df= cm_attacking_search.query('advance_cluster == 1 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==2:
 		search_df= cm_attacking_search.query('advance_cluster == 2 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 def Replacement_am_attacking(am_attacking_search,Player, Age, Value):
 	Basic_Cluster_number=int(am_attacking_search[am_attacking_search['player']==Player]['basic_cluster'])
 	if Basic_Cluster_number==0:
 		search_df= am_attacking_search.query('basic_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==1:
 		search_df= am_attacking_search.query('basic_cluster == 0 or basic_cluster == 2 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==2:
 		search_df= am_attacking_search.query('basic_cluster == 2 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 def Replacement_am_passing(am_passing_search,Player, Age, Value):
 	Advance_Cluster_number=int(am_passing_search[am_passing_search['player']==Player]['advance_cluster'])
 	if Advance_Cluster_number==0:
 		search_df= am_passing_search.query('advance_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==1:
 		search_df= am_passing_search.query('advance_cluster == 1 or advance_cluster == 0 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 def Replacement_lw_attacking(lw_attacking_search,Player, Age, Value):
 	Basic_Cluster_number=int(lw_attacking_search[lw_attacking_search['player']==Player]['basic_cluster'])
 	if Basic_Cluster_number==0:
 		search_df= lw_attacking_search.query('basic_cluster == 0 or basic_cluster == 2 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==1:
 		search_df= lw_attacking_search.query('basic_cluster == 0 or basic_cluster == 2 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==2:
 		search_df= lw_attacking_search.query('basic_cluster == 0 or basic_cluster == 2 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==3:
 		search_df= lw_attacking_search.query('basic_cluster == 3 or basic_cluster == 0 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 def Replacement_lw_passing(lw_passing_search,Player, Age, Value):
 	Advance_Cluster_number=int(lw_passing_search[lw_passing_search['player']==Player]['advance_cluster'])
 	if Advance_Cluster_number==0:
 		search_df= lw_passing_search.query('advance_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==1:
 		search_df= lw_passing_search.query('advance_cluster == 1 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==2:
 		search_df= lw_passing_search.query('advance_cluster == 1 or advance_cluster == 0 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 def Replacement_rw_attacking(rw_attacking_search,Player, Age, Value):
 	Basic_Cluster_number=int(rw_attacking_search[rw_attacking_search['player']==Player]['basic_cluster'])
 	if Basic_Cluster_number==0:
 		search_df= rw_attacking_search.query('(basic_cluster == 0 or basic_cluster == 2) and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==1:
 		search_df= rw_attacking_search.query('(basic_cluster == 0 or basic_cluster == 2) and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==2:
 		search_df= rw_attacking_search.query('(basic_cluster == 0 or basic_cluster == 2) and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==3:
 		search_df= rw_attacking_search.query('(basic_cluster == 1 or basic_cluster == 0) and age <= @Age and value_num <= @Value' )
 	return search_df
 
 def Replacement_rw_passing(rw_passing_search,Player, Age, Value):
 	Advance_Cluster_number=int(rw_passing_search[rw_passing_search['player']==Player]['advance_cluster'])
 	if Advance_Cluster_number==0:
 		search_df= rw_passing_search.query('(advance_cluster == 0 or advance_cluster == 1) and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==1:
 		search_df= rw_passing_search.query('(advance_cluster == 1 or advance_cluster == 0) and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==2:
 		search_df= rw_passing_search.query('(advance_cluster == 2 or advance_cluster == 0) and age <= @Age and value_num <= @Value' )
 	return search_df
 
 
 def Replacement_cf_attacking(cf_attacking_search,Player, Age,Value):
 	Basic_Cluster_number=int(cf_attacking_search[cf_attacking_search['player']==Player]['basic_cluster'])
 	if Basic_Cluster_number==0:
 		search_df= cf_attacking_search.query('(basic_cluster == 1 or basic_cluster == 2) and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==1:
 		search_df= cf_attacking_search.query('(basic_cluster == 1 or basic_cluster == 2) and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==2:
 		search_df= cf_attacking_search.query('basic_cluster == 2 and age <= @Age and value_num <= @Value' )
 	elif Basic_Cluster_number==3:
 		search_df= cf_attacking_search.query('(basic_cluster == 0 or basic_cluster == 1) and age <= @Age and value_num <= @Value' )
 	return search_df
 
 def Replacement_cf_passing(cf_passing_search,Player, Age, Value):
 	Advance_Cluster_number=int(cf_passing_search[cf_passing_search['player']==Player]['advance_cluster'])
 	if Advance_Cluster_number==0:
 		search_df= cf_passing_search.query('(advance_cluster == 0 or advance_cluster == 2) and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==1:
 		search_df= cf_passing_search.query('(advance_cluster == 0 or advance_cluster == 2) and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==2:
 		search_df= cf_passing_search.query('(advance_cluster == 0 or advance_cluster == 2) and age <= @Age and value_num <= @Value' )
 	return search_df
 
 
 
 	
 
 def gk_replacement_basic(gk_search,Player, Age, Value):
 		cluster_number=int(gk_search[gk_search['player']==Player]['basic_cluster'])
 		if cluster_number==3:
 			search_df= gk_search.query('(basic_cluster == 3 or basic_cluster == 2) and age <= @Age and value_num <= @Value' )
 		elif cluster_number==2:
 			search_df= gk_search.query('(basic_cluster == 3 or basic_cluster == 2) and age <= @Age and value_num <= @Value' )
 		elif cluster_number==0:
 			search_df= gk_search.query('(basic_cluster == 3 or basic_cluster == 2) and age <= @Age and value_num <= @Value')
 		elif cluster_number==1:
 			search_df= gk_search.query('(basic_cluster == 3 or basic_cluster == 2 or basic_cluster == 1) and age < @Age and value_num <= @Value' )
 	 
 		return search_df
 
 def gk_replacement_advance(gk_advance_search,Player, Age, Value):
 	Advance_Cluster_number=int(gk_advance_search[gk_advance_search['player']==Player]['advance_cluster'])
 	if Advance_Cluster_number==0:
 		search_df= gk_advance_search.query('advance_cluster == 0 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==1:
 		search_df= gk_advance_search.query('advance_cluster == 1 and age <= @Age and value_num <= @Value' )
 	elif Advance_Cluster_number==2:
 		search_df= gk_advance_search.query('advance_cluster == 2 and age <= @Age and value_num <= @Value' )
 	return search_df
 
 
 
 
 def main():
 	menu = ["Home","About","Tool"]
 	choice = st.sidebar.selectbox('Menu',menu)
 	if choice == 'Home':
 		st.header("Football Player Replacement")
 		st.write("Beautiful Project")
 		page_bg_img = '''
 		<style>
 		body {
 		background-image: url("https://cdn.discordapp.com/attachments/690454673601331211/765924833548304444/2020-10-14_06.39.55_1__01.jpg");
 		background-size: cover;
 		color:white;
 		text-align:center;
 		
 		}
 		h2 {
 			text-align:center;
 			color:white;
 		}
 		</style>
 		'''
 		st.markdown(page_bg_img, unsafe_allow_html=True)
 			
 	elif choice== 'About':
 		data=load_data(url9,3000)
 		st.header('About the project')
 		st.subheader('Data')
 		st.write('We have collected multiple datasets from fbref.com which covers various facets like goalkeeping actions, defensive actions etc. Only the top 5 European leagues data have been taken for the year 2019-2020. The problem with the original Fbref datasets was that they had generalized positions into GK, DF, MF and FW. To get a deeper analysis we needed more granular data about the positions of data and that is where we used TransferMarkt.com. We scraped the exact positions and the values of all the players from there and added them into our dataset. The pre-processing included standardizing the data into per 90 mins format, and dropping other variables like wins, losses etc. (Feature Selection) which are overall team performance and do not signify the performance of an individual player. Another important criteria we have used is that we are only considering players who have played 10 matches or more. This is done so that we avoid inconsistent data which is possible for players who have played less matches.')
 		og_pos=st.selectbox('Select a dataset',['GK Saving','GK Passing','Defending','Passing','Shooting','None'])
 		if og_pos=='GK Saving':
 			st.dataframe(data=pd.read_excel('https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Original%20Data/BASIC%20GOALKEEPING%20STATS.xls.xlsx?raw=true'),width=3000,height=500)
 		elif og_pos=='GK Passing':
 			st.dataframe(data=pd.read_excel('https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Original%20Data/Advance%20Goalkeeping.xlsx?raw=true'),width=3000,height=500)
 		elif og_pos=='Defending':
 			st.dataframe(data=pd.read_excel('https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Original%20Data/Defending%20Data.xlsx?raw=true'),width=3000,height=500)
 		elif og_pos=='Passing':
 			st.dataframe(data=pd.read_excel('https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Original%20Data/Basic%20Passing.xlsx?raw=true'),width=3000,height=500)
 		elif og_pos=='Shooting':
 			st.dataframe(data=pd.read_excel('https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Original%20Data/Shooting%20Data.xlsx?raw=true'),width=3000,height=500)
 		 
 	     
 		st.subheader('PCA')
 		st.write('Principal Component Analysis ( PCA )is a dimension reductionality algorithm. Principal component analysis is a technique for feature extraction — so it combines our input variables in a specific linear way, then we can drop the least important variables while still retaining the most valuable parts of all of the variables. Even though there are not a lot of variables in our dataset we have used PCA because the new variables it creates are all independent of each other. In football most of the factors are dependent on each other. For example, if a player shoot more, higher is the chance he/she can score a goal. So, we used PCA so that we could retain valuable information while making the variables independent of each other. Another added benefit of PCA was that we were able to visualise the clusters using the first 2 significant principal components in a scatter plot.')
 		
 		st.subheader('K-Means Clustering')
 		st.write('Clustering is one of the unsupervised learning techniques. We can cluster observations into the same subgroups so that observations within a subgroup are quite similar to each other and observations in different subgroups are quite different from each other. In K-Means clustering, the step that we follow are:')
 		st.write('1) Specify K-clusters where K is the number of clusters and initialize random centroids')
 		st.write('2) Iterate until the cluster assignments stop changing. The method assigns each observation to exactly one of the K clusters')
 		st.write('3) For each K cluster, calculate the cluster mean')
 		st.write('4) Proceed through the list of observations and assign an observation to the cluster whose mean is nearest.')
 		st.write('In our tool we have made two types of clusters for each position. For example, In Goalkeeping clustering we took GK saving and GK passing datasets and performed K-means clustering independent of each other. This helps us to perform a deeper analysis on the Goalkeepers ability to prevent goals as well as thier passing style. By using these 2 clusters we can find a more accurate replacement for a goalkeeper. Below you can see the clusters for different positions based on one of thier aspects:')
 		
 		st.subheader("Clusters")
 		pos= st.selectbox("Select a Position",pd.unique(data['pos']))
 		
 		if pos=="GK":
 			reduced=pd.read_excel("https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/PCA/pca_gk_basic.xlsx?raw=true")
 			fig = px.scatter(reduced,x="PC1", y="PC2",color="Cluster",template="ggplot2", title="Goal Keeper Clusters",hover_data=reduced,hover_name='Name',color_continuous_scale='Redor')
 		elif pos=='CB':
 			reduced=pd.read_excel("https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/PCA/pca_cb_basic.xlsx?raw=true")
 			fig = px.scatter(reduced,x="PC1", y="PC2",color="Basic_Cluster",template="ggplot2", title="Centre Back Clusters",hover_data=reduced,hover_name='Name',color_continuous_scale='Redor')
 		elif pos=='RB':
 			reduced=pd.read_excel("https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/PCA/pca_rb_basic.xlsx?raw=true")
 			fig = px.scatter(reduced,x="PC1", y="PC2",color="Basic_Cluster",template="ggplot2", title="Right Back Clusters",hover_data=reduced,hover_name='Name')
 		elif pos=='LB':
 			reduced=pd.read_excel("https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/PCA/pca_lb_basic.xlsx?raw=true")
 			fig = px.scatter(reduced,x="PC1", y="PC2",color="Basic_Cluster",template="ggplot2", title="Left Back Clusters",hover_data=reduced,hover_name='Name',color_continuous_scale='Redor')
 		elif pos=='DM':
 			reduced=pd.read_excel("https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/PCA/pca_cdm_basic.xlsx?raw=true")
 			fig = px.scatter(reduced,x="PC1", y="PC2",color="Basic_Cluster",template="ggplot2", title="Defensive Midfield Clusters",hover_data=reduced,hover_name='Name',color_continuous_scale='Redor')
 		elif pos=='CM':
 			reduced=pd.read_excel("https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/PCA/pca_cm_basic.xlsx?raw=true")
 			fig = px.scatter(reduced,x="PC1", y="PC2",color="Basic_Cluster",template="ggplot2", title="Central Midfielders Clusters",hover_data=reduced,hover_name='Name',color_continuous_scale='Redor')
 		elif pos=='AM':
 			reduced=pd.read_excel("https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/PCA/pca_am_basic.xlsx?raw=true")
 			fig = px.scatter(reduced,x="PC1", y="PC2",color="Basic_Cluster",template="ggplot2", title="Attacking Midfielders Clusters",hover_data=reduced,hover_name='Name',color_continuous_scale='Redor')
 		elif pos=='RW':
 			reduced=pd.read_excel("https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/PCA/pca_rw_basic.xlsx?raw=true")
 			fig = px.scatter(reduced,x="PC1", y="PC2",color="Basic_Cluster",template="ggplot2", title="Right Wingers Clusters",hover_data=reduced,hover_name='Name',color_continuous_scale='Redor')
 		elif pos=='LW':
 			reduced=pd.read_excel("https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/PCA/pca_lw_basic.xlsx?raw=true")
 			fig = px.scatter(reduced,x="PC1", y="PC2",color="Basic_Cluster",template="ggplot2", title="Left Wingers Clusters",hover_data=reduced,hover_name='Name',color_continuous_scale='Redor')
 	    elif pos=='CF':
 			reduced=pd.read_excel("https://github.com/TazeemKhan9/Football-Player-Replacement/blob/main/Data/PCA/pca_cf_basic.xlsx?raw=true")
 			fig = px.scatter(reduced,x="PC1", y="PC2",color="Basic_Cluster",template="ggplot2", title="Centre Forward Clusters",hover_data=reduced,hover_name='Name',color_continuous_scale='Redor')
 		st.plotly_chart(fig)
 
 		st.subheader('Analysis of Clusters')
 		st.write('')
 		pos= st.selectbox("Select a Position",['Goalkeeper','Centre Back','Left Back','Right Back','Defensive Midfielder','Central Midfielder','Attacking Midfielder','Left Winger','Right Winger','Centre Forward'])
 		
 			
 		st.plotly_chart(fig1)
 	
 	elif choice== 'Tool':
 		st.header("Player Replacement Tool")
 
 		data=load_data(url9,3000)
 
 	
 		data.dropna(axis=0,inplace=True)
 		league_list=pd.unique(data['league'])
 		league_select=st.selectbox('Select league',options=league_list)
 		l=str(league_select)
 		mask0=(data['league']==l)
 		data=data[mask0]
  
 	
 	
 	
 		team_list=pd.unique(data['squad'])
 		team_select=st.selectbox('Select team',options=team_list)
 		r=str(team_select)
  
 	
 	
 		pos_list=pd.unique(data['pos'])
 		user_input= st.selectbox('Select Position',options=list(pos_list))
 		f=list(data['value_num'].astype('int32'))
 		f.sort()
 		mask3=(data['squad']==r)
 		
 
 		
 		mask1=(data['pos']==user_input)
 		data=data[mask1]
 		data=data[mask3]
 		player_list=list(data['player'])
 		player_select=st.selectbox('Select Player',options=player_list)
 		x = st.select_slider(label='Player value',options=f)
 		num=int(x)
 		mask2=(data['value_num']<=num)
 		data=data[mask2]
 		mask4=(data['player']==str(player_select))
 		
 		data=data[mask4]
 		
 		val=num
 		Age=st.number_input('Enter age')
 		if user_input=='GK':
 			gk_search=load_data(url1,1000)
 			gk_advance=load_data(url2,1000)
 			search_df=gk_replacement_basic(gk_search,player_select,Age,val)
 			advance_data=load_data(url2,1000)
 			df2=gk_replacement_advance(gk_advance,player_select,Age,val)
 			output_df = pd.merge(search_df,df2, how='inner', on='player')
 			st.subheader("The replacements are:")
 			st.dataframe(data=output_df,width=2000,height=2000)
 			
 		elif user_input=='RB':
 			rb_basic=load_data(url3,1000)
 			rb_advanced=load_data(url4,1000)
 			result_basic=Replacement_rb(rb_basic,player_select,Age,val)
 			result_rb_passing=Replacement_rb_passing(rb_advanced,player_select,Age,val)
 			
 			result_rb_passing.drop(['value','value_num','pos','squad','age'],inplace=True,axis=1)
 			result_basic['basic_cluster']=result_basic['basic_cluster'].replace(to_replace =[0,1,2],value =["Defensive","Mix","Attacking"])
 			result_rb_passing['advance_cluster']=result_rb_passing['advance_cluster'].replace(to_replace =[0,1,2],value =["Conservative Passing","Mix Passing","Attacking Passing"])
 			output_rb = pd.merge(result_basic,result_rb_passing, how='inner', on='player')
 			output_rb=output_rb[['player','nation','pos','value','value_num','squad','age','basic_cluster','advance_cluster']]
 			st.subheader("The replacements are:")
 			st.dataframe(data=output_rb,width=2000,height=2000)
 
 		elif user_input=='LB':
 			lb_basic=load_data(url5,200)
 			lb_advanced=load_data(url6,200)
 			result_basic= Replacement_lb(lb_basic,player_select,Age,val)
 			result_lb_passing=Replacement_lb_passing(lb_advanced,player_select,Age,val)
 			result_lb_passing.drop(['value','value_num','pos','squad','age'],inplace=True,axis=1)
 			result_lb_passing['advance_cluster']=result_lb_passing['advance_cluster'].replace(to_replace =[1,2,0],value =["Ball Playing","Defensive","Mix"])
 			result_basic['basic_cluster']=result_basic['basic_cluster'].replace(to_replace =[2,1,0],value =["Conservative Passing","Mix Passing","Attacking Passing"])
 			output_lb = pd.merge(result_basic,result_lb_passing, how='inner', on='player')
 			output_lb=output_lb[['player','nation','pos','value','value_num','squad','age','basic_cluster','advance_cluster']]
 			st.subheader("The replacements are:")
 			st.dataframe(data=output_lb,width=2000,height=2000)
 
 
 		elif user_input=='CB':
 			cb_basic=load_data(url8,1000)
 			cb_advanced=load_data(url7,1000)
 			result_basic=Replacement_cb(cb_basic,player_select,Age,val)
 			result_cb_passing=Replacement_cb_passing(cb_advanced,player_select,Age,val)
 			result_cb_passing.drop(['value','value_num','pos','squad','age'],inplace=True,axis=1)
 			result_cb_passing['advance_cluster']=result_cb_passing['advance_cluster'].replace(to_replace =[0,1,2],value =["Average Passing",'Best Passing','Worst Passing'])
 			result_basic['basic_cluster']=result_basic['basic_cluster'].replace(to_replace =[1,0,2],value =["Ball Playing","Sweeper","Ball Winning"])
 			output_cb = pd.merge(result_basic,result_cb_passing, how='inner', on='player')
 			output_cb=output_cb[['player','nation','pos','value','value_num','squad','age','basic_cluster','advance_cluster']]
 			st.subheader("The replacements are:")
 			st.dataframe(data=output_cb,width=2000,height=2000)
 		
 
 		elif user_input=='CM':
 			cm_basic=load_data(url10,1000)
 			cm_advanced=load_data(url11,1000)
 			result_cm_passing=Replacement_cm_passing(cm_basic,player_select,Age,val)
 			result_attacking_cm=Replacement_cm_attacking(cm_advanced,player_select,Age,val)
 			result_attacking_cm.drop(['value','value_num','pos','squad','age'],inplace=True,axis=1)
 			result_cm_passing['basic_cluster']=result_cm_passing['basic_cluster'].replace(to_replace =[0,1,2,3],value =["Best Pass Completers","Bad Passers","Best Creative Passes",'Best Long Passers'])
 			result_attacking_cm['advance_cluster']=result_attacking_cm['advance_cluster'].replace(to_replace =[0,1,2],value =["Least Attacking","Average Attacking","Best Attacking"])
 			output_cm = pd.merge(result_cm_passing,result_attacking_cm, how='inner', on='player')
 			output_cm=output_cm[['player','nation','pos','value','value_num','squad','age','basic_cluster','advance_cluster']]
 			st.subheader("The replacements are:")
 			st.dataframe(data=output_cm,width=2000,height=2000)
 		
 		elif user_input=='DM':
 			cdm_basic=load_data(url12,1000)
 			cdm_advanced=load_data(url13,1000)
 			result_cdm_basic=Replacement_cdm(cdm_basic,player_select,Age,val)
 			result_cdm_passing=Replacement_cdm_passing(cdm_advanced,player_select,Age,val)
 			result_cdm_passing.drop(['value','value_num','pos','squad','age'],inplace=True,axis=1)
 			result_cdm_basic['basic_cluster']=result_cdm_basic['basic_cluster'].replace(to_replace =[0,1,2],value =["Passive Defending","Least Defensive","Aggresive Defending"])
 			result_cdm_passing['advance_cluster']=result_cdm_passing['advance_cluster'].replace(to_replace =[0,1,2],value =["Creative Passing ","Mix Passing","Safe Passing"])
 			output_cdm = pd.merge(result_cdm_basic,result_cdm_passing, how='inner', on='player')
 			output_cdm=output_cdm[['player','nation','pos','value','value_num','squad','age','basic_cluster','advance_cluster']]
 			st.subheader("The replacements are:")
 			st.dataframe(data=output_cdm,width=2000,height=2000)
 
 
 		elif user_input=='AM':
 			am_basic=load_data(url14,1000)
 			am_advanced=load_data(url15,1000)
 			result_attacking_am=Replacement_am_attacking(am_basic,player_select,Age,val)
 			result_passing_am=Replacement_am_passing(am_advanced,player_select,Age,val)
 			
 			result_passing_am.drop(['value','value_num','pos','squad','age'],inplace=True,axis=1)
 			result_attacking_am['basic_cluster']=result_attacking_am['basic_cluster'].replace(to_replace =[0,1,2],value =["Best Attackers","Bad Attackers","Good Attackers"])
 			result_passing_am['advance_cluster']=result_passing_am['advance_cluster'].replace(to_replace =[0,1],value =["Good Passers","Average Passers"])
 			output_am = pd.merge(result_passing_am,result_attacking_am, how='inner', on='player')
 			output_am=output_am[['player','nation','pos','value','value_num','squad','age','basic_cluster','advance_cluster']]
 			st.subheader("The replacements are:")
 			st.dataframe(data=output_am,width=5000,height=2000)
 	
 
 		elif user_input=='LW':
 			lw_basic=load_data(url16,1000)
 			lw_advanced=load_data(url17,1000)
 			result_attacking_lw=Replacement_lw_attacking(lw_basic,player_select,Age,val)
 			result_passing_lw=Replacement_lw_passing(lw_advanced,player_select,Age,val)
 			
 			result_passing_lw.drop(['value','value_num','pos','squad','age'],inplace=True,axis=1)
 			result_attacking_lw['basic_cluster']=result_attacking_lw['basic_cluster'].replace(to_replace =[0,1,2,3],value =["Elite Attackers","Below Average Attackers","Good Attackers","Average Attackers"])
 			result_passing_lw['advance_cluster']=result_passing_lw['advance_cluster'].replace(to_replace =[0,1,2],value =["Best Attacking Passes","Best Pass Completers","Average Passers"])
 			output_lw = pd.merge(result_passing_lw,result_attacking_lw, how='inner', on='player')
 			output_lw=output_lw[['player','nation','pos','value','value_num','squad','age','basic_cluster','advance_cluster']]
 			st.subheader("The replacements are:")
 			st.dataframe(data=output_lw,width=2000,height=2000)
 
 
 		elif user_input=='RW':
 			rw_basic=load_data(url18,1000)
 			rw_advanced=load_data(url19,1000)
 			result_passing_rw=Replacement_rw_passing(rw_advanced,player_select,Age,val)
 			result_attacking_rw=Replacement_rw_attacking(rw_basic,player_select,Age,val)
 		
 			
 			result_passing_rw.drop(['value','value_num','pos','squad','age'],inplace=True,axis=1)
 			result_attacking_rw['basic_cluster']=result_attacking_rw['basic_cluster'].replace(to_replace =[2,3,0,1],value =["Elite Attackers","Below Average Attackers","Good Attackers","Average Attackers"])
 			result_passing_rw['advance_cluster']=result_passing_rw['advance_cluster'].replace(to_replace =[0,1,2],value =["Best Overall Passers","Good Attacking Passers","Good Pass Completion"])
 			output_rw = pd.merge(result_passing_rw,result_attacking_rw, how='inner', on='player')
 			output_rw=output_rw[['player','nation','pos','value','value_num','squad','age','basic_cluster','advance_cluster']]
 			st.subheader("The replacements are")
 			st.dataframe(data=output_rw,width=2000,height=2000)
 		
 		elif user_input=='CF':
 			cf_basic=load_data(url20,1000)
 			cf_advanced=load_data(url21,1000)
 			result_attacking_cf=Replacement_cf_attacking(cf_basic,player_select,Age,val)
 			result_passing_cf=Replacement_cf_passing(cf_advanced,player_select,Age,val)
 			result_passing_cf.drop(['value','value_num','pos','squad','age'],inplace=True,axis=1)
 			result_attacking_cf['basic_cluster']=result_attacking_cf['basic_cluster'].replace(to_replace =[2,3,1,0],value =["Elite Attackers","Below Average Attackers","Good Attackers","Average Attackers"])
 			result_passing_cf['advance_cluster']=result_passing_cf['advance_cluster'].replace(to_replace =[2,0,1],value =["Best Overall Passers","Best Pass Completion","Average Passers"])
 			output_cf = pd.merge(result_passing_cf,result_attacking_cf, how='inner', on='player')
 			output_cf=output_cf[['player','nation','pos','value','value_num','squad','age','basic_cluster','advance_cluster']]
 			st.subheader("The replacements are")
 			st.dataframe(data=output_cf,width=2000,height=2000)
 
 
 
 		
 		
 		
 		
 	
 	
 
 
  
 
 
 	
 
 
 		
 
 		
 		
 
 		
 		
 
 	
 
 	
  
 
  
  
  
  
  
                 
 
  
  
 if __name__ == '__main__':
 	main()

