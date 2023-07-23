
import pandas as pd
import dplython as dp
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

"""
This function was created due to matplotlib library has not the jitter plot as ggplot in R.
For this aim, this function was crated in order to plot in a graphic way the comparision between
two different parameters of the data base
"""
def plot_jitter(x,y,title:str, varx:str, vary:str):
    
    # Jitter size, adjust
    jitter_amount = 0.1

    # creation x-axis and y-axis with normal distribution
    x_jittered = np.array(x) + np.random.normal(loc=0, scale=jitter_amount, size=len(x))
    y_jittered = np.array(y) + np.random.normal(loc=0, scale=jitter_amount, size=len(y))

    # Plot creation with jitter dispersion
    plt.scatter(x_jittered, y_jittered, alpha=0.3, color= "#00665e")
    plt.xlabel(varx)
    plt.ylabel(vary)
    plt.title(title)
    plt.xticks([0, 1])
    plt.yticks([0, 1])
    # Shows the plot generated
    plt.show()

def plot_cross_analysis(x,y,title:str):

    # Calculate probailistic table with cross_analysis() function
    prob_table = cross_analysis(x,y)

    # Creation of subplots
    fig, ax = plt.subplots()

    # Values corresponding to the binary combination of the database  (XY)
    values = ["00", "01", "10","11"]

    # Colors selected for bars and labels
    bar_colors = ['#019EDC','#E13A3E','#FEB827','#61BB46']

    #Plot corresponding bar figure
    ax.bar(values, prob_table.values.flatten(), label=prob_table.values.flatten(), color=bar_colors)
    ax.set_ylabel('Prob (%)')
    ax.set_title(title)
    ax.legend(title='Prob. Distibution in %')
    plt.show()

def plot_extra_analysis(x,y,title:str):
    # Calculate probailistic table with cross_analysis() function
    prob_table = cross_analysis(x,y)

    # Creation of subplots
    fig, ax = plt.subplots()

    # Values corresponding to the binary combination of the database  (XY)
    values = ["01 over 00&01","11 over 10&11"]

    # Colors selected for bars and labels
    bar_colors = ['#019EDC','#FEB827']

    over_prob = list(prob_table.values.flatten())
    over_prob = [(over_prob[1]/(over_prob[0]+over_prob[1])*100).round(2) , (over_prob[3]/(over_prob[3]+over_prob[2])*100).round(2)]

    #Plot corresponding bar figure
    ax.bar(values, over_prob, label=over_prob, color=bar_colors)
    ax.set_ylabel('Prob (%)')
    ax.set_title(title)
    ax.legend(title='Prob. Distibution in %')
    plt.show()


def cross_analysis(x,y):
    cross_table = pd.crosstab(x, y)
    prob_cross_table = (cross_table / cross_table.values.sum() ) * 100
    print(prob_cross_table)
    print(type(prob_cross_table))
    return prob_cross_table.round(2)

"""
* In this section the two database files are read in order to work with them. The first that we will call 
* UCIDataset is the MIMIC-MIT data base v2. The other one (UCIDescription) is the description of all
* the parameters included in the data base.
"""

UCIDataset = pd.read_csv("c:\\Users\\Toni\\Desktop\\Programming\\AA_Portfolio\\UCI_EDA_II\\ICU.csv")
UCIDescription = pd.read_excel("c:\\Users\\Toni\\Desktop\\Programming\\AA_Portfolio\\UCI_EDA_II\\VariableDescriptionsUCI.xlsx")

IDvariables = UCIDescription[UCIDescription['Type'] == "ID"]
UCIDataset = dp.mutate(UCIDataset, IDvariables['VarName'], lambda x: x.astype(str))

Numvariables = UCIDescription[UCIDescription['Type'] == "Num"]
UCIDataset = dp.mutate(UCIDataset, Numvariables['VarName'], lambda x: x.astype(int))

Factorvariables = UCIDescription[UCIDescription['Type'] == "Factor"]
UCIDataset = dp.mutate(UCIDataset, Factorvariables['VarName'], lambda x: x.astype(float))

# All the graphics will be plot with ggplot theme
plt.style.use('ggplot')

# Depression against Paralysis
x = UCIDataset["DEPRESSION"]
y = UCIDataset["PARALYSIS"]
plot_jitter(x,y,"Depression vs Paralysis, Jitter plot","DEPRESSION","PARALYSIS")
plot_cross_analysis(x,y,"Depression vs Paralysis, Cross probability bar plot")
plot_extra_analysis(x,y,"Depression over Paralysis and Depression, bar plot")


# Depression against Neurological
x = UCIDataset["DEPRESSION"]
y = UCIDataset["OTHER_NEUROLOGICAL"]
plot_jitter(x,y,"Depression vs Neurological injuries, Jitter plot","DEPRESSION","OTHER_NEUROLOGICAL")
plot_cross_analysis(x,y,"Depression vs Neurological injuries, Cross probability bar plot")
plot_extra_analysis(x,y,"Depression over Neurological injuries and Depression, bar plot")

# Depression against CHRONIC_PULMONARY
x = UCIDataset["DEPRESSION"]
y = UCIDataset["CHRONIC_PULMONARY"]
plot_jitter(x,y,"Depression vs Chronic Pulmonary Desease, Jitter plot","DEPRESSION","CHRONIC_PULMONARY")
plot_cross_analysis(x,y,"Depression vs Chronic Pulmonary Desease, Cross probability bar plot")
plot_extra_analysis(x,y,"Depression over Chronic Pulmonary Desease and Depression, bar plot")

# Depression against AIDS
x = UCIDataset["DEPRESSION"]
y = UCIDataset["AIDS"]
plot_jitter(x,y,"Depression vs AIDS, Jitter plot","DEPRESSION","AIDS")
plot_cross_analysis(x,y,"Depression vs AIDS, Cross probability bar plot")
plot_extra_analysis(x,y,"Depression over AIDS and Depression, bar plot")

# Depression against LYMPHOMA
x = UCIDataset["DEPRESSION"]
y = UCIDataset["LYMPHOMA"]
plot_jitter(x,y,"Depression vs Lymphoma, Jitter plot","DEPRESSION","LYMPHOMA")
plot_cross_analysis(x,y,"Depression vs Lymphoma, Cross probability bar plot")
plot_extra_analysis(x,y,"Depression over Lymphoma and Depression, bar plot")

# Depression against METASTATIC_CANCER
x = UCIDataset["DEPRESSION"]
y = UCIDataset["METASTATIC_CANCER"]
plot_jitter(x,y,"Depression vs Metastasic Cancer, Jitter plot","DEPRESSION","METASTATIC_CANCER")
plot_cross_analysis(x,y,"Depression vs Metastasic Cancer, Cross probability bar plot")
plot_extra_analysis(x,y,"Depression over Metastasic Cancer and Depression, bar plot")