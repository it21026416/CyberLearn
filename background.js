chrome.action.onClicked.addListener(function(tab) {
    // Use this function to open your Flask application
    chrome.tabs.create({ url: 'http://127.0.0.1:5000/' });
});
