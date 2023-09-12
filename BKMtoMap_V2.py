import arcpy
workspace = arcpy.GetParameterAsText(0)
arcpy.env.workspace = workspace
arcpy.env.scratchworkspace = workspace
arcpy.env.overwriteOutput = True
mxdPath = arcpy.GetParameterAsText(1) # arcpy.mapping.MapDocument("CURRENT")
prefix = u"{}".format(arcpy.GetParameterAsText(2))
postfix = u"{}".format(arcpy.GetParameterAsText(3))
desiredresolution = arcpy.GetParameter(4)
mxd = arcpy.mapping.MapDocument(mxdPath)
df = arcpy.mapping.ListDataFrames(mxd)[0]
bookmarkList = arcpy.mapping.ListBookmarks(mxd, data_frame=df)
arcpy.AddMessage("""{0} bookmarks found. Exporting JPEGs...""".format(len(bookmarkList)))
mxd.activeView = "PAGE_LAYOUT"
i = 1
for bookmark in bookmarkList:
    df.extent = bookmark.extent
    outName = u"{0}".format(bookmark.name)
    outFile = u"{0}\{1}{2}{3}".format(workspace, prefix, outName, postfix)
    arcpy.mapping.ExportToJPEG(mxd, outFile, df, df_export_width=1600, df_export_height=1200, resolution = desiredresolution, world_file=True)
    ###arcpy.mapping.ExportToPDF(mxd, outFile, "PAGE_LAYOUT", resolution = desiredresolution)
    arcpy.AddMessage("""Bookmark Nr. {0} exported...""".format(i))
    i += 1
