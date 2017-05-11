
chrome.app.runtime.onLaunched.addListener(function() {
  chrome.app.window.create('background.html', {
    'outerBounds': {
      'width': 400,
      'height': 500
    }
  });
});
