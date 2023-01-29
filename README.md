# PDF Generator
This code generates a PDF document based on the data from a CSV file "topics.csv".

# Requirements
- fpdf
- pandas

# How it works
The code reads the "topics.csv" file using pandas and iterates through each row of the data. For each row, a new page is added to the PDF document and the header is set with the value of the "Topic" column. The header is a 24-point font size and bold style "Times" font in a dark gray color. A line is drawn under the header and several horizontal lines are drawn across the page.

For each page, the footer is set with the same "Topic" value and a 8-point font size and italic style "Times" font in a dark gray color. The footer is located at the bottom of the page.

For each row with more than one page, the succeeding pages are generated with a line grid pattern and the same footer.

The final output is saved as "output.pdf".
