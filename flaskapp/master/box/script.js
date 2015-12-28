$(function(){
 /*
////tips层-上
layer.tips('提示文本', '#id或者.class', {
    tips: [1, '#0FA6D8'] //还可配置颜色
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
*/
$('#a1').click(function(event){
alert("test");
}）



$('#server_m').click(function(event){
layer.alert('開發中...請稍候再來...   -_-!!', {
    skin: 'layui-layer-lan'
    ,closeBtn: 0,shift: 4
});
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#online').hide();
	$('#server').show();
});
$('#group_m').click(function(event){
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#online').hide();
	$('#server').hide();
	$('#group').show();
});
$('#player_m').click(function(event){
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#online').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').show();
});
$('#item_m').click(function(event){
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#online').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').show();
});
$('#Projectile_m').click(function(event){
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#online').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').show();
});
$('#block_m').click(function(event){
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#online').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').show();
});
$('#lindi_m').click(function(event){
	$('#howse').hide();
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#online').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').show();
});
$('#howse_m').click(function(event){
	$('#tpa').hide();
	$('#wanjiaziliao').hide();
	$('#online').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').show();
});
$('#tpa_m').click(function(event){
	$('#wanjiaziliao').hide();
	$('#online').hide();
	$('#server').hide();
	$('#group').hide();
	$('#player').hide();
	$('#item').hide();
	$('#Projectile').hide();
	$('#block').hide();
	$('#lindi').hide();
	$('#howse').hide();
	$('#tpa').show();
});
$('#wanjiaziliao_m').click(function(event){
	$('#online').hide();
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
});
$('#online_m').click(function(event){
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
	$('#online').show();
});





































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