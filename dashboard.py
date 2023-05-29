import pandas as pd
import numpy as np
import math
import yfinance as yf
from datetime import date, timedelta
from pandas_datareader import data as pdr
import warnings
import statsmodels.api as sm
import plotly.express as px
import plotly.figure_factory as ff
import datapane as dp
import altair as alt
from vega_datasets import data
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import chart_studio

from PIL import Image
import urllib
import os

yf.pdr_override()
chart_studio.tools.set_credentials_file(username='asamfellows', api_key='3Oh2VmHwaLb8lpIXDwDd')


column_names = ['Group', 'Date', 'Security', 'Action', 'Quantity', 'Price', 'Total']
# Replace the line directly below with the output from data_restructure.ipynb
# data = [['Low Beta, High Interest Coverage Ratio', '2022-12-28', 'Cash', 'Deposit', 1, 344687.94, 344687.94], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'ABT', 'Buy', 104, 110.65, 11507.6], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'AMPH', 'Buy', 404, 28.51, 11518.04], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'BAX', 'Buy', 224, 51.37, 11506.88], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'BCPC', 'Buy', 94, 123.52, 11610.88], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'CASS', 'Buy', 251, 45.82, 11500.82], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'CHD', 'Buy', 141, 81.84, 11539.44], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'CL', 'Buy', 145, 79.62, 11544.900000000001], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'CLX', 'Buy', 81, 142.58, 11548.980000000001], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'COST', 'Buy', 26, 458.42, 11918.92], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'DG', 'Buy', 47, 248.93, 11699.710000000001], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'DGX', 'Buy', 73, 157.34, 11485.82], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'EA', 'Buy', 94, 122.38, 11503.72], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'FDS', 'Buy', 29, 404.3, 11724.7], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'GIS', 'Buy', 136, 84.57, 11501.519999999999], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'HOLX', 'Buy', 151, 76.33, 11525.83], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'HSTM', 'Buy', 460, 25.02, 11509.199999999999], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'JNJ', 'Buy', 65, 177.81, 11557.65], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'KMB', 'Buy', 84, 137.3, 11533.2], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'LH', 'Buy', 49, 236.01, 11564.49], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'LMT', 'Buy', 24, 487.89, 11709.36], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'LOPE', 'Buy', 108, 107.17, 11574.36], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'LSTR', 'Buy', 70, 165.32, 11572.4], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'MKTX', 'Buy', 41, 284.53, 11665.73], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'MRK', 'Buy', 104, 111.12, 11556.48], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'PFE', 'Buy', 223, 51.55, 11495.65], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'PG', 'Buy', 76, 152.99, 11627.240000000002], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'QDEL', 'Buy', 134, 86.16, 11545.439999999999], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'SFM', 'Buy', 353, 32.64, 11521.92], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'STRA', 'Buy', 125, 80.91, 10113.75], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'TTWO', 'Buy', 101, 101.87, 10288.87], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-28', 'Cash', 'Deposit', 1, 249011.38, 249011.38], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'AM', 'Buy', 766, 10.85, 8311.1], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'BIO', 'Buy', 20, 425.94, 8518.8], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'BPOP', 'Buy', 128, 65.22, 8348.16], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'CFG', 'Buy', 210, 39.53, 8301.300000000001], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'CINF', 'Buy', 80, 104.58, 8366.4], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'CVX', 'Buy', 47, 178.17, 8373.99], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'DOW', 'Buy', 164, 50.68, 8311.52], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'ERIE', 'Buy', 34, 249.09, 8469.06], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'FAF', 'Buy', 158, 52.72, 8329.76], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'FHI', 'Buy', 228, 36.55, 8333.4], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'FHN', 'Buy', 340, 24.48, 8323.2], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'FIZZ', 'Buy', 172, 48.45, 8333.4], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'FNB', 'Buy', 635, 13.09, 8312.15], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'KMI', 'Buy', 457, 18.18, 8308.26], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'MDC', 'Buy', 263, 31.68, 8331.84], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'MET', 'Buy', 114, 72.86, 8306.039999999999], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'MSM', 'Buy', 101, 82.72, 8354.72], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'MTB', 'Buy', 58, 145.49, 8438.42], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'PB', 'Buy', 114, 73.1, 8333.4], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'PFG', 'Buy', 97, 85.55, 8298.35], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'PPBI', 'Buy', 241, 31.73, 7646.93], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'PRU', 'Buy', 83, 100.27, 8322.41], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'RF', 'Buy', 385, 21.6, 8316], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'T', 'Buy', 449, 18.51, 8310.990000000002], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'UBSI', 'Buy', 203, 40.89, 8300.67], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'UMPQ', 'Buy', 465, 17.85, 8300.25], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'UNM', 'Buy', 202, 41.18, 8318.36], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'VOYA', 'Buy', 136, 61.41, 8351.76], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'X', 'Buy', 328, 25.35, 8314.800000000001], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'XOM', 'Buy', 70, 109.2, 7644], ['Net Income Growth', '2022-12-28', 'Cash', 'Deposit', 1, 382447.5, 382447.5], ['Net Income Growth', '2023-01-11', 'AMAT', 'Buy', 118, 108.57, 12811.259999999998], ['Net Income Growth', '2023-01-11', 'AOSL', 'Buy', 429, 29.77, 12771.33], ['Net Income Growth', '2023-01-11', 'ASH', 'Buy', 115, 111.29, 12798.35], ['Net Income Growth', '2023-01-11', 'CPE', 'Buy', 346, 36.9, 12767.4], ['Net Income Growth', '2023-01-11', 'CRTO', 'Buy', 453, 28.22, 12783.66], ['Net Income Growth', '2023-01-11', 'CSGP', 'Buy', 160, 79.8, 12768], ['Net Income Growth', '2023-01-11', 'CTRA', 'Buy', 512, 24.93, 12764.16], ['Net Income Growth', '2023-01-11', 'CVCO', 'Buy', 52, 246.29, 12807.08], ['Net Income Growth', '2023-01-11', 'CWEN', 'Buy', 373, 34.2, 12756.6], ['Net Income Growth', '2023-01-11', 'HCCI', 'Buy', 361, 35.35, 12761.35], ['Net Income Growth', '2023-01-11', 'LAMR', 'Buy', 128, 100.36, 12846.08], ['Net Income Growth', '2023-01-11', 'LHX', 'Buy', 64, 200.5, 12832], ['Net Income Growth', '2023-01-11', 'LRCX', 'Buy', 25, 459.41, 11485.25], ['Net Income Growth', '2023-01-11', 'MATX', 'Buy', 204, 62.72, 12794.88], ['Net Income Growth', '2023-01-11', 'META', 'Buy', 96, 133.03, 12770.880000000001], ['Net Income Growth', '2023-01-11', 'MOH', 'Buy', 43, 296.77, 12761.109999999999], ['Net Income Growth', '2023-01-11', 'MPLX', 'Buy', 378, 33.82, 12783.960000000001], ['Net Income Growth', '2023-01-11', 'NFLX', 'Buy', 40, 323.64, 12945.599999999999], ['Net Income Growth', '2023-01-11', 'NVEE', 'Buy', 95, 134.91, 12816.449999999999], ['Net Income Growth', '2023-01-11', 'PXD', 'Buy', 56, 231.26, 12950.56], ['Net Income Growth', '2023-01-11', 'QDEL', 'Buy', 150, 85, 12750], ['Net Income Growth', '2023-01-11', 'QLYS', 'Buy', 121, 105.83, 12805.43], ['Net Income Growth', '2023-01-11', 'RRC', 'Buy', 517, 24.68, 12759.56], ['Net Income Growth', '2023-01-11', 'SPSC', 'Buy', 100, 127.65, 12765], ['Net Income Growth', '2023-01-11', 'SUN', 'Buy', 288, 44.39, 12784.32], ['Net Income Growth', '2023-01-11', 'UFPI', 'Buy', 147, 84.47, 12417.09], ['Net Income Growth', '2023-01-11', 'VRTV', 'Buy', 106, 121.12, 12838.720000000001], ['Net Income Growth', '2023-01-11', 'WES', 'Buy', 463, 27.55, 12755.65], ['Net Income Growth', '2023-01-11', 'WIRE', 'Buy', 89, 143.68, 12787.52], ['Net Income Growth', '2023-01-11', 'XPEL', 'Buy', 186, 68.85, 12806.099999999999], ['Winsorized Low Beta strategy', '2022-12-28', 'Cash', 'Deposit', 1, 247323.73, 247323.73], ['Winsorized Low Beta strategy', '2023-01-05', 'CAG', 'Buy', 311, 39.77, 12368.470000000001], ['Winsorized Low Beta strategy', '2023-01-05', 'CHD', 'Buy', 151, 82.05, 12389.55], ['Winsorized Low Beta strategy', '2023-01-05', 'CLX', 'Buy', 88, 142.13, 12507.439999999999], ['Winsorized Low Beta strategy', '2023-01-05', 'CONX', 'Buy', 1240, 9.98, 12375.2], ['Winsorized Low Beta strategy', '2023-01-05', 'CPB', 'Buy', 222, 55.86, 12400.92], ['Winsorized Low Beta strategy', '2023-01-05', 'ED', 'Buy', 131, 95.14, 12463.34], ['Winsorized Low Beta strategy', '2023-01-05', 'FLO', 'Buy', 433, 28.56, 12366.48], ['Winsorized Low Beta strategy', '2023-01-05', 'GIS', 'Buy', 147, 84.24, 12383.279999999999], ['Winsorized Low Beta strategy', '2023-01-05', 'HRL', 'Buy', 270, 45.87, 12384.9], ['Winsorized Low Beta strategy', '2023-01-05', 'K', 'Buy', 176, 70.5, 12408], ['Winsorized Low Beta strategy', '2023-01-05', 'KMB', 'Buy', 91, 135.9, 12366.9], ['Winsorized Low Beta strategy', '2023-01-05', 'KR', 'Buy', 277, 44.81, 12412.37], ['Winsorized Low Beta strategy', '2023-01-05', 'PFE', 'Buy', 250, 49.62, 12405], ['Winsorized Low Beta strategy', '2023-01-05', 'PNM', 'Buy', 253, 48.92, 12376.76], ['Winsorized Low Beta strategy', '2023-01-05', 'SEB', 'Buy', 3, 3720, 11160], ['Winsorized Low Beta strategy', '2023-01-05', 'SFM', 'Buy', 414, 30.86, 12776.039999999999], ['Winsorized Low Beta strategy', '2023-01-05', 'SJM', 'Buy', 78, 159.07, 12407.46], ['Winsorized Low Beta strategy', '2023-01-05', 'THS', 'Buy', 251, 49.41, 12401.91], ['Winsorized Low Beta strategy', '2023-01-05', 'TR', 'Buy', 279, 44.41, 12390.39], ['Winsorized Low Beta strategy', '2023-01-05', 'WEC', 'Buy', 134, 92.93, 12452.62]]
data = [['Low Beta, High Interest Coverage Ratio', '2022-12-28', 'Cash', 'Deposit', 1, 344687.94, 344687.94], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'ABT', 'Buy', 104, 110.65, 11507.6], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'AMPH', 'Buy', 404, 28.51, 11518.04], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'BAX', 'Buy', 224, 51.37, 11506.88], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'BCPC', 'Buy', 94, 123.52, 11610.88], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'CASS', 'Buy', 251, 45.82, 11500.82], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'CHD', 'Buy', 141, 81.84, 11539.44], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'CL', 'Buy', 145, 79.62, 11544.900000000001], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'CLX', 'Buy', 81, 142.58, 11548.980000000001], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'COST', 'Buy', 26, 458.42, 11918.92], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'DG', 'Buy', 47, 248.93, 11699.710000000001], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'DGX', 'Buy', 73, 157.34, 11485.82], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'EA', 'Buy', 94, 122.38, 11503.72], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'FDS', 'Buy', 29, 404.3, 11724.7], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'GIS', 'Buy', 136, 84.57, 11501.519999999999], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'HOLX', 'Buy', 151, 76.33, 11525.83], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'HSTM', 'Buy', 460, 25.02, 11509.199999999999], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'JNJ', 'Buy', 65, 177.81, 11557.65], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'KMB', 'Buy', 84, 137.3, 11533.2], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'LH', 'Buy', 49, 236.01, 11564.49], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'LMT', 'Buy', 24, 487.89, 11709.36], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'LOPE', 'Buy', 108, 107.17, 11574.36], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'LSTR', 'Buy', 70, 165.32, 11572.4], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'MKTX', 'Buy', 41, 284.53, 11665.73], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'MRK', 'Buy', 104, 111.12, 11556.48], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'PFE', 'Buy', 223, 51.55, 11495.65], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'PG', 'Buy', 76, 152.99, 11627.240000000002], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'QDEL', 'Buy', 134, 86.16, 11545.439999999999], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'SFM', 'Buy', 353, 32.64, 11521.92], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'STRA', 'Buy', 125, 80.91, 10113.75], ['Low Beta, High Interest Coverage Ratio', '2022-12-29', 'TTWO', 'Buy', 101, 101.87, 10288.87], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-28', 'Cash', 'Deposit', 1, 249011.38, 249011.38], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'AM', 'Buy', 766, 10.85, 8311.1], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'BIO', 'Buy', 20, 425.94, 8518.8], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'BPOP', 'Buy', 128, 65.22, 8348.16], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'CFG', 'Buy', 210, 39.53, 8301.300000000001], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'CINF', 'Buy', 80, 104.58, 8366.4], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'CVX', 'Buy', 47, 178.17, 8373.99], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'DOW', 'Buy', 164, 50.68, 8311.52], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'ERIE', 'Buy', 34, 249.09, 8469.06], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'FAF', 'Buy', 158, 52.72, 8329.76], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'FHI', 'Buy', 228, 36.55, 8333.4], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'FHN', 'Buy', 340, 24.48, 8323.2], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'FIZZ', 'Buy', 172, 48.45, 8333.4], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'FNB', 'Buy', 635, 13.09, 8312.15], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'KMI', 'Buy', 457, 18.18, 8308.26], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'MDC', 'Buy', 263, 31.68, 8331.84], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'MET', 'Buy', 114, 72.86, 8306.039999999999], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'MSM', 'Buy', 101, 82.72, 8354.72], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'MTB', 'Buy', 58, 145.49, 8438.42], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'PB', 'Buy', 114, 73.1, 8333.4], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'PFG', 'Buy', 97, 85.55, 8298.35], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'PPBI', 'Buy', 241, 31.73, 7646.93], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'PRU', 'Buy', 83, 100.27, 8322.41], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'RF', 'Buy', 385, 21.6, 8316], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'T', 'Buy', 449, 18.51, 8310.990000000002], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'UBSI', 'Buy', 203, 40.89, 8300.67], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'UNM', 'Buy', 202, 41.18, 8318.36], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'VOYA', 'Buy', 136, 61.41, 8351.76], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'X', 'Buy', 328, 25.35, 8314.800000000001], ['High Dividend Yield, Low Leverage, Low P/E', '2022-12-29', 'XOM', 'Buy', 70, 109.2, 7644], ['Net Income Growth', '2022-12-28', 'Cash', 'Deposit', 1, 382447.5, 382447.5], ['Net Income Growth', '2023-01-11', 'AMAT', 'Buy', 118, 108.57, 12811.259999999998], ['Net Income Growth', '2023-01-11', 'AOSL', 'Buy', 429, 29.77, 12771.33], ['Net Income Growth', '2023-01-11', 'ASH', 'Buy', 115, 111.29, 12798.35], ['Net Income Growth', '2023-01-11', 'CPE', 'Buy', 346, 36.9, 12767.4], ['Net Income Growth', '2023-01-11', 'CRTO', 'Buy', 453, 28.22, 12783.66], ['Net Income Growth', '2023-01-11', 'CSGP', 'Buy', 160, 79.8, 12768], ['Net Income Growth', '2023-01-11', 'CTRA', 'Buy', 512, 24.93, 12764.16], ['Net Income Growth', '2023-01-11', 'CVCO', 'Buy', 52, 246.29, 12807.08], ['Net Income Growth', '2023-01-11', 'CWEN', 'Buy', 373, 34.2, 12756.6], ['Net Income Growth', '2023-01-11', 'HCCI', 'Buy', 361, 35.35, 12761.35], ['Net Income Growth', '2023-01-11', 'LAMR', 'Buy', 128, 100.36, 12846.08], ['Net Income Growth', '2023-01-11', 'LHX', 'Buy', 64, 200.5, 12832], ['Net Income Growth', '2023-01-11', 'LRCX', 'Buy', 25, 459.41, 11485.25], ['Net Income Growth', '2023-01-11', 'MATX', 'Buy', 204, 62.72, 12794.88], ['Net Income Growth', '2023-01-11', 'META', 'Buy', 96, 133.03, 12770.880000000001], ['Net Income Growth', '2023-01-11', 'MOH', 'Buy', 43, 296.77, 12761.109999999999], ['Net Income Growth', '2023-01-11', 'MPLX', 'Buy', 378, 33.82, 12783.960000000001], ['Net Income Growth', '2023-01-11', 'NFLX', 'Buy', 40, 323.64, 12945.599999999999], ['Net Income Growth', '2023-01-11', 'NVEE', 'Buy', 95, 134.91, 12816.449999999999], ['Net Income Growth', '2023-01-11', 'PXD', 'Buy', 56, 231.26, 12950.56], ['Net Income Growth', '2023-01-11', 'QDEL', 'Buy', 150, 85, 12750], ['Net Income Growth', '2023-01-11', 'QLYS', 'Buy', 121, 105.83, 12805.43], ['Net Income Growth', '2023-01-11', 'RRC', 'Buy', 517, 24.68, 12759.56], ['Net Income Growth', '2023-01-11', 'SPSC', 'Buy', 100, 127.65, 12765], ['Net Income Growth', '2023-01-11', 'SUN', 'Buy', 288, 44.39, 12784.32], ['Net Income Growth', '2023-01-11', 'UFPI', 'Buy', 147, 84.47, 12417.09], ['Net Income Growth', '2023-01-11', 'VRTV', 'Buy', 106, 121.12, 12838.720000000001], ['Net Income Growth', '2023-01-11', 'WES', 'Buy', 463, 27.55, 12755.65], ['Net Income Growth', '2023-01-11', 'WIRE', 'Buy', 89, 143.68, 12787.52], ['Net Income Growth', '2023-01-11', 'XPEL', 'Buy', 186, 68.85, 12806.099999999999], ['Winsorized Low Beta strategy', '2022-12-28', 'Cash', 'Deposit', 1, 247323.73, 247323.73], ['Winsorized Low Beta strategy', '2023-01-05', 'CAG', 'Buy', 311, 39.77, 12368.470000000001], ['Winsorized Low Beta strategy', '2023-01-05', 'CHD', 'Buy', 151, 82.05, 12389.55], ['Winsorized Low Beta strategy', '2023-01-05', 'CLX', 'Buy', 88, 142.13, 12507.439999999999], ['Winsorized Low Beta strategy', '2023-01-05', 'CONX', 'Buy', 1240, 9.98, 12375.2], ['Winsorized Low Beta strategy', '2023-01-05', 'CPB', 'Buy', 222, 55.86, 12400.92], ['Winsorized Low Beta strategy', '2023-01-05', 'ED', 'Buy', 131, 95.14, 12463.34], ['Winsorized Low Beta strategy', '2023-01-05', 'FLO', 'Buy', 433, 28.56, 12366.48], ['Winsorized Low Beta strategy', '2023-01-05', 'GIS', 'Buy', 147, 84.24, 12383.279999999999], ['Winsorized Low Beta strategy', '2023-01-05', 'HRL', 'Buy', 270, 45.87, 12384.9], ['Winsorized Low Beta strategy', '2023-01-05', 'K', 'Buy', 176, 70.5, 12408], ['Winsorized Low Beta strategy', '2023-01-05', 'KMB', 'Buy', 91, 135.9, 12366.9], ['Winsorized Low Beta strategy', '2023-01-05', 'KR', 'Buy', 277, 44.81, 12412.37], ['Winsorized Low Beta strategy', '2023-01-05', 'PFE', 'Buy', 250, 49.62, 12405], ['Winsorized Low Beta strategy', '2023-01-05', 'PNM', 'Buy', 253, 48.92, 12376.76], ['Winsorized Low Beta strategy', '2023-01-05', 'SEB', 'Buy', 3, 3720, 11160], ['Winsorized Low Beta strategy', '2023-01-05', 'SFM', 'Buy', 414, 30.86, 12776.039999999999], ['Winsorized Low Beta strategy', '2023-01-05', 'SJM', 'Buy', 78, 159.07, 12407.46], ['Winsorized Low Beta strategy', '2023-01-05', 'THS', 'Buy', 251, 49.41, 12401.91], ['Winsorized Low Beta strategy', '2023-01-05', 'TR', 'Buy', 279, 44.41, 12390.39], ['Winsorized Low Beta strategy', '2023-01-05', 'WEC', 'Buy', 134, 92.93, 12452.62]]
df = pd.DataFrame(data, columns=column_names)


def prev_weekday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() > 4: # Mon-Fri are 0-4
        adate -= timedelta(days=1)
    return adate


analysis_start_date = '2022-12-29'#the day first stock was bought
analysis_end_date = prev_weekday(date.today()).strftime('%Y-%m-%d') #should be a trading day
analysis_end_date_plusone = (prev_weekday(date.today())+timedelta(days=1)).strftime('%Y-%m-%d') #just add one to the above mentioned date, need not be a working day
rf = 0.01/100*252 #riskfree-- just add current daily percent before the slash
bench_list = ['SP500','DJI','Nasdaq','Russell']
prtfolio = bench_list[3] #switch no. to change benchmark
#input_file_name= "C:/Users/nelso/Downloads/ASAM_21-22_Tracker_2_1.xlsx"
#output_file_name='ASAM_Excel_Out.xlsx'

transactions = df
teams = transactions.Group.unique() #storing names of teams
transactions['Action_Postion'] = [-1 if x == 'Sell' else 1 for x in transactions['Action']] #sorting selling and buying actions
transactions['ToalXAction_Postion'] = transactions.Total * transactions.Action_Postion #Transaction value X Action
transactions['QuantXAction'] = transactions.Quantity * transactions.Action_Postion #Quantity X Action

postions_calc = pd.DataFrame()
for i in teams:
    a = pd.DataFrame(transactions.groupby(['Group','Security']).sum().loc[i]['QuantXAction'])
    a['Group'] = i
    a = a.reset_index()
    a = a[['Group','Security','QuantXAction']]
    a = a[a.Security!='Cash']
    postions_calc= postions_calc.append(a)
transactions_filter_buy= transactions[transactions.Action=='Buy'][['Group','Security','Price']]
postions_calc = postions_calc.merge(transactions_filter_buy,how='right')[['Group','Security','QuantXAction','Price']]
postions_calc= postions_calc.rename(columns= {'Security':'Tickers','QuantXAction':'Shares','Price':'Purchase'})
postions_calc = postions_calc[postions_calc.Shares>0]
postions_calc['Cost'] = postions_calc['Shares']* postions_calc['Purchase']
total_cost = postions_calc.groupby(['Group']).sum()
ASAM_Total_cash= total_cost.Cost.sum()
total_cost = pd.DataFrame(total_cost['Cost'])
total_cost.loc['ASAM'] =total_cost.sum()

tickers_list = postions_calc.Tickers.unique().tolist()
# Fetch the data
daily_data = yf.download(tickers_list , start=analysis_end_date ,period= '1d' ,end= analysis_end_date_plusone )['Close'].dropna(axis=0,how='all')
daily_data_transpose = daily_data.transpose().reset_index().rename(columns={'index':'Tickers'})
postions_calc =postions_calc.merge(daily_data_transpose,left_on='Tickers',right_on='Tickers', how ='left')
postions_calc.columns = ['Group','Tickers','Shares','Purchase','Cost','Price']
postions_calc['Value'] = postions_calc['Shares']*postions_calc['Price']
postions_calc['Gain $'] = postions_calc['Value'] - postions_calc['Cost']
postions_calc['Gain %'] = postions_calc['Gain $']/postions_calc['Cost']

data_main = pdr.get_data_yahoo(tickers_list, start=analysis_start_date, end=analysis_end_date_plusone).dropna(axis=0,how='all') #switch this date for different cohorts
data = data_main['Close'].T
data_adjusted = data_main['Adj Close'].T
data = data.T[data.columns>=transactions[transactions.Action=='Buy'].Date.max()].T
data_adjusted = data_adjusted.T[data_adjusted.columns>=transactions[transactions.Action=='Buy'].Date.max()].T

history = postions_calc[['Group','Tickers']].copy()
history = history.merge(data,how='left',left_on='Tickers',right_index=True)

Total_Value = postions_calc[['Group','Tickers','Shares']].copy()
Total_Value = Total_Value.merge(data,how='left',left_on='Tickers',right_index=True)
Total_Value_sliced = Total_Value.iloc[:,3:]
Total_Value_sliced  = Total_Value_sliced.T*Total_Value.Shares
Total_Value_sliced  = Total_Value_sliced.T
Total_Value.iloc[:,3:] = Total_Value_sliced

adjustment_factor = postions_calc.Purchase/ (Total_Value.iloc[:,3]/Total_Value.iloc[:,2])

Total_Value_adj = postions_calc[['Group','Tickers','Shares']].copy()
Total_Value_adj = Total_Value_adj.merge(data_adjusted,how='left',left_on='Tickers',right_index=True)
Total_Value_sliced_adj = Total_Value_adj.iloc[:,3:]
Total_Value_sliced_adj  = Total_Value_sliced_adj.T*Total_Value.Shares*adjustment_factor
Total_Value_sliced_adj  = Total_Value_sliced_adj.T
Total_Value_adj.iloc[:,3:] = Total_Value_sliced_adj

Daily_returns = Total_Value_adj.copy()
Daily_returns_sliced = Daily_returns.iloc[:,4:].T.reset_index(drop=True).T/Daily_returns.iloc[:,3:-1].T.reset_index(drop=True).T-1
Daily_returns = Daily_returns.drop(Daily_returns.columns[3],axis=1)
Daily_returns.iloc[:,3:] = Daily_returns_sliced*100

Total_Returns = Total_Value_adj.copy()
Total_Returns_sliced  = Total_Returns.iloc[:,4:].T/Total_Returns.iloc[:,3] -1
Total_Returns_sliced  = Total_Returns_sliced.T*100
Total_Returns = Total_Returns.drop(Total_Returns.columns[3],axis=1)
Total_Returns.iloc[:,3:] = Total_Returns_sliced
Total_Returns_sliced= Total_Returns.copy()
Total_Returns_sliced=pd.concat([Total_Returns_sliced.iloc[:,:3] ,Total_Returns_sliced.iloc[:,-1]],axis=1)

postions_calc = postions_calc.merge(Total_Returns_sliced,on=['Group','Tickers','Shares']).iloc[:,:10]
postions_calc.columns= ['Group', 'Tickers', 'Shares', 'Purchase', 'Cost', 'Price', 'Value',
       'Gain $', 'Gain %','Overall_retruns']
postions_calc.Overall_retruns =postions_calc.Overall_retruns/100

weights = postions_calc.copy()
ew_weight = 1/weights.groupby(by=['Group']).Shares.count()
weights= weights.merge(ew_weight,on ='Group')
weights= weights.rename(columns={"Shares_y":'ew_weight'}) #equal weights done
weights= weights.merge(weights.groupby(by=['Group']).Cost.sum(),on ='Group')
weights['value_weight'] = weights['Cost_x']/weights['Cost_y']
weights = weights.rename(columns={'Shares_x':'Shares','Cost_x':'Cost'}).drop('Cost_y',axis=1)

ew_daily_return_matrix = pd.DataFrame() # in pct
vw_daily_return_matrix = pd.DataFrame() # in pct
for i in teams:
    ew_daily_return_matrix[i]=Daily_returns[Daily_returns.Group==i].iloc[:,3:].T.dot(weights[weights.Group==i].ew_weight)
    vw_daily_return_matrix[i]=Daily_returns[Daily_returns.Group==i].iloc[:,3:].T.dot(weights[weights.Group==i].value_weight)
vw_total_return_matrix=(((vw_daily_return_matrix/100)+1).cumprod()-1)*100
ew_total_return_matrix=(((ew_daily_return_matrix/100)+1).cumprod()-1)*100

Dividends = postions_calc[['Group','Tickers','Shares']].copy()
Dividends['Dividend_per_share']=0.0
for i in range(len(Dividends.Tickers)):
    stock = yf.Ticker(Dividends.Tickers[i])
    div = stock.dividends[(stock.dividends.index.tz_localize(None)<= analysis_end_date)&(stock.dividends.index.tz_localize(None)>= transactions[(transactions.Group== Dividends.Group[i])  & (transactions.Security ==Dividends.Tickers[i])].Date.iloc[0])].sum()
    Dividends['Dividend_per_share'][i]=div
    warnings.filterwarnings("ignore")
Dividends['Total Dividend'] = Dividends['Dividend_per_share']*Dividends['Shares']

Cum_Dividends = pd.DataFrame(Dividends.groupby('Group').sum()['Total Dividend'])
Cum_Dividends.loc['ASAM'] =Cum_Dividends.sum()

index_list = ['^GSPC','^DJI','^IXIC','^RUT','^VIX']
index_data_main = pdr.get_data_yahoo(index_list, start=analysis_start_date, end=analysis_end_date_plusone) #switch this date for different cohorts
index_data = index_data_main['Close'].T
index_data_adjusted = index_data_main['Adj Close'].T
index_data_adjusted=index_data_adjusted.T[index_data_adjusted.columns>=transactions[transactions.Action=='Buy'].Date.max()]
index_data_adjusted = index_data_adjusted.pct_change().dropna()
index_data_adjusted= index_data_adjusted.rename(columns={'^GSPC':'SP500','^DJI':'DJI','^IXIC':'Nasdaq','^RUT':'Russell','^VIX':'VIX'})
index_daily_retruns_adjusted = index_data_adjusted *100
index_total_retruns_adjusted = ((index_data_adjusted+1).cumprod() -1)*100 # in decimal
vw_total_return_matrix= index_total_retruns_adjusted.merge(vw_total_return_matrix,left_index= True,right_index=True)


def get_alpha_beta_sharpe(portfolio, benchmark, riskfree=0):
    '''
    Give daily returns of your portfolio and then daily returns of your benchmark. The function will return the annualized alpha and beta
    '''
    X = benchmark.fillna(0)
    Y = portfolio.fillna(0)
    X = sm.add_constant(X)
    model = sm.OLS(Y, X, missing='none')
    results = model.fit()
    alpha = results.params[0] * 250  # in pct annualized
    beta = results.params[1]
    excess_ret = (portfolio.mean() * 250) - riskfree
    std = portfolio.std() * np.sqrt(250)
    sharpe_ratio = (excess_ret) / std
    sharpe_ratio_holding_period = portfolio.mean() / portfolio.std() * np.sqrt(
        (pd.to_datetime(analysis_end_date) - pd.to_datetime(analysis_start_date)).days)

    return round(alpha, 2), round(beta, 2), round(sharpe_ratio, 2), round(sharpe_ratio_holding_period, 2)

alpha_matrix = pd.DataFrame()
for i in teams:
    alpha_matrix[i]= get_alpha_beta_sharpe(riskfree=rf,portfolio =vw_daily_return_matrix[i] ,benchmark=index_daily_retruns_adjusted[prtfolio] )

alpha_matrix['ASAM'] =get_alpha_beta_sharpe(riskfree=rf,portfolio =vw_daily_return_matrix.mean(axis=1) ,benchmark=index_daily_retruns_adjusted[prtfolio] )
alpha_matrix[prtfolio] = get_alpha_beta_sharpe(riskfree=rf,portfolio =index_daily_retruns_adjusted[prtfolio] ,benchmark=index_daily_retruns_adjusted[prtfolio] )

alpha_matrix =  alpha_matrix.T.rename(columns= {0:'alpha',1:'beta',2:'sharpe_ratio',3:'Holding_Period_Sharpe_Ratio'})
stock_regression = Daily_returns.set_index('Tickers').drop(['Group','Shares'],axis=1)
stock_regression = stock_regression.T.merge(index_daily_retruns_adjusted,left_index=True,right_index=True)
stock_regression = stock_regression.T.reset_index().drop_duplicates(subset=['index']).set_index('index')

allstock_alpha_matrix = pd.DataFrame()
for i in stock_regression.index:
    allstock_alpha_matrix[i]= get_alpha_beta_sharpe(riskfree=rf,portfolio =stock_regression.loc[i] ,benchmark=stock_regression.loc[prtfolio] )
allstock_alpha_matrix =  allstock_alpha_matrix.T.rename(columns= {0:'alpha',1:'beta',2:'sharpe_ratio'})

final_rets = (vw_total_return_matrix.dropna().iloc[-1,:])
final_rets= final_rets.append(pd.Series({'ASAM':final_rets.loc[teams].mean()}))
value_matrix=total_cost.merge(pd.DataFrame(final_rets),left_index=True,right_index=True,how='inner')

value_matrix.columns=['Cost','Ret']
value_matrix['Value']= value_matrix['Cost']*(1+(value_matrix['Ret']/100))
value_matrix['Value_ex_dividend'] = value_matrix['Value']- Cum_Dividends['Total Dividend']
value_matrix['Ret_ex_dividend']= np.round(((value_matrix['Value_ex_dividend']/value_matrix['Cost'])-1)*100,2)

Total_Cost = total_cost.reset_index()
Transactions = transactions.copy()
Positions = postions_calc.copy()
vw_total_return_matrix = vw_total_return_matrix.reset_index()
allstock_alpha_matrix = allstock_alpha_matrix.reset_index().rename(columns={'index': 'ticker'})
alpha_matrix = alpha_matrix.reset_index().rename(columns={'index': 'Column1'})
Cum_Dividends = Cum_Dividends.reset_index()
ew_daily_return_matrix = ew_daily_return_matrix.reset_index().rename(columns={'index': 'Column1'})
ew_total_return_matrix = ew_total_return_matrix.reset_index().rename(columns={'index': 'Column1'})
index_daily_retruns_adjusted = index_daily_retruns_adjusted.reset_index()
index_total_retruns_adjusted = index_total_retruns_adjusted.reset_index()
total_cost = total_cost.reset_index()
value_matrix = value_matrix.reset_index().rename(columns={'index': 'Column1'})
vw_daily_return_matrix = vw_daily_return_matrix.reset_index().rename(columns={'index': 'Column1'})
vw_total_return_matrix = vw_total_return_matrix.reset_index()

def round_to_2_decimal_places(num):
    return round(num, 2)

line_chart = vw_total_return_matrix.rename(columns={'Low Beta, High Interest Coverage Ratio':'Low Beta, High Int. Cov.','High Dividend Yield, Low Leverage, Low P/E':'High Div. Yield, Low Lev., Low P/E','Net Income Growth':'Net Income Growth','Winsorized Low Beta strategy':'Winsorized Low Beta'})
line_chart['SP500'] = line_chart['SP500'].map(round_to_2_decimal_places)
line_chart['Russell'] = line_chart['Russell'].map(round_to_2_decimal_places)
line_chart['Low Beta, High Int. Cov.'] = line_chart['Low Beta, High Int. Cov.'].map(round_to_2_decimal_places)
line_chart['High Div. Yield, Low Lev., Low P/E'] = line_chart['High Div. Yield, Low Lev., Low P/E'].map(round_to_2_decimal_places)
line_chart['Net Income Growth'] = line_chart['Net Income Growth'].map(round_to_2_decimal_places)
line_chart['Winsorized Low Beta'] = line_chart['Winsorized Low Beta'].map(round_to_2_decimal_places)


fig = px.line(line_chart, x='Date', y=['SP500','Russell','Low Beta, High Int. Cov.','High Div. Yield, Low Lev., Low P/E','Net Income Growth','Winsorized Low Beta'])
fig.update_layout(title='Portfolio Performance vs. S&P500 and Russell Indices',
                   xaxis_title='Date',
                   yaxis_title='Strategy or Index',
                  title_x=0.5)

fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1,
    xanchor="right",
    x=1,))

fig.update_layout(legend_title_text=None)
fig.update_traces(mode="lines", hovertemplate=None)

fig.update_layout(hovermode="x unified")

fig.update_layout(hoverlabel = dict(
    bgcolor = "black",
    font_color = "white",
    font_size = 11))

fig.update_layout(legend=dict(title_font_family="Times New Roman",
                              font=dict(size= 9.3)))


fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

def format_currency(x):
    return "${:,.2f}".format(x)

def round_to_2_decimal_places(num):
    return round(num, 2)

mapper = pd.DataFrame({
    'Group':['Winsorized Low Beta strategy','Net Income Growth','High Dividend Yield, Low Leverage, Low P/E','Low Beta, High Interest Coverage Ratio','ASAM'],
    'Team':['Group 4','Group 3','Group 2','Group 1','ASAM'],
})

dashboard = Total_Cost.merge(value_matrix[['Column1','Ret','Value','Value_ex_dividend','Ret_ex_dividend']], left_on='Group', right_on='Column1')
Dashboard = dashboard.merge(alpha_matrix[['Column1','sharpe_ratio','alpha','beta']],left_on='Group',right_on='Column1',how='left')
Dashboard = Dashboard[['Group','Cost','alpha','beta','Ret','Value','Value_ex_dividend','Ret_ex_dividend','sharpe_ratio']]
Dashboard2 = Dashboard.merge(mapper, on='Group')
Dashboard2['Cost'] = Dashboard2['Cost'].apply(format_currency)
Dashboard2['Value'] = Dashboard2['Value'].apply(format_currency)
Dashboard2['Ret'] = Dashboard2['Ret'].map(round_to_2_decimal_places)
Dashboard2 = Dashboard2.sort_values(by=['Team'], ascending=False)
Dashboard2

fig2 = plt.figure(figsize=(7,2), dpi=300)
ax = plt.subplot()

ncols = 5
nrows = Dashboard2.shape[0]

ax.set_xlim(0, ncols + 1)
ax.set_ylim(0, nrows + 1)

positions = [0.25, 2, 3.5, 4.55, 5.5]
columns = ['Team', 'Cost', 'Value', 'Ret', 'sharpe_ratio']

# Add table's main text
for i in range(nrows):
    for j, column in enumerate(columns):
        if j == 0:
            ha = 'left'
        else:
            ha = 'center'
        if column == 'Value':
            text_label = f'{Dashboard2[column].iloc[i]}'
            weight = 'bold'
        else:
            text_label = f'{Dashboard2[column].iloc[i]}'
            weight = 'normal'
        ax.annotate(
            xy=(positions[j], i + .5),
            text=text_label,
            ha=ha,
            va='center',
            font="arial",
            fontsize=6,
            color='#2a3f5f',
            weight=weight
        )

# Add column names
column_names = ['Group', 'Cost', 'Value', 'Ret', 'Sharpe']
for index, c in enumerate(column_names):
        if index == 0:
            ha = 'left'
        else:
            ha = 'center'
        ax.annotate(
            xy=(positions[index], nrows + .25),
            text=column_names[index],
            ha=ha,
            va='bottom',
            font="arial",
            fontsize=7,
            color='#2a3f5f',
            weight='bold'
        )

        

# Add Fill to first column
ax.fill_between(
    x=[0,1],
    y1=nrows,
    y2=0,
    color='#2a3f5f',
    alpha=0.3,
    ec='None'
)

# Add dividing lines
ax.plot([ax.get_xlim()[0], ax.get_xlim()[1]], [nrows, nrows], lw=1.5, color='#2a3f5f', marker='', zorder=4)
ax.plot([ax.get_xlim()[0], ax.get_xlim()[1]], [0, 0], lw=1.5, color='#2a3f5f', marker='', zorder=4)
for x in range(1, nrows):
    ax.plot([ax.get_xlim()[0], ax.get_xlim()[1]], [x, x], lw=1.15, color='#2a3f5f', ls=':', zorder=3 , marker='')



ax.set_title(
    'At A Glance as of {}'.format(analysis_end_date),
    loc='Center',
    font="arial",
    fontsize=8,
    weight='bold',
    color='#2a3f5f',
    y=1
)

ax.set_axis_off()

Positions = postions_calc.copy()
Positions['Purchase'] = Positions['Purchase'].apply(format_currency)
Positions['Cost'] = Positions['Cost'].apply(format_currency)
Positions['Price'] = Positions['Price'].apply(format_currency)
Positions['Value'] = Positions['Value'].apply(format_currency)
Positions['Gain $'] = Positions['Gain $'].apply(format_currency)
Positions['Gain %'] = Positions['Gain %'].map(round_to_2_decimal_places)
Positions['Overall_retruns'] = Positions['Overall_retruns'].map(round_to_2_decimal_places)

alpha_table= dp.DataTable(allstock_alpha_matrix[['ticker','alpha','beta','sharpe_ratio']])

app =dp.App(
    dp.Page(title="Total Returns", blocks=[fig]),
    dp.Page(title="Dashboard", blocks=[dp.DataTable(Dashboard2.set_index(Dashboard2.columns[9]).T)]),
    dp.Page(title="Positions", blocks=[Positions]),
    dp.Page(title="Stock Regressions", blocks=[alpha_table])
)

app2 = dp.App(dp.Plot(fig2))

app2.upload(name='At_A_Glance', embed_mode=True,  publish=True)
app.upload(name='ASAM_Dashboard', embed_mode=True,  publish=True)


# ### Band-Aid Solution Until Permanent One is Found
# line_chart2 = line_chart.rename(columns= {'Low Beta, High Int. Cov.':'Group 1','High Div. Yield, Low Lev., Low P/E':'Group 2','Net Income Growth':'Group 3', 'Winsorized Low Beta':'Group 4'})

# figtemp = px.line(line_chart2, x='Date', y=['SP500','Russell','Group 1','Group 2','Group 3','Group 4'])
# figtemp.update_layout(title='Portfolio Performance vs. S&P500 and Russell Indices',
#                    xaxis_title='Date',
#                    yaxis_title='Strategy or Index',
#                   title_x=0.5)

# figtemp.update_layout(legend=dict(
#     orientation="h",
#     y=-.05,
#     x=.2,))

# figtemp.update_layout(legend_title_text=None)
# figtemp.update_traces(mode="lines", hovertemplate=None)

# figtemp.update_layout(hovermode="x unified")

# figtemp.update_layout(hoverlabel = dict(
#     bgcolor = "black",
#     font_color = "white",
#     font_size = 11))

# figtemp.update_layout(legend=dict(title_font_family="Times New Roman",
#                               font=dict(size= 9.3)))


# figtemp.update_layout({
# 'plot_bgcolor': 'rgba(0, 0, 0, 0)',
# 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
# })

# py.plot(figtemp, filename = 'basic-line', auto_open=False)
