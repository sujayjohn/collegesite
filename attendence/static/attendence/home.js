Chart.defaults.global.animation=false;
Chart.defaults.global.tooltipXOffset=0;
Chart.defaults.global.animateScale=false;
var attended={
		value: 0,
		color: "#29AA66",
		highlight: "green",
		label: "Present"
	};
var missed={
		value: 0,
		color:"#F7464A",
		highlight: "red",
		label: "Absent"
	};
var classdata=[];
//..........................................................
$(document).ready(function() {  
	$("#get_attendence").click(function() {  
        	var course=$('#course').find(":selected").val();
		var semester=$('#semester').find(":selected").val();
		var class_id=course+'-'+semester;
		document.location.href=$('#attendence_url').val()+class_id;
	});
	
	$('#namecloud a').click(function () {  
	
	console.log(this.id);
	});
});
