//--------------------------------------------------------------------------------------------

function detect_enter(e)
{
	var characterCode;
	if(e && e.which){ // NN4 specific code
		e = e;
		characterCode = e.which;
		}
	else {
		e = event;
		characterCode = e.keyCode; // IE specific code
		}
	if (characterCode == 13) return true; // Enter key is 13
	else return false;
}
//------------------------------------------------------------------------------------------------------------------------------------------
$('#search_box').keypress(function search_status(event)
{
	var enter=detect_enter(event);
	var docid=document.getElementById("search_box").value;
 	if(enter)
		{
		var url=$("#main_url").val();
		url+=docid;
		window.location.href=url;
		}
	console.log('search called');
		
});
$('#search_control button').click(function (){
var docid=document.getElementById("search_box").value;
var url=$("#main_url").val();
url+=docid;
window.location.href=url;
console.log('search called');
});
//------------------------------------------------------------------------------------------------------------------------------------------
$('.tray button').click(
function move()
	{
	var id=this.id;
	console.log(id);
	var inbox=$('#inbox')[0];
	var outbox=$('#outbox')[0];
	
	var parent=this.parentElement;
	
	if (parent==inbox)
	{inbox.removeChild(this);
	outbox.appendChild(this);
	}
	if (parent==outbox)
	{outbox.removeChild(this);
	inbox.appendChild(this);}
	}
);
//------------------------------------------------------------------------------------------------------------------------------------------
$('#table_search_box').keyup(
function search_table()
	{
	var id=this.value;
	var buttons=$('.tray button');
	for(var i=0;i<buttons.length;i++)
		{
		if((buttons[i].id+'')==id)
			{
			var parent=buttons[i].parentElement;
			//do domethig to the boxes
			}
		}
	
	}
);

