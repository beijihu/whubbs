//首页left-nav控制
window.onscroll = function(){ 
    var t = document.documentElement.scrollTop || document.body.scrollTop;  
    var left_div = document.getElementById( "nav_left" ); 
    if( t >= 50 ) { 
        left_div.style.top="0";
    } else { 
          left_div.style.top="50px";
    } 
} 


if(document.body.scrollWidth < 748){
      document.getElementById('nav_left').style.display = 'none';
    }
//首页left-nav控制



//首页仿知乎风格的js代码


        var tabcurrent = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
        function foucs(c, i, str) {
            if (tabcurrent[i] == c) {
                return;
            }
            $("#" + str + "_tab_" + tabcurrent[i]).removeClass("on");
            $("#" + str + "_tab_" + tabcurrent[i]).removeClass("current");
            $("#" + str + "_con_" + tabcurrent[i]).hide();
            tabcurrent[i] = c;
            $("#" + str + "_tab_" + tabcurrent[i]).addClass("on");
            $("#" + str + "_tab_" + tabcurrent[i]).addClass("current");
            $("#" + str + "_con_" + tabcurrent[i]).show();
        }
        var level = setInterval("autoplay()", 30000);
        var tablock = 0;
        var start = 1;
        function autoplay() {
            if (tablock) return;
            foucs(start, '2', 'foucs');
            start++;
            if (start == 16)/*页卡有n项，这里的数字就是n+1*/
                start = 1;
        }
        for (var l = 1; l <16; l++)/*页卡有n项，这里的数字就是n+1*/ {
            $("#foucs_tab_" + l).mouseover(function () { tablock = 1; });
            $("#foucs_tab_" + l).mouseout(function () { tablock = 0; });
            $("#foucs_con_" + l).mouseover(function () { tablock = 1; });
            $("#foucs_con_" + l).mouseout(function () { tablock = 0; });
        }

//首页仿知乎风格的js代码        