# ASAM
Work for my UCLA Anderson Capstone

## requirements
This file is all of the python packages needed for the code to work

## Final_Code_FF_FM
This file is the bulk of the project
1. Grab and clean stock data from CRSP and COMPUSTAT
2. Calculate 10-year CAGRs and other metrics need for the strategy
3. Run Fama-French and Fama-Macbeth regressions on the data to backtest the investment strategy for a different number of stocks

## Stock_Selection_Code
This file uses quarterly data for the last year to get the most up to date financial information and selects the stock I will invest in

## data_restructure
This files takes in an excel template of stocks invested and converts it to a line of code to be added in the next file

## dashboard
Creates a dashboard of all stocks invested in and embeds it to the ASAM website (In production repo, this is done automatically each day using an automation.yml and GitHub actions)
### Final Product:
https://cloud.datapane.com/reports/Y3Yl8MA/asam-dashboard/?utm_medium=embed
https://cloud.datapane.com/reports/MA1BKY3/at-a-glance/?utm_medium=embed
