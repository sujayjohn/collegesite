Chart.defaults.global.animation=false;
Chart.defaults.global.tooltipXOffset=0;
Chart.defaults.global.animateScale=false;
function attended(value){
		this.value= value;
		this.color= "green";
		this.highlight= "#8ae234";
		this.label= "Present";
	};
function missed(value){
		this.value= value;
		this.color="#f66666";
		this.highlight= "red";
		this.label= "Absent";
	};
var classdata=[];
var paper_access_list=[];

//..........................................................
$(document).ready(function() {  
	$("#get_attendence").click(function() {  
        	var course=$('#course').find("=selected").val();
		var semester=$('#semester').find("=selected").val();
		var class_id=course+'-'+semester;
		document.location.href=$('#attendence_url').val()+class_id;
	});
	
	$('#namecloud a').click(function () {  
	var new_student_data=classdata[this.id];
	for(var i=0;i<paper_access_list.length;i+=1)
		{
		}
	console.log(this.id);
	});
});
