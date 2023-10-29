# Load required libraries
library(dplyr)
library(readr)
library(data.table)
library(ggplot2)

# Load the RDS file
data <- readRDS("exgr_test.rds")

# Show basic information about the data frame and the first few rows
str(data)
head(data)

# Convert data frame to data table
setDT(data)

# Total number of unique transcripts
total_unique_transcripts <- n_distinct(data$transcript_id)

# Total number of unique exons
total_unique_exons <- n_distinct(data$exon_id)

# Print the results
cat("Total number of unique transcripts:", total_unique_transcripts, "\n")
cat("Total number of unique exons:", total_unique_exons, "\n")


# Calculate the average length of exons
average_exon_length <- mean(data$width, na.rm = TRUE)

# Print the results
cat("Average length of exons:", average_exon_length, "\n")

# Calculate the median length of exons
median_exon_length <- median(data$width, na.rm = TRUE)

# Print the result
cat("Median length of exons:", median_exon_length, "\n")

# Initialize intron_length with zeros
data[, intron_length := 0]

# Calculate intron lengths
data[, intron_length := c(0, start[-1] - end[-.N]), by = transcript_id]

# Ensure all intron lengths are non-negative
data[intron_length < 0, intron_length := 0]

# View some rows to verify the result
head(data)

#Bonus task

# Calculate L1, L2, U1, U2
data[, `:=`(
  L1 = pmax(start - 100, 1),
  L2 = pmin(start + 100, end),
  U1 = pmax(end - 100, start),
  U2 = end + 100
), by = transcript_id]

# Adjust L and U regions if they overlap or if exon/intron is too short
data[, `:=`(
  L2 = ifelse(L2 - L1 < 200, start + (end - start)/2, L2),
  U1 = ifelse(U2 - U1 < 200, end - (end - start)/2, U1)
), by = transcript_id]

# Ensure L2 and U1 do not overlap
data[, `:=`(
  L2 = pmin(L2, U1 - 1),
  U1 = pmax(U1, L2 + 1)
), by = transcript_id]

# View some rows to verify the result
head(data)


# Prepare data for plotting
L_intervals <- data[, .(Interval = L2 - L1)]
U_intervals <- data[, .(Interval = U2 - U1)]

# Plot L intervals
p1 <- ggplot(L_intervals, aes(x = Interval)) +
  geom_histogram(binwidth = 1, fill = "skyblue", color = "black") +
  labs(title = "Distribution of Intervals at 5’ End (L1 to L2)",
       x = "Interval Length",
       y = "Frequency") +
  theme_minimal()

# Plot U intervals
p2 <- ggplot(U_intervals, aes(x = Interval)) +
  geom_histogram(binwidth = 1, fill = "lightgreen", color = "black") +
  labs(title = "Distribution of Intervals at 3’ End (U1 to U2)",
       x = "Interval Length",
       y = "Frequency") +
  theme_minimal()

#save the plots
ggsave("L_intervals_plot.png", p1)
ggsave("U_intervals_plot.png", p2)

# Show the plots
print(p1)
print(p2)

