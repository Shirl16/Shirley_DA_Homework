Sub Volume_Totals_by_Ticker():

'loop through all the sheets
For Each ws In Worksheets

'------------------------------------------------------------
'INSERT THE STATE
'------------------------------------------------------------

'create a variable for each worksheet
Dim WorkSheetName As String

'set an initial variable for ticker
Dim Ticker As String

'set initial variable for holding the ticker volume total
Dim Total_Stock_Volume As Double
Total_Stock_Volume = 0

'set table headers
ws.Range("I1").Value = "Ticker"
ws.Range("J1").Value = "Total Stock Volume"

'keep track of the location for each ticker volume total in the summary table
Dim Summary_Table_Row As Double
Summary_Table_Row = 2

'determine last row
lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row

'loop through all the ticker symbols
For i = 2 To lastrow

    'check to see if ticker symbol is the same, if it is not
    If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
    
    'set ticker name
    Ticker = ws.Cells(i, 1).Value
    
    'add ticker volume
    Total_Stock_Volume = Total_Stock_Volume + ws.Cells(i, 7).Value
    
    'print ticker symbol in summary table
    ws.Range("I" & Summary_Table_Row).Value = Ticker
    
    'print total volume in summary table
    ws.Range("J" & Summary_Table_Row).Value = Total_Stock_Volume
    
    'add one to the summary table row
    Summary_Table_Row = Summary_Table_Row + 1
    
    'reset volume total
    Total_Stock_Volume = 0
    
    
    'if the cell immediately following a row is the same ticker symbol
    Else
    
        'add to the volume total
        Total_Stock_Volume = Total_Stock_Volume + ws.Cells(i, 7).Value
        
    End If
    
Next i

Next ws


End Sub
