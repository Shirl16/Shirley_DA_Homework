var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 100
};


var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import Data
d3.csv("./assets/data/data.csv") 
  .then(function (ageVsmokeData) {
  console.log(ageVsmokeData);

    // Parse Data/Cast as numbers
    // ==============================
ageVsmokeData.forEach(function (data) {
  data.age = +data.age;
  data.smokes = +data.smokes;
           
});

  // Create scale functions
  // ==============================
  var ageLinearScale = d3.scaleLinear()
    // d3.scaleBand()
      .domain([28, d3.max(ageVsmokeData, d => d.age)])
      
      .range([0, width]);

  var smokesLinearScale = d3.scaleLinear()
      .domain([0, d3.max(ageVsmokeData, d => d.smokes)])
      .range([height, 0]);

    // Create axis functions
    // ==============================
  var bottomAxis = d3.axisBottom(ageLinearScale);
  var leftAxis = d3.axisLeft(smokesLinearScale);

    // Append Axes to the chart
    // ==============================
  chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

  chartGroup.append("g")
      .call(leftAxis);

  // Create Circles
  // ==============================
  var circlesGroup = chartGroup.selectAll("circle")
      .data(ageVsmokeData)
      .enter()
      .append("circle")
      .attr("cx", d => ageLinearScale(d.age))
      .attr("cy", d => smokesLinearScale(d.smokes))
      .attr("r", "20")
      .attr("fill", "blue")
      .attr('stroke-width', '1')
      .attr('stroke', 'darkblue')
      .attr("opacity", ".25")
      .classed('circle-data', true)
      ;

  var stateAbbrGroup = chartGroup.selectAll('text.circle-text')
      .data(ageVsmokeData)
      .enter()
      .append('text')
      .classed('circle-text', true)
      .attr('x', d => ageLinearScale(d.age) - 10)
      .attr('y', d => smokesLinearScale(d.smokes) + 8)
      .text(function(d){return d.abbr});

  // Initialize tool tip
  // ==============================
  var toolTip = d3
      .tip()
      .attr("class", "tooltip")
      .offset([80, -60])
      .html(function (d) {
        return (`Age: ${d.age}<br>Smokes: ${d.smokes}`);
      });

  // Create tooltip in the chart
  // ==============================
  chartGroup.call(toolTip);

  // Create event listeners to display and hide the tooltip
  // ==============================
  circlesGroup.on("click", function (data) {
      toolTip.show(data, this);
  })
  
  // onmouseout event
  .on("mouseout", function (data, index) {
      toolTip.hide(data); 
        
  });
  // return circlesGroup;

  // Create axes labels
  chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40 )
      .attr("x", 0 - (height / 2))
      .attr("dy", ".5em")
      .attr("class", "axisText")
      .text("Number of Smokes");

    chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .attr("class", "axisText")
      .text("Median Age");
  }
);
