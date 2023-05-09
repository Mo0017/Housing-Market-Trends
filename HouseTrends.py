import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Read the data from the csv file
state_data = pd.read_csv("G:\My Drive\VSC\Code\PythonProg\Project\StateData.csv")

# Organize / Clean the data
state_data = state_data.drop(['RegionType', 'StateName', 'RegionID', 'SizeRank'], axis=1)
state_data = state_data.sort_values(by=['RegionName'])
state_data = state_data.drop(state_data.iloc[:, state_data.columns.get_loc('2000-01-31'):state_data.columns.get_loc('2013-01-31')], axis = 1)
state_data = state_data.rename(columns={'RegionName': 'State'})
state_data = state_data.drop(state_data.index[state_data['State'] == 'District of Columbia'])
state_data.reset_index(drop=True, inplace = True)
state_data = state_data.fillna(method='ffill', axis=1)
state_data[state_data.columns[1:]] = state_data[state_data.columns[1:]].astype(int)

print('State Data: ')
print(state_data)   

# We see lots of data, but lets focus on what the user wants to compare 
first_state = input('Enter the first state: ')
# check if the state is in the list

while(first_state not in state_data['State'].tolist()):
    print('State not found, try like this: New Jersey')
    first_state = input('Enter the first state: ')
    

second_state = input('Enter the second state: ')
while(second_state not in state_data['State'].tolist()):
    print('State not found, try like this: New Jersey')
    second_state = input('Enter the second state: ')

compare_data = state_data.drop(state_data.index[state_data['State'] != first_state])
compare_data = pd.concat([compare_data, state_data.drop(state_data.index[state_data['State'] != second_state])])
# Now lets plot both states housing prices using plotly


first_x = compare_data.columns[1:]
first_y = compare_data.iloc[0, 1:]
second_x = compare_data.columns[1:]
second_y = compare_data.iloc[1, 1:]

plt.plot(first_x,first_y)  
plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f"{first_state} Housing Prices vs {second_state} Housing Prices")

fig = go.Figure()
fig.add_trace(go.Scatter(x=first_x, y=first_y, mode='lines', name= first_state))
fig.add_trace(go.Scatter(x=second_x, y=second_y, mode='lines', name= second_state))
fig.update_layout(title='New Jersey Housing Prices', xaxis_title='Date', yaxis_title='Price')
fig.show()

