import pandas as pd
import plotly
import plotly.express as px


def plot_x_given_x(col_name2="f1-macro",col_color='NN_type'):
  global df_all
  fig = px.box(df_all, y=col_name2, color=col_color,  points="all",
                  title=col_name2 + " x " + col_color)
  fig.show()


path_file = 'finally_0.csv'
df_all = pd.read_csv(path_file)


df_all['prob_text_right'] = df_all['prob_text_right'].apply(abs)

metrics = ['accuracy', 'f1-macro', 'f1-micro']

types_of_NN = ['ATT_NN', 'NN_img', 'NN_txt', 'BY_2', 'Monkey']

basic_val = ['fusion_type','class_sep_img','class_sep_text','prob_img_right','prob_text_right','prob_wrong','num_cases']

dict_df ={
'fusion_type' : [],	
'class_sep_img'	: [],
'class_sep_text' : [],
'prob_img_right' : [],
'prob_text_right' : [],
'prob_wrong' : [],
'num_cases' : [],
'accuracy' : [],
'f1-macro' : [],
'f1-micro' : [],
'NN_type' : [],
}

for _, row in df_all.iterrows():
  for cur_type in types_of_NN:
    dict_df['NN_type'].append(cur_type)
    for cur_metric in metrics:
      dict_df[cur_metric].append(row[cur_metric + "_" + cur_type]) 
    for cur_val in basic_val:
      dict_df[cur_val].append(row[cur_val])
    



df_all = pd.DataFrame(dict_df)



plot_x_given_x()
