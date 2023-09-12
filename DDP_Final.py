#Thank the Triune GOD for the wisdom to make this script :)
import os
import arcpy
input_mxd = arcpy.GetParameterAsText(0)
output_folder = arcpy.GetParameterAsText(1)

mxd = arcpy.mapping.MapDocument(input_mxd)
PAGE_LAYOUT = arcpy.mapping.ListDataFrames(mxd)
field_name = arcpy.GetParameterAsText(2)
if len(field_name) == 0:
    field_name = mxd.dataDrivenPages.pageNameField.name
Resolution = arcpy.GetParameterAsText(3)
PrintPages = arcpy.GetParameterAsText(4)
if PrintPages == "All":
    for i in range(1, mxd.dataDrivenPages.pageCount + 1):
        mxd.dataDrivenPages.currentPageID = i
        row = mxd.dataDrivenPages.pageRow
        page_name = row.getValue(field_name)
        out_file = os.path.join(output_folder,  str(page_name) + ".jpg")
	arcpy.AddMessage("Exporting {}. {} remaining ".format((page_name),mxd.dataDrivenPages.pageCount-i))
        arcpy.mapping.ExportToJPEG(mxd, out_file,"PAGE_LAYOUT",resolution = Resolution)
        
else:
    Pages = arcpy.GetParameterAsText(5)
    splitpages = [int(x.strip()) for x in Pages.split(",")]
    for p in splitpages:
        mxd.dataDrivenPages.currentPageID = p
        row = mxd.dataDrivenPages.pageRow
        page_name = row.getValue(field_name)
        out_file = os.path.join(output_folder,  str(page_name) + ".jpg")
	arcpy.AddMessage("Exporting {}, Page {}".format((page_name), p))
        arcpy.mapping.ExportToJPEG(mxd, out_file,"PAGE_LAYOUT",resolution = Resolution)
        






















