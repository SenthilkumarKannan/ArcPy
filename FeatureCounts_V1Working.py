import arcpy
import xlwt
import os

# Path to the file geodatabase
file_geodatabase = r"C:\Users\skannan\featurecounts.gdb"

# Create a new Excel workbook
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Feature Counts_Point')

# Header row
sheet.write(0, 0, 'Feature Class')
sheet.write(0, 1, 'Feature Count')

# Function to count features and write to Excel
def count_and_write_feature_count(feature_class, row):
    count = arcpy.GetCount_management(feature_class)[0]
    sheet.write(row, 0, feature_class)
    sheet.write(row, 1, int(count))

# Iterate through feature classes and count features
row_index = 1
for dirpath, dirnames, filenames in arcpy.da.Walk(file_geodatabase, datatype="FeatureClass"):
    for filename in filenames:
        feature_class = os.path.join(dirpath, filename)
        count_and_write_feature_count(feature_class, row_index)
        row_index += 1

# Save Excel workbook
excel_filename = 'feature_counts_Polyline.xls'
workbook.save(excel_filename)

print(f"Feature counts written to '{excel_filename}'")
