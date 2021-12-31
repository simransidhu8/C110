import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("average.csv")
data = df["average"].tolist()
population_mean = statistics.mean(data)
print("The population mean is ", population_mean)

population_std = statistics.stdev(data)
print("The standard deviation of population is ", population_std)

def random_set_of_means(counter):
    df = pd.read_csv("average.csv")
    data = df["average"].tolist()
    dataset = [] 
    for i in range(0, counter):
        random_index = random.randint(0,len(data) -1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("The mean of the sampling data is ", mean)
    fig = ff.create_distplot([df], ["average"], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean, mean], y =[0,1], mode = "lines", name = "mean"))
    fig.show()

def setup():
    mean_list = []
    for x in range(0, 1000):
        set_of_means = random_set_of_means(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()

def std_dev():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_means(100)
        mean_list.append(set_of_means)
    std = statistics.stdev(mean_list) 
    print("The standard deviation of sampling data is ", std)
std_dev()