import datetime
import arcpy
from datetime import date
import os.path
today = str(date.today())
arcpy.env.overwriteOutput ="True"
arcpy.ClearEnvironment("workspace")
workspace=arcpy.env.workspace


Final_Output =arcpy.GetParameterAsText(0)
AOI=arcpy.GetParameterAsText(1)
Dwg_Output=Final_Output + "\Future_Services_" + today + ".DWG"

mxd=arcpy.mapping.MapDocument(r"C:\Users\skannan\Future_Services.mxd")
df=arcpy.mapping.ListDataFrames(mxd)[0]
lay_list=arcpy.mapping.ListLayers(mxd,"",df)
now=datetime.datetime.now()
if os.path.exists(Dwg_Output):
     os.remove(Dwg_Output)
##try:
for lay in lay_list:
    if lay.isFeatureLayer:
        if AOI:
            Result=arcpy.Clip_analysis(lay,AOI,lay.name + "_Clip")
        else:
            Result=arcpy.FeatureClassToFeatureClass_conversion(lay,workspace,lay.name + "_Exp")
        Output =Result.getOutput(0)
        arcpy.AddMessage(Output)
        if Output:
            arcpy.ExportCAD_conversion(Output,"DWG_R2013",Dwg_Output,"","Append_To_Existing_Files","")
            del Output
        














