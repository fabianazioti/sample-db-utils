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
#data(" br_mt_1_8K_9classes_6bands.rda")
data("br_mt_2K_9classes_6bands.rda")

#write.csv(dplyr::select(br_mt_1_8K_9classes_6bands, -time_series), file = file.path(outputFolder, "br_mt_1_8K_9classes_6bands.csv"), row.names = FALSE)
write.csv(dplyr::select(br_mt_2K_9classes_6bands, -time_series), file = file.path(outputFolder, "br_mt_2K_9classes_6bands.csv"), row.names = FALSE)
