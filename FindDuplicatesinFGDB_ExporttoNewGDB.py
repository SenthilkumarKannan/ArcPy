import arcpy
import os

# Function to find duplicates in a feature class based on geometry (converted to WKT)
def find_duplicates_in_fc(fc):
    duplicates = {}
    object_ids = set()
    duplicate_ids = set()

    with arcpy.da.SearchCursor(fc, ['OID@', 'SHAPE@WKT']) as cursor:  # Use SHAPE@WKT for ArcMap
        for row in cursor:
            object_id = row[0]
            geometry_wkt = row[1]  # Directly retrieve WKT representation

            # Check if geometry is already seen (duplicate geometry)
            if geometry_wkt in object_ids:
                duplicate_ids.add(object_id)
            else:
                object_ids.add(geometry_wkt)

    if duplicate_ids:
        duplicates[fc] = duplicate_ids  # Store duplicates

    return duplicates

# Function to export duplicates to another geodatabase
def export_duplicates_to_gdb(gdb_path, target_gdb, duplicates):
    for fc, duplicate_ids in duplicates.iteritems():  # Use .iteritems() for Python 2.7
        fc_path = os.path.join(gdb_path, fc)
        where_clause = "OBJECTID IN (%s)" % (",".join(map(str, duplicate_ids)))

        # Define target feature class path
        target_fc = os.path.join(target_gdb, fc + "_duplicates")

        # Export selected features
        arcpy.Select_analysis(fc_path, target_fc, where_clause)
        print "Exported duplicates from %s to %s" % (fc, target_fc)

# Function to check each feature class in a geodatabase for duplicates
def check_duplicates_in_gdb(gdb_path, target_gdb):
    duplicates = {}

    arcpy.env.workspace = gdb_path
    feature_classes = arcpy.ListFeatureClasses()

    print "Feature classes in the geodatabase:"
    for fc in feature_classes:
        print fc

    for fc in feature_classes:
        duplicate_fc = find_duplicates_in_fc(fc)
        if duplicate_fc:
            duplicates.update(duplicate_fc)

    if duplicates:
        export_duplicates_to_gdb(gdb_path, target_gdb, duplicates)

    return duplicates

# Define paths for geodatabases
gdb_path = r"C:\Senthil\FGDB.gdb"
target_gdb = r"C:\Senthil\Dup_1.gdb"

# Run duplicate check and export process
duplicate_feature_classes = check_duplicates_in_gdb(gdb_path, target_gdb)

# Output results
if duplicate_feature_classes:
    print "\nDuplicate feature classes found (with count of duplicates):"
    for fc, duplicate_ids in duplicate_feature_classes.iteritems():  # Use .iteritems() for Python 2.7
        print "Feature class: %s - Duplicates count: %d" % (fc, len(duplicate_ids))
else:
    print "No duplicates found."

