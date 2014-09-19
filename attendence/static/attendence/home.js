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
