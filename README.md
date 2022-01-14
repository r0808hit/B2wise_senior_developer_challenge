# B2wise_senior_developer_challenge

#Approach for Challenge 1
Backtracking Approach is used for solving this challenge

First the sudoko csv file is imported as data frame and the blank spaces are then converted to zeroes
Then the dtype is converted to Int and then the dataframe is converted to a numpy array.
Two methods are then used to solve the sudoko 9X9 grid.
First method is used to traverse through the sudoko's different value. 
If the values equal to 0 are then the sudoko_solver function is called and backtracking method is used to assign values to solve the sudoko.

#Run Challenge 1-solution.py
To run this file-
  1) Open cmd and run command : python "Challenge 1-solution.py"
  2) Open Jupyter and paste the code there and the csv file in the directory. And run the cell.


#Approach for Challenge 2
Both the CSV files(Sales and master)  are imported using pandas
The PartId which are Active are only selected and based on that data from sales csv file is selected
Then in sales csv file based on different PartId for loop is used and then using the ARIMA timeseries model a ML model is created and based on that forecasting is done
for next 52 weeks.

Based on that forecast data of all the PartId that are Active a graph is plotted and its png image is saved.
After that initial stock value is taken 1000 for each of the Id and the weekly stock on hand value is calculated from that.
Based on the stock on hand value the output column is defined.. If the stock on hand value is positive then the output is 1 else if the stock on hand value is less than 0
then output woulde be 0.

#Run Challenge 2-solution.py
To run this file-
  1) Open Jupyter and paste this code in a cell and run that cell. Make sure the csv files are also in the same directory.
  


