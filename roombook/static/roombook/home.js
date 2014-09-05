var ROOMS_DISPLAY_ID='rooms_display';


function pretty_print_timestamp(reservation)
{
var st=reservation[0];
var ed=	reservation[1];
var by=	reservation[2];
var html='';


html+=st.day+'/';
html+=st.month+'/';
html+=st.year+':';

if(st.hour<10)
	{
	html+='0'+st.hour;
	}
else	{
	html+=st.hour+'';
	}

if(st.minute<10)
	{
	html+='0'+st.minute+' HRS';
	}
else	{
	html+=st.minute+' HRS';
	}

html+='   to   ';


html+=ed.day+'/';
html+=ed.month+'/';
html+=ed.year+':';
if(ed.hour<10)
	{
	html+='0'+ed.hour;
	}
else	{
	html+=ed.hour+'';
	}
if(ed.minute<10)
	{
	html+='0'+ed.minute+' HRS';
	}
else	{
	html+=ed.minute+' HRS';
	}

html+='---------BY>>>'+by;

return html;
}


function show_rooms()
{
	console.log('show_rooms');
	var ac=document.getElementById('air_cond').checked;
	var proj=document.getElementById('projector').checked;
	
	document.getElementById('air_cond').setAttribute('onclick','show_rooms();');
	document.getElementById('projector').setAttribute('onclick','show_rooms();');
	
	var rooms_display=document.getElementById(ROOMS_DISPLAY_ID);
	rooms_display.innerHTML='';
	
	var table_cont=document.createElement('table');
	var table=document.createElement('tbody');
	table_cont.appendChild(table);

	var row_alternate_color=true;
	
	for(var i=0;i<window.room_data.length;i+=1)
		{
		var room=window.room_data[i];


		if(ac)
			{
			if(!room.ac)
				{
				continue;
				}
			}
		if(proj)
		{
		if(!room.projector)
			{
			continue;
			}
		}
				
						var row=document.createElement('tr');
						var rm_nm=document.createElement('td');
						rm_nm.innerHTML=room.name;
						if(row_alternate_color)
							{
							row.setAttribute('class','one');
							row_alternate_color=false;
							}
						else
							{
							row.setAttribute('class','two');
							row_alternate_color=true;
							}
						row.appendChild(rm_nm);

				
				
				for(var key in room.reservations)
					{
					
					var bk=document.createElement('tr');
					var dt_time=document.createElement('td');
					dt_time.innerHTML=pretty_print_timestamp(room.reservations[key]);
					bk.appendChild(dt_time);
					row.appendChild(bk);
					}
				
			
				try{table.appendChild(row);}catch(err){console.log(err);}
		}
	rooms_display.appendChild(table_cont);
}

function setup_rooms()
	{	
		var room_data_string=document.getElementById('list_of_rooms').value;
		window.room_data=JSON.parse(room_data_string);
		show_rooms();
	}	
