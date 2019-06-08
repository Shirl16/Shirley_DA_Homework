// from data.js
var tableData = data;
// console.log(tableData);

// YOUR CODE HERE!
var tbody = d3.select('tbody');

// append rows to table and use object entries to 
// log values and append data to html table

function buildTable(data) {

tbody.html("")
    data.forEach((datum) => {
        var tr = tbody.append('tr');
            Object.entries(datum)
                  .forEach(([datumKey, datumValue]) => {
                    tr.append('td').text(datumValue);
                console.log(datumValue);
        });
    console.log('--------------');
    })
};



var input = d3.select('#datetime');
var shape = d3.select('#shape');
var submit = d3.select('#filter-btn');


submit.on('click', function() {
    d3.event.preventDefault();
    
    
    var inputDate = input.property("value");
    var inputShape = shape.property('value');
       
    console.log('date', inputDate);
    console.log('shape', inputShape);

    var filterData = tableData
        if (inputDate){
            filterData = filterData.filter(row => row.datetime === inputDate);
        }
    console.log(filterData);

    if (inputShape){
        filterData = filterData.filter(row => row.shape === inputShape);
    };

    console.log(filterData);
    
    buildTable(filterData);
});

    

buildTable(tableData);
