import arcpy
import os
import shutil

#ścieżki do folderu

folder_SHP = r"C:\Users\Tytus\Desktop\ppa_programowanie_arca\zajecia1wsze\2862_SHP_2020"
folder_new_SHP = r"C:\Users\Tytus\Desktop\ppa_programowanie_arca\zajecia1wsze\new_2862_SHP_2020"
arcpy.env.workspace = r"C:\Users\Tytus\Documents\ArcGIS\Projects\zajecia_pierwsze_arc_programowanie\zajecia_pierwsze_arc_programowanie.gdb"

for file in os.listdir(folder_SHP):
    #print(file)
    name, ext = os.path.splitext(file)
    print(name, ext)
    new_name = name.replace(".", "_") + ext
    #print(new_name)
    shutil.copy(f"{folder_SHP}\\{file}", f"{folder_new_SHP}\\{new_name}")

for file in os.listdir(folder_new_SHP):
    name, ext = os.path.splitext(file)
    if ext == ".shp":
        new_name = name.split("__")[1]
        print(file)
        print(new_name)



        arcpy.conversion.ExportFeatures(
            in_features=f"{folder_new_SHP}\\{file}",
            out_features="OLS2020" + new_name
        )


print("Koniec")