import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import pandas as pd
import csv

df=pd.read_csv("Data.csv")
data=df["Math_score"].tolist()

fig=ff.create_distplot([data],["Math_score"],show_hist=False)
fig.show()

mean=statistics.mean(data)
SD=statistics.stdev(data)


def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range (0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

sd=statistics.stdev(mean_list)
mean1=statistics.mean(mean_list)

print("Mean of marks : ",mean1,"Standard deviation for marks : ",sd)
fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))
fig.show()

first_sd_start,first_sd_end=mean-sd,mean+sd
second_sd_start,second_sd_end=mean-(2*sd),mean+(2*sd)
third_sd_start,third_sd_end=mean-(3*sd),mean+(3*sd)

print("SD 1 = ",first_sd_start,first_sd_end)
print("SD 2 = ",second_sd_start,second_sd_end)
print("SD 3 = ",third_sd_start,third_sd_end)

fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode="lines",name="MEAN OF 1SD"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="MEAN OF 1SD"))
fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode="lines",name="MEAN OF 2SD"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="MEAN OF 2SD"))
fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.17],mode="lines",name="MEAN OF 3SD"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode="lines",name="MEAN OF 3SD"))
fig.show()
df=pd.read_csv("Data.csv")
data=df["Math_score"].tolist()
mean_of_sample_3=statistics.mean(data)
print("sample 3",mean_of_sample_3)
fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample_3,mean_of_sample_3],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="2SD"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode="lines",name="3SD"))
fig.show()