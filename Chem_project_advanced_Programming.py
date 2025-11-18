# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 15:56:23 2025

@author: Daniel.duggan22
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as py
 
Killy_Aug = r"Killarney August per metre cub.csv"
Killy_Feb = r"Killarney Feb per metre cub.csv"
Raffen = r"Raffen per metre cub.csv"

August_info =  pd.read_csv(Killy_Aug)
Feb_info = pd.read_csv(Killy_Feb)
Raffen_info = pd.read_csv(Raffen)

August_info.columns
Date_Aug = np.array(August_info.Date)
Alternia_Aug = np.array(August_info.Alternaria)
Pen_Asp_Aug = np.array(August_info.Pen_Asp)
Cladiosporium_Aug = np.array(August_info.Cladiosporium)
Epicoccum_Aug = np.array(August_info.Epicoccum)
Basidiospores_Aug = np.array(August_info.Basidiospores)
Ganoderma_Aug = np.array(August_info.Ganoderma)
Smuts_Aug = np.array(August_info.Smuts)
Rusts_Aug = np.array(August_info.Rusts)
Ascospores_Aug = np.array(August_info.Ascospores)
Torula_Aug = np.array(August_info.Torula)
Polythrincium_Aug = np.array(August_info.Polythrincium)
Pithomyces_Aug = np.array(August_info.Pithomyces)
Other_spores_Aug = np.array(August_info.Other_spores)
Total_Aug = np.array(August_info.Total)

Feb_info.columns
Date_Feb = np.array(Feb_info.Date)
Yew_Feb = np.array(Feb_info.Yew)
Hazel_Feb = np.array(Feb_info.Hazel)
Alder_Feb = np.array(Feb_info.Alder)
Total_Feb = np.array(Feb_info.Total)

Raffen_info.columns
Date_Raff = np.array(Raffen_info.Date)
Alternia_Raff = np.array(Raffen_info.Alternaria)
Pen_Asp_Raff = np.array(Raffen_info.Pen_Asp)
Cladiosporium_Raff = np.array(Raffen_info.Cladiosporium)
Epicoccum_Raff = np.array(Raffen_info.Epicoccum)
Coloured_Basidiospores_Raff = np.array(Raffen_info.Coloured_Basidiospores)
Ganoderma_Raff = np.array(Raffen_info.Ganoderma)
Smuts_Raff = np.array(Raffen_info.Smuts)
Rusts_Raff = np.array(Raffen_info.Rusts)
Ascospores_Raff = np.array(Raffen_info.other_ascospores)
Torula_Raff = np.array(Raffen_info.Torula)
Polythrincium_Raff = np.array(Raffen_info.Polythrincium)
Pithomyces_Raff = np.array(Raffen_info.Pithomyces)
other_spores_Raff = np.array(Raffen_info.other_spo)
Total_Raff = np.array(Raffen_info.Total)

user_want = ""
user_dataset = str(input("please enter the desired month(e.g. Feb, JUl, Aug)"))
user_pollen = str(input("please enter the desired pollen type(e.g Alternia, Pen_Asp, Total)"))

if user_dataset == "Feb":
    user_want += "_Feb"
elif user_dataset == "Aug" or "august":
    user_want += "_Aug"
elif user_dataset == "JUL" or "july":
    user_want += "_Raff"
    
if user_pollen == "Alternia":
    user_want = "Alternia" + user_want
elif user_pollen == "Pen_Asp":
    user_want = "Pen_Asp" + user_want
elif user_pollen == "Cladiosporium":
    user_want = "Cladiosporium" + user_want
elif user_pollen == "Epicoccum":
    user_want = "Epicoccum" + user_want
elif user_pollen == "Coloured_Basidiospores":
    user_want = "Coloured_Basidiospores" + user_want
elif user_pollen == "Ganoderma":
    user_want = "Ganoderma" + user_want
elif user_pollen == "Smuts":
    user_want = "Smuts" + user_want
elif user_pollen == "Rusts":
    user_want = "Rusts" + user_want


print(user_want)
