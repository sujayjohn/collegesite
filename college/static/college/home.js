var image_count=0;
var TIME_STEP_INTERVAL=100;
var DISPLAY_TIME=3000;
var OPACITY_STEP=0.02;
var opacity_steps=[];
for(var i=1;i>=0;i-=OPACITY_STEP)
	{
	opacity_steps.push(i);
	}
var opacity_step_count=0;
var DOCK_ID='images_dock';


function set_opacity(passed_object,opacity)
{
var opacity_100=opacity*100;
var newcss='-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity='+opacity_100+')";filter:alpha(opacity='+opacity_100+');-moz-opacity:'+opacity+';-khtml-opacity:'+opacity+';opacity:'+opacity+';';
passed_object.setAttribute('style',newcss);
}

function move_dom()
{
var top_pic=document.getElementById('top_pic');
var bottom_pic=document.getElementById('bottom_pic');
var dock=document.getElementById(DOCK_ID);

top_pic.src=bottom_pic.src;
set_opacity(top_pic,1);

bottom_pic.src=image_src_list[image_count]
set_opacity(bottom_pic,1);

top_pic.width=dock.clientWidth;
top_pic.height=dock.clientHeight;
top_pic.clientLeft=dock.clientLeft;
top_pic.clientTop=dock.clientTop;


bottom_pic.width=dock.clientWidth;
bottom_pic.height=dock.clientHeight;
bottom_pic.clientLeft=dock.clientLeft;
bottom_pic.clientTop=dock.clientTop;


image_count+=1;
if(image_count>=image_src_list.length)
	{
		image_count=0;
	}
setTimeout('start_show()',DISPLAY_TIME);
}

function move_top()
{
	var top_pic=document.getElementById('top_pic');
	var bottom_pic=document.getElementById('bottom_pic');
	
	set_opacity(top_pic,opacity_steps[opacity_step_count]);
	opacity_step_count+=1;
	if(opacity_step_count>=opacity_steps.length)
		{
		move_dom();
		opacity_step_count=0;
		return;
		}
	setTimeout('move_top()',TIME_STEP_INTERVAL);
}
		
function start_show()
{
var top_pic=document.getElementById('top_pic');
var bottom_pic=document.getElementById('bottom_pic');
var dock=document.getElementById(DOCK_ID);

top_pic.width=dock.clientWidth;
top_pic.height=dock.clientHeight;
top_pic.clientLeft=dock.clientLeft;
top_pic.clientTop=dock.clientTop;


bottom_pic.width=dock.clientWidth;
bottom_pic.height=dock.clientHeight;
bottom_pic.clientLeft=dock.clientLeft;
bottom_pic.clientTop=dock.clientTop;

set_opacity(top_pic,1);
set_opacity(bottom_pic,1);
setTimeout('move_top()',TIME_STEP_INTERVAL);


}
