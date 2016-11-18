import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import os

#change the file for private scoring
test_public = pd.read_csv("test_public.csv")
l_target_cols = ['num_pax_000_014_mins_before_sdt', 'num_pax_015_029_mins_before_sdt', 'num_pax_030_044_mins_before_sdt', 'num_pax_045_059_mins_before_sdt', 
'num_pax_060_074_mins_before_sdt', 'num_pax_075_089_mins_before_sdt', 'num_pax_090_104_mins_before_sdt', 'num_pax_105_119_mins_before_sdt',  'num_pax_120_134_mins_before_sdt', 'num_pax_135_149_mins_before_sdt', 'num_pax_150_164_mins_before_sdt', 'num_pax_165_179_mins_before_sdt',  'num_pax_180_194_mins_before_sdt', 'num_pax_195_209_mins_before_sdt', 'num_pax_210_224_mins_before_sdt', 'num_pax_225_239_mins_before_sdt', 
'num_pax_240plus_mins_before_sdt']

#getting a list of ids to separate the submissions to public and private
list_of_ids = test_public['id'].tolist()

def check_for_negatives_in_pred(df_pred, l_cols_to_range_over):
	'''A negative number of passengers turning up in a 15 minute window is not valid, so we set any negatives predictions to zero'''
	df_pred[df_pred[l_cols_to_range_over] < 0] = 0
	return df_pred

def calculate_score(df_target_cases, df_predictions):
	'''Root-mean-squared error is the chosen error metric. This function calculates and returns the root-mean-squared error'''
	f_rmse = np.sqrt(mean_squared_error(df_target_cases, df_predictions))
	return f_rmse

#reading csv files from the folder
def find_csv_files(path_to_dir, suffix=".csv"):
	filenames = os.listdir(path_to_dir)
	return [ filename for filename in filenames if filename.endswith(suffix)]


files_csv = find_csv_files("results")	

#added a check for mis match of number of ids 
leaderboard=[]
for names in files_csv:
    team_name, sub = names.split("_")
    sub_num = sub.rsplit(".")[0]
    scoring=pd.read_csv("folder_csv/"+names)
    scoring_rn = check_for_negatives_in_pred(scoring, l_target_cols)
    scoring_public = scoring_rn[scoring_rn['id'].isin(list_of_ids)]
    if test_public.shape[0] == scoring_public.shape[0]:
        rmse_score=calculate_score(scoring_public, test_public)
        leaderboard.append({"Team Name":team_name, "Submission Number":sub_num, "Score" : rmse_score})
    else :
        leaderboard.append({"Team Name":team_name, "Submission Number":sub_num})
    
leaderboard_df=pd.DataFrame(leaderboard)
display_leaderboard= leaderboard_df.loc[leaderboard_df.groupby(['Team Name'])['Score'].idxmin()]
display_leaderboard.to_csv("display_leaderboard.csv", header=True, index=False)
