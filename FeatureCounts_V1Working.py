import arcpy
import pythonaddins
import xlwt
arcpy.env.workspace= r'Z:\IMP NK\AERIAL SURVEY 2019 COMPILATION\Bahra Photogrammetry Data\Bahra.gdb'
excelPath = "Z:\IMP NK\AERIAL SURVEY 2019 COMPILATION\Bahra Photogrammetry Data\Featureclasscounts.xls"
datasetList = arcpy.ListDatasets("*", "Feature")
#For Excel sheet
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
listFCName = []
listFCount = []

for dataset in datasetList:
        #print dataset
        fcList = arcpy.ListFeatureClasses("*","",dataset)
        fcList.sort()
        for fc in fcList:
            count=arcpy.GetCount_management(fc)
            #print fc+":"+str(count)
            listFCName.append(str(fc))
            listFCount.append(str(count))

print "Writing to Sheet...."

sheet1.write(0,0, "Feature Class Name") #Row=0, Column=1
sheet1.write(0,1, "Feature Count") #Row=0, Column=1

totRows = len(listFCName)
startRow = 0

for fNm in listFCName:
        #print("{0} = {1}".format(listFCName[startRow], listFCount[startRow]) )
        if startRow < totRows:
                sheet1.write((startRow+1),0, listFCName[startRow])
                sheet1.write((startRow+1),1, listFCount[startRow])
        startRow = startRow+1
book.save(excelPath)
print "Printed all the feature classes..."

