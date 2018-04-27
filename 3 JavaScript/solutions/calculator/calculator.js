$(function() {
    var op = ['+', '-', '÷', '/', '×', 'x', '*'];
    var lhs = [0];
    var ans = 0;
    var display = $('.output-display');
    
    $('.calc-btn').on({
       'click': function(event) {
           let clicked = $(event.delegateTarget).text();
           if (op.includes(lhs[lhs.length-1]) && op.includes(clicked)) {
               lhs.pop();
           }
           if (clicked === '=') {
               ans = eval(lhs.join(''));
               console.log(lhs.join('')+'='+ans)
               lhs = [ans];
               display.text(ans);
           } else if (clicked === 'AC') {
               lhs = [];
               ans = 0;
               display.text(ans);
           } else if (clicked === 'CE') {
               lhs = [ans];
               display.text(ans);               
           } else {
               if (clicked === '×') clicked = '*';
               if (clicked === '÷') clicked = '/';
               lhs.push(clicked);
               display.text(lhs.join(''));
           }
       },
    });
});

