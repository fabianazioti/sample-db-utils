#
# Script responsible for export inSitu samples to CSV files
# It will generate .csv files into provided directory (Directory must exists before)
#
# Usage: R -f export-inSitu-samples-csv.R --args OUTPUT_DIRECTORY
# Example: R -f export-inSitu-samples-csv.R --args /tmp/
#

args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)==0) {
  stop("Please inform the output folder to generate CSV sample files", call.=FALSE)
}

outputFolder = args[1]

library("inSitu")
list_datasets()
data("br_mt_1_8K_9classes_6bands.rda")
# data("amazonia_33K_12classes_4bands.rda")
# data("br_mt_2K_9classes_6bands.rda")
# data("cerrado_124K_16classes_6bands.rda")
# data("cerrado_64K_13classes_6bands.rda")
# data("prodes_samples_interpolated.rda")
# data("prodes_samples_starfm.rda")

write.csv(dplyr::select(br_mt_1_8K_9classes_6bands, -time_series), file = file.path(outputFolder, "br_mt_1_8K_9classes_6bands.csv"), row.names = FALSE)
# write.csv(dplyr::select(br_mt_2K_9classes_6bands, -time_series), file = file.path(outputFolder, "br_mt_2K_9classes_6bands.csv"), row.names = FALSE)
# write.csv(dplyr::select(cerrado_124K_16classes_6bands, -time_series), file = file.path(outputFolder, "cerrado_124K_16classes_6bands.csv"), row.names = FALSE)
# write.csv(dplyr::select(cerrado_64K_13classes_6bands, -time_series), file = file.path(outputFolder, "cerrado_64K_13classes_6bands.csv"), row.names = FALSE)
# write.csv(dplyr::select(prodes_samples_interpolated, -time_series), file = file.path(outputFolder, "prodes_samples_interpolated.csv"), row.names = FALSE)
# write.csv(dplyr::select(prodes_samples_starfm, -time_series), file = file.path(outputFolder, "prodes_samples_starfm.csv"), row.names = FALSE)
# write.csv(dplyr::select(amazonia_33K_12classes_4bands, -time_series), file = file.path(outputFolder, "amazonia_33K_12classes_4bands.rda.csv"), row.names = FALSE)
