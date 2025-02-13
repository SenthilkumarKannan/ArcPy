import datetime
import arcpy
from datetime import date
import os.path
today = str(date.today())
arcpy.env.overwriteOutput ="True"
arcpy.ClearEnvironment("workspace")
workspace=arcpy.env.workspace
tPath=arcpy.env.scratchGDB
seed=r"C:\Users\skannan\Future_Service_Seed_File.dwt"
Final_Output =arcpy.GetParameterAsText(0)
AOI=arcpy.GetParameterAsText(1)
Dwg_Output=Final_Output + "\Future_Services_" + today + ".DWG"

mxd=arcpy.mapping.MapDocument(r"C:\Users\skannan\Future_Services.mxd")
df=arcpy.mapping.ListDataFrames(mxd)[0]
lay_list=arcpy.mapping.ListLayers(mxd,"",df)
now=datetime.datetime.now()
if os.path.exists(Dwg_Output):
     os.remove(Dwg_Output)

for lay in lay_list:
    if lay.isFeatureLayer:
        if AOI:
            Result=arcpy.Clip_analysis(lay,AOI,lay.name + "_Exp")
        else:
            Result=arcpy.FeatureClassToFeatureClass_conversion(lay,workspace,lay.name + "_Exp")
        if Result:
            Output =Result.getOutput(0)
            arcpy.AddMessage(Output)
            if Output:
                arcpy.ExportCAD_conversion(Output,"DWG_R2013",Dwg_Output,"","Append_To_Existing_Files",seed)
                del Output

del mxd



           



























