/* VIRTUAL KEYBOARD DEMO - https://github.com/Mottie/Keyboard */
$(function() {

  $('.keyboard').keyboard({
    usePreview: true,
    layout: 'custom',
    customLayout: {
      'normal': [
        '1 2 3 4 5 6 7 8 9 0',
        'q w e r t y u i o p',
        'a s d f g h j k l ',
        'z x c v b n m {left} {right} -',
        '{accept} {space} {bksp}'
      ]
    }
  });


  $('.keyboardNum').keyboard({
    layout: 'custom',
    usePreview: true,
    customLayout: {
      'normal': [
        '1 2 3',
        '4 5 6',
        '7 8 9',
        '0 {left} {right}',
        '{accept} {bksp}'
      ]
    }
  });


});
