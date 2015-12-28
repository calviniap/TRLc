$(function(){

 /*
////tips层-上
layer.tips('提示文本', '#id或者.class', {
    tips: [1, '#0FA6D8'] //还可配置颜色
});

//信息框-例5
layer.msg('玩命卖萌中', function(){
//关闭后的操作
});

//询问框
layer.confirm('確定這樣做嗎？', {
    btn: ['確定','取消'] //按钮
}, function(){
    layer.msg('完成！', {icon: 1});
}, function(){

});



layer.alert('内容')


//墨绿深蓝风
layer.alert('墨绿风格，点击确认看深蓝', {
    skin: 'layui-layer-molv' //样式类名
    ,closeBtn: 0
}, function(){
    layer.alert('偶吧深蓝style', {
        skin: 'layui-layer-lan'
        ,closeBtn: 0
        ,shift: 4 //动画类型
    });
});



//加载层
var index = layer.load(0, {shade: false}); //0代表加载的风格，支持0-2


layer.msg('正在进入');



layer.alert('開發中...請稍候再來...   -_-!!', {//服務器信息
    skin: 'layui-layer-lan'
    ,closeBtn: 0,shift: 4
});

*/
$('#command').html('content');


$('#server').load('/menu/server');
autorun();
$('#server_m').click(function(event){
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#user').hide();
	$('#server').show();
	$('#server').load('/menu/server');
});
$('#group_m').click(function(event){//組列表
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#user').hide();
	$('#server').hide();
	$('#group').show();
	$('#group').load('/menu/group');
});
$('#player_m').click(function(event){//禁止玩家
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#user').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').show();
	$('#player').load('/menu/player');
});
$('#item_m').click(function(event){//禁止物品
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#user').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').show();
	$('#item').load('/menu/item');
});
$('#Projectile_m').click(function(event){//禁止彈藥
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#user').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').show();
	$('#Projectile').load('/menu/Projectile');
});
$('#block_m').click(function(event){//禁止方塊
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#user').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').show();
	$('#block').load('/menu/block');
});
$('#lindi_m').click(function(event){//玩家領地
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#user').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').show();
	$('#lindi').load('/menu/lindi');
});
$('#howse_m').click(function(event){//玩家住宅
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#user').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').show();
	$('#howse').load('/menu/howse');
});
$('#tpa_m').click(function(event){//跳躍點
	$('#wanjiaziliao').hide();
	$('#user').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').show();
	$('#tpa').load('/menu/tpa');
});
$('#wanjiaziliao_m').click(function(event){//玩家資料
	$('#user').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').show();
	$('#wanjiaziliao').load('/menu/wanjiaziliao');
});

$('#user_m').click(function(event){//用戶管理
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#user').show();
	$('#user').load('/menu/user');
});


 //jquery.validate
$("#registerform").validate({
    submitHandler: function() {
        //验证通过后 的js代码写在这里
      $.post("/register_get",
    {
      username:$('#username').val(),
      userpass:$('#userpass').val(),
      qq:$('#qq').val(),
      signature:$('#signature').val(),
    },
    function(data,status){
      layer.alert(data);
      if(data=='用戶已存在'){$('#username').val('');}
      if(data=='QQ號碼重復'){$('#qq').val('');}
      if(data=='郵箱重復'){$('#signature').val('');}
      if(data=='注冊完成'){$('#username').val('');$('#userpass').val('');$('#userpass2').val('');$('#qq').val('');$('#signature').val('');}
    });
}});




 //jquery.validate
$("#loginform").validate({
    submitHandler: function() {
        //验证通过后 的js代码写在这里
      $.post("/checklog",
    {
      username:$('#username').val(),
      userpass:$('#userpass').val(),
    },
    function(data,status){
		d=data;
      layer.alert(d);
      if(d =='歡迎回來!'){
      location.href = "/index";
      }
    });
}});














































});
//▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
function play(url){
var div = document.getElementById('player');
div.innerHTML = '<embed src="'+url+'" loop="0" autostart="true" hidden="true"></embed>';
}


function paste(this_){
this_.value=window.clipboardData.getData('text');//點擊粘貼文本
}
//▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
function save(x,id){
	switch (x){
		case 'server_name':
			$.ajax({
            type:"post",
            url:"/save/server/server_name",
            data:{
				server_name:$('#server_name').val()
			},
            datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
            beforeSend:function(){$("#msg").html("waiting...");},
            success:function(data){
           $("#msg").html(decodeURI(data));
            }   ,
            complete: function(XMLHttpRequest, textStatus){
               //alert(XMLHttpRequest.responseText);
               //alert(textStatus);
            },
            error: function(){
				$("#msg").html('失敗!');
				location.href = "/index";
            }
         });
		break;

		case 'server_url':
			$.ajax({
            type:"post",
            url:"/save/server/server_url",
            data:{
				server_url:$('#server_url').val()
			},
            datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
            beforeSend:function(){$("#msg").html("waiting...");},
            success:function(data){
           $("#msg").html(decodeURI(data));
            }   ,
            complete: function(XMLHttpRequest, textStatus){
               //alert(XMLHttpRequest.responseText);
               //alert(textStatus);
            },
            error: function(){
				$("#msg").html('失敗!');
				location.href = "/index";
            }
         });
		break;

		case 'canregister':
		if($("input[name='canregister']").is(':checked')){
			var a=1;
		}else{
			var a=0;
		}
			$.ajax({
            type:"post",
            url:"/save/server/canregister",
            data:{
				canregister:a
			},
            datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
            beforeSend:function(){$("#msg").html("waiting...");},
            success:function(data){
           $("#msg").html(decodeURI(data));
            }   ,
            complete: function(XMLHttpRequest, textStatus){
               //alert(XMLHttpRequest.responseText);
               //alert(textStatus);
            },
            error: function(){
				$("#msg").html('失敗!');
				location.href = "/index";
            }
         });
		break;

		case 'serveronline':
	    if($("input[name='serveronline']").is(':checked')){
	    	var a=1;
	    }else{
	    	var a=0;
	    }
	    	$.ajax({
	    	type:"post",
	    	url:"/save/server/serveronline",
	    	data:{
	    		serveronline:a
	    	},
	    	datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
	    	beforeSend:function(){$("#msg").html("waiting...");},
	    	success:function(data){
	       $("#msg").html(decodeURI(data));
	    	}   ,
	    	complete: function(XMLHttpRequest, textStatus){
	    	   //alert(XMLHttpRequest.responseText);
	    	   //alert(textStatus);
	    	},
	    	error: function(){
	    		$("#msg").html('失敗!');
	    		location.href = "/index";
	    	}
	     });
	    break;

		case 'selectlevel':
		$.ajax({
		type:"post",
		url:"/edituser/selectlevel",
		data:{
			level:$('#level_'+id).val(),
			   id:$('#id_'+id).val(),
		},
		datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
		beforeSend:function(){},
		success:function(data){
		}   ,
		complete: function(XMLHttpRequest, textStatus){
		   //alert(XMLHttpRequest.responseText);
		   //alert(textStatus);
		   layer.msg('完成！', {icon: 1});
		},
		error: function(){
			//location.href = "/index";
		}
	 });
	    break;

		case 'selectban':
		$.ajax({
		type:"post",
		url:"/edituser/selectban",
		data:{
			ban:$('#ban_'+id).val(),
			 id:$('#id_'+id).val(),
		},
		datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
		beforeSend:function(){},
		success:function(data){
		}   ,
		complete: function(XMLHttpRequest, textStatus){
		   //alert(XMLHttpRequest.responseText);
		   //alert(textStatus);
		   layer.msg('完成！', {icon: 1});
		},
		error: function(){
			//location.href = "/index";
		}
	 });
	    break;

		case 'QQ'://保存QQ
		$.ajax({
		type:"post",
		url:"/edituser/QQ",
		data:{
			QQ:$('#QQ_'+id).val(),
			 id:$('#id_'+id).val(),
		},
		datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
		beforeSend:function(){},
		success:function(data){
		}   ,
		complete: function(XMLHttpRequest, textStatus){
		   //alert(XMLHttpRequest.responseText);
		   //alert(textStatus);
		   layer.msg('完成！', {icon: 1});
		},
		error: function(){
			//location.href = "/index";
		}
	 });
	    break;

		case 'signature'://保存signature
		$.ajax({
		type:"post",
		url:"/edituser/signature",
		data:{
			signature:$('#signature_'+id).val(),
			 id:$('#id_'+id).val(),
		},
		datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
		beforeSend:function(){},
		success:function(data){
		}   ,
		complete: function(XMLHttpRequest, textStatus){
		   //alert(XMLHttpRequest.responseText);
		   //alert(textStatus);
		   layer.msg('完成！', {icon: 1});
		},
		error: function(){
			//location.href = "/index";
		}
	 });
	    break;

		case 'COIN'://保存COIN
		$.ajax({
		type:"post",
		url:"/edituser/COIN",
		data:{
			COIN:$('#COIN_'+id).val(),
			 id:$('#id_'+id).val(),
		},
		datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
		beforeSend:function(){},
		success:function(data){
		}   ,
		complete: function(XMLHttpRequest, textStatus){
		   //alert(XMLHttpRequest.responseText);
		   //alert(textStatus);
		   layer.msg('完成！', {icon: 1});
		},
		error: function(){
			//location.href = "/index";
		}
	 });
	    break;

	}
  }


function user_del(id){
	//询问框
	layer.confirm('汝確定欲安爾做?', {
	    btn: ['確定','取消'] //按钮
	}, function(){
		$.ajax({
		type:"get",
		url:"/user_del/"+id,
		data:{},
		datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
		beforeSend:function(){},success:function(data){},
		complete: function(XMLHttpRequest, textStatus){
		   //alert(XMLHttpRequest.responseText);
		   //alert(textStatus);
		   $('#user').load('/menu/user');
		},
		error: function(){
			alert('失敗!');
			location.href = "/index";
		}
	 });
	    layer.msg('完成！', {icon: 1});
	}, function(){

	});

}


function getnew(){
	$.ajax({
	type:"get",
	url:"/getnew",
	data:{

	},
	datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
	beforeSend:function(){},
	success:function(data){
	}   ,
	complete: function(XMLHttpRequest, textStatus){
	   //alert(XMLHttpRequest.responseText);
	   //alert(textStatus);
	   //layer.msg('更新個人資料完成！', {icon: 1});
	   $('#mybox').load('/getmybox');
	   autorun();
	},
	error: function(){
		//location.href = "/index";
	}
 });
}

function autorun(){
	setTimeout("getnew()", 10000);
}
