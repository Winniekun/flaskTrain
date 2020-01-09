var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
var ball = new Array();
var ballnum = 70;
var num = 1;


//一分钟刷新重绘次数
self.setInterval("draw()",1000/30);

function draw(){
	//每一帧绘制内容

	//初始化小球数据
	if(num == 1){
		ballcfg();
	};
	
	//重绘canvas
//	ctx.fillStyle = 'rgba(255,255,255,0.3)';
//	ctx.fillRect(0,0,canvas.width,canvas.height);
	ctx.clearRect(0,0,canvas.width,canvas.height);
	
	i = 0;
	while(i<ballnum){
			
		//绘制小球
		ctx.beginPath();
	    ctx.arc(ball[i].x, ball[i].y, 3, 0, Math.PI * 2, true);
	    ctx.closePath();
	    ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
	    ctx.fill();
    
	    //赋予小球加速度
		ball[i].x += ball[i].vx;
		ball[i].y += ball[i].vy;
		
		//防止小球出界
		if(ball[i].x<=0 || ball[i].x>=canvas.width){
			ball[i].vx = -ball[i].vx;
		};
		if(ball[i].y<=0 || ball[i].y>=canvas.height){
			ball[i].vy = -ball[i].vy;
		};
		i++;
	};
	num++;
};


function ballcfg(){
	//获取60个随机小球配置
	
	i = 0;
	while(i<ballnum){

		var city ={
			x: Math.ceil(Math.random()*canvas.width),
			y: Math.ceil(Math.random()*canvas.height),
			vx: bunum(-3,3),
			vy: bunum(-3,3),
		};
		
		ball[i] = city;
		i++;
	};
};


//生成不为0随机数
function bunum(min,max){
	var i = 0;
	while(i == 0){
		var i = Math.floor(Math.random()*(max-min+1)+min);
	};
	return i;
};