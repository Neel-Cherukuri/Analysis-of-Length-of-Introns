Exon and Intron Analysis in Gene Transcripts

OVERVIEW:
This project provides a Python script to analyze exon and intron lengths in gene transcripts, calculate specific regions around splice junctions, and visualize the distribution of these intervals. The script utilizes pandas for data manipulation, numpy for numerical operations, and matplotlib for generating plots.

Background:
Gene Transcripts, Exons, and Introns
A gene transcript is a sequence of RNA produced by transcription from DNA. It consists of exons and introns.

Exons: These are the coding regions of the gene that remain in the RNA after splicing and contribute to the final mature RNA.
Introns: These are non-coding regions that are transcribed into RNA but are removed during RNA splicing.
Splicing and Splice Junctions
Splicing is a process where introns are removed from the RNA transcript, and exons are joined together. The regions where exons are joined together are known as splice junctions.

Code Functionality:
The script performs the following tasks:
Load the Data: Reads a CSV file containing exon and intron information for gene transcripts.
Basic Analysis: Calculates the total number of unique transcripts, the total number of unique exons, the average length of exons, and the median length of exons.
Intron Length Calculation: Calculates the length of introns based on the start and end positions of exons.
Region Calculation around Splice Junctions: Calculates L1, L2, U1, and U2 regions around splice junctions, adjusting for short exons and introns to ensure non-overlapping regions.
Data Visualization: Generates histograms to visualize the distribution of intervals at the 5’ (L1 to L2) and 3’ (U1 to U2) ends of the exons.

Code Structure:
Data Loading and Preprocessing: Importing libraries, loading the data, and initial data setup.
Basic Transcript and Exon Analysis: Calculating basic statistics about the transcripts and exons.
Intron Length Calculation: Determining the lengths of the introns.
Splice Junction Region Calculation: Calculating the regions around splice junctions.
Data Visualization: Plotting the distribution of intervals at splice junctions.

Results
The script outputs:
Console Output: .
Plots: Two histogram plots visualizing the distribution of intervals at the 5’ and 3’ ends of the exons. These plots are saved as PNG files in the project directory. Histograms have been created to visualize the distribution of intervals at the 5’ (L1 to L2) and 3’ (U1 to U2) ends of the exons. The highest peak in both distributions is observed at 200, indicating a common interval length


Conclusion:
This script provides a comprehensive analysis of exon and intron lengths in gene transcripts, offering insights into their distribution and the regions around splice junctions. It leverages the power of pandas for data manipulation, numpy for numerical calculations, and matplotlib for visualization, making it a robust tool for genomic data analysis.
