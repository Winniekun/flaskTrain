function bodyCard(){
	//获取浏览器可用宽度与高度
	var w=window.innerWidth
	|| document.documentElement.clientWidth
	|| document.body.clientWidth;
	var h=window.innerHeight
	|| document.documentElement.clientHeight
	|| document.body.clientHeight;
	
	//定义想要的宽高比例值
//	var a=w/2;
//	var b=h/2;

	//设置canvas大小
	var opd = document.getElementById('canvas');
	opd.width=w;
	opd.height=h;
	
	//设置遮挡层大小
	var masking = document.getElementById('masking');
	masking.style.width = w+'px';
	masking.style.height = h+'px';

	//设置主要内容位置
	var mainlay = document.getElementById('mainlay');
	
	//login宽高设置
	var x = w * 0.65;//login宽度
	var y = h * 0.5;//login高度
	mainlay.style.width = x + 'px';
	mainlay.style.height = y + 'px';
	
	//左右居中设置
	
	if (x>500) {
		mainlay.style.left = (w-500)/2 +'px';
	}else if(x<300){
		mainlay.style.left = (w-300)/2 +'px';
	}else{
		mainlay.style.left = (w-x)/2 +'px';
	}
	
	if (y>500) {
		mainlay.style.top = (h-500)/2 +'px';
	}else if(y<300){
		mainlay.style.top = (h-300)/2 +'px';
	}else{
		mainlay.style.top = (h-y)/2 +'px';
	}
	
	
};
	
	//当页面加载完成时执行
window.onload= function(){
	bodyCard();
};
	
	//当浏览器大小改变时执行
window.onresize = function(){
	bodyCard();
};
