Chart.defaults.global.animateScale=false;
function attended(value){
		this.value= value;
		this.color= "#6fb22f";
		this.highlight= "green";
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
var chart_list={};

//..........................................................
$(document).ready(function() {  
	$("#get_attendence").click(function() {  
        	var course=$('#course').val();
		var semester=$('#semester').val();
		var class_id=course+'-'+semester;
		document.location.href=$('#attendence_url').val()+class_id;
	});
	
	$('#namecloud a').click(function () {  
	
	$('.active_name').removeClass('active_name');
	$('#'+this.id).addClass('active_name');
	
	
	var new_student_data=classdata[this.id];
	for(var i=0;i<paper_access_list.length;i+=1)
		{
		chart_list[paper_access_list[i]+'_l'].removeData();
		chart_list[paper_access_list[i]+'_t'].removeData();
		chart_list[paper_access_list[i]+'_p'].removeData();
		
		chart_list[paper_access_list[i]+'_l'].removeData();
		chart_list[paper_access_list[i]+'_t'].removeData();
		chart_list[paper_access_list[i]+'_p'].removeData();
		
		chart_list[paper_access_list[i]+'_l'].addData(classdata[this.id][paper_access_list[i]].lec[0]);
		chart_list[paper_access_list[i]+'_l'].addData(classdata[this.id][paper_access_list[i]].lec[1]);
		chart_list[paper_access_list[i]+'_t'].addData(classdata[this.id][paper_access_list[i]].tut[0]);
		chart_list[paper_access_list[i]+'_t'].addData(classdata[this.id][paper_access_list[i]].tut[1]);
		chart_list[paper_access_list[i]+'_p'].addData(classdata[this.id][paper_access_list[i]].prc[0]);
		chart_list[paper_access_list[i]+'_p'].addData(classdata[this.id][paper_access_list[i]].prc[1]);
		
		chart_list[paper_access_list[i]+'_l'].render();
		chart_list[paper_access_list[i]+'_t'].render();
		chart_list[paper_access_list[i]+'_p'].render();
		}

	});
});
