/* VIRTUAL KEYBOARD DEMO - https://github.com/Mottie/Keyboard */
$(function() {

  $('.keyboard').keyboard({
    usePreview: true,
    layout: 'custom',
    customLayout: {
      'normal': [
        '1 2 3 4 5 6 7 8 9 0',
        'Q W E R T Y U I O P',
        'A S D F G H J K L',
        'Z X C V B N M - {left} {right}',
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
