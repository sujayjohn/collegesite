$(document).ready(function(){ 
    $("#").click(function(){ 
      $("#search_result").load("script.php"); 
    }); 
  }); 








function setup_table()
	{
	var inbox=document.getElementById('inbox');	
	var files=document.getElementById('docs').value;
	files=JSON.parse(files);
	window['files_on_table']=files;
	for(var keys in files)
		{
		var btn=document.createElement('button');
		btn.innerHTML=keys;
		btn.setAttribute('onclick','move('+keys+');');
		btn.setAttribute('class','files');
		btn.setAttribute('id','file_id_'+keys);
		inbox.appendChild(btn);
		}
	
	}
	
function move(docid)
	{
	if (docid!=undefined)
		{
			var file=document.getElementById('file_id_'+docid);
			var inbox=document.getElementById('inbox');
			var outbox=document.getElementById('outbox');
			if(file.parentElement.id=='inbox')
				{
				inbox.removeChild(file);
				outbox.appendChild(file);
				}
			else
				{
				outbox.removeChild(file);
				inbox.appendChild(file);
				}
		}
	else
		{
		var doc_id_from_box=document.getElementById('table_search_box').value;
		if(doc_id_from_box!='')
			{
			move(doc_id_from_box);
			}
		}
	
	}
	
function table_search()
	{
	document.getElementById('table_search_box').style.background='';
	var docid=document.getElementById('table_search_box').value;
	for(var k in window.files_on_table)
			{
			if(docid==k)
					{
					var parent=document.getElementById('file_id_'+docid).parentElement;
					parent.style.background='lightgreen';
					if(parent.id=='inbox')
							{
							document.getElementById('outbox').style.background='';
							}
					else
							{
							document.getElementById('inbox').style.background='';
							}
					break;
					}
			else
					{
					document.getElementById('outbox').style.background='';
					document.getElementById('inbox').style.background='';
					}
			}
	}
function clear_outbox()
	{
	var outb={};
	for(var k in window.files_on_table)
		{
		var parent=document.getElementById('file_id_'+k).parentElement.id;
		if(parent=='outbox')
			{
			outb[k]='';
			}
		}
	var datastr=JSON.stringify(outb);
	var sendform=document.getElementById('edit_form');
	sendform.setAttribute('action','/docs/edit');
	sendform.setAttribute('method','POST');
	var hidden=document.createElement('input');
	hidden.setAttribute('type','hidden');
	hidden.setAttribute('value',datastr);
	hidden.setAttribute('name','data');
	sendform.appendChild(hidden);
	sendform.submit();
	sendform.removeChild(hidden);
	}
function add_note()
	{
	var outb={};
	var docid=document.getElementById('table_search_box').value;
	if(docid=='')
		{
		
		document.getElementById('table_search_box').style.background='pink';
		alert('You have not entered a document ID in the ID search box.');
		return;
		}
	outb[docid]=document.getElementById('note_text').value;
	var datastr=JSON.stringify(outb);
	var sendform=document.getElementById('edit_form');
	sendform.setAttribute('action','/docs/edit');
	sendform.setAttribute('method','POST');
	var hidden=document.createElement('input');
	hidden.setAttribute('type','hidden');
	hidden.setAttribute('value',datastr);
	hidden.setAttribute('name','edit');
	sendform.appendChild(hidden);
	sendform.submit();
	sendform.removeChild(hidden);
	}