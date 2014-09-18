$(document).ready(function() {  
	$("#get_attendence").click(function() {  
        	var course=$('#course').find(":selected").val();
		var semester=$('#semester').find(":selected").val();
		var class_id=course+'-'+semester;
		document.location.href=$('#attendence_url').val()+class_id;
	});  
}); 

var randomScalingFactor = function(){ return Math.round(Math.random()*100)};	
var barChartData = {
			labels : ["January","February","March","April","May","June","July"],
			datasets : [
				{
					fillColor : "rgba(220,220,220,0.5)",
					strokeColor : "rgba(220,220,220,0.8)",
					highlightFill: "rgba(220,220,220,0.75)",
					highlightStroke: "rgba(220,220,220,1)",
					data : [randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]
				},
				{
					fillColor : "rgba(151,187,205,0.5)",
					strokeColor : "rgba(151,187,205,0.8)",
					highlightFill : "rgba(151,187,205,0.75)",
					highlightStroke : "rgba(151,187,205,1)",
					data : [randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]
				}
			]

		}


window.onload=function(){
		var ctx = $("#canvas").get(0).getContext("2d");
		new Chart(ctx).Bar(barChartData, {
			responsive : true, scaleFontColor: "black"
		});
	}
