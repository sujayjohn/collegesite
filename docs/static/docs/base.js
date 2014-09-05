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
function pretty_print(data)
{
var output='<table style="text-align:left;">';
for(var key in data)
	{
	output+='<tr><td>';
	output+=key+'</td>';
	output+='<td>'+data[key]+'</td></tr>';
	}
output+='</table>';
return output;
}
//------------------------------------------------------------------------------------------------------------------------------------------
function search_status(event)
{
var enter=detect_enter(event);
var docid=document.getElementById("search_box").value;
//---------------------------------------------------------------------
var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
//---------------------------------------------------------------------
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    var data=JSON.parse(xmlhttp.responseText);
    
    document.getElementById("search_result").innerHTML=pretty_print(data);
    if (data.Action == 'Ready for Pickup')
    	{
    		document.getElementById("search_result").style.background='lightgreen';
    	}
    else
    	{
    		document.getElementById("search_result").style.background='';
    	}
    }
  }
//---------------------------------------------------------------------
if(enter)
	{
		xmlhttp.open("GET",'/docs/'+docid,true);
		xmlhttp.send();
	}

}
//------------------------------------------------------------------------------------------------------------------------------------------