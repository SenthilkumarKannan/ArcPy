import arcgisscripting
#Create the geoprocessor object
gp = arcgisscripting.create(9.3)
# Set Workspace to list feature classes
#gp.workspace = "C:\Temp\TEST\POLYGON_SPLIT.gdb"
#Get Input Workspace as Argument
gp.workspace = gp.GetParameterAsText(0)
# Get List of Feature Classes in Workspace
lstFCs = gp.ListFeatureClasses()

print "\n"
gp.AddMessage("\n")
print "--------------------------------------------------"
#gp.AddMessage("--------------------------------------------------")
for dataset in datasetList:
    #print dataset
    fcList = arcpy.ListFeatureClasses("*","",dataset)
    fcList.sort()
    for fc in fcList:
        print "Processing " + fc
        gp.AddMessage("Processing " + fc)
        recCnt = int(gp.GetCount_management(fc).GetOutput(0))
    if recCnt == 0:
        print "Empty - Deleting " + fc
        gp.AddMessage("Empty - Deleting " + fc)
        gp.Delete_management(fc)
    else:
        print str(recCnt) + " Records - Keeping " + fc
        gp.AddMessage(str(recCnt) + " Records - Keeping " + fc)
print "--------------------------------------------------"
gp.AddMessage("--------------------------------------------------")
print "\n"
gp.AddMessage("\n")
